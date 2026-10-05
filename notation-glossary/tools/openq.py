#!/usr/bin/env python3
"""Generate site/docs/open-problems.md (开放问题总表).

Usage: openq.py <docs_dir> <built_site_dir> <out.md>

Links are resolved by heading text against the built HTML (not by line numbers), so the page
survives edits that shift lines.  Counts come from the "## 开放问题" section at the end of each
chapter: list items (`1.`, `-`) and bold-led paragraphs count as items; whole-line bold group
headers and "**预告。**" paragraphs do not.  An item's status is its first 【…】 label.
"""
import collections, glob, html, os, re, sys

DOCS, BUILT, OUT = sys.argv[1:4]
PARTS = [('part1', '第一部 · 环境的科学'), ('part2', '第二部 · 链的定理'),
         ('part3', '第三部 · 网络的优化论'), ('part4', '第四部 · 群体的决策论')]
PART_SHORT = {'part1': '第一部', 'part2': '第二部', 'part3': '第三部', 'part4': '第四部'}


def squash(t):
    t = re.sub(r'^\s*\d+(?:\.\d+)+\s+', '', t)   # 标题开头的节号（如 4.3、4.3.1）不参与匹配
    return re.sub(r'[\s"“”「」]+', '', t)


_ids = {}


def heading_ids(page):
    """[(level, text, id)] for h1–h3 inside <article> of a built page."""
    if page not in _ids:
        s = open(os.path.join(BUILT, page.replace('.md', '.html')), encoding='utf-8').read()
        art = s[s.find('<article'):s.find('</article>')]
        out = []
        for m in re.finditer(r'<h([1-3]) id="([^"]+)"[^>]*>(.*?)</h\1>', art, re.S):
            txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(3))).replace('¶', '').strip().rstrip('#').strip()
            out.append((int(m.group(1)), txt, m.group(2)))
        _ids[page] = out
    return _ids[page]


def link(page, prefix, text):
    """Markdown link to the heading on `page` whose text starts with `prefix` (math-free prefix)."""
    want = squash(prefix)
    hits = [i for lv, t, i in heading_ids(page) if squash(t).startswith(want)]
    if len(hits) > 1:
        hits = [i for lv, t, i in heading_ids(page) if squash(t) == want] or hits
    if len(hits) != 1:
        sys.exit(f'heading {prefix!r} on {page}: {len(hits)} hits')
    return f'[{text}]({page}#{hits[0]})'


def chap(page):
    """Short link text: 第一部第 8 章 · <title after the dot>."""
    first = open(os.path.join(DOCS, page), encoding='utf-8').readline()
    m = re.match(r'#\s*(\d+)\s*·\s*(.*)', first)
    return m.group(1), m.group(2).strip()


def chap_link(page, prefix=None):
    n, title = chap(page)
    text = f'{PART_SHORT[page.split("/")[0]]}第 {n} 章 · {title.split("：")[0]}'
    if prefix is None:
        return f'[{text}]({page})'
    return link(page, prefix, text)


# ---------------------------------------------------------------- section 1
P1, P2, P3, P4 = ('part1/10-research-agenda.md', 'part2/07-research-agenda.md',
                  'part3/09-research-agenda.md', 'part4/09-research-agenda.md')
ROWS = [
    ('第一部 · 环境', 'Q1 有效维度 $d_{\\mathrm{eff}}(E;\\varepsilon)$', link(P1, 'Q1 · 静力学的接口', 'Q1 · 静力学的接口'),
     link('part1/08-dimension-and-prediction.md', 'Q1 的形式化', '第 8 章 · Q1 的形式化')),
    ('', 'Q2 预测半径', link(P1, 'Q2 · 预测论的接口', 'Q2 · 预测论的接口'),
     link('part1/08-dimension-and-prediction.md', 'Q2 的形式化', '第 8 章 · Q2 的形式化')),
    ('', 'Q3 知识汇率 $\\Delta C(R_{\\mathrm{env}})$【开放·本站提法】', link(P1, 'Q3 · 价值论的接口', 'Q3 · 价值论的接口'),
     link('part1/09-exchange-and-universality.md', '"CKM 的香农曲线"', '第 9 章 · CKM 的香农曲线')),
    ('', 'Q4 衰落的统计力学与平均情形', link(P1, 'Q4 · 统计力学的接口', 'Q4 · 统计力学的接口'),
     link('part1/09-exchange-and-universality.md', '衰落的统计力学', '第 9 章 · 衰落的统计力学')),
    ('第二部 · 链', '定理一 · 知识排序', link(P2, '7.3 定理一', '7.3 定理一'), chap_link('part2/02-blackwell.md')),
    ('', '定理二 · 任务格与任务充分统计量', link(P2, '7.4 定理二', '7.4 定理二'), chap_link('part2/03-task-knowledge-lattice.md')),
    ('', '定理三 · 物理泛化界', link(P2, '7.5 定理三', '7.5 定理三'), chap_link('part2/04-environment-generalization.md')),
    ('', '暗线 · 认知平衡点', link(P2, '7.6 暗线', '7.6 暗线'), chap_link('part2/05-cognitive-triangle.md')),
    ('第三部 · 优化与网络', '$V(I)$ · 信息的价值函数【本站原创】', link(P3, '缺失定理一', '缺失定理一'), chap_link('part3/05-price-of-prediction.md')),
    ('', '$C(\\varepsilon)$ · $\\varepsilon$-最优性的比特成本', link(P3, '缺失定理二', '缺失定理二'), chap_link('part3/06-communication-lower-bounds.md')),
    ('', 'PoL · 分层的代价【本站原创】', link(P3, '缺失定理三', '缺失定理三'), chap_link('part3/07-price-of-layering.md')),
    ('', '暗线 · 随机性如何决定可解性（average-case）', link(P3, '暗线：随机性如何决定可解性', '暗线'),
     link('part3/03-nonconvex-era.md', '3.7 之谜的形式化', '第三部第 3 章 · 3.7 之谜的形式化')),
    ('第四部 · 群体', '定理一 · 信息结构相图', link(P4, '9.3 定理一', '9.3 定理一'), chap_link('part4/03-information-structure-phase-diagram.md')),
    ('', '定理二 · 协商的最小话费', link(P4, '9.4 定理二', '9.4 定理二'),
     chap_link('part4/04-coordination-information-theory.md') + '、' + chap_link('part4/05-shared-world-model.md')),
    ('', '定理三 · 学习动力学相图', link(P4, '9.5 定理三', '9.5 定理三'), chap_link('part4/06-learning-dynamics.md')),
    ('', '定理四 · 协同增益的 scaling law', link(P4, '9.6 定理四', '9.6 定理四'),
     chap_link('part4/07-mean-field.md') + '、' + chap_link('part4/08-network-games.md')),
]

# ---------------------------------------------------------------- section 2
def norm(lab):
    if lab is None:
        return '无标签'
    if lab.startswith('开放') or '·开放' in lab:
        return '开放'
    if lab.startswith('部分'):
        return '部分结果'
    if lab.startswith('已解决'):
        return '已解决'
    if '预印本' in lab:
        return '预印本'
    if '表述待核' in lab:
        return '表述待核'
    if '空白' in lab:
        return '空白'
    if '本站提法' in lab:
        return '本站提法'
    return lab[:8]


def count(page):
    """章末"开放问题"一节的条目计数。按条目块解析：
    题目行 = 带【】或以 Q/P 编号开头的粗体行、或顶层列表项、或粗体开头的段落；
    题目下的分条细节、"精确陈述/第一步"等粗体引导段、缩进续行都归入该条；
    以冒号结尾的说明句后面的列表、"预告"段与分组小标题不计。状态取整块里第一个【】。"""
    lines = open(os.path.join(DOCS, page), encoding='utf-8').read().split('\n')
    i = next(k for k, l in enumerate(lines) if re.sub(r'\s*\{#[^}]*\}$', '', l.strip()) == '## 开放问题')
    j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith('## ')), len(lines))
    labq = lambda l: re.search(r'【[^】]*】', l) or re.match(r'^\*\*(Q\d|P\d)', l)
    blocks, cur, in_item, prev, trailing, after_prose = [], None, False, '', False, False
    for l in lines[i + 1:j]:
        if not l.strip():
            continue
        whole_bold = re.match(r'^\*\*[^*]+\*\*\s*$', l)
        start = False
        if not re.match(r'^(\d+\. |- )', l):
            trailing = False
        if l.startswith('**预告'):
            in_item, cur = False, None
        elif whole_bold and not labq(l):
            in_item, cur, after_prose = False, None, False   # 分组小标题
        elif whole_bold or (l.startswith('**') and (labq(l) or not in_item)):
            start, in_item = True, True
        elif re.match(r'^(\d+\. |- )', l):
            if blocks and cur is None and (after_prose or trailing):
                trailing = True                         # 条目列完以后、说明段落后面的列表不计
            elif not in_item:
                start = True
        elif not l.startswith(' '):
            if not in_item:
                cur = None                              # 说明段
                after_prose = True
        if start:
            cur = [l]; blocks.append(cur); after_prose = False
        elif cur is not None:
            cur.append(l)
        prev = l
    c = collections.Counter()
    for blk in blocks:
        m = re.search(r'【([^】]*)】', '\n'.join(blk))
        c[norm(m.group(1) if m else None)] += 1
    return c


OTHER_ORDER = ['已解决', '预印本', '表述待核', '空白', '本站提法', '无标签']
tables, grand = [], collections.Counter()
for part, name in PARTS:
    rows, tot = [], collections.Counter()
    for page in sorted(p.replace(DOCS + '/', '') for p in glob.glob(f'{DOCS}/{part}/[0-9][0-9]-*.md')):
        c = count(page)
        tot.update(c)
        n, title = chap(page)
        other = '、'.join(f'{k} {c[k]}' for k in OTHER_ORDER if c.get(k)) or '—'
        rows.append(f"| {link(page, '开放问题', f'第 {n} 章 · ' + title.split('：')[0])} | {sum(c.values())} | {c.get('开放', 0)} | {c.get('部分结果', 0)} | {other} |")
    grand.update(tot)
    other = '、'.join(f'{k} {tot[k]}' for k in OTHER_ORDER if tot.get(k)) or '—'
    rows.append(f"| **合计** | **{sum(tot.values())}** | **{tot.get('开放', 0)}** | **{tot.get('部分结果', 0)}** | {other} |")
    tables.append((part, name, rows))

n_chap = sum(len(r) - 1 for _, _, r in tables)
N = sum(grand.values())

# ---------------------------------------------------------------- criteria
# 第一节末的"从定理到判据"：16 条缺失定理各补四列（判据形式、改变的设计决策、运行期是否因果可行、
# 复杂环境下的验证路径），2026-10-02 加；{LINK98} 换成第四部 9.8 节的链接（自评框在那里）。
CRITERIA = r'''
### 从定理到判据 { #criteria }

上面那张表里的十六条大多是 converse 的形态：资源不超过多少，任何方案都做不到多少。反过来读，每一条都是一条潜在的工程判据，但从定理到判据还隔着两道关：规则要能在运行期只用当时拿得到的量算出来，结论要能在真实的复杂环境里复现。下表给每条补四列，依次写判据长什么样、它改掉哪个具体决定、运行期能不能算（可以 / 部分可以 / 只能设计期）、怎样在射线追踪数字孪生、实测数据或 3GPP 评估方法里检验以及哪一步最容易出错；四列都是本站的翻译【本站判断】，定理的状态以各章原文为准。

<div class="criteria-table" markdown>

| 缺的定理 | 判据形式 | 改变的设计决策 | 运行期是否因果可行 | 复杂环境下的验证路径 |
|---|---|---|---|---|
| 第一部 · Q1 有效维度 | 上限：噪声水平 $\varepsilon$ 下信道只分辨得出 $d_{\mathrm{eff}}(E;\varepsilon)$ 个环境方向，多出的环境参数标定不出来；阶数 $\Theta((ka)^{d-1})$ 是猜想 8.1 | 数字孪生与环境重建的参数化：标定几个几何与材质参数，体素有没有必要细到 $\lambda/10$ | 只能设计期：要对环境模型求 $\mathrm{D}\Phi[E]$ 的奇异值 | 可微射线追踪在孪生上算 $\mathrm{D}\Phi$ 的谱，扫频率与孔径看阶数；最易出错在环境参数的选法与归一化会改变谱 |
| 第一部 · Q2 预测半径 | 阈值：离采样域超过 $r_{\max}$ 处任何外推都没有信息，只能加测；墙内提高 SNR 只按 $1-\ln\delta/\ln\varepsilon$ 多换半径（猜想 8.2） | 信道预测与 CKM 在哪里外推、在哪里补测；加采样点还是提高 SNR | 部分可以：$\varepsilon$、$\delta$ 已知，$r_{\max}$ 取决于最近的有效散射体，要靠地图或孪生事先估 | 孪生与实测上扫外推距离和 SNR，看各条误差曲线是否在同一 $r$ 归零；最易出错是把模型失配或时间轴的极限当成空间硬墙 |
| 第一部 · Q3 知识汇率 | 边际：环境描述再加 1 比特能买回 $\Delta C'(R_{\mathrm{env}})$，低于获取与维护的边际成本就停；曲线中段形状未知 | CKM 与数字孪生建多精细（要不要材质层、家具层），建图预算与导频预算怎么分 | 只能设计期：$\Delta C$ 对一切环境编码取上确界，是分布层面的量 | 孪生里按轮廓、高度、材质、家具逐级加描述，测容量增益；最易出错在环境失真度量未定，降精度方式不同曲线就不同 |
| 第一部 · Q4 统计力学与平均情形 | 相图：$N_{\mathrm{eff}}\gg1$ 时统计模型够用，$N_{\mathrm{eff}}\lesssim1$ 时几何知识最值钱（相边界无定理）；检测：$\rho>2\log N$ 时 $O(N^3)$ 算法已到 ML 门限（候选结果） | 新频段、大阵列要不要配 CKM 或射线追踪；检测器用 LMMSE 取整加贪心翻转，还是球形译码 | 部分可以：$\rho$、$N$ 已知；分辨单元内各径分不开，$N_{\mathrm{eff}}$ 只能借 K 因子粗估（"一条主径、其余等幅"时可以换算）【本站判断】 | 宽带实测按不同带宽与孔径重算 $N_{\mathrm{eff}}$ 并拟合衰落分布，检测改用实测的相关、非方形信道；最易出错在 $N_{\mathrm{eff}}$ 随测量系统的分辨率而变 |
| 第二部 · 定理一 知识排序 | 排序：A 能对一切任务顶替 B 当且仅当 $\delta(\mathcal{E}_A,\mathcal{E}_B)=0$，否则顶替的风险至多多付 $\|L_T\|\delta$；码本对有跨界胞腔即 $\delta\ge1/2$（引理 7.3） | 两侧模型跨厂商能否互换，码本要不要设计成嵌套；地图、量化 CSI、感知模态之间谁能顶替谁 | 只能设计期：亏格是对全部环境状态取最坏的线性规划，要两张完整的似然表 | 公开 CSI 数据集向量量化后批量算亏格表，再拿跨厂商数据集核对；最易出错在离散化不稳，先验质量 1% 的跨界胞腔就能吃满 $1/2$ |
| 第二部 · 定理二 任务格 | 下界与清单：单任务要达最优至少 $H(\mathcal{S}_T)$ 比特；任务类存各任务充分划分的并 $\bigvee_T\mathcal{S}_T$ 就够，多存的层冗余（有限、无平局时已证） | CKM 存哪几层（波束索引图加 LoS 或 K 因子图）；任务导向反馈的载荷，64 个波束不超过 6 比特 | 只能设计期：充分划分要用全部状态的似然与损失算，运行期只能查表执行 | 射线追踪生成真实 DFT 波束下的状态与观测，算各任务的最优动作划分，比较分层存与全量存；最易出错在波束边界附近的平局 |
| 第二部 · 定理三 物理泛化界 | 阈值：特征级偏移 $d_{\mathrm{feat}}<\rho_{\mathrm{feat}}$ 时可复用，否则本地重学；相位型 $\lambda/4$，结构型约 $L$（单散射体已证，多散射体为猜想 4.5） | 模型哪些层跨站点共享、哪些逐站点学；CKM 哪些层能迁移；何时重训或回退 | 部分可以：偏移本身看不见，只能用复测链路上按 $\Delta_{\mathrm{feat}}$ 归一化的特征残差判断 | 可微射线追踪挪墙 0–30 mm，比 3.5 与 28 GHz 的饱和点，再按 TR 38.843 的 Case 1–4 跨数据集测（那些数据集也是仿真生成的，最后仍要实测）；最易出错在遮挡，它是跳变，不在界内 |
| 第二部 · 暗线 认知平衡点 | 比例与门槛：最优感知占比 $\alpha^\star$ 由等边际条件定；饱和型汇率下 $\Lambda\le\Lambda_c=C_0/\Delta C_{\max}$ 的层不建耐用知识（模型内已证） | 数字孪生各层的更新预算与周期：建筑层、家具层、行人层各花多少资源去测 | 只能设计期：要知道 $\kappa$、$T_{\mathrm{env}}$ 与 $\Delta C$ 曲线，运行期改用可观测残差触发 | 试验台人为改变 $T_{\mathrm{env}}$，让 $\Lambda$ 跨三个数量级，测 $\alpha^\star$ 的对数斜率 $\nu$；最易出错在 $\Delta C$ 可能分段换形状 |
| 第三部 · $V(I)$ | 价目表：预测通道每多 1 比特省多少由 $V$ 的斜率给出；两点作业时任何策略的误判率至少 $h_2^{-1}((h_2(q)-R)^{+})$ | 长度预测器做多准，要不要多传一个分位数；预测卸载里给预测信息多少比特 | 部分可以：作业做完会揭晓真实大小，$I(S;\hat{S})$ 可用日志滚动估，排队侧常数仍靠模型 | 用真实请求日志回放，带上批处理与显存约束；最易出错在真实服务不是 M/G/1，误判率换算成时延的常数会变 |
| 第三部 · $C(\varepsilon)$ | 下界：任何达到 $\varepsilon$-最优的协议至少交换 $C(\varepsilon)$ 比特，预算不够就加比特或放宽 $\varepsilon$；两小区 $\varepsilon=0.01$ 时已知约 56 比特够用（可达一侧） | 协作要交换多少 CSI 比特、回传给多少；联邦学习压缩到多狠；两侧 CSI 模型的接口传什么 | 只能设计期：$\varepsilon$ 量的是离未知最优值 $f^{*}$ 的差距 | 系统级仿真加射线追踪信道做两小区功控，量化交换后测 $\varepsilon$ 与比特数的曲线；最易出错在下界是渐近的，异质度项还缺 |
| 第三部 · PoL | 比值下界：架构内任何算法至少差 $\mathrm{PoL}$ 倍；接口维度不小于耦合资源维度 $m$ 时为 $1+O(m/n)$（$n$ 为任务数），否则存在实例随缺失维度线性增长 | 要不要分层、接口回传什么：分割推理的切点由编排层定还是联合定，补几比特能把损失买断 | 只能设计期：对实例取最坏、对架构内一切算法取最好，是架构层面的量 | 算力网络孪生回放真实信道与负载，小实例上穷举架构内最优与联合最优；最易出错在"架构"本身还没有公认的形式化 |
| 第三部 · 暗线 average-case | 警示：近最优解的重叠度出现间隙时，一大类稳定算法（局部、低度、Langevin）必败；这是对算法类的下界，不是 converse | 要不要上学习式或扩散式求解器，哪些实例族要留经典算法兜底 | 只能设计期：要对实例分布大量采样，求近最优解集的重叠分布 | 用射线追踪或实测信道代替 i.i.d. 瑞利生成实例，数值普查重叠分布；最易出错在低度方法本身的地位正被质疑 |
| 第四部 · 定理一 信息结构相图 | 阈值（已证）：回传时延满足三角不等式时，$t_{ij}\le p_{ij}$ 对一切 $i,j$ 等价于二次不变，协作综合是凸的；出界只是不再凸，增益未必消失 | 联合传输、每时隙协调还是半静态协调；CoMP 簇的直径；哪些功能放进近实时 RIC | 可以：回传时延与按帧结构定的耦合时标，运行期都已知 | 试验台或系统级仿真接入实测的回传时延分布；最易出错在抖动与丢包让信息结构变成随机的，整数时隙模型失效 |
| 第四部 · 定理二 协商话费 | 下界：每对坏时隙率 $\epsilon$ 至少付 $1-h(\epsilon)$ 比特/时隙；星形干扰图上广播比点对点省 $K-1$ 倍；纯 Nash 要 $\Omega(2^N)$，相关均衡多项式即可 | 协调信令走广播还是点对点；协议目标定纯 Nash 还是相关均衡；分布式调度的开销预算 | 部分可以：$\epsilon$ 与干扰图已知，但下界是长块渐近的，短块协议只能拿它作参照 | 系统级仿真里按真实信令格式实现协议，测开销离下界多远；最易出错在外围互扰的拓扑只有内外界 |
| 第四部 · 定理三 学习动力学相图 | 阈值（两小区已证）：学习率低于 $\eta^\star=\frac{2}{x^\star(1-x^\star)(D_A+D_B)}$ 对称模才稳，总量口径再除以度 $d$；对称混合点在含边的图上不是吸引子 | MARL 功控的学习率与回报归一化（Mb/s 直接进 softmax 等于放大几十倍）；初始化要不要打破对称 | 部分可以：$\eta$ 与度 $d$ 已知，代价斜率与 $x^\star$ 要在仿射模型下在线估 | 系统级仿真在射线追踪拓扑与真实业务下扫 $\eta$，记录吸引子类型；最易出错在代价对负载并非仿射，更新也是异步的 |
| 第四部 · 定理四 scaling law | 上界与最优点：协作谱效有与功率无关的天花板（定理 8.9）；Wyner 模型里最优簇 $K^\star$ 只由 $(\alpha,\tau/L)$ 定，再大开销就吃掉增益 | CoMP 簇大小与导频、回传预算联合设计；耦合度低时干脆不协作 | 部分可以：簇内外功率比 $\kappa$ 可从测量报告估，开销已知；二维几何修正要事先算 | 按 TR 36.819 附录 A 的 CoMP 系统级仿真假设做仿真，再上射线追踪城区部署，对照外场增益通常不超过 30%；最易出错在二维几何（3.22 对 2.54） |

</div>

*怎么读这张表：先看第四列。标"只能设计期"的八条，要用的东西运行期拿不到：环境模型的真值、全部状态的似然表、汇率曲线或实例分布、未知的最优值，或对一切方案取的极值；它们适合在设计阶段定预算、定周期、定架构，不能直接当运行期的触发器。要在运行期用，得换成看得见的代理量，第二部定理三那一行用复测链路上的特征残差代替看不见的环境偏移，就是一例。再看第五列的"最易出错"，多半落在玩具模型约掉的东西上：遮挡、回传抖动、非仿射的代价、二维几何。第二、三列写的是定理证出来以后的样子；哪些今天已经能用、哪些只适合教学或警示，见{LINK98}的自评框。*
'''

# ---------------------------------------------------------------- page
out = [
    '# 开放问题总表',
    '',
    f'本站要做的，是把 AI 原生无线网络底下还没有定理的地方系统地暴露出来。这一页不重复正文，只把散在四部 {n_chap} 章里的开放问题编成索引：第一节列四部各自立下的缺失定理，再把每一条反过来读成工程判据；第二节逐章列出章末"开放问题"一节的条数与状态。状态标签照录各章原文，含义见首页的[诚实声明与状态标签](index.md#诚实声明与状态标签)；四部如何合成一个元命题，以及带数字的总表，见{link(P4, "9.8 全站收尾", "第四部 9.8 节")}。',
    '',
    '## 一、四部各自缺的定理 { #theorems }',
    '',
    '每一条在所属部的研究纲领章里都有专节，多数写成"四件套"：精确陈述、已知工具箱、第一步可证引理、AI 可攻子问题。第三列链到那一节，第四列链到正文里最早把它立起来的章节。',
    '',
    '| 部 | 缺的定理 | 研究纲领里的四件套 | 正文主要展开处 |',
    '|---|---|---|---|',
] + [f'| {a} | {b} | {c} | {d} |' for a, b, c, d in ROWS] + [
    '',
    '想直接找能动手的题目：四个研究纲领章都给了 AI 可攻子问题；第二、三、四部还各自给出了四维打分表——'
    + link(P2, 'AI 适配性打分', '第二部 7.7') + '、' + link(P3, '四维打分与三线路线图', '第三部四维打分') + '、'
    + link(P4, 'AI 适配性打分', '第四部 9.7') + '。第一部的四份清单分别在 Q1–Q4 各节的"四件套"末尾。',
    '',
] + CRITERIA.strip('\n').replace('{LINK98}', link(P4, '9.8 全站收尾', '第四部 9.8 节')).split('\n') + [
    '',
    '## 二、各章章末的开放问题 { #chapters }',
    '',
    f'计数口径：每章末"开放问题"一节里的列表项与粗体条目各算一条，分组小标题和"预告"段落不算；按条目第一个状态标签归类。{n_chap} 章合计 {N} 条，其中【开放】{grand.get("开放", 0)} 条、【部分结果】{grand.get("部分结果", 0)} 条；"其他"一列里的"无标签"指条目本身没有挂状态标签，状态写在正文里。',
    '',
]
for part, name, rows in tables:
    out += [f'### {name} {{ #op-{part} }}', '', '| 章 | 条目 | 【开放】 | 【部分结果】 | 其他 |', '|---|---|---|---|---|'] + rows + ['']
open(OUT, 'w', encoding='utf-8').write('\n'.join(out).rstrip() + '\n')
print('wrote', OUT, 'chapters', n_chap, 'items', N, dict(grand))
