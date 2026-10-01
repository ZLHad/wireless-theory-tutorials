# -*- coding: utf-8 -*-
"""生成站点的统计图（SVG，浅色、深色各一份）。

用法（在本目录下）：
    /usr/bin/python3 build.py            # 全部重画，写到 ../site/docs/assets/charts/
    /usr/bin/python3 build.py p0-03-3    # 只画指定的图
    /usr/bin/python3 build.py --png ...  # 另出 prev/<id>.png 预览，方便目视检查

数据在 src/<id>.mmd（沿用 mermaid xychart / quadrantChart 写法，正文里不再放图源）；
标题、轴名、图例、刻度等标注写在 ov_*.py 的 OV 字典里，公式用 LaTeX（matplotlib mathtext）。
图在哪一页用到，见 src/index.json。"""
import sys, os, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chartlib import parse_xy, draw_xy, parse_quadrant, draw_quadrant
OUT = os.path.join(HERE, '..', 'site', 'docs', 'assets', 'charts')
PREV = os.path.join(HERE, 'prev')
args = [a for a in sys.argv[1:] if not a.startswith('--')]
png = '--png' in sys.argv
OV = {}
for f in sorted(glob.glob(os.path.join(HERE, 'ov_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for k, v in mod.OV.items():
        if k in OV:
            raise SystemExit('duplicate id %s in %s' % (k, f))
        OV[k] = v
os.makedirs(OUT, exist_ok=True)
if png:
    os.makedirs(PREV, exist_ok=True)
ids = args or sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(HERE, 'src', '*.mmd')))
for cid in ids:
    src = open(os.path.join(HERE, 'src', cid + '.mmd'), encoding='utf-8').read()
    ov = OV.get(cid, {})
    if src.lstrip().startswith('quadrantChart'):
        sp, fn = parse_quadrant(src), draw_quadrant
    else:
        sp, fn = parse_xy(src), draw_xy
    fn(sp, ov, 'light', os.path.join(OUT, cid + '.svg'))
    fn(sp, ov, 'dark', os.path.join(OUT, cid + '-dark.svg'))
    if png:
        fn(sp, ov, 'light', os.path.join(PREV, cid + '.png'))
    print('ok', cid)
