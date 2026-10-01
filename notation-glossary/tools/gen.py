#!/usr/bin/env python3
"""Resolve link macros in *_src.md and write site pages.

Macro forms (inside the source markdown):
  @[p0/04:788]            -> link to the h3 (else h2) containing line 788 of part0/04-*.md
  @[p0/04:788|自定义文字]   -> same target, custom link text
  @[p3/05]                -> chapter link, text "第三部第 5 章"
  @[p1/05:0]              -> chapter link, text "第一部第 5 章 · 章首"
  @[p0/04:788^h2]         -> force the h2 (not the h3)
Usage: gen.py notation_src.md out.md [--report]
"""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
# 站点正文目录：默认是仓库里的 site/docs；在别处的副本上跑时用环境变量 SIBUQU_DOCS 指定
DOCS = os.environ.get("SIBUQU_DOCS") or os.path.normpath(os.path.join(HERE, "..", "..", "site", "docs"))
anc = json.load(open(os.path.join(HERE, "anchors.json")))
PART = {"part0": "预备篇", "part1": "第一部", "part2": "第二部", "part3": "第三部", "part4": "第四部"}
GENERIC = {"第一部", "第二部", "第三部", "直觉", "定义", "算例", "例", "白话", "物理意义", "行为分析",
           "小结", "注意", "陷阱", "思路", "问题", "回顾", "动机", "完整示范", "模型", "设定", "结论", "推导", "解读", "逐步推导", "证明",
           "参数一", "参数二", "参数三", "参数四", "第一步", "第二步", "第三步", "第四步", "第五步"}

files = {}
for p in anc:
    m = re.match(r"(part\d)/(\d\d)-", p)
    if m:
        files["p" + m.group(1)[4] + "/" + m.group(2)] = p


def short(text):
    t = re.sub(r"^\d+(\.\d+)+\s*", "", text.strip())
    parts = re.split(r"[：:]", t, maxsplit=1)
    if len(parts) == 2:
        pre, post = parts[0].strip(), parts[1].strip()
        if pre in GENERIC or len(pre) <= 1:
            t = post
        else:
            t = pre
    # trim parenthetical tails and overly long text
    t = re.sub(r"（[^）]*）\s*$", "", t).strip()
    if len(t) > 22 and "$" not in t:
        t = t[:20] + "…"
    return t


def secnum(text):
    m = re.match(r"^(\d+(\.\d+)+)\s", text.strip())
    return m.group(1) if m else None


def resolve(key, line, force_h2=False):
    path = files[key]
    part = PART[path.split("/")[0]]
    chap = int(path.split("/")[1][:2])
    href = path
    if line is None:
        return href, "%s第 %d 章" % (part, chap)
    h2 = h3 = None
    for h in anc[path]:
        if h["line"] > line:
            break
        if h["level"] == 2:
            h2, h3 = h, None
        elif h["level"] == 3:
            h3 = h
    if h2 is None and h3 is None:
        return href, "%s第 %d 章 · 章首" % (part, chap)
    tgt = h2 if (force_h2 or h3 is None) else h3
    href = path + "#" + tgt["id"]
    num = secnum(h2["text"]) if h2 else None
    if num:
        text = "%s %s · %s" % (part, num, short(tgt["text"]))
    else:
        text = "%s第 %d 章 · %s" % (part, chap, short(tgt["text"]))
    return href, text


MAC = re.compile(r"@\[(p\d/\d\d)(?::(\d+))?(\^h2)?(?:\|([^\]]+))?\]")


def render(src, report):
    def rep(m):
        key, line, fh2, custom = m.group(1), m.group(2), m.group(3), m.group(4)
        ln = int(line) if line is not None else None
        if ln == 0:
            href, text = files[key], resolve(key, 0)[1]
            path = files[key]
            part = PART[path.split("/")[0]]
            text = "%s第 %d 章 · 章首" % (part, int(path.split("/")[1][:2]))
        else:
            href, text = resolve(key, ln, bool(fh2))
        if custom:
            text = custom
        report.append((m.group(0), href, text))
        return "[%s](%s)" % (text, href)
    return MAC.sub(rep, src)


ORDER = {"p0": 0, "p1": 1, "p2": 2, "p3": 3, "p4": 4}


def rowkey(row):
    cells = row.split("|")
    col = cells[3] if len(cells) > 3 else row
    m = MAC.search(col)
    if not m:
        return (9, 99, 99999)
    part, chap = m.group(1).split("/")
    ln = int(m.group(2)) if m.group(2) else 0
    return (ORDER[part], int(chap), ln)


def sort_tables(src):
    """Sort data rows of every 4-column table whose header starts with '| 符号 | 含义 | 首次出现'
    (or '| 术语 |') by the first macro in the 3rd column (reading order)."""
    lines = src.split("\n")
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        if (l.startswith("| 符号 | 含义 | 首次出现") or l.startswith("| 术语 |")) and i + 1 < len(lines) and lines[i + 1].startswith("|---"):
            out += [l, lines[i + 1]]
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].startswith("|"):
                rows.append(lines[j]); j += 1
            if l.startswith("| 术语 |"):
                rows.sort(key=lambda r: (rowkey("|".join([""] + r.split("|")[2:])) if len(r.split("|")) > 4 else (9, 99, 99999), rowkey(r)))
            else:
                rows.sort(key=rowkey)
            out += rows
            i = j
            continue
        out.append(l); i += 1
    return "\n".join(out)


def main():
    src_path, out_path = sys.argv[1], sys.argv[2]
    src = open(src_path, encoding="utf-8").read()
    src = sort_tables(src)
    # drop authoring comments  <!-- ... --> lines starting with %%
    src = "\n".join(l for l in src.split("\n") if not l.startswith("%%"))
    report = []
    out = render(src, report)
    left = re.findall(r"@\[[^\]]*\]", out)
    if left:
        print("UNRESOLVED:", left[:10])
    open(out_path, "w", encoding="utf-8").write(out)
    if "--report" in sys.argv:
        for mac, href, text in report:
            print("%-22s -> %-40s %s" % (mac, text, href))
    print("links:", len(report))


if __name__ == "__main__":
    main()
