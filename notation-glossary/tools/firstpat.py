#!/usr/bin/env python3
"""firstpat.py REGEX [--n 2] [--files ...]: first spans (reading order, chapters only) whose TeX matches."""
import json, re, os, sys, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("pat"); ap.add_argument("--n", type=int, default=2); ap.add_argument("--files", default=""); ap.add_argument("--w", type=int, default=45)
a = ap.parse_args(); rx = re.compile(a.pat)
d = json.load(open(os.path.join(HERE, "scan.json"))); k = 0
sel = a.files.split(",") if a.files else None
def preview_lines(f):
    """line numbers inside the chapter-top '你将学会' list (before first h2)."""
    first_h2 = next((h["line"] for h in f["headings"] if h["level"] == 2), 10**9)
    out = set(); on = False
    for i, l in enumerate(f["lines"], 1):
        if i >= first_h2: break
        if "你将学会" in l: on = True; out.add(i); continue
        if on:
            if l.strip() == "---": break
            out.add(i)
    return out
for f in d:
    if f["path"].endswith("index.md"): continue
    if sel and not any(f["path"].startswith(s) for s in sel): continue
    skip = preview_lines(f)
    for sp in f["spans"]:
        if sp["line"] in skip: continue
        if rx.search(sp["tex"]):
            line = f["lines"][sp["line"]-1]
            if sp.get("end") is None:
                ctx = "$$" + sp["tex"].replace("\n", " ")[:2*a.w] + "$$"
            else:
                c0, c1 = sp["col"], sp["end"]; ctx = line[max(0,c0-a.w):c0] + "⟦" + line[c0:c1][:70] + "⟧" + line[c1:c1+a.w]
            print("%s:%d  %s" % (f["path"][:9].replace("part","p").replace("-",""), sp["line"], ctx.replace("\n"," ")))
            k += 1
            if k >= a.n: sys.exit()
