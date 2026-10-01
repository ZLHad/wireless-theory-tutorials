# 开篇之作：一个方向是怎样被打开的

教科书给你的是打磨好的结论：容量公式、注水解、标度律，一条比一条干净。这些结论刚出现时是什么样子，作者是怎么想到的，教科书一般不讲。读一个方向的开篇论文，看到的正是这一段：作者挑了一个怎样的最简单的案例，在里面看出了什么别人没看出的东西，搭了一个多简单的模型，给出的第一个结论又有多干净。

这一页挑了十三个方向的开篇之作，每篇按同一条线拆开：

- **最简案例**：作者面对的那个小到能手算、却保留了新现象本质的设定；
- **洞见**：作者在这个案例里看出的关键事实；
- **模型**：把洞见固定下来的最少几个式子；
- **解**：第一个干净的结论，可能是一个闭式解、一条标度律或一个折中区域；
- **打开的门**：后来的人在这个模型上接着做了什么；
- **还没解决的**：这条路上至今没有答案的问题。

前五篇是地基，它们给出了整个领域今天默认的语言；后八篇是近二十年打开的新方向。读的时候可以留意一件事：开篇之作的结论总是附着在它的模型假设上，后来的许多进展，正是改掉了其中一条假设。

关于出处。书目逐条经 Crossref 核对到 DOI（截至 2026 年 10 月）；模型与结论尽量读自原文，读的是期刊版或作者公开的 arXiv 版，只读到摘要或借助二手来源的地方会写明。"开篇之作"往往不止一篇，几乎每个方向都有同期或更早的平行工作，下面如实列出，不把任何一篇写成独占。文中的式子用今天通行的记号重写过，与原文记号不完全相同。

| # | 方向 | 开篇之作 | 最简案例 | 第一个干净的解 |
|---|---|---|---|---|
| 1 | 信息论 | 香农 1948 [1] | 二元信源过一条每百个符号错一个的信道 | 低于容量的速率可以几乎无错 |
| 2 | 多天线 | Telatar 1999 [2]，Foschini–Gans 1998 [3] | 收发各若干根天线，独立瑞利衰落 | 容量随 $\min(N_t,N_r)$ 线性增长 |
| 3 | 大规模 MIMO | Marzetta 2010 [4] | 每个基站天线数趋于无穷，导频在小区间复用 | 噪声与快衰落消失，只剩导频污染 |
| 4 | 网络容量 | Gupta–Kumar 2000 [5] | $n$ 个节点随机撒在单位面积上互相通信 | 每节点吞吐 $\Theta(W/\sqrt{n\log n})$ |
| 5 | 安全与隐蔽 | Wyner 1975 [6]，Bash 等 2013 [7] | 窃听者的信道更差；守卫想判断你在不在发 | 保密容量为正；隐蔽比特数按 $\sqrt n$ 增长 |
| 6 | 携能通信 | Zhang–Ho 2013 [8] | 一个发射机、一个收能机、一个解码机 | 速率–能量区域 |
| 7 | 无人机 | Zeng–Zhang 2017 [9] | 一架固定翼无人机给一个地面终端发数据 | 能效最优的轨迹介于"悬停"与"直飞"之间 |
| 8 | 智能反射面 | Wu–Zhang 2019 [10] 等 | 单用户、$N$ 个单元的反射面 | 接收功率随 $N^2$ 增长 |
| 9 | 无蜂窝 | Ngo 等 2017 [11] | 大量单天线接入点共同服务少量用户 | 95% 用户速率比小小区高数倍 |
| 10 | 可移动与流体天线 | Wong 等 2021 [12]，Zhu–Ma–Zhang 2024 [13] | 一根天线在一小块区域里换位置 | 同一块区域里的 SNR 可多出约 10 dB |
| 11 | 信道知识地图 | Zeng–Xu 2021 [14] | 两个离基站一样远的用户，一个被楼挡住 | 按位置查表就能免训练通信 |
| 12 | 通感一体化 | Sturm–Wiesbeck 2011 [15] | 一部 OFDM 收发机兼做雷达 | 逐元素除掉数据，二维 FFT 得出距离与速度 |
| 13 | 空中计算 | Nazer–Gastpar 2007 [16] | 两个发端，接收端只要两个比特的模 2 和 | 计算速率是分离方案的两倍 |

---

## 一、地基

### 1 香农 1948：噪声里也能可靠地传

这篇论文回答了"一条有噪声的信道最多能可靠地传多快"，而且答案不是零 [1]。

**最简案例。** 论文第 12 节用了一个极小的例子：信源每秒发 1000 个二元符号，0 和 1 各占一半；信道平均每 100 个符号错一个。传输速率是多少？直觉的答案是 990 bit/s，把错的减掉。香农指出这不对，因为接收者并不知道错在哪里。把这个算法推到极端就露馅了：若输出与输入完全无关，接收者靠瞎猜也能对一半，按"减去错误数"的算法还剩 500 bit/s，可实际上一比特信息也没传过去。

**洞见。** 有两层。第一层，工程问题只关心"从所有可能的消息里选出了哪一个"，与消息的意义无关，信息因此可以被计量，单位是比特。第二层出人意料：该从信源速率里扣掉的，是接收之后仍然剩下的不确定性（香农称为含糊度，今天写作条件熵 $H(X\mid Y)$）；而且要让差错趋于零，速率并不需要趋于零，只要低于一个由信道决定的数 $C$。

**模型。** 熵 $H=-\sum_ip_i\log p_i$；传输速率 $R=H(X)-H(X\mid Y)$；容量

$$
C=\max_{p(x)}\bigl[H(X)-H(X\mid Y)\bigr].
$$

带宽 $W$、白噪声功率 $N$、平均功率不超过 $P$ 的连续信道是同一个框架的特例。

**解。** 例子里，接收后判断正确的概率是 0.99，含糊度是 $-[0.99\log_20.99+0.01\log_20.01]=0.081$ bit/符号，每秒 81 bit，传输速率 $1000-81=919$ bit/s。论文的定理 11 说，信源熵率低于 $C$ 时存在编码使差错任意小，高于 $C$ 时做不到；定理 17 给出连续信道的 $C=W\log_2\frac{P+N}{N}$。证明不是造出一本具体的码，而是证明"随机选一本码本，平均而言已经足够好"，于是好码必然存在。这是一个码长趋于无穷的渐近结论，不涉及编译码的复杂度与时延。

校验：输出与输入独立时含糊度是 1 bit/符号，速率为零，正是直觉算法给出 500 bit/s 的那个极端；差错率趋于零时含糊度趋于零，速率回到 1000 bit/s。

**打开的门。** 逼近容量的实用码：1993 年的 Turbo 码 [17]，2009 年的极化码 [18]（后来成了 5G 控制信道的编码）；从广播信道 [19] 开始的多用户信息论；有限码长下速率与差错的精确关系 [20]。

**还没解决的。** 大多数多用户信道的容量区域至今未知，连两用户的高斯干扰信道，也只把容量确定到 1 bit/s/Hz 以内 [21]【开放】。香农明确把"意义"排除在工程问题之外，为任务与语义建立同样严格的极限理论，仍是开放方向（见领域地图的[语义通信](01-field-map.md#语义与任务导向通信)）。

*在本站：[预备篇 4.5 节](../part0/04-information-theory-basics.md#45-信道容量与香农编码定理)讲编码定理的直觉证明，[4.6 节](../part0/04-information-theory-basics.md#46-awgn-容量cblog_21mathrmsnr-的来历)推高斯信道容量。*

### 2 Telatar 1999 与 Foschini–Gans 1998：多根天线就是多条管道

这两篇论文说明，多天线带来的不只是更稳的信号，还有多条可以同时传数据的管道 [2] [3]。

**最简案例。** 发端 $t$ 根、收端 $r$ 根天线，$\mathbf y=H\mathbf x+\mathbf n$，总发射功率 $P$。信道矩阵的元素独立同分布于复高斯（天线之间隔得足够远），接收端知道 $H$，发射端只知道它的统计。Telatar 先看两个最小的确定性例子：$H$ 的元素全是 1 时只有一个非零奇异值，容量 $\log(1+rtP)$，各天线发同一个信号、在接收端相干叠加，这是纯粹的阵列增益；$r=t=n$、$H=I_n$ 时容量 $n\log(1+P/n)$，是 $n$ 条并行的子信道，这是纯粹的复用。

**洞见。** 多天线信道经奇异值分解，等价于若干条并行的标量信道。发射端知道信道，就在奇异值上注水；不知道而信道又是独立瑞利衰落时，各方向等功率发送就是最优的，容量随 $\min(r,t)$ 近似线性增长。Foschini 与 Gans 用一句很工程的话说出了它的分量：单天线每多 3 dB 只多 1 bit，$n\times n$ 的阵列几乎每多 3 dB 就多 $n$ bit。

**模型。** 独立瑞利衰落、接收端知道信道时的遍历容量（Telatar 定理 1）：

$$
C=\mathbb E\Bigl[\log\det\Bigl(I_r+\frac{P}{t}\mathbf H\mathbf H^{H}\Bigr)\Bigr].
$$

**解。** 定理 1 说上式由等功率的圆对称复高斯输入达到；定理 2 用随机矩阵特征值的分布把期望化成一个积分；$r=t$ 很大时容量对 $r$ 线性增长，而且只要求信道元素独立同分布、单位方差，不必是高斯的。Telatar 的数值表（20 dB，以 nats 计）：一发一收 4.0785，一发十收 6.8580，十发一收只有 4.5654，已经很接近上限 $\ln101=4.615$。发射端不知道信道时，多发单收很快就饱和了。Foschini–Gans 的摘要给出：21 dB 时，$n=2,4,16$ 在 99% 的信道实现里分别约有 7、19、88 bit/cycle。常与它一起被引用的"$n=8$ 时 42 b/s/Hz"，出自 Foschini 1996 年的分层空时架构论文 [22]，不是这一篇。

校验：4.0785 nats 换成比特是 $4.0785/\ln2=5.884$ bit/s/Hz，正是预备篇 4.8 节算出的 20 dB 瑞利衰落信道的遍历容量，两处是同一个数。

**打开的门。** 空时编码，以 Alamouti 的两天线发射分集为代表 [23]；分集与复用的基本折中 [24]；多用户 MIMO 与大规模 MIMO（下一篇）。

**还没解决的。** Telatar 在论文第 5.1 节提了一个猜想：信道实现固定不变时，让中断概率最小的发射协方差，是否总是"在其中 $k$ 根天线上等功率发送、其余关掉"。多发单收的情形 2013 年被证明 [25]，两发多收的情形 2018 年有人给出了反例 [26]，一般多入多出的中断最优输入至今没有完整刻画【开放】。收发两端都不知道衰落实现时，高 SNR 下容量通常只按 $\log\log\mathrm{SNR}$ 增长 [27]，一般 SNR 下只有上下界。

*在本站：[预备篇 5.5 节](../part0/05-mimo.md#55-mimo-容量与自由度从-logdet-到-minn_tn_rlogmathrmsnr)与 [5.6 节](../part0/05-mimo.md#56-分集复用折中zhengtse-曲线)；八条线索里[讲自由度的一节](05-eight-threads.md#3-自由度与秩先问能不能再问有多好)。*

### 3 Marzetta 2010：天线多到无穷时，只剩导频污染

这篇论文把"基站天线越多越好"推到极限，看看最后剩下什么 [4]。

**最简案例。** 六边形蜂窝，每个基站有 $M$ 根天线，$M\to\infty$；每个小区 $K$ 个单天线终端；OFDM 加时分双工（TDD）。基站和终端都不预先知道信道，全靠上行导频估计；同一组正交导频在各小区复用；小区之间不协作。下行用估计信道的共轭做预编码，上行做最大比合并。

**洞见。** 天线数趋于无穷时，不同终端的信道向量渐近正交，噪声、快衰落和小区内干扰于是全部消失。唯一剩下的是导频污染：基站估计本小区终端的信道时，不可避免地把别的小区里用同一导频的终端的信道也一起估了进来，于是下行会把信号也送给它们，上行会把它们一起相干合并。这份小区间干扰不随天线数消失。作者特意强调，"免费假设已知信道"的分析会把这一点完全掩盖。

**模型。** 上行的极限信干比：

$$
\mathrm{SIR}_k=\frac{\beta_{jkj}^2}{\sum_{\ell\ne j}\beta_{jk\ell}^2},
$$

$\beta_{jk\ell}$ 是第 $\ell$ 个小区第 $k$ 个终端到第 $j$ 个基站的大尺度衰落系数。

**解。** 极限信干比与发射功率无关，也与小区的绝对尺寸无关（路损指数项在分子分母里约掉了），由此推出几条惊人的结论：每比特所需能量可以任意小，每小区的吞吐与可服务终端数和小区大小无关。数值例沿用 LTE 参数，20 MHz 带宽、每小区 42 个终端、频率复用因子 7：每终端平均 17 Mb/s，95% 的终端至少有 3.6 Mb/s，每小区平均 730 Mb/s，也就是 36.5 bit/s/Hz（校验：$730/20=36.5$）。更激进的复用（因子 3 或 1）提高平均吞吐，却会压低 95% 用户能达到的那一档。

**打开的门。** 有限天线数下的能效与谱效 [28]；导频污染到底是不是根本限制 [29]；走向分布式的无蜂窝（第 9 篇）；频分双工下的两级预编码 [30]。

**还没解决的。** "导频污染是上限"依赖模型：在独立同分布快衰落、共轭处理下成立；换成空间相关信道加多小区 MMSE 处理，容量可以随天线数无界增长 [29]，代价是需要协方差信息和更高的复杂度。真实系统更接近哪一种描述，仍有争议【本站判断】。Marzetta 自己在文末留了两道题：有限多少根天线才算"无限"，以及"渐近正交"这条传播假设要靠实测去检验。

*在本站：[预备篇 5.9 节](../part0/05-mimo.md#导频污染唯一不随-m-消失的损伤)"导频污染：唯一不随 $M$ 消失的损伤"。*

### 4 Gupta–Kumar 2000：节点越多，每个人分到的越少

这篇论文问的是整张网络，而不是一条链路：节点越来越多时，每个节点还能分到多少吞吐 [5]。

**最简案例。** $n$ 个相同的节点独立均匀地撒在面积 1 m² 的区域上（为了排除边界效应，作者用的是球面），每个节点能以 $W$ bit/s 发送，各自随机选一个目的地，允许多跳中继。

**洞见。** 每个节点都得和邻居分享自己附近那一片信道。节点越多，一条流平均要走的跳数越多，每一跳又要给周围的传输让出空间，每个节点分到的就越来越少。原因不是网络中心形成了热点，而是空间本身是被共享的。

**模型。** 协议模型：节点 $i$ 向 $j$ 的传输成功，当且仅当其他所有同时在发的节点离 $j$ 的距离至少是 $i$ 到 $j$ 距离的 $1+\Delta$ 倍。物理模型：接收信干噪比不低于门限 $\beta$，路损指数 $\alpha>2$。

**解。** 随机网络中，每个节点的吞吐是

$$
\lambda(n)=\Theta\!\Bigl(\frac{W}{\sqrt{n\log n}}\Bigr).
$$

即使节点位置与流量都能最优安排，整张网络能"搬运"的量也只是 $\Theta(W\sqrt n)$ bit·m/s，摊到每个节点仍是 $\Theta(W/\sqrt n)$。论文给了一个直观的数：100 个源节点，想把每个源的吞吐提到原来的 5 倍，至少要加 4476 个纯中继节点。

校验：加 $m$ 个中继后，每个源的吞吐相对 $m=0$ 的倍数是 $\sqrt{\frac{(n+m)\log n}{n\log(n+m)}}$；$n=100$、$m=4476$ 时为 5.00。

**打开的门。** 这条标度律后来被一次次修正，很适合用来看"一个理论模型怎样被推进"：移动性可以提高容量 [31]；渗流论去掉了 $\sqrt{\log n}$ 的缺口 [32]；层级协作把标度推到近线性 [33]；而从电磁自由度出发，二维区域里的独立信道数只有 $\sqrt n$ 阶，每用户容量又被拉回 $1/\sqrt n$ [34]。

**还没解决的。** 层级协作的近线性标度与电磁自由度给出的 $1/\sqrt n$，各自适用于什么样的尺度、波长与功率，怎样统一，仍有讨论【本站判断】。作者自己留下的两道题，时延，以及一个更信息论的表述，也只部分有了答案。

*在本站：[第三部第 8 章](../part3/08-computing-network-capacity.md#换个问法不问容量问-scaling)"换个问法：不问容量，问 scaling"；[第一部第 4 章](../part1/04-spatial-structure.md#散射几何的自由度从-buccifranceschetti-到-miller)的空间自由度，与 [34] 说的是同一个物理事实。*

### 5 Wyner 1975 与 Bash 等 2013：不用密钥的保密，不被发现的通信

这两篇论文在物理层上回答了两个不同的问题：怎样让窃听者听不懂，以及怎样让守卫察觉不到你在说话 [6] [7]。

**最简案例。** Wyner 的例子：合法接收者的信道没有噪声；窃听者看到的是同一个码字经过一条翻转概率为 $p_0$ 的二元对称信道。直接发送，速率为 1，可窃听者的不确定性只有 $h(p_0)$。另一种做法是每次只送 1 比特：用偶校验的码字集合表示 0、奇校验的表示 1，在集合里随机挑一个发出去。码长 $N$ 增大时窃听者几乎一无所知，可速率 $1/N$ 也趋于零。问题是：能不能速率不趋于零，同时几乎完全保密？

Bash 等的例子：Alice 经一条加性高斯噪声信道发给 Bob；守卫 Willie 在另一条高斯信道上旁听，对 $n$ 个观测做假设检验，判断 Alice 有没有在发；Alice 和 Bob 预先共享一个秘密。

**洞见。** Wyner：保密不一定靠密钥。只要窃听者的信道比合法接收者的差，编码就能把这份差距换成保密。Bash 等：隐蔽（不被发现在通信）与保密（内容不被知道）是两回事；要让 Willie 的检测接近瞎猜，Alice 的功率必须随 $1/\sqrt n$ 降下去。

**模型。** Wyner 用窃听者的含糊度度量保密程度。高斯窃听信道（Leung-Yan-Cheong 与 Hellman [35]）里，主信道与窃听信道的容量分别是

$$
C_M=\tfrac12\log\Bigl(1+\frac{P}{\sigma_1^2}\Bigr),\qquad C_{MW}=\tfrac12\log\Bigl(1+\frac{P}{\sigma_1^2+\sigma_2^2}\Bigr),
$$

窃听者在合法接收者已有的噪声 $\sigma_1^2$ 之上再多受一份噪声 $\sigma_2^2$。Bash 等用 Willie 最优检验的虚警概率与漏检概率之和度量隐蔽，它等于 1 减去两个观测分布之间的全变差距离。

**解。** Wyner 的例子里，保密容量恰为 $C_s=h(p_0)$：$p_0=0.1$ 时是 0.469 bit/符号，不需要任何密钥。他还注意到可达区域不是凸的，这在当时的多用户问题里很少见。高斯情形下 $C_s=C_M-C_{MW}$ [35]；窃听者的信道若反而更好，保密容量为零，所以今天常写成 $[C_B-C_E]^+$，这个分段写法见 [36]。隐蔽通信满足平方根律：$n$ 次信道使用里，能可靠又隐蔽地送出的比特数是 $O(\sqrt n)$；想多送，要么被 Willie 发现，要么 Bob 译不出来。所以隐蔽信道的"容量"（每次使用送出的比特数）是零，总比特数却仍随 $\sqrt n$ 增长：信道用上 100 倍长的时间，能隐蔽送出的比特只多 10 倍。

**打开的门。** 非退化窃听信道与机密广播 [37]；衰落与多天线下的保密 [36]；一般信道上的隐蔽通信 [38] [39]。

**还没解决的。** 被动的窃听者不会上报自己的信道，保密容量却依赖它。在窃听者信道未知时给出可证明的保密保证，是物理层安全走向应用的核心障碍 [40]【本站判断】。隐蔽通信的工程化，包括共享秘密要多长、Willie 的噪声水平不确定、多天线与网络化的场景，也还没有定论。一种站得住的提法是"已知窃听者在某个区域内，对区域里最坏的位置设计"，见八条线索里[讲信息结构的一节](05-eight-threads.md#2-信息结构谁在什么时候知道什么)。

*在本站：[预备篇 11.4 节](../part0/11-new-network-frontiers.md#114-物理层安全与隐蔽通信不靠密钥的保密)推导保密容量、人工噪声与平方根律；领域地图的[物理层安全与隐蔽通信](01-field-map.md#物理层安全与隐蔽通信)。*

---

## 二、新范式

### 6 Zhang–Ho 2013：同一个信号既送信息又送能量

这篇论文把"无线信号同时携带能量与信息"变成了一个可以优化的问题 [8]。

**最简案例。** 一个 $M$ 天线的发射机，一个收能接收机，一个解码接收机，准静态信道，发射端知道到两者的信道 $G$ 与 $H$。两种情形：两台接收机分开，一台收能、一台解码；或者同一台终端既要收能又要解码。

**洞见。** 同一个发射信号怎样在能量与信息之间分配，就是这个方向的核心问题，用速率–能量（R–E）区域来刻画。收能最优的是"能量波束赋形"，把全部功率对准 $G^HG$ 最强的特征方向；传信息最优的是空间复用加注水。两者一般不同，所以存在真正的折中。两者对信号的要求也不同：收能不在乎输入是不是高斯的，信息传输在乎。

**模型。** 在收能不低于 $\bar Q$ 的约束下最大化速率：

$$
\max_{S\succeq0}\ \log\det\bigl(I+HSH^H\bigr)\quad\text{s.t.}\quad \operatorname{tr}\bigl(GSG^H\bigr)\ge\bar Q,\ \ \operatorname{tr}(S)\le P.
$$

这是一个凸问题，$S$ 是发射协方差。

**解。** 论文的定理 3.1 给出这个问题的全局最优解，是一种修正的注水；同一台终端收能又解码时，化为"水位随信道增益变化"的注水。数值例（4×4 天线、发射 1 W、收能机在 1 m 外、解码机在 10 m 外、900 MHz）：只做能量波束赋形能收约 0.57 mW，只做空间复用速率约 225 Mbps，最优协方差得到的边界严格好于两者的简单分时。同址接收时，理想边界要求"全部接收功率都被收集，同时信息照样被解码"，现有电路做不到；能实现的是时间切换与功率分割，后者只在射频到基带的处理噪声可以忽略时才接近这条外界。

**打开的门。** 接收机架构与速率–能量折中 [41]；先收能再上传的无线供能网络 [42]。它也有前史：Varshney 2008 [43] 与 Grover–Sahai 2010 [44] 已在信息论层面研究过同时传信息和能量，这篇论文把它带进了多天线系统设计。

**还没解决的。** 同址接收的理想边界怎样达到，原文自己写明是开放问题。一旦把整流电路的非线性计入模型，最优的输入分布、波形与 R–E 区域都会改变，线性模型下的结论不再成立 [45]【开放】。

*在本站：领域地图的[携能通信](01-field-map.md#携能通信无线能量传输与环境物联网)算了一个数：915 MHz、1 W 发射时，10 m 外只能收到微瓦级的功率；[预备篇 11.3 节](../part0/11-new-network-frontiers.md#113-携能通信与环境物联网用电磁波送能量)比较了时间切换与功率分割两种接收机的速率–能量折中。*

### 7 Zeng–Zhang 2017：把无人机的轨迹变成设计变量

这篇论文把无人机通信里最独特的东西，飞行轨迹，变成了一个优化变量，而且把推进能耗算进了账 [9]。

**最简案例。** 一架固定翼无人机以恒定高度 $H$ 飞行，给原点处的一个地面终端发数据；链路以视距为主，路损按自由空间算；发射功率恒定；通信耗能远小于推进耗能。目标是在时长 $T$ 内最大化"每焦耳送出的比特数"。

**洞见。** 无人机通信的耗能主角是推进，不是发射；推进耗能取决于速度与加速度，与位置无关。"离用户越近速率越高"与"飞得省电"互相拉扯，所以能效必须对整条轨迹优化。两个极端都不可取：悬停在用户正上方速率最高，可固定翼不能悬停，耗能趋于无穷；以最省电的速度直线飞走，飞得越远送的比特越少，能效趋于零。

**模型。** 速率 $R(t)=B\log_2\bigl(1+\gamma_0/(H^2+\|\mathbf q(t)\|^2)\bigr)$，$\mathbf q(t)$ 是水平位置；匀速直线平飞的推进功率是 $c_1V^3+c_2/V$，第一项用来克服阻力，第二项用来产生升力，速度为零时趋于无穷。一般轨迹还要加上与加速度有关的项。能效是总比特数除以总耗能。

**解。** 只求省能时，最优是以 $V_{em}=(c_2/3c_1)^{1/4}$ 匀速直飞。能效最大的圆轨迹有闭式的最优速度，一般轨迹用序列凸优化求解，只保证收敛到满足 KKT 条件的点，不保证全局最优。

!!! example "算例：论文的四种设计"
    论文参数：$c_1=9.26\times10^{-4}$，$c_2=2250$，高度 100 m，正上方 SNR 30 dB，时长 60 s。

    | 设计 | 平均速度 (m/s) | 平均速率 (Mbps) | 平均功率 (W) | 能效 (kbit/J) |
    |---|---|---|---|---|
    | 只求速率（悬停） | 0 | 9.97 | $\infty$ | 0 |
    | 只求省能（直飞） | 30 | 6.06 | 100 | 60.6 |
    | 能效最大·圆轨迹（半径约 158 m） | 25.2 | 8.16 | 119.1 | 68.5 |
    | 能效最大·一般轨迹 | 25.67 | 8.34 | 116.0 | 71.9 |

    校验：（a）$V_{em}=\bigl(2250/(3\times9.26\times10^{-4})\bigr)^{1/4}=30.0$ m/s，对应功率 $(3^{-3/4}+3^{1/4})c_1^{1/4}c_2^{3/4}=100.0$ W。（b）圆轨迹的最优速度是 $\bigl(c_2/[3(c_1+c_2/(g^2r^2))]\bigr)^{1/4}$，$r=158$ m 时为 25.2 m/s，向心加速度 $V^2/r\approx4.0$ m/s²，代回功率式得 119.1 W，与表一致。（c）能效等于速率除以功率，$6.06\ \text{Mbps}/100\ \text{W}=60.6$ kbit/J。arXiv 版正文把圆轨迹的速度写成 25.67 m/s，与它自己的表和式 (23) 都不符，应是误抄了下一行的数，期刊版是否更正未核。

**打开的门。** 旋翼无人机的能耗模型 [46]；多无人机的轨迹与调度联合设计 [47]。前一年的杂志文已经勾勒出无人机通信的全貌 [48]；空地链路视距概率的经典模型见 [49]。

**还没解决的。** 连续时间、非凸、带动力学约束的轨迹设计一般没有全局最优保证【本站判断】；三维部署、空地信道建模、与地面网络的干扰共存 [50]；能耗模型的实测校准，比如风、载荷与电池特性。

*在本站：[预备篇 11.2 节](../part0/11-new-network-frontiers.md#112-无人机与低空网络位置和航迹成了设计变量)算了最优高度与"飞到用户头上"的速率账；领域地图的[无人机与低空网络](01-field-map.md#无人机与低空网络)；[第一部第 7 章](../part1/07-channel-cartography.md#三个社区三个投影)的地图学，用无线电地图给无人机导航，正是信道知识地图的起点之一。*

### 8 Wu–Zhang 2019 与同期工作：让墙面成为可设计的变量

这篇论文把可编程的反射面写进了通信系统的优化，让"环境"第一次成为可以设计的变量 [10]。

**最简案例。** 一个 $M$ 天线的接入点、一个单天线用户、一面 $N$ 个单元的反射面。用户同时收到直达信号与反射信号；反射面的每个单元只能调相位，不需要射频链；信道完美已知。为了看清标度，再取 $M=1$，并忽略直达链路。

**洞见。** 反射面用大量无源单元做"无源波束赋形"，可以和接入点的有源波束赋形联合设计。接收功率随 $N^2$ 增长有两层原因：在反射面到用户这一段，$N$ 个单元相干叠加，带来 $N$ 倍的波束赋形增益；在接入点到反射面这一段，面越大，收集到的功率越多，又是 $N$ 倍。后一倍是总功率固定时、靠增加发射天线数得不到的。

**模型。** 单用户时，在接收信噪比达标的前提下最小化发射功率：

$$
\min_{\mathbf w,\boldsymbol\theta}\ \|\mathbf w\|^2\quad\text{s.t.}\quad\bigl|(\mathbf h_r^H\boldsymbol\Theta G+\mathbf h_d^H)\mathbf w\bigr|^2\ge\gamma\sigma^2,\qquad\boldsymbol\Theta=\operatorname{diag}\bigl(e^{j\theta_1},\dots,e^{j\theta_N}\bigr).
$$

$G$ 是接入点到反射面的信道，$\mathbf h_r$ 是反射面到用户，$\mathbf h_d$ 是直达链路。

**解。** 给定相位时最大比发射最优；相位用半定松弛或交替优化求解，$M=1$ 时两种方法都能达到最优。命题 2：信道为独立瑞利衰落、$N\to\infty$ 时，最优相位下用户的接收功率趋于 $N^2P\frac{\pi^2}{16}\varrho_h^2\varrho_g^2$，随机相位时只有 $NP\varrho_h^2\varrho_g^2$。单元数每加倍，发射功率可以省 6 dB；论文的数值例正是如此，用户靠近反射面时，$N$ 从 30 加到 60，所需发射功率从 2 dBm 降到 −4 dBm。多用户时用交替优化，只保证收敛到次优解。

校验：系数 $\pi^2/16\approx0.617$（约 −2.1 dB）来自瑞利衰落幅度的均值：$\mathbb E|h|=\varrho\sqrt\pi/2$，两段相乘再平方，得 $\varrho_h^2\varrho_g^2\pi^2/16$。

**开篇之作不止一篇。** 同期至少还有三篇常被并列为开篇的工作：Huang 等 2019 联合优化功率与相位以最大化能效，并与放大转发中继比较 [51]；Di Renzo 等 2019 提出"智能无线环境"的愿景 [52]；Basar 等 2019 做了综述与历史回顾 [53]。Wu–Zhang 的期刊版在结论里提到，投稿之后才得知 Huang 等的并行工作。更早还有 2012–2018 年的智能墙、智能反射阵等工作，物理上的可编程超材料则来自 [54]。

**打开的门。** 离散相位 [55]；信道估计；更真实的单元模型，比如幅度随相位变化 [56]。

**还没解决的。** 乘性路损：反射链路要付两段路损之积，表面要做得很大才能胜过一个中继 [57]；无源表面不能自己收导频，级联信道的维度随 $N$ 增长，估计开销是部署的瓶颈；电磁上自洽的模型，包括单元之间的互耦与幅相耦合。

*在本站：[预备篇 9.3 节](../part0/09-new-landscape.md#93-ris-智能超表面可编程的反射镜)有 $N^2$ 增益的三行推导，以及"256 个单元打不过一条健康的直达径"的算例；八条线索里[讲自由度的一节](05-eight-threads.md#3-自由度与秩先问能不能再问有多好)讲级联信道的秩。*

### 9 Ngo 等 2017：不要小区了

这篇论文把"分布式天线"与"大规模 MIMO"合在一起，干脆取消了小区 [11]。

**最简案例。** $M$ 个单天线接入点和 $K$ 个单天线用户随机分布在一块区域里，所有接入点经回程连到一个中央处理器，在同一时频资源上同时服务所有用户。时分双工；每个接入点自己估计信道，不交换瞬时 CSI，回程上只传数据和缓变的功控系数；下行用共轭波束赋形。对照组是小小区：每个用户只由一个专属的接入点服务。

**洞见。** 没有小区，也就没有小区边界。它把分布式天线抗阴影的"宏分集"，与大规模 MIMO 的有利传播、信道硬化结合了起来。论文关注的是"人人都有好服务"，所以用 95% 的用户能达到的速率作指标，用最大最小的功控。

**模型。** 每个接入点做最小均方误差信道估计、再做共轭预编码，得到下行可达速率的闭式（定理 1），分母里有一项正是导频污染。

**解。** 定理 1 对任意有限的 $M$、$K$ 给出闭式可达速率；最大最小功控问题是拟凹的，用二分法、每步解一个凸的可行性问题，就能求得全局最优。数值例（1 km² 的区域、100 个接入点、40 个用户）：95% 的用户能达到的下行速率，无蜂窝是 14 Mbit/s，小小区是 2.08 Mbit/s，约 6.7 倍；阴影衰落空间相关时约 9.8 倍。上行分别约 3.1 倍与 11.5 倍。论文摘要里"近 5 倍""10 倍"的说法与正文表格的口径不同，引用时要写明是上行还是下行。

**打开的门。** 迫零预编码与功率优化；最小均方误差处理与集中式实现；可扩展的无蜂窝 [58]；以用户为中心的体系化论述 [59]。论文自己说明，它是网络 MIMO、分布式 MIMO、协作多点（CoMP）等思想的一种具体化，新意在工作区间：大量单天线接入点服务少得多的用户，只用简单的共轭处理。

**还没解决的。** 原文把理想的回程、完美的上下行互易校准列为假设；前传容量、分布式接入点之间的相位同步、可扩展性与部署成本，是这个方向公认的瓶颈 [60]。

*在本站：[预备篇 10.3 节](../part0/10-new-phy-dof.md#103-无蜂窝与分布式-mimo拆掉小区的边界)用两个接入点、两个用户算出边缘用户的增益；领域地图的[无蜂窝](01-field-map.md#无蜂窝与分布式-mimo)；[第四部 3.5 节](../part4/03-information-structure-phase-diagram.md#35-两小区comp-的工程常识是一条相边界)说的是分布式处理什么时候不亏：回传时延要跑得过干扰耦合的时间尺度。*

### 10 可移动天线与流体天线：让天线的位置动起来

这两条线把天线的位置变成了新的设计自由度 [12] [13] [61]。

**最简案例。** 流体天线：一根天线可以在长 $W\lambda$ 的线段上 $N$ 个等距端口之间瞬时切换，总取信号最强的那个端口；各端口的信道是相关的瑞利衰落。可移动天线：天线在二维区域里连续移动，例如收端一根天线在 $A\times A$ 的方形区域里移动，信道由若干条路径叠加而成。

**洞见。** 固定的天线只能待在离散的位置上，用不上给定区域里信道的连续空间变化。多条路径在区域里叠加，形成驻波式的增益图，同相处最强、反相处最弱，几个波长之内的差距可以超过 40 dB [62]。流体天线的原文也指出，深衰落里只需挪动很小的距离就能跳出来。

**模型。** 可移动天线的"场响应"模型 [61]：

$$
H(\tilde{\mathbf t},\tilde{\mathbf r})=F(\tilde{\mathbf r})^H\,\Sigma\,G(\tilde{\mathbf t}),
$$

$\tilde{\mathbf t}$、$\tilde{\mathbf r}$ 是收发天线的位置，$\Sigma$ 是路径响应矩阵；在远场假设下，区域里各点看到的路径角度与幅度相同，只有相位随位置变。目标是在天线间距不小于 $D$ 的约束下，对位置和发射协方差联合最大化 $\log\det(I+HQH^H/\sigma^2)$。

**解。** 多入多出的可移动天线用交替优化：给定位置时按特征模传输，再逐根天线优化位置，只保证收敛到局部最优。4×4 天线、每端 10 条路径、15 dB、区域边长 3 个波长时，相对固定天线容量提高约 38% [61]。单天线时，区域边长 20 个波长、20 条路径，期望的最大 SNR 约提高 10 dB；视距主导时增益下降 [62]。流体天线的原文证明，只要端口之间的相关不为 1，端口足够多时任意小的尺寸都能让中断概率任意小 [12]；但后来有工作指出，原文的端口相关模型偏乐观，在更准确的相关模型下增益有限 [63]，引用原文数字时要带上这条说明。

**开篇之作不止一篇。** 两条线先后独立提出：流体天线 2020 年进入无线通信文献，可移动天线 2022 年。可移动天线最早的通信论文是 Zhu–Ma–Zhang 的建模与性能分析 [13]（arXiv 版 2022 年 10 月），比常被引用的杂志综述 [62] 更早、更基础。两组作者 2024 年合写的历史回顾认为，两者在"灵活调整天线位置"这一数学模型上同源，术语可以互换 [64]。

**打开的门。** 多用户与多址 [65] [66]；更准确的流体天线性能分析。

**还没解决的。** 连续区域上的信道怎样获取：逐点测量的开销与机械移动的能耗都太高；位置优化是高度非线性的问题，现有方法只得次优解；移动时延与快变信道下是否适用，还缺实测【开放】。增益上限应当由区域里信道场的有效维度决定【本站提法】，见八条线索里[讲自由度的一节](05-eight-threads.md#3-自由度与秩先问能不能再问有多好)。

*在本站：[第一部第 4 章](../part1/04-spatial-structure.md#三位一体λ2-采样相干距离与自由度密度)讲一块区域里的信道场有多少独立维度；[预备篇 10.1 节](../part0/10-new-phy-dof.md#101-可移动天线与流体天线让天线的位置成为变量)推出单天线增益不超过路径数的上界；领域地图的[可移动天线与流体天线](01-field-map.md#可移动天线与流体天线)。*

### 11 Zeng–Xu 2021：把信道知识存成地图

这篇论文提出把与地点绑定的信道知识存成一张地图，用来辅助乃至取代实时的信道训练 [14]。

**最简案例。** 论文用三个直观的例子开场。两个用户离基站一样远，其中一个被楼挡住：按距离算路损的模型会认为两人的信道相同，只要知道位置和楼在哪里，就知道谁差。免训练的波束赋形：与其对准用户，不如对准会把信号反射给用户的那面墙。用户沿一条路走向基站：视距在哪一段存在，在具体的环境里是确定的，概率视距模型只给出一条平均曲线。

**洞见。** 把与具体地点绑定的信道知识，存成一个以收发位置为索引的数据库。它和三维城市地图不同，直接反映无线传播，不需要材料的电磁参数，也不必实时跑射线追踪；它和频谱数据库也不同，后者记录的是谁在用频谱，取决于发射机的配置，信道知识地图记录的是信道的固有特性，原则上只取决于环境。

**模型。** 论文是杂志文，没有编号的式子，这里按原文的意思形式化：信道知识地图是一个映射

$$
\mathcal M:(\mathbf q_{\mathrm{tx}},\mathbf q_{\mathrm{rx}})\mapsto\boldsymbol\kappa,
$$

由有限个带位置标签的样本学出或插值得到。按链路分为基站到任意位置（B2X）与任意收发对（X2X）；按知识分为准静态的（路损、阴影、视距与否、主要路径的参数）与易变的（瞬时 CSI）。

**解。** 两个射线追踪案例。30 对设备到设备通信分配 12 个子带：用神经网络学出的信道增益图做分配，显著好于按拟合路损模型分配，接近完美 CSI，而且不需要任何信道训练。毫米波波束选择：存三条最强路径的信道路径图，用户定位误差 1 m 时，400 根天线下免训练方案约达到完美 CSI 性能的 90%，天线越多，对定位精度越敏感。这些是仿真，不是实测；论文没有给出建图需要多少数据、多高精度的理论保证。

**打开的门。** 系统化的教程 [67]；深度学习的无线电地图估计 [68]。前史：信道增益图的分布式克里金跟踪 [69]。

**还没解决的。** 建图需要多少数据、多高的定位精度；环境变化时怎样更新，又不陷入"要算更新的收益，就得先知道真实信道"的因果循环；易变的知识在高移动场景下是否可行；位置数据的隐私与跨运营商共享【开放】。

*在本站：[预备篇 11.5 节](../part0/11-new-network-frontiers.md#115-信道知识地图的工业形态数据已经在流动)讲网络里已经在流动的测量数据；[第一部第 7 章](../part1/07-channel-cartography.md#可地图化判据地图是-φ-的边缘化)把地图写成条件分布的泛函；第二部第 3 章与第 5 章讲任务怎样决定地图的分辨率、地图怎样按层折旧。*

### 12 Sturm–Wiesbeck 2011：让通信信号顺便当雷达

这篇论文系统地展示了，同一段 OFDM 通信信号可以同时用来做雷达 [15]。

本站只核到这篇论文的摘要，下面的模型借助 Braun 2014 年的博士论文 [70] 转述，该论文把这套处理方法归于 Sturm 与 Wiesbeck；原文的具体参数一律不引。

**最简案例。** 一部单站的 OFDM 收发机：同一帧 $N$ 个子载波 × $M$ 个 OFDM 符号，既是发给通信用户的数据，也是雷达的探测信号；雷达接收端知道自己发了什么；场景里有一个点目标，距离 $d$，相对速度 $v$。

**洞见。** 传统雷达信号占了带宽，却几乎不携带信息；通信信号既然反正要发，何不顺便用来探测。关键的一步在于，雷达接收端知道发了哪些符号，可以在频域逐元素地把数据除掉，剩下的就只和目标的时延与多普勒有关，与数据无关。

**模型。** 第 $k$ 个子载波、第 $l$ 个符号上，除掉数据之后

$$
F_{k,l}=b_0\,e^{j2\pi lT_Of_D}\,e^{-j2\pi k\tau\Delta f}\,e^{j\varphi_0}+\text{噪声},\qquad\tau=\frac{2d}{c},\ \ f_D=\frac{2vf_c}{c},
$$

$T_O$ 是含循环前缀的符号长度，$\Delta f$ 是子载波间隔。它是一个二维的复正弦，沿子载波方向做逆 FFT 得距离，沿符号方向做 FFT 得速度。

**解。** 距离分辨率 $\Delta d=c/(2N\Delta f)=c/(2B)$，速度分辨率 $\Delta v=c/(2MT_Of_c)$，无模糊距离 $c/(2\Delta f)$。论文摘要所述的贡献包括：用于高动态范围雷达测量的波形条件、多种处理算法、用多天线估计到达角，以及一套完整"雷达通信一体"系统的仿真与实测，说明它在实践中可行。

!!! example "算例：一个 5G 载波能把目标看多清"
    取 3.5 GHz、30 kHz 子载波间隔、3276 个子载波（约 98 MHz）、280 个符号（每个约 35.7 μs，共约 10 ms）。

    - 距离分辨率 $\Delta d=3\times10^8/(2\times98.3\times10^6)\approx1.5$ m；
    - 速度分辨率 $\Delta v=3\times10^8/(2\times280\times35.7\times10^{-6}\times3.5\times10^9)\approx4.3$ m/s；
    - 无模糊距离 $3\times10^8/(2\times3\times10^4)=5$ km。

    校验：（a）速度换一条路径算：观测 10 ms 的多普勒分辨率是 $1/(MT_O)=100$ Hz，对应速度 $\lambda\cdot100/2=0.0857\times50\approx4.3$ m/s。（b）距离分辨率 $c/(2B)$ 与第二部 4.6 节里时延特征的泛化半径是同一个量，100 MHz 时都是 1.5 m。

**开篇之作不止一篇。** 雷达与通信合一的想法可以追溯到 1963 年 [71]；把 OFDM 用作雷达信号，由 Levanon 在 2000 年提出 [72]；Sturm 与 Wiesbeck 在 2009 年已有会议版本 [73]。

**打开的门。** 感知与通信之间的基本折中 [74]；通感一体化的系统梳理 [75]。

**还没解决的。** 完整的感知–通信容量区域：在点对点的高斯信道下，也只刻画了 CRB–速率区域的两个角点，网络化、多目标、杂波环境下的极限还没有建立 [74]；单站感知要一边发一边收，就碰上了全双工的自干扰 [76]；感知参考信号的标准化与隐私问题。

*在本站：[预备篇 9.4 节](../part0/09-new-landscape.md#94-isac-通感一体化一段波形两种任务)；[第二部 5.1 节](../part2/05-cognitive-triangle.md#51-回顾isac-已经把两件事定了价用的是两把不同的尺)；八条线索里讲"通信要维度，感知要能量"的[自由度一节](05-eight-threads.md#3-自由度与秩先问能不能再问有多好)。*

### 13 Nazer–Gastpar 2007：让信道替我们做加法

这篇论文指出，无线信号在空中叠加这件"坏事"，在接收端只想要一个函数值时可以变成好事 [16]。

期刊版本站只核到摘要，最简案例与定理取自作者公开的 2005 年会议版与 2009 年的博士论文。

**最简案例。** 两个发端各看到一个二元信源 $S_1$、$S_2$，两者不同的概率为 $p$；信道是"模 2 加法多址信道"$Y=X_1\oplus X_2\oplus W$，$W$ 是翻转概率为 $q$ 的噪声；接收端不要 $S_1$、$S_2$ 本身，只要它们的模 2 和 $U=S_1\oplus S_2$。

**洞见。** 多址信道本身就在做叠加。接收端只要和的时候，不该先把每个人的消息分别解出来再相加，而应让信道替我们做加法：各发端用同一个线性码，接收端直接译出码字之和。由此得到一个反直觉的结论：即使信源相互独立，函数计算问题里也没有信源–信道分离定理。

**模型。** 计算速率 $\kappa$：每使用一次信道，接收端平均能算出多少个和。

**解。** 分离方案（先做分布式压缩，再按多址信道的容量传）最多做到

$$
\kappa_{\mathrm{SEP}}=\frac{1-h(q)}{2h(p)},
$$

计算码能达到 $\frac{1-h(q)}{h(p)}$，而且是最优的，恰好翻倍。$L$ 个独立均匀的信源时，在线性信道上计算线性函数的优势约为 $L$ 倍，用户越多越明显。前史是 1979 年 Körner 与 Marton 的模 2 和编码 [77]，它第一次显示结构化的码可以胜过随机码。

校验：$p=0.1$、$q=0.05$ 时，$h(0.05)=0.286$，$h(0.1)=0.469$，分离方案 $0.714/(2\times0.469)=0.761$，计算码 1.522，正好两倍。

**打开的门。** 计算–转发 [78]；空中计算用于联邦学习的模型聚合 [79]。

**还没解决的。** 一般信道、一般函数的计算容量仍未解决，Körner–Marton 只解决了两个二元信源求模 2 和这个特例；实用的空中计算要求各发端严格同步、按信道预先补偿，深衰落的用户受功率所限，数字化的方案仍在发展 [80]【开放】。

*在本站：[第三部第 8 章](../part3/08-computing-network-capacity.md#正面反转无线叠加把干扰变成加法器)"正面反转：无线叠加把干扰变成加法器"。*

---

## 三、从这些开篇之作里看出的几件事

最简案例都小到能手算，却保留了新现象的本质结构。携能通信只有三个节点，反射面只有一个用户，隐蔽通信只有一个守卫，空中计算只有两个二元信源。它们不是玩具：能量与信息的拉扯、$N^2$ 的孔径增益、$\sqrt n$ 的隐蔽极限、信道替我们做加法，这些本质的东西在最小的设定里已经完整出现了。玩具例子的毛病是连本质结构也一起剥掉，开篇之作剥掉的只是枝叶。

洞见常常是把一个物理事实和一个系统需求对上了号。天线多到一定程度，不同用户的信道自然趋于正交，这是大数定律，对上的是"同时服务很多用户"的需求；固定翼必须向前飞，推进耗能远大于发射耗能，对上的是"怎样飞才省电又能送数据"；多址信道天然在做叠加，对上的是"接收端只要一个和"。没有这一步对号，模型再漂亮也只是数学练习。

第一个解几乎都是干净的：一个闭式、一条标度律、一个折中区域。而且它往往直接告诉你该怎么设计：单元数加倍可以省 6 dB，隐蔽通信的时长要加 100 倍才能多送 10 倍的比特，能效最优的飞行速度在悬停与直飞之间。

结论附着在假设上，后来的进展常常就是改掉其中一条。Marzetta 的导频污染上限，换成空间相关信道加 MMSE 处理就不再是上限 [29]；Gupta–Kumar 的标度律被移动性、渗流论、层级协作和电磁自由度依次修正；反射面的 $N^2$ 增益，一算上乘性路损就要求表面大得惊人 [57]；流体天线的增益，换了更准确的相关模型就缩小了 [63]；携能通信的折中，计入整流电路的非线性就要重算 [45]；香农的容量是码长趋于无穷的结果，有限码长下另有一笔账 [20]。所以读一篇开篇之作，除了看它证明了什么，还要问一句：它的哪条假设，后来被改掉了。

开篇之作往往不止一篇。反射面有四篇同期的工作，可移动天线与流体天线是两条独立的线，无蜂窝是网络 MIMO、协作多点等思想的具体化，携能通信之前已有信息论上的探索，通感一体化可以追溯到 1963 年。一个方向真正"打开"的标志，不在于谁第一个写出来，而在于别人能不能在它的模型上写出自己的问题：反射面的模型被套进了 OFDM、多用户、通感、安全，可移动天线的场响应模型被套进了多用户、近场与感知。这样的模型就成了平台。

读一篇开篇之作时，可以随手问这四句：

1. 它的系统模型有多简单，保留了哪个本质结构？
2. 它的第一个结论有多干净，是一个判据、一条标度律，还是一条折中曲线？
3. 它和通信系统在哪里结合：哪个时间尺度、哪种自由度、付什么代价？
4. 它的哪条假设后来被改掉了，改掉以后结论还剩多少？

这四句和[八条线索](05-eight-threads.md)是同一套问题，一个用来读别人的开篇之作，一个用来审自己的想法。

---

## 四、其他开篇之作

下面这些论文同样打开或塑造了一个方向，本页没有逐篇拆开，只列出它们各自开的是哪扇门。书目同样经 Crossref 核对。

- **多天线**：Foschini 1996 提出分层空时架构（后称 BLAST），用多个独立编码的一维子系统去逼近随天线数线性增长的容量 [22]；Alamouti 1998 给出两根发射天线、不需要发射端信道知识的发射分集 [23]；Zheng–Tse 2003 指出分集与复用之间存在基本折中，并给出富散射信道上的最优折中曲线 [24]。
- **多用户分集**：Knopp–Humblet 1995 证明单小区上行让信道最好的用户独占带宽能使容量最大，用户越多容量越高 [81]。
- **毫米波**：Rappaport 等 2013 用 28 GHz 与 38 GHz 的实测说明，配合可转向的定向天线，毫米波可以用于蜂窝 [82]。
- **非正交多址**：Saito 等 2013 提出功率域非正交多址，按功率叠加多个用户、接收端串行干扰消除 [83]。
- **全双工**：Bharadia 等 2013 做出了用标准 Wi-Fi 物理层、单天线同频同时收发的原型，把自干扰压到噪声底 [84]。
- **新波形**：Hadani 等 2017 提出在时延–多普勒域上设计的 OTFS [85]；Bemani 等 2023 提出基于线性调频的多载波波形 AFDM，在双色散信道中达到最优分集阶数 [86]。
- **近场与超大规模阵列**：Cui–Dai 2022 指出近场的球面波使传统的角度域稀疏性失效，提出同时编码角度与距离的"极域"表示 [87]。
- **语义与深度联合信源信道编码**：Bourtsoulatze 等 2019 用神经网络端到端地学习从像素到信道符号的映射，在低 SNR、低带宽时胜过分离式方案 [88]。
- **认知无线电**：Zhang–Liang 2008 在对主用户的干扰功率约束下刻画次用户的多天线容量，用多天线在空间复用与干扰规避之间折中 [89]。
- **通感一体化的系统梳理**：Liu 等 2022 [75]。
- **随机几何**：Andrews 等 2011 把基站位置建模为泊松点过程，得到覆盖概率与平均速率的易算表达式 [90]。
- **联邦学习**：McMahan 等 2017 提出"联邦学习"的名称与模型平均的方法，数据留在终端，只聚合本地更新 [91]。
- **协调容量**：Cuff 等 2010 问的不是能传多少信息，而是给定通信速率下各节点的动作能建立怎样的联合分布 [92]，见[第四部第 4 章](../part4/04-coordination-information-theory.md)。
- **分散控制**：Witsenhausen 1968 的反例说明，信息分散在不同决策者手里时，线性、二次、高斯也不再保证线性控制器最优 [93]，见[第四部第 1 章](../part4/01-one-counterexample.md)。
- **网络效用最大化**：Kelly 等 1998 把速率控制写成网络效用最大化，用影子价格得到分布式算法 [94]，见[第三部第 2 章](../part3/02-classical-foundations.md)。

---

## 参考文献

1. C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, Jul. 1948; vol. 27, no. 4, pp. 623–656, Oct. 1948. DOI: 10.1002/j.1538-7305.1948.tb01338.x；10.1002/j.1538-7305.1948.tb00917.x
2. İ. E. Telatar, "Capacity of multi-antenna Gaussian channels," *European Transactions on Telecommunications*, vol. 10, no. 6, pp. 585–595, 1999. DOI: 10.1002/ett.4460100604
3. G. J. Foschini, M. J. Gans, "On limits of wireless communications in a fading environment when using multiple antennas," *Wireless Personal Communications*, vol. 6, no. 3, pp. 311–335, 1998. DOI: 10.1023/A:1008889222784
4. T. L. Marzetta, "Noncooperative cellular wireless with unlimited numbers of base station antennas," *IEEE Transactions on Wireless Communications*, vol. 9, no. 11, pp. 3590–3600, 2010. DOI: 10.1109/TWC.2010.092810.091092
5. P. Gupta, P. R. Kumar, "The capacity of wireless networks," *IEEE Transactions on Information Theory*, vol. 46, no. 2, pp. 388–404, 2000. DOI: 10.1109/18.825799
6. A. D. Wyner, "The wire-tap channel," *Bell System Technical Journal*, vol. 54, no. 8, pp. 1355–1387, 1975. DOI: 10.1002/j.1538-7305.1975.tb02040.x
7. B. A. Bash, D. Goeckel, D. Towsley, "Limits of reliable communication with low probability of detection on AWGN channels," *IEEE Journal on Selected Areas in Communications*, vol. 31, no. 9, pp. 1921–1930, 2013. DOI: 10.1109/JSAC.2013.130923
8. R. Zhang, C. K. Ho, "MIMO broadcasting for simultaneous wireless information and power transfer," *IEEE Transactions on Wireless Communications*, vol. 12, no. 5, pp. 1989–2001, 2013. DOI: 10.1109/TWC.2013.031813.120224
9. Y. Zeng, R. Zhang, "Energy-efficient UAV communication with trajectory optimization," *IEEE Transactions on Wireless Communications*, vol. 16, no. 6, pp. 3747–3760, 2017. DOI: 10.1109/TWC.2017.2688328
10. Q. Wu, R. Zhang, "Intelligent reflecting surface enhanced wireless network via joint active and passive beamforming," *IEEE Transactions on Wireless Communications*, vol. 18, no. 11, pp. 5394–5409, 2019. DOI: 10.1109/TWC.2019.2936025
11. H. Q. Ngo, A. Ashikhmin, H. Yang, E. G. Larsson, T. L. Marzetta, "Cell-free massive MIMO versus small cells," *IEEE Transactions on Wireless Communications*, vol. 16, no. 3, pp. 1834–1850, 2017. DOI: 10.1109/TWC.2017.2655515
12. K.-K. Wong, A. Shojaeifard, K.-F. Tong, Y. Zhang, "Fluid antenna systems," *IEEE Transactions on Wireless Communications*, vol. 20, no. 3, pp. 1950–1962, 2021. DOI: 10.1109/TWC.2020.3037595
13. L. Zhu, W. Ma, R. Zhang, "Modeling and performance analysis for movable antenna enabled wireless communications," *IEEE Transactions on Wireless Communications*, vol. 23, no. 6, pp. 6234–6250, 2024. DOI: 10.1109/TWC.2023.3330887
14. Y. Zeng, X. Xu, "Toward environment-aware 6G communications via channel knowledge map," *IEEE Wireless Communications*, vol. 28, no. 3, pp. 84–91, 2021. DOI: 10.1109/MWC.001.2000327
15. C. Sturm, W. Wiesbeck, "Waveform design and signal processing aspects for fusion of wireless communications and radar sensing," *Proceedings of the IEEE*, vol. 99, no. 7, pp. 1236–1259, 2011. DOI: 10.1109/JPROC.2011.2131110
16. B. Nazer, M. Gastpar, "Computation over multiple-access channels," *IEEE Transactions on Information Theory*, vol. 53, no. 10, pp. 3498–3516, 2007. DOI: 10.1109/TIT.2007.904785
17. C. Berrou, A. Glavieux, P. Thitimajshima, "Near Shannon limit error-correcting coding and decoding: Turbo-codes. 1," in *Proc. IEEE ICC*, vol. 2, pp. 1064–1070, 1993. DOI: 10.1109/ICC.1993.397441
18. E. Arıkan, "Channel polarization: A method for constructing capacity-achieving codes for symmetric binary-input memoryless channels," *IEEE Transactions on Information Theory*, vol. 55, no. 7, pp. 3051–3073, 2009. DOI: 10.1109/TIT.2009.2021379
19. T. M. Cover, "Broadcast channels," *IEEE Transactions on Information Theory*, vol. 18, no. 1, pp. 2–14, 1972. DOI: 10.1109/TIT.1972.1054727
20. Y. Polyanskiy, H. V. Poor, S. Verdú, "Channel coding rate in the finite blocklength regime," *IEEE Transactions on Information Theory*, vol. 56, no. 5, pp. 2307–2359, 2010. DOI: 10.1109/TIT.2010.2043769
21. R. H. Etkin, D. N. C. Tse, H. Wang, "Gaussian interference channel capacity to within one bit," *IEEE Transactions on Information Theory*, vol. 54, no. 12, pp. 5534–5562, 2008. DOI: 10.1109/TIT.2008.2006447
22. G. J. Foschini, "Layered space-time architecture for wireless communication in a fading environment when using multi-element antennas," *Bell Labs Technical Journal*, vol. 1, no. 2, pp. 41–59, 1996. DOI: 10.1002/bltj.2015
23. S. M. Alamouti, "A simple transmit diversity technique for wireless communications," *IEEE Journal on Selected Areas in Communications*, vol. 16, no. 8, pp. 1451–1458, 1998. DOI: 10.1109/49.730453
24. L. Zheng, D. N. C. Tse, "Diversity and multiplexing: A fundamental tradeoff in multiple-antenna channels," *IEEE Transactions on Information Theory*, vol. 49, no. 5, pp. 1073–1096, 2003. DOI: 10.1109/TIT.2003.810646
25. E. Abbe, S.-L. Huang, E. Telatar, "Proof of the outage probability conjecture for MISO channels," *IEEE Transactions on Information Theory*, vol. 59, no. 5, pp. 2596–2602, 2013. DOI: 10.1109/TIT.2013.2240762
26. G. Li, J. Yan, Y. Gu, "Outage probability conjecture does not hold for two-input-multiple-output (TIMO) system," in *Proc. IEEE ISIT*, pp. 1345–1349, 2018. DOI: 10.1109/ISIT.2018.8437337
27. A. Lapidoth, S. M. Moser, "Capacity bounds via duality with applications to multiple-antenna systems on flat-fading channels," *IEEE Transactions on Information Theory*, vol. 49, no. 10, pp. 2426–2467, 2003. DOI: 10.1109/TIT.2003.817449
28. H. Q. Ngo, E. G. Larsson, T. L. Marzetta, "Energy and spectral efficiency of very large multiuser MIMO systems," *IEEE Transactions on Communications*, vol. 61, no. 4, pp. 1436–1449, 2013. DOI: 10.1109/TCOMM.2013.020413.110848
29. E. Björnson, J. Hoydis, L. Sanguinetti, "Massive MIMO has unlimited capacity," *IEEE Transactions on Wireless Communications*, vol. 17, no. 1, pp. 574–590, 2018. DOI: 10.1109/TWC.2017.2768423
30. A. Adhikary, J. Nam, J.-Y. Ahn, G. Caire, "Joint spatial division and multiplexing—The large-scale array regime," *IEEE Transactions on Information Theory*, vol. 59, no. 10, pp. 6441–6463, 2013. DOI: 10.1109/TIT.2013.2269476
31. M. Grossglauser, D. N. C. Tse, "Mobility increases the capacity of ad hoc wireless networks," *IEEE/ACM Transactions on Networking*, vol. 10, no. 4, pp. 477–486, 2002. DOI: 10.1109/TNET.2002.801403
32. M. Franceschetti, O. Dousse, D. N. C. Tse, P. Thiran, "Closing the gap in the capacity of wireless networks via percolation theory," *IEEE Transactions on Information Theory*, vol. 53, no. 3, pp. 1009–1018, 2007. DOI: 10.1109/TIT.2006.890791
33. A. Özgür, O. Lévêque, D. N. C. Tse, "Hierarchical cooperation achieves optimal capacity scaling in ad hoc networks," *IEEE Transactions on Information Theory*, vol. 53, no. 10, pp. 3549–3572, 2007. DOI: 10.1109/TIT.2007.905002
34. M. Franceschetti, M. D. Migliore, P. Minero, "The capacity of wireless networks: Information-theoretic and physical limits," *IEEE Transactions on Information Theory*, vol. 55, no. 8, pp. 3413–3424, 2009. DOI: 10.1109/TIT.2009.2023705
35. S. K. Leung-Yan-Cheong, M. E. Hellman, "The Gaussian wire-tap channel," *IEEE Transactions on Information Theory*, vol. 24, no. 4, pp. 451–456, 1978. DOI: 10.1109/TIT.1978.1055917
36. M. Bloch, J. Barros, M. R. D. Rodrigues, S. W. McLaughlin, "Wireless information-theoretic security," *IEEE Transactions on Information Theory*, vol. 54, no. 6, pp. 2515–2534, 2008. DOI: 10.1109/TIT.2008.921908
37. I. Csiszár, J. Körner, "Broadcast channels with confidential messages," *IEEE Transactions on Information Theory*, vol. 24, no. 3, pp. 339–348, 1978. DOI: 10.1109/TIT.1978.1055892
38. M. R. Bloch, "Covert communication over noisy channels: A resolvability perspective," *IEEE Transactions on Information Theory*, vol. 62, no. 5, pp. 2334–2354, 2016. DOI: 10.1109/TIT.2016.2530089
39. L. Wang, G. W. Wornell, L. Zheng, "Fundamental limits of communication with low probability of detection," *IEEE Transactions on Information Theory*, vol. 62, no. 6, pp. 3493–3503, 2016. DOI: 10.1109/TIT.2016.2548471
40. A. Mukherjee, S. A. A. Fakoorian, J. Huang, A. L. Swindlehurst, "Principles of physical layer security in multiuser wireless networks: A survey," *IEEE Communications Surveys & Tutorials*, vol. 16, no. 3, pp. 1550–1573, 2014. DOI: 10.1109/SURV.2014.012314.00178
41. X. Zhou, R. Zhang, C. K. Ho, "Wireless information and power transfer: Architecture design and rate-energy tradeoff," *IEEE Transactions on Communications*, vol. 61, no. 11, pp. 4754–4767, 2013. DOI: 10.1109/TCOMM.2013.13.120855
42. H. Ju, R. Zhang, "Throughput maximization in wireless powered communication networks," *IEEE Transactions on Wireless Communications*, vol. 13, no. 1, pp. 418–428, 2014. DOI: 10.1109/TWC.2013.112513.130760
43. L. R. Varshney, "Transporting information and energy simultaneously," in *Proc. IEEE ISIT*, pp. 1612–1616, 2008. DOI: 10.1109/ISIT.2008.4595260
44. P. Grover, A. Sahai, "Shannon meets Tesla: Wireless information and power transfer," in *Proc. IEEE ISIT*, pp. 2363–2367, 2010. DOI: 10.1109/ISIT.2010.5513714
45. B. Clerckx, R. Zhang, R. Schober, D. W. K. Ng, D. I. Kim, H. V. Poor, "Fundamentals of wireless information and power transfer: From RF energy harvester models to signal and system designs," *IEEE Journal on Selected Areas in Communications*, vol. 37, no. 1, pp. 4–33, 2019. DOI: 10.1109/JSAC.2018.2872615
46. Y. Zeng, J. Xu, R. Zhang, "Energy minimization for wireless communication with rotary-wing UAV," *IEEE Transactions on Wireless Communications*, vol. 18, no. 4, pp. 2329–2345, 2019. DOI: 10.1109/TWC.2019.2902559
47. Q. Wu, Y. Zeng, R. Zhang, "Joint trajectory and communication design for multi-UAV enabled wireless networks," *IEEE Transactions on Wireless Communications*, vol. 17, no. 3, pp. 2109–2121, 2018. DOI: 10.1109/TWC.2017.2789293
48. Y. Zeng, R. Zhang, T. J. Lim, "Wireless communications with unmanned aerial vehicles: Opportunities and challenges," *IEEE Communications Magazine*, vol. 54, no. 5, pp. 36–42, 2016. DOI: 10.1109/MCOM.2016.7470933
49. A. Al-Hourani, S. Kandeepan, S. Lardner, "Optimal LAP altitude for maximum coverage," *IEEE Wireless Communications Letters*, vol. 3, no. 6, pp. 569–572, 2014. DOI: 10.1109/LWC.2014.2342736
50. M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, M. Debbah, "A tutorial on UAVs for wireless networks: Applications, challenges, and open problems," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 3, pp. 2334–2360, 2019. DOI: 10.1109/COMST.2019.2902862
51. C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," *IEEE Transactions on Wireless Communications*, vol. 18, no. 8, pp. 4157–4170, 2019. DOI: 10.1109/TWC.2019.2922609
52. M. Di Renzo et al., "Smart radio environments empowered by reconfigurable AI meta-surfaces: An idea whose time has come," *EURASIP Journal on Wireless Communications and Networking*, vol. 2019, Art. no. 129, 2019. DOI: 10.1186/s13638-019-1438-9
53. E. Basar, M. Di Renzo, J. de Rosny, M. Debbah, M.-S. Alouini, R. Zhang, "Wireless communications through reconfigurable intelligent surfaces," *IEEE Access*, vol. 7, pp. 116753–116773, 2019. DOI: 10.1109/ACCESS.2019.2935192
54. T. J. Cui, M. Q. Qi, X. Wan, J. Zhao, Q. Cheng, "Coding metamaterials, digital metamaterials and programmable metamaterials," *Light: Science & Applications*, vol. 3, e218, 2014. DOI: 10.1038/lsa.2014.99
55. Q. Wu, R. Zhang, "Beamforming optimization for wireless network aided by intelligent reflecting surface with discrete phase shifts," *IEEE Transactions on Communications*, vol. 68, no. 3, pp. 1838–1851, 2020. DOI: 10.1109/TCOMM.2019.2958916
56. S. Abeywickrama, R. Zhang, Q. Wu, C. Yuen, "Intelligent reflecting surface: Practical phase shift model and beamforming optimization," *IEEE Transactions on Communications*, vol. 68, no. 9, pp. 5849–5863, 2020. DOI: 10.1109/TCOMM.2020.3001125
57. E. Björnson, Ö. Özdogan, E. G. Larsson, "Intelligent reflecting surface versus decode-and-forward: How large surfaces are needed to beat relaying?" *IEEE Wireless Communications Letters*, vol. 9, no. 2, pp. 244–248, 2020. DOI: 10.1109/LWC.2019.2950624
58. E. Björnson, L. Sanguinetti, "Scalable cell-free massive MIMO systems," *IEEE Transactions on Communications*, vol. 68, no. 7, pp. 4247–4261, 2020. DOI: 10.1109/TCOMM.2020.2987311
59. Ö. T. Demir, E. Björnson, L. Sanguinetti, "Foundations of user-centric cell-free massive MIMO," *Foundations and Trends in Signal Processing*, vol. 14, no. 3–4, pp. 162–472, 2021. DOI: 10.1561/2000000109
60. H. A. Ammar, R. Adve, S. Shahbazpanahi, G. Boudreau, K. V. Srinivas, "User-centric cell-free massive MIMO networks: A survey of opportunities, challenges and solutions," *IEEE Communications Surveys & Tutorials*, vol. 24, no. 1, pp. 611–652, 2022. DOI: 10.1109/COMST.2021.3135119
61. W. Ma, L. Zhu, R. Zhang, "MIMO capacity characterization for movable antenna systems," *IEEE Transactions on Wireless Communications*, vol. 23, no. 4, pp. 3392–3407, 2024. DOI: 10.1109/TWC.2023.3307696
62. L. Zhu, W. Ma, R. Zhang, "Movable antennas for wireless communication: Opportunities and challenges," *IEEE Communications Magazine*, vol. 62, no. 6, pp. 114–120, 2024. DOI: 10.1109/MCOM.001.2300212
63. M. Khammassi, A. Kammoun, M.-S. Alouini, "A new analytical approximation of the fluid antenna system channel," *IEEE Transactions on Wireless Communications*, vol. 22, no. 12, pp. 8843–8858, 2023. DOI: 10.1109/TWC.2023.3266411
64. L. Zhu, K.-K. Wong, "Historical review of fluid antenna and movable antenna," arXiv:2401.02362, 2024.【预印本·未评审】
65. K.-K. Wong, K.-F. Tong, "Fluid antenna multiple access," *IEEE Transactions on Wireless Communications*, vol. 21, no. 7, pp. 4801–4815, 2022. DOI: 10.1109/TWC.2021.3133410
66. L. Zhu, W. Ma, B. Ning, R. Zhang, "Movable-antenna enhanced multiuser communication via antenna position optimization," *IEEE Transactions on Wireless Communications*, vol. 23, no. 7, pp. 7214–7229, 2024. DOI: 10.1109/TWC.2023.3338626
67. Y. Zeng, J. Chen, J. Xu, D. Wu, X. Xu, S. Jin, X. Gao, D. Gesbert, S. Cui, R. Zhang, "A tutorial on environment-aware communications via channel knowledge map for 6G," *IEEE Communications Surveys & Tutorials*, vol. 26, no. 3, pp. 1478–1519, 2024. DOI: 10.1109/COMST.2024.3364508
68. R. Levie, Ç. Yapar, G. Kutyniok, G. Caire, "RadioUNet: Fast radio map estimation with convolutional neural networks," *IEEE Transactions on Wireless Communications*, vol. 20, no. 6, pp. 4001–4015, 2021. DOI: 10.1109/TWC.2021.3054977
69. E. Dall'Anese, S.-J. Kim, G. B. Giannakis, "Channel gain map tracking via distributed kriging," *IEEE Transactions on Vehicular Technology*, vol. 60, no. 3, pp. 1205–1211, 2011. DOI: 10.1109/TVT.2011.2113195
70. K. M. Braun, *OFDM Radar Algorithms in Mobile Communication Networks*, Ph.D. dissertation, Karlsruhe Institute of Technology, 2014. DOI: 10.5445/IR/1000038892
71. R. M. Mealey, "A method for calculating error probabilities in a radar communication system," *IEEE Transactions on Space Electronics and Telemetry*, vol. 9, no. 2, pp. 37–42, 1963. DOI: 10.1109/TSET.1963.4337601
72. N. Levanon, "Multifrequency complementary phase-coded radar signal," *IEE Proceedings – Radar, Sonar and Navigation*, vol. 147, no. 6, pp. 276–284, 2000. DOI: 10.1049/ip-rsn:20000734
73. C. Sturm, T. Zwick, W. Wiesbeck, "An OFDM system concept for joint radar and communications operations," in *Proc. IEEE VTC Spring*, pp. 1–5, 2009. DOI: 10.1109/VETECS.2009.5073387
74. Y. Xiong, F. Liu, Y. Cui, W. Yuan, T. X. Han, G. Caire, "On the fundamental tradeoff of integrated sensing and communications under Gaussian channels," *IEEE Transactions on Information Theory*, vol. 69, no. 9, pp. 5723–5751, 2023. DOI: 10.1109/TIT.2023.3284449
75. F. Liu, Y. Cui, C. Masouros, J. Xu, T. X. Han, Y. C. Eldar, S. Buzzi, "Integrated sensing and communications: Toward dual-functional wireless networks for 6G and beyond," *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 6, pp. 1728–1767, 2022. DOI: 10.1109/JSAC.2022.3156632
76. C. Baquero Barneto et al., "Full-duplex OFDM radar with LTE and 5G NR waveforms: Challenges, solutions, and measurements," *IEEE Transactions on Microwave Theory and Techniques*, vol. 67, no. 10, pp. 4042–4054, 2019. DOI: 10.1109/TMTT.2019.2930510
77. J. Körner, K. Marton, "How to encode the modulo-two sum of binary sources," *IEEE Transactions on Information Theory*, vol. 25, no. 2, pp. 219–221, 1979. DOI: 10.1109/TIT.1979.1056022
78. B. Nazer, M. Gastpar, "Compute-and-forward: Harnessing interference through structured codes," *IEEE Transactions on Information Theory*, vol. 57, no. 10, pp. 6463–6486, 2011. DOI: 10.1109/TIT.2011.2165816
79. G. Zhu, Y. Wang, K. Huang, "Broadband analog aggregation for low-latency federated edge learning," *IEEE Transactions on Wireless Communications*, vol. 19, no. 1, pp. 491–506, 2020. DOI: 10.1109/TWC.2019.2946245
80. A. Şahin, R. Yang, "A survey on over-the-air computation," *IEEE Communications Surveys & Tutorials*, vol. 25, no. 3, pp. 1877–1908, 2023. DOI: 10.1109/COMST.2023.3264649
81. R. Knopp, P. A. Humblet, "Information capacity and power control in single-cell multiuser communications," in *Proc. IEEE ICC*, vol. 1, pp. 331–335, 1995. DOI: 10.1109/ICC.1995.525188
82. T. S. Rappaport et al., "Millimeter wave mobile communications for 5G cellular: It will work!" *IEEE Access*, vol. 1, pp. 335–349, 2013. DOI: 10.1109/ACCESS.2013.2260813
83. Y. Saito, Y. Kishiyama, A. Benjebbour, T. Nakamura, A. Li, K. Higuchi, "Non-orthogonal multiple access (NOMA) for cellular future radio access," in *Proc. IEEE VTC Spring*, pp. 1–5, 2013. DOI: 10.1109/VTCSpring.2013.6692652
84. D. Bharadia, E. McMilin, S. Katti, "Full duplex radios," in *Proc. ACM SIGCOMM*, pp. 375–386, 2013. DOI: 10.1145/2486001.2486033
85. R. Hadani et al., "Orthogonal time frequency space modulation," in *Proc. IEEE WCNC*, pp. 1–6, 2017. DOI: 10.1109/WCNC.2017.7925924
86. A. Bemani, N. Ksairi, M. Kountouris, "Affine frequency division multiplexing for next generation wireless communications," *IEEE Transactions on Wireless Communications*, vol. 22, no. 11, pp. 8214–8229, 2023. DOI: 10.1109/TWC.2023.3260906
87. M. Cui, L. Dai, "Channel estimation for extremely large-scale MIMO: Far-field or near-field?" *IEEE Transactions on Communications*, vol. 70, no. 4, pp. 2663–2677, 2022. DOI: 10.1109/TCOMM.2022.3146400
88. E. Bourtsoulatze, D. Burth Kurka, D. Gündüz, "Deep joint source-channel coding for wireless image transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567–579, 2019. DOI: 10.1109/TCCN.2019.2919300
89. R. Zhang, Y.-C. Liang, "Exploiting multi-antennas for opportunistic spectrum sharing in cognitive radio networks," *IEEE Journal of Selected Topics in Signal Processing*, vol. 2, no. 1, pp. 88–102, 2008. DOI: 10.1109/JSTSP.2007.914894
90. J. G. Andrews, F. Baccelli, R. K. Ganti, "A tractable approach to coverage and rate in cellular networks," *IEEE Transactions on Communications*, vol. 59, no. 11, pp. 3122–3134, 2011. DOI: 10.1109/TCOMM.2011.100411.100541
91. H. B. McMahan, E. Moore, D. Ramage, S. Hampson, B. Agüera y Arcas, "Communication-efficient learning of deep networks from decentralized data," in *Proc. AISTATS*, PMLR vol. 54, pp. 1273–1282, 2017.（无 DOI）
92. P. W. Cuff, H. H. Permuter, T. M. Cover, "Coordination capacity," *IEEE Transactions on Information Theory*, vol. 56, no. 9, pp. 4181–4206, 2010. DOI: 10.1109/TIT.2010.2054651
93. H. S. Witsenhausen, "A counterexample in stochastic optimum control," *SIAM Journal on Control*, vol. 6, no. 1, pp. 131–147, 1968. DOI: 10.1137/0306011
94. F. P. Kelly, A. K. Maulloo, D. K. H. Tan, "Rate control for communication networks: Shadow prices, proportional fairness and stability," *Journal of the Operational Research Society*, vol. 49, no. 3, pp. 237–252, 1998. DOI: 10.1057/palgrave.jors.2600523
