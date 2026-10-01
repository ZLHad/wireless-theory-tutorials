#!/usr/bin/env python3
import re, sys
bad = 0
for p in sys.argv[1:]:
    for ln, line in enumerate(open(p, encoding="utf-8"), 1):
        l = line.rstrip("\n")
        # red lines
        if re.search(r"\\bar\\mathbf|\\tilde\\mathbf|\\hat\\mathbf|\\label\{|\\cite\{|\\newcommand|\\begin\{equation\}", l):
            print("REDLINE", p, ln); bad += 1
        # $ pairing (ignore $$ lines)
        n = len(re.findall(r"(?<!\\)\$", l))
        if n % 2:
            print("ODD $", p, ln, l[:80]); bad += 1
        # math spans
        for m in re.finditer(r"(?<!\\)\$(.+?)(?<!\\)\$", l):
            t = m.group(1)
            depth = 0; ok = True
            i = 0
            while i < len(t):
                c = t[i]
                if c == "\\": i += 2; continue
                if c == "{": depth += 1
                elif c == "}":
                    depth -= 1
                    if depth < 0: ok = False
                i += 1
            if depth != 0 or not ok:
                print("BRACE", p, ln, t[:60]); bad += 1
            if t.count("\\left") != t.count("\\right"):
                print("LEFTRIGHT", p, ln, t[:60]); bad += 1
            if l.startswith("|") and re.search(r"(?<!\\)\|", t):
                print("PIPE-IN-TABLE-MATH", p, ln, t[:60]); bad += 1
        # table column count
        if l.startswith("|") and not l.startswith("|---"):
            cols = len(re.sub(r"\$[^$]*\$", "", l).split("|")) - 2
            if cols != 4:
                print("COLS=%d" % cols, p, ln, l[:60]); bad += 1
print("issues:", bad)
