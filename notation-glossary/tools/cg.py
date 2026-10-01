#!/usr/bin/env python3
"""cg.py PATTERN [--filter RX] [--w N] [--max N] files...  : context grep (python regex)."""
import re, sys, argparse
ap = argparse.ArgumentParser()
ap.add_argument("pat"); ap.add_argument("files", nargs="+")
ap.add_argument("--filter", default=None); ap.add_argument("--w", type=int, default=90); ap.add_argument("--max", type=int, default=12)
a = ap.parse_args()
rx = re.compile(a.pat); fx = re.compile(a.filter) if a.filter else None
for f in a.files:
    n = 0
    for ln, line in enumerate(open(f, encoding="utf-8"), 1):
        for m in rx.finditer(line):
            lo, hi = max(0, m.start() - a.w), min(len(line), m.end() + a.w)
            seg = line[lo:hi].rstrip("\n")
            if fx and not fx.search(seg): continue
            if n == 0: print("===", f)
            print("  L%d: %s" % (ln, seg)); n += 1
            if n >= a.max: break
        if n >= a.max: break
