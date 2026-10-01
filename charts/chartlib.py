# -*- coding: utf-8 -*-
"""把 mermaid xychart / quadrantChart 图源重画成 SVG（浅色、深色各一份）。

数据一律取自正文里的 mermaid 图源（charts/src/*.mmd 冻结副本），不重新计算。
横轴按 mermaid 的规则排点：数值区间 a --> b 时 n 个点等距铺满 [a, b]；类别轴时各类别等距。
标题、轴名、图例、刻度可用 LaTeX（matplotlib mathtext，$...$ 内不能放中文）。
"""
import re, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 中文字体取本机装了的第一种：macOS 冠黑体、苹方，Linux 思源黑体或 Noto CJK，Windows 微软雅黑。
# 站点里的 SVG 是用冠黑体画的，换字体重画，字形会略有不同。
_CJK_CANDIDATES = ['Hiragino Sans GB', 'PingFang SC', 'Source Han Sans SC', 'Noto Sans CJK SC', 'Microsoft YaHei']
_installed = {f.name for f in font_manager.fontManager.ttflist}
CJK = next((f for f in _CJK_CANDIDATES if f in _installed), 'DejaVu Sans')
plt.rcParams.update({
    'font.family': [CJK, 'DejaVu Sans'],
    'mathtext.fontset': 'cm',
    'axes.unicode_minus': True,
    'svg.fonttype': 'path',
    'svg.hashsalt': 'sibuqu',
    'figure.dpi': 100,
})

THEMES = {
    'light': dict(fg='#2b2321', sub='#5f5552', grid='#e9e3e0', spine='#b9aeab', ref='#8d7f7b',
                  colors=['#2f6fd1', '#e0552d', '#1f9d55', '#9b59b6', '#c9a227', '#17a2b8'],
                  q=['#fbeeeb', '#f7f2ec', '#f5f5f4', '#f2eff6'], qline='#d9cbc7', pt='#b71c1c'),
    'dark': dict(fg='#ece6e4', sub='#c4bbb8', grid='#383b46', spine='#6d6a72', ref='#a9a0a0',
                 colors=['#5b9cf5', '#ff7a50', '#3ccf7e', '#c08ad6', '#e8c24a', '#3cc8dc'],
                 q=['#3a2b2e', '#34312c', '#2b2d33', '#322d38'], qline='#4b4d58', pt='#ef9a9a'),
}
WIDTH = 6.88   # 英寸；正文栏宽 688 px 时 1 pt ≈ 1.39 px，10.5 pt 字约 14.6 px

def _cats(rest):
    rest = rest.strip()
    if '"' in rest:
        return [str(x) for x in json.loads(rest)]
    return [x.strip() for x in rest.strip('[]').split(',')]

def parse_xy(src):
    spec = {'series': [], 'horizontal': False}
    for raw in src.split('\n'):
        l = raw.strip()
        if not l:
            continue
        if l.startswith('xychart'):
            spec['horizontal'] = 'horizontal' in l
        elif l.startswith('title'):
            spec['title'] = l[len('title'):].strip().strip('"')
        elif l.startswith('x-axis') or l.startswith('y-axis'):
            ax = l[0]
            rest = l[len('x-axis'):].strip()
            lab = None
            m = re.match(r'^"([^"]*)"\s*(.*)$', rest)
            if m:
                lab, rest = m.group(1), m.group(2).strip()
            ent = {'label': lab}
            m = re.match(r'^(-?[\d.]+)\s*-->\s*(-?[\d.]+)$', rest)
            if m:
                ent['range'] = (float(m.group(1)), float(m.group(2)))
            elif rest.startswith('['):
                ent['cats'] = _cats(rest)
            spec[ax] = ent
        elif re.match(r'^(line|bar)\b', l):
            kind, arr = l.split(None, 1)
            spec['series'].append({'kind': kind, 'data': json.loads(arr)})
    return spec

def _style_axes(ax, T):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(T['spine'])
    ax.tick_params(colors=T['sub'], labelsize=10.5, length=3)
    ax.grid(True, color=T['grid'], linewidth=0.8)
    ax.set_axisbelow(True)

def draw_xy(spec, ov, theme, path):
    """ov 可用的键：
    文字：title xlabel ylabel legend（与序列一一对应）legend_loc（默认 'outside lower center'）legend_ncol
    横轴：xticklabels xticks=(位置, 文字) xrot xnumeric（类别本身是数时按数值摆放）xscale xlim
    纵轴：yticks=(位置, 文字) ylog10（数据是 log10 值时显示成 10^k）ylog10_step yscale ylim
    线：markers（'auto'、None、或逐条列表）styles colors（逐条给配色序号，或 'ref' 表示灰色辅助线）
    其他：size barh value_labels value_fmt hlines vlines notes"""
    T = THEMES[theme]
    fig, ax = plt.subplots(figsize=ov.get('size', (WIDTH, 4.3)), layout='constrained')
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    _style_axes(ax, T)
    xs, ys = spec['x'], spec['y']
    n = max(len(s['data']) for s in spec['series'])
    barh = ov.get('barh', False)
    if 'cats' in xs:
        if ov.get('xnumeric'):
            xpos = [float(c) for c in xs['cats']]
        else:
            xpos = list(range(len(xs['cats'])))
        ticklabels = ov.get('xticklabels', xs['cats'])
        if barh:
            ax.set_yticks(xpos); ax.set_yticklabels(ticklabels)
            ax.invert_yaxis()
        else:
            ax.set_xticks(xpos); ax.set_xticklabels(ticklabels, rotation=ov.get('xrot', 0),
                                                   ha='right' if ov.get('xrot') else 'center')
            if not ov.get('xnumeric'):
                ax.set_xlim(-0.4, len(xpos) - 0.6)
    else:
        a, b = xs['range']
        xpos = [a + (b - a) * i / (n - 1) for i in range(n)] if n > 1 else [a]
        ax.set_xlim(a, b)
    if ov.get('xscale'):
        ax.set_xscale(ov['xscale'])
    if ov.get('yscale'):
        ax.set_yscale(ov['yscale'])
    labels = ov.get('legend') or [None] * len(spec['series'])
    styles = ov.get('styles') or ['-'] * len(spec['series'])
    cidx = ov.get('colors') or list(range(len(spec['series'])))
    bars = [s for s in spec['series'] if s['kind'] == 'bar']
    nb = len(bars); bi = 0
    for k, s in enumerate(spec['series']):
        ck = cidx[k]
        c = T['ref'] if ck == 'ref' else T['colors'][ck % len(T['colors'])]
        lab = labels[k] if k < len(labels) else None
        xx = xpos[:len(s['data'])]
        if s['kind'] == 'bar':
            w = 0.72 / max(nb, 1)
            off = (bi - (nb - 1) / 2) * w; bi += 1
            pos = [x + off for x in xx]
            if barh:
                bb = ax.barh(pos, s['data'], height=w, color=c, label=lab, zorder=2)
            else:
                bb = ax.bar(pos, s['data'], width=w, color=c, label=lab, zorder=2)
            if ov.get('value_labels'):
                ax.bar_label(bb, padding=3, fontsize=9.5, color=T['sub'],
                             fmt=ov.get('value_fmt', '%g'))
        else:
            mk = ov.get('markers', 'auto')
            if isinstance(mk, list):
                mk = mk[k]
            if mk == 'auto':
                mk = 'o' if len(s['data']) <= 16 and ck != 'ref' else None
            ax.plot(xx, s['data'], color=c, linewidth=2.0 if ck != 'ref' else 1.4, marker=mk, markersize=4,
                    label=lab, linestyle=styles[k], zorder=3)
    for h in ov.get('hlines', []):
        ax.axhline(h, color=T['ref'], lw=1, ls=':', zorder=1)
    for v in ov.get('vlines', []):
        ax.axvline(v, color=T['ref'], lw=1, ls=':', zorder=1)
    if barh:
        if 'range' in ys:
            ax.set_xlim(*ys['range'])
        ax.grid(axis='y', visible=False)
    else:
        if 'range' in ys:
            ax.set_ylim(*ys['range'])
        if 'cats' in xs and not ov.get('xnumeric'):
            ax.grid(axis='x', visible=False) if bars else None
    if ov.get('ylim'):
        ax.set_ylim(*ov['ylim'])
    if ov.get('xlim'):
        ax.set_xlim(*ov['xlim'])
    if ov.get('ylog10'):
        lo, hi = ax.get_ylim()
        step = ov.get('ylog10_step', 2)
        import math
        ticks = list(range(int(math.ceil(lo / step) * step), int(math.floor(hi)) + 1, step))
        ax.set_yticks(ticks)
        ax.set_yticklabels(['$1$' if t == 0 else ('$10$' if t == 1 else '$10^{%d}$' % t) for t in ticks])
    if ov.get('yticks'):
        ax.set_yticks(ov['yticks'][0]); ax.set_yticklabels(ov['yticks'][1])
    if ov.get('xticks'):
        ax.set_xticks(ov['xticks'][0]); ax.set_xticklabels(ov['xticks'][1])
    xl = ov.get('xlabel', xs.get('label') or '')
    yl = ov.get('ylabel', ys.get('label') or '')
    if barh:
        xl, yl = yl, xl
    ax.set_xlabel(xl, color=T['fg'], fontsize=11.5)
    ax.set_ylabel(yl, color=T['fg'], fontsize=11.5)
    for note in ov.get('notes', []):
        x, y, txt = note[:3]
        kw = note[3] if len(note) > 3 else {}
        ax.annotate(txt, (x, y), fontsize=kw.get('fs', 10), color=T['sub'], ha=kw.get('ha', 'left'),
                    va=kw.get('va', 'bottom'), xytext=kw.get('off', (4, 4)), textcoords='offset points')
    title = ov.get('title', spec.get('title', ''))
    if title:
        ax.set_title(title, color=T['fg'], fontsize=12.5, loc='left', pad=10)
    if any(labels):
        loc = ov.get('legend_loc', 'outside lower center')
        nser = len([x for x in labels if x])
        ncol = ov.get('legend_ncol', nser if nser <= 4 else (nser + 1) // 2)
        if loc.startswith('outside'):
            hs, ls = ax.get_legend_handles_labels()
            if ncol < len(hs):
                # matplotlib 按列填图例；重排成按行读也是序列顺序
                rows = -(-len(hs) // ncol)
                order = [r * ncol + c for c in range(ncol) for r in range(rows) if r * ncol + c < len(hs)]
                hs, ls = [hs[i] for i in order], [ls[i] for i in order]
            lg = fig.legend(hs, ls, frameon=False, fontsize=10.5, loc=loc, ncols=ncol, handlelength=1.8, columnspacing=1.4)
        else:
            lg = ax.legend(frameon=False, fontsize=10.5, loc=loc, ncols=ov.get('legend_ncol', 1))
        for t in lg.get_texts():
            t.set_color(T['fg'])
    fig.savefig(path, format=path.rsplit('.', 1)[1], transparent=(theme == 'dark' or path.endswith('.svg')),
                metadata={'Date': None, 'Creator': None} if path.endswith('.svg') else None,
                facecolor='white' if path.endswith('.png') and theme == 'light' else 'none')
    plt.close(fig)

def parse_quadrant(src):
    spec = {'points': [], 'q': {}}
    for raw in src.split('\n'):
        l = raw.strip()
        if l.startswith('title'):
            spec['title'] = l[len('title'):].strip().strip('"')
        elif l.startswith('x-axis') or l.startswith('y-axis'):
            spec[l[0]] = re.findall(r'"([^"]*)"', l)
        elif l.startswith('quadrant-'):
            spec['q'][int(l[len('quadrant-')])] = l.split(None, 1)[1].strip().strip('"')
        else:
            m = re.match(r'^"([^"]+)"\s*:\s*\[\s*([\d.]+)\s*,\s*([\d.]+)\s*\]', l)
            if m:
                spec['points'].append((m.group(1), float(m.group(2)), float(m.group(3))))
    return spec

def draw_quadrant(spec, ov, theme, path):
    """ov 可用的键：title x y（两端文字）q（象限文字，可换行可含 LaTeX）qpos{k:(x,y,ha,va)}
    pname{原名:显示名} poff{原名:(dx,dy,ha,va)} size"""
    T = THEMES[theme]
    fig, ax = plt.subplots(figsize=ov.get('size', (WIDTH, 5.6)), layout='constrained')
    fig.patch.set_alpha(0)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    rect = {1: (0.5, 0.5), 2: (0, 0.5), 3: (0, 0), 4: (0.5, 0)}   # mermaid：1 右上、2 左上、3 左下、4 右下
    for k, (x0, y0) in rect.items():
        ax.add_patch(plt.Rectangle((x0, y0), 0.5, 0.5, facecolor=T['q'][k - 1], edgecolor='none', zorder=0))
    ax.axhline(0.5, color=T['qline'], lw=1); ax.axvline(0.5, color=T['qline'], lw=1)
    qlab = ov.get('q', spec['q']); qpos = ov.get('qpos', {})
    for k, (x0, y0) in rect.items():
        if k in qlab:
            x, y, ha, va = qpos.get(k, (x0 + 0.25, y0 + 0.47, 'center', 'top'))
            ax.text(x, y, qlab[k], ha=ha, va=va, fontsize=10.5, color=T['fg'], zorder=2, linespacing=1.5,
                    multialignment='center')
    poff = ov.get('poff', {}); pname = ov.get('pname', {})
    for name, x, y in spec['points']:
        ax.scatter([x], [y], s=34, color=T['pt'], zorder=4)
        dx, dy, ha, va = poff.get(name, (0, -8, 'center', 'top'))
        ax.annotate(pname.get(name, name), (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va=va,
                    fontsize=9.5, color=T['sub'], zorder=4)
    for s in ax.spines.values():
        s.set_color(T['spine'])
    ax.set_xticks([]); ax.set_yticks([])
    xl = ov.get('x', spec['x']); yl = ov.get('y', spec['y'])
    ax.set_xlabel('← ' + xl[0] + '　　　' + xl[1] + ' →', color=T['fg'], fontsize=10.5)
    ax.set_ylabel('← ' + yl[0] + '　　　' + yl[1] + ' →', color=T['fg'], fontsize=10.5)
    title = ov.get('title', spec.get('title', ''))
    if title:
        ax.set_title(title, color=T['fg'], fontsize=12.5, loc='left', pad=10)
    fig.savefig(path, format=path.rsplit('.', 1)[1], transparent=(theme == 'dark' or path.endswith('.svg')),
                metadata={'Date': None, 'Creator': None} if path.endswith('.svg') else None,
                facecolor='white' if path.endswith('.png') and theme == 'light' else 'none')
    plt.close(fig)
