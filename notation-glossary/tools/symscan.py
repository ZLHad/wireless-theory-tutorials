#!/usr/bin/env python3
"""Scan site/docs chapters: headings, math spans, symbol atoms, with contexts.

Output: scan.json  = {files:[{path,title,part,chap,headings:[{line,level,text}],
                             spans:[{line,start,end,display,tex,atoms:[...] }]}]}
"""
import json, re, sys, os
import yaml

OUT = os.path.dirname(os.path.abspath(__file__))
# 站点目录（含 mkdocs.yml 与 docs/）：默认是仓库里的 site/；在别处的副本上跑时用环境变量 SIBUQU_SITE 指定
SITE = os.environ.get("SIBUQU_SITE") or os.path.normpath(os.path.join(OUT, "..", "..", "site"))

GREEK = """alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega ell hbar nabla partial""".split()
GREEK_SET = set(GREEK)
DECOR = {"hat", "tilde", "bar", "overline", "widehat", "widetilde", "vec", "dot",
         "ddot", "check", "breve", "underline", "mathring"}
FONTS = {"mathbf", "boldsymbol", "bm", "mathcal", "mathbb", "mathsf", "mathrm",
         "mathfrak", "mathscr", "mathit", "mathbfit", "pmb"}
SKIP_ARG = {"text", "textrm", "textbf", "textit", "mbox", "operatorname", "label",
            "tag", "begin", "end", "color", "textsf", "texttt"}


def load_nav():
    with open(os.path.join(SITE, "mkdocs.yml")) as f:
        txt = f.read()
    # strip python tags that yaml.safe_load can't parse
    txt = re.sub(r"!!python/\S+", "", txt)
    cfg = yaml.safe_load(txt)
    files = []

    def walk(node):
        if isinstance(node, list):
            for x in node:
                walk(x)
        elif isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str):
                    files.append((k, v))
                else:
                    walk(v)
        elif isinstance(node, str):
            files.append((None, node))
    walk(cfg["nav"])
    return files


def read_group(s, i):
    """s[i] == '{' -> return (content, index after closing brace)."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def read_arg(s, i):
    """Read one TeX argument starting at s[i] (skip spaces). Return (arg, next)."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        return read_group(s, i)
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def norm_sub(sub):
    sub = sub.strip()
    sub = re.sub(r"\\(mathrm|text|textrm|mathit|operatorname)\s*\{([^{}]*)\}", r"\2", sub)
    sub = re.sub(r"\\rm\b|\\mathrm|\\text", "", sub)
    sub = re.sub(r"[{}\s]+", "", sub)
    return sub


def atomize(tex):
    """Return list of atoms: dict(base, font, decor, sub, key)."""
    s = tex
    atoms = []
    i = 0
    n = len(s)
    pend_decor = []
    pend_font = None
    while i < n:
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)", s[i:])
            if not m:
                i += 2
                continue
            name = m.group(1)
            i += len(m.group(0))
            if name in SKIP_ARG:
                if name in ("begin", "end"):
                    _, i = read_arg(s, i)
                else:
                    _, i = read_arg(s, i)
                continue
            if name in DECOR:
                pend_decor.append(name)
                continue
            if name in FONTS:
                arg, i = read_arg(s, i)
                arg_s = arg.strip()
                # font applied to a group: may contain decorations / greek
                inner = atomize(arg_s) if (len(arg_s) > 1 and not re.fullmatch(r"[A-Za-z]+", arg_s)) else None
                if inner:
                    for a in inner:
                        a["font"] = name
                        a["decor"] = pend_decor + a["decor"]
                    pend_decor = []
                    # subscript attaches to last inner atom
                    sub, i = read_sub(s, i)
                    if sub is not None and inner:
                        inner[-1]["sub"] = norm_sub(sub)
                    atoms.extend(inner)
                    continue
                base = arg_s
                sub, i = read_sub(s, i)
                atoms.append(mk(base, name, pend_decor, sub))
                pend_decor = []
                continue
            if name in GREEK_SET:
                sub, i = read_sub(s, i)
                atoms.append(mk("\\" + name, pend_font, pend_decor, sub))
                pend_decor = []
                continue
            # other commands (\log, \sum, \frac ...) ignored
            continue
        if c.isalpha() and c.isascii():
            sub, j = read_sub(s, i + 1)
            atoms.append(mk(c, None, pend_decor, sub))
            pend_decor = []
            i = j
            continue
        if c == "{" and pend_decor:
            arg, i = read_group(s, i)
            inner = atomize(arg)
            if inner:
                inner[0]["decor"] = pend_decor + inner[0]["decor"]
                sub, i = read_sub(s, i)
                if sub is not None:
                    inner[-1]["sub"] = norm_sub(sub)
                atoms.extend(inner)
            pend_decor = []
            continue
        i += 1
    return atoms


def read_sub(s, i):
    """If s[i:] starts with optional prime/space then '_', read subscript.
    Skip a following/preceding superscript. Return (sub or None, next)."""
    j = i
    sub = None
    for _ in range(2):
        k = j
        while k < len(s) and s[k] in " '":
            k += 1
        if k < len(s) and s[k] == "_":
            sub, j = read_arg(s, k + 1)
        elif k < len(s) and s[k] == "^":
            _, j = read_arg(s, k + 1)
        else:
            break
    return sub, j


def mk(base, font, decor, sub):
    sub_n = norm_sub(sub) if sub is not None else ""
    return {"base": base, "font": font, "decor": list(decor), "sub": sub_n}


def keyof(a):
    key = "".join("\\%s " % d for d in a["decor"])
    key += ("\\%s{%s}" % (a["font"], a["base"])) if a["font"] else a["base"]
    if a["sub"]:
        key += "_{%s}" % a["sub"]
    return key


def scan_file(rel):
    path = os.path.join(SITE, "docs", rel)
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    headings = []
    spans = []
    in_fence = False
    fence_mark = None
    in_disp = False
    disp_buf = []
    disp_start = None
    for ln, raw in enumerate(lines, 1):
        line = raw
        st = line.strip()
        if not in_disp:
            fm = re.match(r"^\s*(```+|~~~+)", line)
            if fm:
                mark = fm.group(1)[0] * 3
                if not in_fence:
                    in_fence, fence_mark = True, mark
                    continue
                elif line.strip().startswith(fence_mark):
                    in_fence = False
                    continue
            if in_fence:
                continue
            hm = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if hm:
                headings.append({"line": ln, "level": len(hm.group(1)), "text": hm.group(2)})
        # display math blocks: lines that are exactly $$ open/close, or $$...$$ on one line
        if in_disp:
            if st.endswith("$$"):
                disp_buf.append(st[:-2])
                tex = "\n".join(disp_buf)
                spans.append({"line": disp_start, "col": 0, "display": True, "tex": tex,
                              "ctx_line": disp_start})
                in_disp = False
                disp_buf = []
            else:
                disp_buf.append(line)
            continue
        if st.startswith("$$") and not (len(st) > 4 and st.endswith("$$")):
            in_disp = True
            disp_start = ln
            disp_buf = [st[2:]]
            continue
        # inline / one-line display
        for m in re.finditer(r"\$\$(.+?)\$\$|\$(?!\s)((?:\\\$|[^$])+?)(?<!\s)\$", line):
            if m.group(1) is not None:
                spans.append({"line": ln, "col": m.start(), "end": m.end(), "display": True,
                              "tex": m.group(1)})
            else:
                spans.append({"line": ln, "col": m.start(), "end": m.end(), "display": False,
                              "tex": m.group(2)})
    for sp in spans:
        ats = atomize(sp["tex"])
        sp["atoms"] = [keyof(a) for a in ats]
        sp["bases"] = [a["base"] for a in ats]
    return {"path": rel, "lines": lines, "headings": headings, "spans": spans}


def main():
    nav = load_nav()
    out = []
    for title, rel in nav:
        d = scan_file(rel)
        d["title"] = title
        out.append(d)
    with open(os.path.join(OUT, "scan.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    tot = sum(len(d["spans"]) for d in out)
    print("files", len(out), "spans", tot)


if __name__ == "__main__":
    main()
