#!/usr/bin/env python3
"""Query scan.json: python3 symq.py <base-regex> [--files part1,part2] [--n 3] [--w 70] [--key]
Lists, per chapter in reading order, atom-key counts for matching bases and
the first N contexts per distinct atom key (with nearest heading)."""
import json, re, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))


def heading_at(d, ln):
    h2 = h3 = None
    for h in d["headings"]:
        if h["line"] > ln:
            break
        if h["level"] == 2:
            h2, h3 = h["text"], None
        elif h["level"] == 3:
            h3 = h["text"]
    return h2, h3


def ctx(d, sp, w):
    line = d["lines"][sp["line"] - 1]
    if sp.get("display") and "col" in sp and sp.get("end") is None:
        # display block: show previous non-empty text line tail + tex
        k = sp["line"] - 2
        while k >= 0 and not d["lines"][k].strip():
            k -= 1
        prev = d["lines"][k][-w:] if k >= 0 else ""
        return prev + " ⟦$$ " + sp["tex"].strip().replace("\n", " ")[:w] + " $$⟧"
    a = max(0, sp["col"] - w)
    b = min(len(line), sp.get("end", sp["col"]) + w)
    return ("…" if a > 0 else "") + line[a:sp["col"]] + "⟦" + line[sp["col"]:sp.get("end", sp["col"])] + "⟧" + line[sp.get("end", sp["col"]):b] + ("…" if b < len(line) else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base")
    ap.add_argument("--files", default="")
    ap.add_argument("--n", type=int, default=2)
    ap.add_argument("--w", type=int, default=60)
    ap.add_argument("--key", action="store_true", help="match regex against full atom key instead of base")
    ap.add_argument("--summary", action="store_true", help="only counts")
    a = ap.parse_args()
    data = json.load(open(os.path.join(HERE, "scan.json")))
    rx = re.compile(a.base)
    sel = a.files.split(",") if a.files else None
    for d in data:
        if sel and not any(d["path"].startswith(s) for s in sel):
            continue
        counts = {}
        first = {}
        for sp in d["spans"]:
            atoms = sp["atoms"]
            bases = sp["bases"]
            for k, b in zip(atoms, bases):
                target = k if a.key else b
                if rx.fullmatch(target):
                    counts[k] = counts.get(k, 0) + 1
                    first.setdefault(k, [])
                    if len(first[k]) < a.n and (not first[k] or first[k][-1] is not sp):
                        first[k].append(sp)
        if not counts:
            continue
        print("=" * 8, d["path"], "|", ", ".join("%s×%d" % (k, v) for k, v in sorted(counts.items(), key=lambda x: -x[1])))
        if a.summary:
            continue
        for k in sorted(counts, key=lambda x: -counts[x]):
            for sp in first[k]:
                h2, h3 = heading_at(d, sp["line"])
                print("  [%s] L%d §%s%s" % (k, sp["line"], (h2 or "")[:30], (" / " + h3[:25]) if h3 else ""))
                print("     ", ctx(d, sp, a.w))


if __name__ == "__main__":
    main()
