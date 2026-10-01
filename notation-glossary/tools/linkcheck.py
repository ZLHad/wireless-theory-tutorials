#!/usr/bin/env python3
"""linkcheck.py <built_dir> page.html [...]: every <a href> in article must hit an existing file and id."""
import os, re, sys, html
from urllib.parse import unquote
built = sys.argv[1]
bad = 0; n = 0
idcache = {}
def ids(f):
    if f not in idcache:
        s = open(f, encoding="utf-8").read()
        idcache[f] = set(re.findall(r'\bid="([^"]+)"', s))
    return idcache[f]
for page in sys.argv[2:]:
    src = os.path.join(built, page)
    s = open(src, encoding="utf-8").read()
    art = s[s.find("<article"):s.find("</article>")]
    for href in re.findall(r'<a[^>]+href="([^"]+)"', art):
        href = html.unescape(href)
        if href.startswith(("http", "mailto:")) or href.startswith("#__") : continue
        if href.startswith("#") and "headerlink" in href: continue
        path, _, frag = href.partition("#")
        tgt = os.path.normpath(os.path.join(os.path.dirname(src), unquote(path))) if path else src
        n += 1
        if not os.path.exists(tgt):
            print("MISSING FILE", page, href); bad += 1; continue
        if frag and unquote(frag) not in ids(tgt):
            print("MISSING ID", page, href); bad += 1
print("checked", n, "links; bad", bad)
