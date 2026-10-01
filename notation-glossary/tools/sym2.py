#!/usr/bin/env python3
"""Compact per-h2 listing: sym2.py <base-regex> [--files ..] [--w 38] [--key] [--skip regex-of-context-to-skip]
Prints for each file & h2 section: counts per key, then ONE context per distinct key (first in section)."""
import json, re, os, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("base"); ap.add_argument("--files", default=""); ap.add_argument("--w", type=int, default=38)
ap.add_argument("--key", action="store_true"); ap.add_argument("--maxkeys", type=int, default=3)
a = ap.parse_args()
rx = re.compile(a.base)
data = json.load(open(os.path.join(HERE, "scan.json")))
sel = a.files.split(",") if a.files else None
def h2of(d, ln):
    cur = ("章首", 0)
    for h in d["headings"]:
        if h["line"] > ln: break
        if h["level"] == 2: cur = (h["text"], h["line"])
    return cur
for d in data:
    if d["path"].endswith("index.md"): continue
    if sel and not any(d["path"].startswith(s) for s in sel): continue
    secs = {}; order = []
    for sp in d["spans"]:
        hit = [k for k, b in zip(sp["atoms"], sp["bases"]) if rx.fullmatch(k if a.key else b)]
        if not hit: continue
        s = h2of(d, sp["line"])
        if s not in secs: secs[s] = {"c": {}, "ex": {}}; order.append(s)
        for k in hit:
            secs[s]["c"][k] = secs[s]["c"].get(k, 0) + 1
            secs[s]["ex"].setdefault(k, sp)
    if not secs: continue
    print("== %s" % d["path"])
    for s in order:
        c = secs[s]["c"]; keys = sorted(c, key=lambda x: -c[x])
        print("  §%s L%d [%s]" % (re.sub(r"\$[^$]*\$", "·", s[0])[:26], s[1], " ".join("%s×%d" % (k, c[k]) for k in keys)))
        seen = set()
        for k in keys[:a.maxkeys]:
            sp = secs[s]["ex"][k]
            if id(sp) in seen: continue
            seen.add(id(sp))
            line = d["lines"][sp["line"] - 1]
            if sp.get("end") is None:
                t = sp["tex"].replace("\n", " ").strip()
                print("     L%d $$%s$$" % (sp["line"], t[:2*a.w]))
            else:
                c0, c1 = sp["col"], sp["end"]
                print("     L%d …%s⟦%s⟧%s…" % (sp["line"], line[max(0, c0-a.w):c0], line[c0:c1][:60], line[c1:c1+a.w]))
