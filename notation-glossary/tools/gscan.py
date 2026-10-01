#!/usr/bin/env python3
"""For each glossary term: first body occurrence (reading order; skip index pages, '你将学会' preview,
code fences, 参考文献 sections), and per-chapter counts (top 3)."""
import json, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "scan.json")))
def preview_lines(f):
    first_h2 = next((h["line"] for h in f["headings"] if h["level"] == 2), 10**9)
    out = set(); on = False
    for i, l in enumerate(f["lines"], 1):
        if i >= first_h2: break
        if "你将学会" in l: on = True; out.add(i); continue
        if on:
            if l.strip() == "---": break
            out.add(i)
    return out
def ref_lines(f):
    out = set(); on = False
    hs = {h["line"]: h for h in f["headings"]}
    for i, l in enumerate(f["lines"], 1):
        if i in hs and hs[i]["level"] == 2:
            on = hs[i]["text"].startswith("参考文献")
        if on: out.add(i)
    return out
chap = [f for f in d if not f["path"].endswith("index.md")]
skips = {f["path"]: preview_lines(f) | ref_lines(f) for f in chap}
terms = []
for line in open(os.path.join(HERE, "gterms.txt"), encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    part, name, pat = line.rstrip("\n").split("|", 2)
    terms.append((part, name, pat))
sel = sys.argv[1] if len(sys.argv) > 1 else None
showdef = "--def" in sys.argv
bypath = {f["path"]: f for f in chap}
for part, name, pat in terms:
    if sel and part != sel: continue
    rx = re.compile(pat)
    first = None; counts = {}; dfn = None
    for f in chap:
        in_f = False; c = 0
        for ln, l in enumerate(f["lines"], 1):
            if re.match(r"^\s*(```|~~~)", l): in_f = not in_f; continue
            if in_f or ln in skips[f["path"]] or l.startswith("# "): continue
            ms = list(rx.finditer(l))
            if ms and dfn is None and (l.startswith("#") or any(("**" in l[max(0,m.start()-3):m.start()] or "**" in l[m.end():m.end()+3]) for m in ms)):
                dfn = (f["path"], ln)
            if ms:
                c += len(ms)
                if first is None:
                    m = ms[0]; first = (f["path"], ln, l[max(0, m.start()-30):m.end()+30])
        if c: counts[f["path"][:9].replace("part", "p").replace("-", "")] = c
    top = sorted(counts.items(), key=lambda x: -x[1])[:4]
    fp = first[0][:9].replace("part","p").replace("-","") + ":%d" % first[1] if first else "-"
    dp = dfn[0][:9].replace("part","p").replace("-","") + ":%d" % dfn[1] if dfn else "-"
    if showdef:
        tgt = dfn or (first[:2] if first else None)
        if tgt:
            L = bypath[tgt[0]]["lines"][tgt[1]-1]; m = rx.search(L); a0 = max(0, (m.start() if m else 0) - 20)
            print("%s|%s| %s:%d | %s" % (part, name, tgt[0][:9].replace("part","p").replace("-",""), tgt[1], L[a0:a0+230].replace("\n"," ")))
        continue
    print("%s|%-14s| first %-9s def %-9s| top %s\n      %s" % (part, name[:14], fp, dp, " ".join("%s:%d" % t for t in top), (first[2] if first else "").replace("\n"," ")[:100]))
