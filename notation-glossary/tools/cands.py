#!/usr/bin/env python3
"""cands.py <file-prefix> [--min 5] [--w 36]: per-chapter candidate core symbols
(atom keys with count>=min, excluding bare single Latin letters), first context (skipping preview)."""
import json, re, os, sys, argparse
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
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("pref"); ap.add_argument("--min", type=int, default=5); ap.add_argument("--w", type=int, default=36)
ap.add_argument("--all", action="store_true")
a = ap.parse_args()
d = json.load(open(os.path.join(HERE, "scan.json")))
for f in d:
    if not f["path"].startswith(a.pref) or f["path"].endswith("index.md"): continue
    skip = preview_lines(f)
    cnt, first = {}, {}
    for sp in f["spans"]:
        if sp["line"] in skip: continue
        for k in sp["atoms"]:
            cnt[k] = cnt.get(k, 0) + 1
            first.setdefault(k, sp)
    keys = [k for k in cnt if cnt[k] >= a.min and (a.all or not re.fullmatch(r"[a-zA-Z]", k))]
    keys.sort(key=lambda k: first[k]["line"])
    print("=====", f["path"], len(keys))
    for k in keys:
        sp = first[k]; line = f["lines"][sp["line"]-1]
        if sp.get("end") is None: ctx = "$$" + sp["tex"].replace("\n", " ")[:60]
        else:
            c0, c1 = sp["col"], sp["end"]; ctx = line[max(0,c0-a.w):c0] + "⟦" + line[c0:c1][:50] + "⟧" + line[c1:c1+a.w//2]
        print("  %-22s ×%-3d L%-4d %s" % (k[:22], cnt[k], sp["line"], ctx.replace("\n"," ")))
