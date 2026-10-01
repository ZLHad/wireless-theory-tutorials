#!/usr/bin/env python3
"""Map source headings (scan.json) -> built HTML heading ids, in order.
Usage: anchors.py <built_site_dir>   -> writes anchors.json {path: [{line,level,text,id}]}"""
import json, os, re, sys, html
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))


class HP(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hs = []
        self.cur = None
        self.in_article = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article":
            self.in_article = True
        if self.in_article and re.fullmatch(r"h[1-6]", tag):
            self.cur = {"level": int(tag[1]), "id": a.get("id"), "text": ""}
        if self.cur is not None and tag == "a" and "headerlink" in (a.get("class") or ""):
            self.cur["skip"] = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False
        if self.cur is not None and re.fullmatch(r"h[1-6]", tag):
            self.hs.append(self.cur)
            self.cur = None
        if self.cur is not None and tag == "a":
            self.cur.pop("skip", None)

    def handle_data(self, data):
        if self.cur is not None and not self.cur.get("skip"):
            self.cur["text"] += data


def clean(t):
    # 源标题与 HTML 标题共用：去掉 attr_list 的 { #id }、公式（源里是 $…$，HTML 里是 \(…\)）、强调符号与空白
    t = re.sub(r"\{:?\s*#[^}]*\}", "", t)
    t = re.sub(r"\$[^$]*\$", "", t)
    t = re.sub(r"\\\(.*?\\\)", "", t)
    t = re.sub(r"[*`_]", "", t)
    t = re.sub(r"\s+", "", t)
    return t


def norm(t):
    return clean(t)[:8]


def main():
    built = sys.argv[1]
    data = json.load(open(os.path.join(HERE, "scan.json")))
    out = {}
    bad = 0
    for d in data:
        f = os.path.join(built, d["path"][:-3] + ".html")
        p = HP()
        p.feed(open(f, encoding="utf-8").read())
        hs = [h for h in p.hs]
        src = d["headings"]
        if len(hs) != len(src):
            print("COUNT MISMATCH", d["path"], len(src), len(hs))
        res = []
        for i, h in enumerate(src):
            hh = hs[i] if i < len(hs) else None
            ok = hh is not None and hh["level"] == h["level"]
            if hh is not None and norm(h["text"])[:4] and norm(h["text"])[:4] not in clean(hh["text"]):
                ok = False
            if not ok:
                bad += 1
                print("MISMATCH", d["path"], h["line"], h["text"][:40], "| html:", hh and hh["text"][:40])
            res.append({"line": h["line"], "level": h["level"], "text": h["text"], "id": hh and hh["id"]})
        out[d["path"]] = res
    json.dump(out, open(os.path.join(HERE, "anchors.json"), "w"), ensure_ascii=False, indent=0)
    print("pages", len(out), "mismatches", bad)


if __name__ == "__main__":
    main()
