# -*- coding: utf-8 -*-
# A 组标注规格：导览篇第 4–6 章、预备篇第 1–11 章，共 25 张。
# 数据、序列顺序、坐标范围一律取自 charts/src/<id>.mmd，这里只给标注。
OV = {
 # ---------------- 导览篇 ----------------
 'g-04-1': dict(
     title='从开篇论文到第一次进入标准的年数',
     barh=True, value_labels=True,
 ),
 'g-05-1': dict(
     title='能量固定、时长拉长 $k$ 倍：可传比特与检测精度',
     xlabel='时长倍数 $k$',
     ylabel='相对 $k=1$ 的倍数',
     legend=['可传比特数', '检测与测距精度'],
 ),
 'g-06-1': dict(
     title='三个大方向的逐年论文数（2013–2025）',
     legend=['非正交多址', '智能超表面', '通感一体化'],
 ),
 'g-06-2': dict(
     title='几个较新方向的逐年论文数（2015–2025）',
     legend=['语义通信', 'OTFS 与 AFDM', '可移动与流体天线', '无蜂窝大规模 MIMO', '信道知识地图'],
     legend_loc='upper left',   # 五条线放图外会排成两行、按列填充，读序乱；左上角正好空着
 ),
 'g-06-3': dict(
     title='两个较早方向的逐年论文数（2010–2025）',
     legend=['携能通信', '同频全双工'],
     xrot=30,                   # 16 个年份平排会挤在一起
 ),
 # ---------------- 预备篇 ----------------
 'p0-01-2': dict(
     title=r'8 元均匀线阵的归一化阵因子（$d=\lambda/2$）',
     xlabel=r'观察角 $\theta$（度）',
     ylabel='归一化阵因子（dB）',
     legend=[r'法线方向，$\beta=0$', r'扫描到 $30^\circ$，$\beta=-\pi/2$'],
     markers=None,
 ),
 'p0-02-1': dict(
     title='包络分布：从瑞利（$K=0$）到莱斯（$K=1$、$10$），平均功率都是 1',
     xlabel='包络 $r$',
     ylabel='概率密度',
     legend=['$K=0$（瑞利）', '$K=1$（0 dB）', '$K=10$（10 dB）'],
 ),
 'p0-02-2': dict(
     title='Jakes 多普勒谱：两端堆积的浴缸形',
     xlabel='归一化频率 $f/f_m$',
     ylabel=r'归一化谱 $S(f)\cdot\pi f_m/\bar{P}$',
 ),
 'p0-03-3': dict(
     title='BPSK 误码率：AWGN、瑞利与 MRC 分集',
     xlabel='每支路平均 $E_b/N_0$（dB）',
     ylabel='误码率',
     ylog10=True,
     legend=['AWGN', '瑞利，单支路', '瑞利，2 支路 MRC', '瑞利，4 支路 MRC'],
 ),
 'p0-03-4': dict(
     title='有限码长下能达到的速率占容量的比例（错误概率 $10^{-5}$）',
     xlabel='码长 $n$（信道使用次数）',
     ylabel='$R^*/C$（%）',
     legend=['SNR 0 dB', 'SNR 10 dB'],
 ),
 'p0-04-1': dict(
     title='每比特最低能量随频谱效率上升（AWGN 容量边界）',
     xlabel=r'频谱效率 $\eta$（bit/s/Hz）',
     ylabel='所需最低 $E_b/N_0$（dB）',
     legend=[r'容量边界 $(2^{\eta}-1)/\eta$', '绝对底线 $-1.59$ dB'],
     colors=[0, 'ref'], styles=['-', '--'],
 ),
 'p0-05-3': dict(
     title='2×2 MIMO 的分集–复用折中',
     xlabel='复用增益 $r$',
     ylabel='分集增益 $d$',
     legend=[r'最优折中 $d^{\star}(r)$', 'Alamouti $4(1-r)$'],
 ),
 'p0-06-1': dict(
     title=r'两用户上行：MAC 容量域与正交接入（$\mathrm{SNR}_1 = 20$ dB，$\mathrm{SNR}_2 = 0$ dB）',
     xlabel='$R_1$（bit/s/Hz）',
     ylabel='$R_2$（bit/s/Hz）',
     legend=['MAC 容量域外边界', '正交接入边界'],
 ),
 'p0-07-1': dict(
     title=r'三载波注水比均分多出的速率（$\gamma=4$、$1$、$0.25$）',
     xlabel='总功率预算 $P$（每格翻倍）',
     ylabel='注水速率比均分高出（%）',
     xticklabels=['$1/16$', '$1/8$', '$1/4$', '$1/2$', '$1$', '$2$', '$4$', '$8$', '$16$', '$32$', '$64$'],
 ),
 'p0-08-1': dict(
     title=r'$\gamma^k$ 的衰减：奖励的权重，也是值迭代误差的收缩倍数',
     xlabel='步数 $k$',
     ylabel=r'$\gamma^k$',
     legend=[r'$\gamma=0.9$', r'$\gamma=0.99$', '0.1 参照线'],
     colors=[0, 1, 'ref'], styles=['-', '-', '--'], markers=['o', 'o', None],
 ),
 'p0-09-1': dict(
     title='RIS 级联链路损耗随单元数 $N$ 下降（算例 9-3 的几何）',
     xlabel='RIS 单元数 $N$（每格翻倍）',
     ylabel='等效链路损耗（dB，越低越好）',
     legend=['RIS 级联链路', '无遮挡直达径', '直达径被挡 25 dB'],
     markers=['o', None, None], # 两条水平线是比较用的固定水平，不打点
 ),
 'p0-10-0': dict(
     title='可移动天线的平均增益随区域长度的变化',
     xlabel='区域长度 $A$（每格翻倍）',
     ylabel='平均增益（线性倍数）',
     xticklabels=[r'$0.5\lambda$', r'$1\lambda$', r'$2\lambda$', r'$4\lambda$', r'$8\lambda$', r'$16\lambda$'],
     legend=['散射丰富', '三条等幅径', '两条等幅径', '纯视距'],
 ),
 'p0-10-1': dict(
     title='视距自由度随距离的变化（两端孔径相同）',
     xlabel='收发距离 $d$（m）',
     ylabel='自由度',
     legend=[r'28 GHz，$L_tL_r/(\lambda d)$', '28 GHz，占 90% 能量的奇异值数', r'3.5 GHz，$L_tL_r/(\lambda d)$'],
     legend_loc='upper right',  # 三条图例平排几乎占满整宽，右上角空着
 ),
 'p0-10-2': dict(
     title='两 AP 两用户上行：用户 1 的速率（每条链路 SNR 20 dB）',
     legend=['无蜂窝（集中 MMSE）', '蜂窝'],
     markers=['o', None],
 ),
 'p0-10-3': dict(
     title='SNR 20 dB 时全双工与半双工的每方向速率',
     xticklabels=['−10', '−5', '0', '5', '10', '15', '20', '25', '30'],
     legend=['全双工', '半双工（同峰值功率）', '半双工（功率加倍）'],
     markers=['o', None, None],
 ),
 'p0-10-4': dict(
     title='子载波间干扰：近似式与精确值',
     xlabel=r'归一化频移 $\varepsilon$',
     legend=[r'近似式 $(\pi\varepsilon)^2/3$', r'精确值 $1-\operatorname{sinc}^2(\varepsilon)$'],
     styles=['-', '--'],        # 两条线几乎重合，后画的精确值用虚线，透出底下的近似式
 ),
 'p0-10-5': dict(
     title='200 m 处的损耗：两端全向与基站用 0.5 m 面板',
     legend=['两端全向', '基站用 0.5 m 面板'],
 ),
 'p0-11-0': dict(
     title='600 km 低轨的单程时延与 2 GHz 多普勒随仰角变化',
     ylabel='数值（单位见图例）',
     legend=['单程时延（ms）', '2 GHz 多普勒（单位 10 kHz）'],
 ),
 'p0-11-1': dict(
     title='城区无人机基站的平均路损随高度变化（2 GHz，$R$ 取 707 m）',
     xlabel='无人机高度 $h$（m，各点不等距）',
 ),
 'p0-11-2': dict(
     title='功率分割与时间切换的速率能量折中（SNR 20 dB）',
     xlabel='分给能量的比例 $e$',
     legend=[r'功率分割 $R_{\mathrm{PS}}$', r'时间切换 $R_{\mathrm{TS}}$'],
 ),
}
