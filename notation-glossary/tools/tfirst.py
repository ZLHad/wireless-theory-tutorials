#!/usr/bin/env python3
"""tfirst.py 'regex' [--n 3] [--w 70] [--all-files]
First N plain-text occurrences (reading order; skips index.md unless --all-files),
outside code fences, with section heading + anchor id (anchors.json) + counts per file."""
import json, os, re, argparse
from symq import heading_at

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("pat"); ap.add_argument("--n", type=int, default=3); ap.add_argument("--w", type=int, default=70)
ap.add_argument("--all-files", action="store_true"); ap.add_argument("--counts", action="store_true")
a = ap.parse_args()
rx = re.compile(a.pat)
data = json.load(open(os.path.join(HERE, "scan.json")))
anc = json.load(open(os.path.join(HERE, "anchors.json")))


def anchor_for(path, ln):
    best = None
    for h in anc[path]:
        if h["line"] > ln:
            break
        if h["level"] in (2, 3):
            best = h
    return best


shown = 0
counts = []
for d in data:
    if not a.all_files and d["path"].endswith("index.md"):
        continue
    in_f = False
    c = 0
    for ln, line in enumerate(d["lines"], 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_f = not in_f
            continue
        if in_f:
            continue
        for m in rx.finditer(line):
            c += 1
            if shown < a.n:
                h = anchor_for(d["path"], ln)
                lo, hi = max(0, m.start() - a.w), min(len(line), m.end() + a.w)
                print("%s L%d  §%s  #%s" % (d["path"], ln, h["text"][:40] if h else "(章首)", h["id"] if h else ""))
                print("    …%s⟦%s⟧%s…" % (line[lo:m.start()], m.group(0), line[m.end():hi]))
                shown += 1
    if c:
        counts.append("%s:%d" % (d["path"].split("/")[0] + "/" + d["path"].split("/")[1][:2], c))
if a.counts:
    print("  counts:", " ".join(counts))
