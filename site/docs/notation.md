# 符号表

全站预备篇加四部共 46 章，记号是各章按所在领域的惯例分别取的，同一个字母常常在不同章里指不同的东西，同一个量也常常换着字母写。这一页把全站记号分三类整理，每一行都从正文抽取核对过：

- **一、书写约定**：粗体、上标、对数的底、定义号这类贯穿全站的写法；
- **二、一个字母，多种含义**：按字母查，一个字母一张表；
- **三、一个量，几种写法**：同一个物理量或数学对象在不同章换了字母；
- **四、各部核心记号**：按部、按首次出现的先后排列，读某一部之前可以先扫一遍。

几条读法说明：

- "首次出现"按阅读顺序算（预备篇 → 第四部）；首页、各部导读页与章首"你将学会"列表里的预告不计。如果第一次出现只是顺带用到、定义在另一节，括号里另给定义所在的小节。
- 第二节只收**有名字、跨过一整节或多章使用**的含义，以及与另一含义同页并存、容易看混的含义。只在一段推导里出现的哑变量、玩具例子里的一次性常数不收。
- 链接指向小节标题；点开后在该节里找这个记号即可。

## 一、书写约定 { #conventions }

| 写法 | 含义 | 首次出现 | 提醒 |
|---|---|---|---|
| 粗体 $\mathbf{h},\ \mathbf{H}$ | 矢量与矩阵：粗体小写是列矢量，粗体大写是矩阵 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | 预备篇第 1 章与第一部的粗体 $\mathbf E,\ \mathbf H$ 是三维电磁场矢量，预备篇第 5 章起粗体 $\mathbf H$ 才是信道矩阵，见 [H](#sym-H) |
| $(\cdot)^{\mathsf T},\ (\cdot)^{\top},\ (\cdot)^{T}$ | 转置（三种字形同义） | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积) | — |
| $(\cdot)^{H}$；$(\cdot)^{\dagger}$ | 共轭转置 | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积) | 第一部第 4、9 章写 $(\cdot)^{\dagger}$；第四部第 4 章的 $H(Y\dagger X)$ 不是共轭转置，而是 Cuff–Permuter–Cover 原文的"必要条件熵"记号 |
| $(\cdot)^{*}$ | 复共轭 | [预备篇 2.5 · Jakes 谱](part0/02-wireless-channel-basics.md#jakes-谱从散射角分布推出浴缸曲线) | 预备篇第 4 章 $p^{*}(x)$、第 8 章 $V^{*},Q^{*},\pi^{*}$、第三部第 6、9 章 $x^{*},f^{*}$、第四部第 8 章 $a^{*}$ 的星号表示**最优**；全站更常用 $(\cdot)^{\star}$ 表示最优 |
| $(\cdot)^{\star}$ | 最优值、最优解 | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积) | 与上一行的星号 $*$ 字形相近，含义看上下文 |
| $:=,\ \triangleq$ | 定义为（两种写法同义） | [预备篇 1.1 · 从方程组到波动方程](part0/01-em-waves-antennas.md#从方程组到波动方程五步推导) | 预备篇多用 $\triangleq$，第二部起基本都用 $:=$ |
| $\mathbb E,\ \Pr$ | 期望、概率 | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积)（$\Pr$ 见 [预备篇 2.3 · 相关距离](part0/02-wireless-channel-basics.md#相关距离阴影不是白噪声)） | 第一部第 1、2 章的 $\mathcal E$（花体）是环境，第二部的 $\mathcal E$ 是实验，都不是期望，见 [E](#sym-E) |
| $\mathcal{CN}(\mathbf 0,\sigma^2\mathbf I)$ | 循环对称复高斯分布 | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积) | — |
| $(x)^{+}$ | $\max\{x,0\}$ | [预备篇 4.8 · CSIT 与时间注水](part0/04-information-theory-basics.md#第二部csit-与时间注水) | 注水解 $(\mu-1/\gamma)^{+}$ 的来历 |
| $\log_2,\ \ln,\ \log_{10}$ | 以 2 为底（比特）、自然对数（nat）、常用对数（dB） | [预备篇 4.1 · 三步定出唯一形式](part0/04-information-theory-basics.md#三步定出唯一形式) | 不带底的 $\log$ 全站**没有统一约定**，按上下文读：比特计数处以 2 为底；[预备篇 6.4 · PF 准则从哪来](part0/06-wireless-networks.md#推导pf-准则从哪来)、[第二部 4.2 · 译码度量与 GMI](part2/04-environment-generalization.md#定义译码度量与-gmi)、[第三部第 5 章 · 带预测的算法](part3/05-price-of-prediction.md#第三级台阶带预测的算法第一批严格的质量-性能曲线) 三处明确取自然对数；在 $O(\cdot)$ 里底数只差常数倍 |
| dB、dBm | 功率比取 $10\log_{10}$，幅度比（场强、电压、反射系数）取 $20\log_{10}$；dBm 以 1 mW 为基准 | [预备篇 1.5 · 完整推导](part0/01-em-waves-antennas.md#完整推导五步不跳步) | 第一部第 8 章的噪声水平 $\varepsilon$ 按幅度折算：60 dB 对应 $10^{-3}$，见 [ε](#sym-epsilon) |
| $O(\cdot),\ \Omega(\cdot),\ \Theta(\cdot),\ \tilde O(\cdot)$ | 渐近上界、下界、同阶；$\tilde O$ 忽略对数因子 | [预备篇 3.5 · 一个指数被一个概率吃掉了](part0/03-digital-communications.md#解读一个指数被一个概率吃掉了)（$\Theta$ 见 [预备篇 5.7 · 2026 年 8 月](part0/05-mimo.md#2026-年-8-月一个二十年悬案的候选解)） | 大写 $\Theta$ 也常指参数集、$\Omega$ 也指立体角或角谱支撑，见 [Θ](#sym-Theta)、[Ω](#sym-Omega) |

## 二、一个字母，多种含义 { #letters }

按字母查：

- 小写希腊字母：[α](#sym-alpha) · [β](#sym-beta) · [γ](#sym-gamma) · [δ](#sym-delta) · [ε、ϵ](#sym-epsilon) · [η](#sym-eta) · [θ](#sym-theta) · [κ](#sym-kappa) · [λ](#sym-lambda) · [μ](#sym-mu) · [ν](#sym-nu) · [ξ](#sym-xi) · [π](#sym-pi) · [ρ](#sym-rho) · [σ](#sym-sigma) · [τ](#sym-tau) · [φ、ϕ](#sym-phi) · [ψ、Ψ](#sym-psi) · [ω](#sym-omega)
- 大写希腊字母：[Γ](#sym-Gamma) · [Δ](#sym-Delta) · [Θ](#sym-Theta) · [Λ](#sym-Lambda) · [Π](#sym-Pi) · [Φ](#sym-Phi) · [Ω](#sym-Omega)
- 拉丁字母：[C](#sym-C) · [D](#sym-D) · [E、𝓔](#sym-E) · [H、𝓗](#sym-H) · [h](#sym-h) · [K](#sym-K) · [L](#sym-L) · [N、𝒩](#sym-N) · [Q](#sym-Q) · [q](#sym-q) · [R](#sym-R) · [T、𝒯](#sym-T) · [V](#sym-V) · [W](#sym-W)

每张表的行按首次出现排序。

### α { #sym-alpha }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\alpha_l,\ \alpha_n,\ \alpha_p$ | 第 $l$ 条路径（第 $n$ 个 RIS 单元、第 $p$ 条径）的复增益或幅度 | [预备篇 2.8 · 时变冲激响应](part0/02-wireless-channel-basics.md#时变冲激响应) | 第一部第 3 章 S-V 模型的径增益写 $\beta_{kl}$ |
| $\alpha$ | 路径损耗指数：功率按 $d^{-\alpha}$ 衰减 | [预备篇 6.1 · 一根大喇叭，还是一片小音箱](part0/06-wireless-networks.md#直觉一根大喇叭还是一片小音箱) | 预备篇第 2 章写 $n$；第四部第 7 章命题 7.7 的"$\alpha=2$ 相边界"也是它；第四部第 8 章算例 8.3 改写 $\gamma$ |
| $\alpha$ | 资源份额、比例，取值 $[0,1]$ | [预备篇 6.3 · 正交 vs 非正交](part0/06-wireless-networks.md#正交-vs-非正交两用户-mac-容量域) | 同类用法：第一部第 9 章的复用增益比例、第二部第 4 章混合训练集里来自 $A$ 的比例（命题 4.6）、第三部第 5 章的分时硬币 $\mathrm{Bern}(\alpha)$ |
| $\alpha$ | $\alpha$-公平效用的公平参数，$\alpha=1$ 即比例公平 | [预备篇 6.4 · PF 准则从哪来](part0/06-wireless-networks.md#推导pf-准则从哪来) | 第三部第 2 章 2.4 节展开 |
| $\alpha$ | 上行功控的路损补偿因子（$P_0+\alpha\cdot PL$） | [预备篇 6.5 · 上行开环功控](part0/06-wireless-networks.md#上行开环功控) | 预备篇第 6 章一章之内 $\alpha$ 有四种含义，6.3 节正文有提醒 |
| $\alpha,\ \alpha_k,\ \alpha_t$ | 步长、学习率 | [预备篇 7.6 · 价格迭代](part0/07-optimization-basics.md#价格迭代次梯度上升) | 预备篇第 8 章 TD 与 Q-learning 的学习率也是 $\alpha$；第四部第 6 章 Hedge 的步长写 $\eta$，MWU 写 $\varepsilon$ |
| $\alpha$ | 来波方位角（相对运动方向），多普勒 $f=f_m\cos\alpha$ | [第一部 3.3 · Clarke 谱定理](part1/03-statistical-lineage.md#clarke-谱定理一个几何假设锁死整个谱) | Clarke 模型 |
| $\alpha$ | 阴影方差（Xu–Zeng 地图误差模型） | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | 第二部第 6 章开放问题沿用 |
| $\alpha(r)$ | 预测精度指数：离采样域距离 $r$ 处误差 $\sim\varepsilon^{\alpha(r)}$，$\alpha$ 从 1 降到 0 | [第一部 8.4 · 插值与外推](part1/08-dimension-and-prediction.md#插值与外推一步之遥的数学相变) | 第一部 Q2 的核心记号；第四部第 9 章收尾表写成 $\alpha(r)=\max\{0,1-r/r_{\max}\}$ |
| $\alpha$ | BSC 翻转概率（第二部第 2 章的写法之一） | [第二部第 2 章 · 章首](part2/02-blackwell.md) | 同章 BEC 擦除概率写 $\beta$ 或 $\epsilon$；预备篇 BSC 翻转概率写 $\varepsilon$ |
| $\alpha,\ \alpha^\star$ | 感知占比：长期投给"认识环境"的资源份额；$\alpha^\star$ 是认知平衡点 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | 第二部第 5–7 章的核心记号；分层版本 $\alpha_\ell$，双信息版本 $\alpha_{\mathrm e},\ \alpha_{\mathrm f}$ |
| $\alpha_k$ | 加权和速率与 WMMSE 里用户 $k$ 的权重 | [第三部 3.2 · 干扰图](part3/03-nonconvex-era.md#32-干扰图非凸的组合内核与一个必须点破的陷阱) | — |
| $\alpha(t)$ | drift-plus-penalty 框架里时隙 $t$ 的控制动作（沿用 Neely 的记法） | [第三部 4.3 · 核心推导](part3/04-sequential-uncertainty.md#核心推导drift-plus-penalty-的五步骨架) | 第三部第 5 章信息松弛里 $\alpha\in\mathcal A_F$ 也是策略 |
| $\alpha$ | 发射端 CSI 误差随功率缩小的指数：误差 $\propto P^{-\alpha}$，自由度 $\le 1+\alpha$ | [第三部 6.2 · 谱系对照表](part3/06-communication-lower-bounds.md#谱系对照表) | — |
| $\alpha$ | 推测解码的期望接受率，$\alpha=\mathbb E[\beta]$ | [第四部 4.7 · 多方](part4/04-coordination-information-theory.md#47-多方广播是资源不是负担)（定义见 [第四部 5.5 · 推测解码](part4/05-shared-world-model.md#55-推测解码接受率-1-mathrmtvpq)） | 单步接受率写 $\beta$ |
| $\alpha$ | Wyner 线性蜂窝的相邻小区泄漏比：功率增益 $\alpha^{\lvert n-k\rvert}$ | [第四部 8.9 · 协作增益的天花板](part4/08-network-games.md#89-协作增益的天花板耦合度-kappa-的第一个候选) | 正文有提醒：这里是功率比，不是路损指数，也不是拥塞代价斜率 $\alpha_e$ |

### β { #sym-beta }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\beta$ | 阵列的递进相移：第 $n$ 个阵元加 $n\beta$ | [预备篇 1.6 · 均匀线阵的阵因子](part0/01-em-waves-antennas.md#均匀线阵的阵因子逐步推导) | — |
| $\beta$ | 升余弦滚降因子，带宽 $B\approx(1+\beta)R_s$ | [预备篇 3.1 · 每一层的"量纲"](part0/03-digital-communications.md#每一层的量纲) | — |
| $\beta,\ \beta_{jlk}$ | 大尺度衰落系数（大规模 MIMO） | [预备篇 5.9 · 导频污染](part0/05-mimo.md#导频污染唯一不随-m-消失的损伤) | — |
| $\beta_{\mathrm{rms}}$ | 信号的均方根带宽，时延估计 CRB 的分母 | [预备篇 9.4 · 感知这一侧怎么度量](part0/09-new-landscape.md#感知这一侧怎么度量crb-一句话) | 第一部第 6 章沿用 |
| $\beta$ | 信息瓶颈的权衡系数：$\min I(X;Z)-\beta I(Z;Y)$ | [预备篇 9.5 · 严格一点](part0/09-new-landscape.md#严格一点它和率失真理论是什么关系) | 第二部第 1 章沿用 |
| $\beta$ | 波数 $2\pi/\lambda$（第一部第 1 章 Q1 的写法） | [第一部 1.6 · Q1 环境的信道有效维度](part1/01-lie-of-randomness.md#q1-环境的信道有效维度) | 四套写法见[第三节](#same) |
| $\beta_0$ | Keller 锥的半锥角：绕射射线与边缘切线的夹角 | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | 正文提醒：不是相位常数 $\beta$ |
| $\beta_{kl}$ | S-V 模型第 $l$ 簇第 $k$ 条径的增益 | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | — |
| $\beta$ | 阴影的去相关距离（Gudmundson 模型） | [第一部 7.2 · 可地图化判据](part1/07-channel-cartography.md#可地图化判据地图是-φ-的边缘化) | 第二部第 6 章开放问题沿用 |
| $\beta$ | 归一化多普勒带宽 $f_D/f_{\mathrm{Nyq}}$ | [第一部 8.6 · 时间轴](part1/08-dimension-and-prediction.md#时间轴带限悖论与有效维度的重逢) | — |
| $\beta$ | BEC 擦除概率（第二部第 2 章的写法之一） | [第二部第 2 章 · 章首](part2/02-blackwell.md) | 同章 BSC 翻转概率写 $\alpha$ |
| $\beta$ | 幂律型汇率 $\Delta C=c\,(q/q_{\mathrm{sat}})^{\beta}$ 的指数，$0<\beta<1$ | [第二部 5.4 · 认知平衡点](part2/05-cognitive-triangle.md#认知平衡点一阶条件) | 推论 5.3：$\alpha^\star\to\beta/(1+\beta)$ |
| $\beta$ | 带预测算法的一致性（预测完全准确时的竞争比） | [第三部 1.4 · 滑雪租赁](part3/01-three-mountains.md#三滑雪租赁预测的价目表已经精确到公式) | 第三部第 5 章沿用；同处鲁棒性写 $\gamma$ |
| $\beta_s$ | 联邦学习客户端 $s$ 分到的带宽（Hz） | [第三部 2.7 · 当代回声](part3/02-classical-foundations.md#27-当代回声数据中心云边定价边缘卸载与联邦学习) | — |
| $\beta$ | 推测解码的单步接受率 $\sum_x\min\{p,q\}=1-\mathrm{TV}(p,q)$ | [第四部 5.5 · 推测解码](part4/05-shared-world-model.md#55-推测解码接受率-1-mathrmtvpq) | 期望接受率写 $\alpha$ |
| $\beta$ | 平均场功控模型的干扰跟随系数：邻区平均功率涨 1 dB，我跟涨 $\beta$ dB | [第四部 7.3 · 功率军备竞赛](part4/07-mean-field.md#模型功率军备竞赛) | 第四部第 9 章沿用 |
| $\beta_e$ | 仿射拥塞代价 $d_e(x)=\alpha_e x+\beta_e$ 的常数项 | [第四部 8.4 · 无政府的代价](part4/08-network-games.md#84-无政府的代价smoothness-是一台可搬运的证明机器) | — |

### γ { #sym-gamma }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\gamma,\ \bar\gamma$；$\gamma_0,\ \gamma_i$ | 瞬时信噪比与平均信噪比；深衰落门限；第 $i$ 路的信噪比 | [预备篇 3.5 · 模型](part0/03-digital-communications.md#模型) | 预备篇第 4、5 章与第一部第 8、9 章沿用；预备篇第 7 章的 $\gamma_i=g_i/\sigma^2$ 是"每单位功率的信噪比" |
| $\gamma_{\mathrm{EM}}$ | 欧拉常数 | [预备篇 4.8 · CSIR 遍历容量](part0/04-information-theory-basics.md#第一部csir-遍历容量) | 正文提醒与信噪比无关 |
| $\gamma_i$ | 链路 $i$ 的目标 SINR（Foschini–Miljanic 功控） | [预备篇 6.5 · Foschini–Miljanic 迭代](part0/06-wireless-networks.md#foschinimiljanic-迭代分布式功控的经典) | 预备篇第 7 章沿用；对角阵 $\boldsymbol{\Gamma}=\mathrm{diag}(\gamma_i)$ 见 [Γ](#sym-Gamma) |
| $\gamma$ | 折扣因子（MDP 五元组的最后一项） | [预备篇 8.2 · 五元组定义](part0/08-reinforcement-learning.md#五元组定义) | 第四部第 8 章重复博弈的贴现因子写 $\delta$（正文有提醒） |
| $\gamma$ | S-V 模型的簇内衰减常数（簇间写 $\Gamma$） | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | — |
| $\gamma(k_x,k_y)$ | 法向波数 $\sqrt{\kappa^2-k_x^2-k_y^2}$ | [第一部 4.2 · 亥姆霍兹方程](part1/04-spatial-structure.md#亥姆霍兹方程物理白送的低通滤波器) | 第一部第 8 章的 $\gamma$ 是信噪比 $\sigma^2/\sigma_n^2$ |
| $\gamma,\ \gamma_1,\ \gamma_2$ | 电导率（Calderón 问题） | [第一部 6.2 · 从信道观测到边界数据](part1/06-inverse-problem.md#从信道观测到边界数据) | 第一部第 1、2 章的电导率写 $\sigma$ |
| $\gamma_{\mathrm{dB}}(\mathbf q)$ | 位置 $\mathbf q$ 处的信道增益（dB） | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | — |
| $\gamma$ | 最优运输里的耦合（两个边缘分别为 $P,Q$ 的联合分布） | [第二部 4.5 · Wasserstein-1 距离](part2/04-environment-generalization.md#wasserstein-1-距离搬沙子) | — |
| $\gamma_{\mathrm c},\ \gamma_{\mathrm s},\ \gamma_{\mathrm k}$ | 每块资源分给通信、感知、学信道的份额 | [第二部 5.7 · 三元 region](part2/05-cognitive-triangle.md#57-三元-region分时凸包可达内部形状开放) | — |
| $\gamma_i$；$\gamma_{\text{采样}}$ | 比特效率：第 $i$ 环误差按 $\sigma_i^2=c_i2^{-2\gamma_i b_i}$ 随比特下降 | [第二部 6.7 · 问题的精确形式](part2/06-error-budget.md#问题的精确形式) | 第二部第 7 章开放问题沿用 |
| $\gamma$ | 带预测算法的鲁棒性（预测任意差时的竞争比） | [第三部 1.4 · 滑雪租赁](part3/01-three-mountains.md#三滑雪租赁预测的价目表已经精确到公式) | 第三部第 5 章沿用；同处一致性写 $\beta$ |
| $\gamma$ | NUM 价格迭代的步长 | [第三部 2.3 · Step 4 · 梯度投影 = 供求律](part3/02-classical-foundations.md#step-4--梯度投影--供求律) | — |
| $\gamma_s$ | 联邦学习客户端 $s$ 的谱效率（bit/s/Hz） | [第三部 2.7 · 当代回声](part3/02-classical-foundations.md#27-当代回声数据中心云边定价边缘卸载与联邦学习) | — |
| $\gamma_i$；$\gamma=(\gamma_1,\dots,\gamma_N)$ | 决策规则：成员 $i$ 把看到的东西映成动作 | [第四部 1.2 · 反例的精确设置](part4/01-one-counterexample.md#12-反例的精确设置三件套齐全结论塌了) | 第四部第 2 章给出定义；第二部的（随机化）决策规则写 $\rho(a\mid z)$ |
| $\gamma$ | 推测解码每轮的草稿数 | [第四部 5.5 · 推测解码](part4/05-shared-world-model.md#55-推测解码接受率-1-mathrmtvpq) | — |
| $\gamma$ | 路径损耗指数（第四部第 8 章算例 8.3 的数值栏） | [第四部 8.9 · 协作增益的天花板](part4/08-network-games.md#89-协作增益的天花板耦合度-kappa-的第一个候选) | 其余章节路损指数写 $\alpha$ 或 $n$，见 [α](#sym-alpha) |

### δ { #sym-delta }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\delta(\cdot)$；$\delta_a,\ \delta_x$；$\delta_{ij}$ | Dirac 冲激；全部质量集中在一点的点质量分布；Kronecker 符号 | [预备篇 2.8 · 时变冲激响应](part0/02-wireless-channel-basics.md#时变冲激响应) | 点质量见第二部第 4 章（正文提醒它与墙位移只是撞了字母）、第四部第 6、7 章；Kronecker 符号见第一部第 10 章 |
| $\delta$ | BEC 擦除概率 | [预备篇 4.5 · 两个必会的容量](part0/04-information-theory-basics.md#两个必会的容量) | 第二部把 $\delta$ 让给亏格，擦除概率改写 $\epsilon$（第 2 章也写 $\beta$） |
| $\delta>0$ | 任意小正数（切比雪夫不等式、存在性论证里的容差） | [预备篇 5.9 · 两块基石](part0/05-mimo.md#两块基石) | 第三部第 4 章、第四部第 5 章同类 |
| $\delta_t$ | TD 误差：TD 目标与旧估计之差 | [预备篇 8.5 · MC 与 TD](part0/08-reinforcement-learning.md#mc-与-td两种估计哲学) | — |
| $\delta_n$ | 近场阵列第 $n$ 个阵元的坐标 $n\Delta$ | [预备篇 9.2 · 近场给了什么新能力](part0/09-new-landscape.md#近场给了什么新能力距离域聚焦) | — |
| $\delta$ | 终端沿传播方向的位置误差，相位误差为 $2\pi\delta/\lambda$ | [第一部 1.3 · 随机性从哪里进来](part1/01-lie-of-randomness.md#随机性从哪里进来三重无知与一条红线) | — |
| $\delta\mathcal L/\delta p,\ \delta\mathbf E,\ \delta E$ | 微小变化：变分导数、差场、扰动 | [第一部 1.4 · Rayleigh 衰落是最大无知模型](part1/01-lie-of-randomness.md#rayleigh-衰落是最大无知模型) | 第一部第 2、8 章与第二部第 6 章（一阶泰勒展开里的 $\delta$）同类 |
| $\delta$ | 偏离入射阴影边界（ISB）的角度 | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | 只在 UTD 过渡函数的推导里 |
| $\delta$ | 预测的精度要求，按幅度计：$\delta=10^{-2}$ 即功率 $-40$ dB | [第一部 8.7 · Q2 的形式化](part1/08-dimension-and-prediction.md#q2-的形式化预测半径与边界曲线) | 与同章 $\varepsilon$ 同一口径，见 [ε](#sym-epsilon) |
| $\delta(\mathcal E,\mathcal F)$；$\delta_k,\ \delta_{\mathcal T}$ | Le Cam 亏格：用实验 $\mathcal E$ 模拟实验 $\mathcal F$，在最坏参数下差多少（半 $L_1$ 总变差）；$\delta_k$ 只对动作数 $\le k$ 的任务取最坏，$\delta_{\mathcal T}$ 只对任务类 $\mathcal T$ 取最坏 | [第二部 1.5 · 目标形态](part2/01-four-arrows.md#15-目标形态带汇率的数据处理不等式) | 第二部的核心记号，第四部第 2、9 章沿用 |
| $\delta,\ \delta_p,\ \delta_\pi,\ \delta_{\mathrm d}$ | 墙或散射体沿法向的位移（毫米量级）；$\delta_\pi$ 是让反射径相位翻转 $\pi$ 所需的位移 | [第二部 4.4 · 让 Maxwell 说话](part2/04-environment-generalization.md#44-让-maxwell-说话两径像法的灵敏度表) | 第二部第 4、7 章里亏格与位移同页：带两个实验作参数的是亏格，单独出现或带下标 $p,\pi,\mathrm d$ 的是位移（第 7 章 7.5 节有提醒） |
| $\delta$ | LLM 输出长度的预测精度 | [第三部 5.5 · LLM 推理调度](part3/05-price-of-prediction.md#llm-推理调度最鲜活的活例) | — |
| $\delta$ | $\delta$-相关：各机器二次目标的系数差不超过 $\delta$，即数据异构度 | [第三部 6.2 · Arjevani–Shamir 2015](part3/06-communication-lower-bounds.md#arjevanishamir-2015数轮数) | — |
| $\delta_i$ | 团队二次代价 $\tfrac12u^{\top}Qu-u^{\top}\delta$ 里随状态变化的一次项 | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | — |
| $\delta$ | Newman 定理里私有随机性代替公共随机性时多放宽的出错概率 | [第四部 4.7 · 多方](part4/04-coordination-information-theory.md#47-多方广播是资源不是负担) | 第四部第 5 章沿用 |
| $\delta\approx4.669$ | Feigenbaum 常数：倍周期分岔间距之比的极限 | [第四部 6.7 · 算例](part4/06-learning-dynamics.md#算例) | — |
| $\delta$ | 重复博弈的贴现因子 | [第四部 8.6 · 重复博弈](part4/08-network-games.md#86-重复博弈把无界的损失救回来) | 预备篇第 8 章贴现因子写 $\gamma$ |

### ε、ϵ { #sym-epsilon }

两个字形 $\varepsilon$ 与 $\epsilon$ 在多数章节里混用，含义看上下文；第二部第 1、2 章特意用 $\epsilon$ 表示 BEC 擦除概率，需留意。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\varepsilon,\ \varepsilon_0,\ \varepsilon_r,\ \varepsilon',\ \varepsilon(\mathbf r)$ | 介电常数：一般值、真空值、相对值、复相对介电常数的实部、随位置变化的分布 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | 第一部把 $\varepsilon(\mathbf r)$ 当作"环境"的主要载体；第二部第 6 章环一的输入就是材质 $\varepsilon'$ |
| $\varepsilon$ | BSC 翻转概率 | [预备篇 4.2 · 条件作用永不增加熵](part0/04-information-theory-basics.md#条件作用永不增加熵) | 第二部改写 $q$（第 2 章也写 $p,r,\alpha$）；第二部的 $\epsilon$ 是 BEC 擦除概率 |
| $\epsilon,\ \varepsilon>0$ | 任意小正数（典型集、收敛定义里的容差） | [预备篇 4.5 · 直觉证明思路](part0/04-information-theory-basics.md#直觉证明思路典型序列与随机编码) | — |
| $\epsilon$ | 中断概率：中断容量 $C_\epsilon$ 允许以概率 $\epsilon$ 失败 | [预备篇 4.8 · 中断容量](part0/04-information-theory-basics.md#第三部中断容量) | — |
| $\epsilon$ | $\epsilon$-贪心的随机探索概率 | [预备篇 8.1 · regret](part0/08-reinforcement-learning.md#regret给学得慢定价) | — |
| $\epsilon$ | PPO 的裁剪幅度 | [预备篇 8.7 · Actor-Critic 与 PPO](part0/08-reinforcement-learning.md#actor-critic-与-ppo) | — |
| $\epsilon$ | 逆散射稳定性估计里的信道数据误差 | [第一部 6.3 · Alessandrini](part1/06-inverse-problem.md#alessandrini数据误差换重建误差的汇率) | 同章 Mandache 定理里"相距 $\varepsilon$ 的两个环境"指环境之差 |
| $\varepsilon$ | 地图误差，地图效能损失 $\Delta U(\varepsilon)$ 的自变量 | [第一部 7.6 · 诚实盘点](part1/07-channel-cartography.md#诚实盘点三句话与三个基本问题) | 第二部第 1–3 章沿用 $\Delta U(\varepsilon)$ |
| $\varepsilon$；$[E]_\varepsilon,\ \Theta_\varepsilon$ | 相对噪声水平或精度，**按幅度计**：$\varepsilon=10^{-\mathrm{SNR}_{\mathrm{dB}}/20}$，60 dB 对应 $10^{-3}$；$\varepsilon$-秩与环境等价类由它定义 | [第一部 8.3 · Q1 的形式化](part1/08-dimension-and-prediction.md#q1-的形式化有效维度与环境等价类)（约定框见 [第一部 8.7 · Q2 的形式化](part1/08-dimension-and-prediction.md#q2-的形式化预测半径与边界曲线)） | 按功率读会把 60 dB 误作 $10^{-6}$；第二部第 3、5、7 章的 $R_{\mathrm{ceil}}=d_{\mathrm{eff}}\log_2(1/\varepsilon)$ 与 $\Theta_\varepsilon$ 沿用这一口径 |
| $\epsilon^\star(R)$；$\epsilon,\ \epsilon_n$ | 感知失真：速率 $R$ 下可达的最小 CRB（通感 Pareto 边界）；第二部第 5 章三元 region 里的感知损失 | [第一部 10.5 · Q3 · 价值论的接口](part1/10-research-agenda.md#q3--价值论的接口isac-的双重折中) | 第二部第 5 章的边际价格 $\nu(R)=\mathrm d\epsilon^\star/\mathrm dR$ |
| $\epsilon$ | BEC 擦除概率 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 预备篇写 $\delta$；第二部第 2 章也写 $\beta$ |
| $\epsilon_S,\ \epsilon_T$ | 源域、目标域上的分类误差（域适应界） | [第二部 4.3 · 设定与 $\mathcal{H}\Delta\mathcal{H}$ 距离](part2/04-environment-generalization.md#设定与-mathcalhdeltamathcalh-距离) | — |
| $\epsilon$；$C(\varepsilon)$ | $\epsilon$-最优：目标值离最优不超过 $\epsilon$；$C(\varepsilon)$ 是达到 $\varepsilon$-最优所需的最少通信比特 | [第三部 1.2 · 山二 · 分布式](part3/01-three-mountains.md#山二--分布式不知道别的节点知道什么) | 第三部第 6、9 章与第四部第 3–5 章的 $C(\varepsilon)$ |
| $\varepsilon$ | Berry–Gallager 定理里平均功率比最小功率多出的余量，时延 $\Omega(1/\sqrt\varepsilon)$ | [第三部 1.4 · Berry–Gallager 平方根律](part3/01-three-mountains.md#一berrygallager-平方根律无线资源领域的孤本) | — |
| $\varepsilon$ | $\varepsilon$-均衡的偏离收益上界（$\varepsilon$-GNE、$\varepsilon$-Nash、$\varepsilon$-相关均衡） | [第三部 2.7 · 方法盘点](part3/02-classical-foundations.md#方法盘点20242026-各支在做什么以及各自答不了什么) | 第四部第 7 章定理 7.5 |
| $\varepsilon$ | Slater 余量：平均到达率离容量域边界的距离 | [第三部 4.2 · 写法 B · 只要均值稳定 → drif…](part3/04-sequential-uncertainty.md#写法-b--只要均值稳定--drift-plus-penalty) | — |
| $\varepsilon$ | 通信复杂度允许的出错概率（$R^{\mathrm{pub}}_\varepsilon$ 的下标） | [第三部 6.1 · 随机性把 n 打成 O(1)](part3/06-communication-lower-bounds.md#随机性把-n-打成-o1为后文埋一颗雷) | 第四部第 4、5 章沿用 |
| $\epsilon$ | 协调目标里两基站"同开同关"的概率，最小协调速率 $1-h(\epsilon)$ | [第四部 4.3 · 两基站错开发射的协调价签](part4/04-coordination-information-theory.md#43-算例两基站错开发射的协调价签) | — |
| $\varepsilon$ | 两个智能体的世界模型之差，协商罚项 $\Phi_T(\varepsilon)$ 的自变量 | [第四部 5.1 · 两个医生会诊](part4/05-shared-world-model.md#51-两个医生会诊共享模型如何压缩语言) | — |
| $\varepsilon$ | MWU 的步长 | [第四部 6.6 · 一步之差](part4/06-learning-dynamics.md#66-一步之差mwu-的两个变体) | 正文沿用 Palaiopanos 等的记法；第四部别处的步长写 $\eta$ |

### η { #sym-eta }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\eta_0$ | 自由空间波阻抗，约 $120\pi\ \Omega$ | [预备篇 1.1 · 从方程组到波动方程](part0/01-em-waves-antennas.md#从方程组到波动方程五步推导) | — |
| $\eta$；$\eta_{\mathrm{erg}},\ \eta_{\mathrm{WF}}$ | 频谱效率（bit/s/Hz）；遍历容量与注水容量对应的频谱效率 | [预备篇 3.1 · 每一层的"量纲"](part0/03-digital-communications.md#每一层的量纲) | 预备篇第 4、6 章沿用 |
| $\eta_i$ | 第 $i$ 个传感器的测量噪声标准差 | [预备篇 4.10 · 精度相加](part0/04-information-theory-basics.md#精度相加多个独立观测怎么合并) | 第四部第 2 章算例 2.2 沿用 |
| $\eta_1,\ \eta_2,\ \eta_3$ | 线孔径、面孔径、体孔径的空间自由度 | [第一部 4.3 · λ/2 采样、相干距离与自由度密度](part1/04-spatial-structure.md#三位一体λ2-采样相干距离与自由度密度) | — |
| $\eta_m$；$\eta$ | 材质 $m$ 的电磁参数；Fresnel 公式里的复相对介电常数 | [第一部 5.1 · 从渲染画面到渲染电磁场](part1/05-deterministic-revival.md#从渲染画面到渲染电磁场) | 第一部第 5 章的 $\eta$ 与别处的 $\varepsilon_r$ 是同一个量 |
| $\eta$ | 功率谱的噪底 | [第一部 8.6 · 时间轴](part1/08-dimension-and-prediction.md#时间轴带限悖论与有效维度的重逢) | — |
| $\eta_t$ | 投影梯度的步长 | [第三部 4.2 · 写法 C · 知道对手最坏 → OCO …](part3/04-sequential-uncertainty.md#写法-c--知道对手最坏--oco-与竞争分析) | — |
| $\eta$ | 带预测算法的预测误差 | [第三部 4.8 · 三座已经架起的半桥](part3/04-sequential-uncertainty.md#三座已经架起的半桥) | 第三部第 5 章沿用 |
| $\eta$；$\eta^\star$ | 学习率（Hedge、MWU 的指数变体）；从收敛分岔到混沌的阈值 $\eta^\star=7.4536$ | [第四部 6.1 · 两个学下棋的人](part4/06-learning-dynamics.md#61-两个学下棋的人目标在动) | 第四部第 9 章沿用；同章 MWU 的线性变体步长写 $\varepsilon$ |

### θ { #sym-theta }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $(\theta,\varphi)$；$\theta_0,\ \theta_{3\mathrm{dB}},\ \theta_E,\ \theta_H$ | 方向角（俯仰与方位）；波束指向角；半功率波束宽度；E 面与 H 面波束宽度 | [预备篇 1.4 · 方向图](part0/01-em-waves-antennas.md#参数一方向图) | 预备篇第 5 章的半功率波束宽度写 $\Theta_{\mathrm{HPBW}}$ |
| $\theta$ | 来波与运动方向的夹角，多普勒 $f_d=v\cos\theta/\lambda$ | [预备篇 2.5 · 频移的推导](part0/02-wireless-channel-basics.md#频移的推导) | 第一部第 3 章同一个角写 $\alpha$ |
| $\theta_l(t)$ | 第 $l$ 条径的相位 | [预备篇 2.8 · 时变冲激响应](part0/02-wireless-channel-basics.md#时变冲激响应) | — |
| $\theta$ | 凸组合系数，$\theta\in[0,1]$ | [预备篇 7.2 · 凸集](part0/07-optimization-basics.md#凸集两点之间不出界) | 第四部第 3 章写 $\lambda$ |
| $\boldsymbol{\theta}$ | 神经网络或模型的参数：$Q(s,a;\boldsymbol{\theta})$、$\pi_{\boldsymbol{\theta}}$ | [预备篇 8.6 · 为什么必须函数逼近](part0/08-reinforcement-learning.md#为什么必须函数逼近) | 第一部第 5 章可微引擎的参数 $\theta$ 同类 |
| $\theta_n$ | RIS 第 $n$ 个单元的反射相位 | [预备篇 9.3 · 级联信道模型](part0/09-new-landscape.md#级联信道模型) | 相移矩阵 $\boldsymbol{\Theta}$ 见 [Θ](#sym-Theta) |
| $\theta,\ \hat\theta$ | 待估参数及其估计（CRB） | [预备篇 9.4 · 感知这一侧怎么度量](part0/09-new-landscape.md#感知这一侧怎么度量crb-一句话) | — |
| $\theta_i,\ \theta_t,\ \theta_B$ | 入射角、透射角、Brewster 角（从法线量起） | [第一部 2.5 · 反射与透射](part1/02-maxwell-foundations.md#反射与透射边界条件的闭式推论) | 第一部第 5、6 章与第二部第 4、6 章沿用；正文提醒 Rappaport 等教材从界面量起 |
| $\theta\in\Theta$ | 统计决策问题里的未知状态（参数） | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部各章与第四部第 1、2 章的核心记号 |
| $\theta$ | 反注水的水位：$D_i=\min\{\theta,G_i\}$ | [第二部 6.7 · 命题 6.5](part2/06-error-budget.md#命题-65反注水) | 同章预算分配的边际损失水位写 $\lambda'$ |
| $\theta(s)$ | 平均代价 MDP 的相对值函数（$g+\theta(s)=\cdots$） | [第三部 4.2 · 写法 A · 知道分布 → 平均代价 MDP](part3/04-sequential-uncertainty.md#写法-a--知道分布--平均代价-mdp) | — |
| $\theta_1,\ \theta_2$ | 学习动力学相图里收敛区、循环区、混沌区的分界 | [第四部 6.9 · 三条轴，两条有先例，一条没有](part4/06-learning-dynamics.md#三条轴两条有先例一条没有) | 第四部第 9 章沿用 |
| $\theta,\ \theta_i$ | 平均场功控模型的名义功率目标与个体目标 | [第四部 7.3 · 功率军备竞赛](part4/07-mean-field.md#模型功率军备竞赛) | — |

### κ { #sym-kappa }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\kappa_i$ | 矩阵特征值 | [预备篇 5.5 · 容量公式的推导](part0/05-mimo.md#容量公式的推导) | 预备篇第 7 章沿用；多数章节的特征值写 $\lambda_i$ |
| $\kappa$ | 芯片有效开关电容系数：本地计算能耗 $\kappa Lf^2$，功率 $\kappa f^3$ | [预备篇 6.8 · MEC](part0/06-wireless-networks.md#mec把算力放到网络边缘) | 第三部第 4 章沿用 |
| $\kappa$ | 波数 $2\pi/\lambda$（第一部第 4 章的写法） | [第一部 4.1 · 从 2WT 到 2L/λ](part1/04-spatial-structure.md#从-2wt-到-2lλ时间的定理在空间重演) | 四套写法见[第三节](#same) |
| $\kappa$ | 墙面起伏扰动的横向空间频率 | [第一部 8.3 · Q1 的形式化](part1/08-dimension-and-prediction.md#q1-的形式化有效维度与环境等价类) | 第一部第 1 章的记号提醒说第 8、9 章的 $\kappa$ 不是波数 |
| $\kappa$ | 主径能量占比，莱斯因子 $K=\kappa/(1-\kappa)$ | [第一部 9.7 · 收束](part1/09-exchange-and-universality.md#收束普适性相图与知识的价格地图) | — |
| $\kappa$；$\kappa_\ell,\ \kappa_{\mathrm e},\ \kappa_{\mathrm f}$ | 知识获取速率：全部资源投入感知时每秒写进多少比特知识 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | 第二部第 6、7 章沿用 |
| $\kappa$；$\kappa_{\mathrm{SE}},\ \kappa_{\mathrm{gain}}$ | 离散判决损失的二阶系数；谱效对错格的斜率；增益环的转换系数 | [第二部 6.2 · 它在哪里断掉](part2/06-error-budget.md#它在哪里断掉离散判决) | 正文提醒这三者与知识获取速率 $\kappa$ 不是同一个量 |
| $\kappa$ | 条件数 | [第三部 6.2 · Arjevani–Shamir 2015](part3/06-communication-lower-bounds.md#arjevanishamir-2015数轮数) | — |
| $\kappa$ | 批处理时每多一个任务增加的时间：$T(K)\approx T_0+\kappa K$ | [第三部 7.2 · 第三击](part3/07-price-of-layering.md#第三击批处理规模效应杀死支撑价格) | — |
| $\kappa$；$\kappa_{\mathrm{eff}}(N,B)$ | 耦合度：簇外干扰功率与簇内信号功率之比；协作增益 scaling law 的第三个自变量 | [第四部 8.9 · 协作增益的天花板](part4/08-network-games.md#89-协作增益的天花板耦合度-kappa-的第一个候选) | 第四部第 7、9 章沿用；第四部第 1 章本部地图先预告 |

### λ { #sym-lambda }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\lambda$ | 波长，$\lambda=c/f$ | [预备篇 1.1 · 辐射功率](part0/01-em-waves-antennas.md#辐射功率larmor-公式与-f4-定律)（定义见 [预备篇 1.2 · 三个量的铁三角](part0/01-em-waves-antennas.md#三个量的铁三角)） | 全站默认含义；$\lambda/2$、$\lambda/4$、$\lambda/L$ 里的都是它；第二部第 4 章 $\lambda_{3.5},\ \lambda_{28}$ 是 3.5 GHz、28 GHz 的波长 |
| $\lambda^{(n)}$ | 码长为 $n$ 时的最大错误概率 | [预备篇 4.5 · 香农信道编码定理](part0/04-information-theory-basics.md#香农信道编码定理) | 只在香农编码定理处；同章 4.8 节的 $\lambda$ 是拉格朗日乘子（正文有提醒） |
| $\lambda,\ \boldsymbol{\lambda},\ \lambda_i$ | 拉格朗日乘子，经济读法是**影子价格**：约束放松一个单位，最优值改善多少；注水的水位与 $1/\lambda$ 成正比 | [预备篇 4.8 · CSIT 与时间注水](part0/04-information-theory-basics.md#第二部csit-与时间注水)（价格读法见 [预备篇 7.3 · 给约束定个价](part0/07-optimization-basics.md#直觉给约束定个价)） | 预备篇第 5、7 章，第一部第 1、9 章，第三部第 2、7 章都这样用；第二部第 6 章反注水的水位写 $\lambda'$ |
| $\lambda_i$ | 矩阵特征值（第一部第 10 章是积分算子的本征值） | [预备篇 5.5 · 容量公式的推导](part0/05-mimo.md#容量公式的推导) | 预备篇第 5、7 章另用 $\kappa_i$；第二部第 7 章 $\lambda_{\min}(\mathbf G)$、第四部第 2 章 $\lambda_k$、第四部第 9 章图谱 $\lambda_k,\ \lambda_N$ 同属此类 |
| $\lambda$ | 任务的计算密度 $L/D$（CPU 周期/比特） | [预备篇 6.8 · MEC](part0/06-wireless-networks.md#mec把算力放到网络边缘) | 只在预备篇 6.8 节的卸载门限里（正文有提醒） |
| $\lambda_\ell,\ \lambda_r$ | NUM 里的链路价格与用户 $r$ 看到的路径价格 | [预备篇 7.6 · 这是第三部 NUM 的种子](part0/07-optimization-basics.md#这是第三部-num-的种子) | 第三部第 2 章展开；第三部第 7 章指出队列长度就是这个价格 |
| $\lambda$ | 泊松到达率 | [预备篇 8.2 · 把无线计算卸载建成 MDP](part0/08-reinforcement-learning.md#完整示范把无线计算卸载建成-mdp) | 第三部第 4、5、9 章沿用（Little 定律、准入控制、M/G/1） |
| $\lambda$ | S-V 模型的簇内径到达率（簇到达率写 $\Lambda$） | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | 与上一行同是泊松率，对象是多径而不是业务 |
| $\lambda$ | 地图采样点的空间密度（个/m²） | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | 第二部第 6 章为避撞改写 $\lambda_{\mathrm d}$ |
| $\boldsymbol{\lambda}$ | 分离超平面的法向量（证明里的权重向量） | [第二部 3.2 · 记号](part2/03-task-knowledge-lattice.md#记号把第-2-章的向量再用一次) | 只在该证明里 |
| $\lambda$ | 域适应界里理想联合假设的误差 $\min_{h'}[\epsilon_S(h')+\epsilon_T(h')]$ | [第二部 4.3 · 定理 4.3 与四步证明](part2/04-environment-generalization.md#定理-43-与四步证明) | 同章大量出现的 $\lambda$ 是波长 |
| $\lambda$ | 切换代价的单价 | [第三部 1.2 · 山三 · 不确定](part3/01-three-mountains.md#山三--不确定不知道下一秒会发生什么) | — |
| $\lambda$ | 带预测算法的信任旋钮：$\lambda$ 越小越依赖预测 | [第三部 1.4 · 滑雪租赁](part3/01-three-mountains.md#三滑雪租赁预测的价目表已经精确到公式) | 第三部第 4、5 章沿用 |
| $\lambda$ | $\lambda$-强凸的曲率下界 | [第三部 6.2 · Arjevani–Shamir 2015](part3/06-communication-lower-bounds.md#arjevanishamir-2015数轮数) | — |
| $(\lambda,\mu)$ | smoothness 框架的两个常数，无政府代价界 $\lambda/(1-\mu)$ | [第三部 7.3 · 借一把尺子](part3/07-price-of-layering.md#借一把尺子price-of-x-的最坏比值证法) | 第四部第 8 章沿用；正文提醒它与价格 $\lambda$ 无关 |
| $\lambda$ | $\lambda$-exponential 函数类的指数 | [第三部 8.3 · 已知紧的只有三类](part3/08-computing-network-capacity.md#已知紧的只有三类) | — |
| $\lambda$ | 凸组合系数，$\lambda\in[0,1]$ | [第四部 3.2 · 模型与记号](part4/03-information-structure-phase-diagram.md#模型与记号) | 预备篇第 7 章的凸组合系数写 $\theta$ |
| $\lambda$ | Lyapunov 指数：相邻轨道每步平均拉开的对数速率 | [第四部 6.1 · 两个学下棋的人](part4/06-learning-dynamics.md#61-两个学下棋的人目标在动) | — |
| $\lambda$ | 平均场功控模型里功率代价的系数 | [第四部 7.3 · 功率军备竞赛](part4/07-mean-field.md#模型功率军备竞赛) | — |

### μ { #sym-mu }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\mu,\ \mu_0$ | 磁导率与真空磁导率 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | — |
| $\mu_{\mathrm{dB}},\ \mu_X,\ \mu_a$ | 均值（阴影的 dB 均值、随机变量的均值、老虎机臂的平均奖励） | [预备篇 2.3 · 从连乘到高斯](part0/02-wireless-channel-basics.md#从连乘到高斯完整推导) | 预备篇第 4、8 章沿用 |
| $\mu$ | 5G NR 的 numerology：子载波间隔 $15\cdot2^{\mu}$ kHz | [预备篇 2.7 · 四象限分类](part0/02-wireless-channel-basics.md#27-四象限分类判据与系统含义) | 预备篇第 6 章、第四部第 2、3 章沿用 |
| $\mu$ | 注水水位，$\mu=\log_2 e/\lambda$ | [预备篇 4.8 · CSIT 与时间注水](part0/04-information-theory-basics.md#第二部csit-与时间注水) | 预备篇第 7 章写 $\mu\triangleq1/\lambda$；第三部第 2 章水位写 $\nu$ |
| $\mu_i$ | 非负约束 $p_i\ge0$ 的拉格朗日乘子 | [预备篇 7.5 · 逐步推导](part0/07-optimization-basics.md#逐步推导) | 第三部第 2 章沿用；预备篇第 5 章同一乘子写 $\nu_i$ |
| $\mu_n$ | 空间–波数同时受限的算子的特征值（Landau 相变） | [第一部 4.5 · 波数–孔径–角谱乘积定理与 Landau…](part1/04-spatial-structure.md#波数孔径角谱乘积定理与-landau-相变) | — |
| $\mu_j$；$\mu,\ \nu$ | 看到读数 $y_j$ 后的后验分布；泛指概率分布 | [第二部 2.4 · 证明的准备](part2/02-blackwell.md#证明的准备把-bayes-风险写成一堆向量上的凹函数之和) | — |
| $\mu_l$ | 链路 $l$ 的价格（Kelly 的 NETWORK 问题） | [第三部 2.2 · Kelly 的观念转换](part3/02-classical-foundations.md#22-kelly-的观念转换把网络写成一个凸优化) | 预备篇第 7 章链路价格写 $\lambda_\ell$ |
| $(\lambda,\mu)$ | smoothness 框架的两个常数 | [第三部 7.3 · 借一把尺子](part3/07-price-of-layering.md#借一把尺子price-of-x-的最坏比值证法) | 见 [λ](#sym-lambda) |
| $\mu$ | $\mu$-强凸 | [第三部 9.3 · 缺失定理二 · C(ε)](part3/09-research-agenda.md#缺失定理二--cεε-最优性的比特成本) | 第三部第 6 章写 $\lambda$-强凸 |
| $\mu$ | 共享先验：信息复杂度 $\mathrm{IC}(f,\mu)$ 的参数 | [第四部 4.7 · 多方](part4/04-coordination-information-theory.md#47-多方广播是资源不是负担) | 第四部第 5 章沿用 |
| $\mu,\ \mu_N$ | 群体分布；$N$ 个个体的经验分布 | [第四部 7.1 · 高峰期的地铁口](part4/07-mean-field.md#71-高峰期的地铁口人多为什么反而简单) | — |

### ν { #sym-nu }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\nu$ | 莱斯信道的直射分量幅度 | [预备篇 2.4 · 有视距时](part0/02-wireless-channel-basics.md#有视距时莱斯分布与-k-因子) | — |
| $\nu$ | 多普勒频率变量：时延–多普勒扩展函数 $S_h(\tau,\nu)$、模糊函数 $\chi(\tau,\nu)$ | [预备篇 2.8 · 时变传递函数与四个 Bello 函数](part0/02-wireless-channel-basics.md#时变传递函数与四个-bello-函数) | 第一部第 3 章 $\nu(\alpha)=f_m\cos\alpha$ |
| $\nu_i$；$\boldsymbol{\nu},\ \nu_j$ | 拉格朗日乘子：预备篇第 5 章是非负约束的乘子，第 7 章是等式约束的乘子 | [预备篇 5.4 · 功率怎么分](part0/05-mimo.md#功率怎么分注水的完整推导) | 预备篇第 7 章非负约束的乘子写 $\mu_i$ |
| $\nu$ | 刃峰绕射参数（Bullington / ITU-R P.526） | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | 第一部第 5 章沿用 |
| $\nu_D$ | 归一化最大多普勒频率 | [第一部 8.6 · 时间轴](part1/08-dimension-and-prediction.md#时间轴带限悖论与有效维度的重逢) | — |
| $\nu(R)$ | 感知的边际价格 $\mathrm d\epsilon^\star(R)/\mathrm dR$：多要 1 bit/s/Hz 要付多少感知精度 | [第一部 10.5 · Q3 · 价值论的接口](part1/10-research-agenda.md#q3--价值论的接口isac-的双重折中) | 第二部第 3、5 章沿用 |
| $\nu$ | 认知平衡点的标度指数 $\lim\mathrm d\ln\alpha^\star/\mathrm d\ln\Lambda$ | [第二部 7.6 · 精确陈述](part2/07-research-agenda.md#精确陈述精简四件套) | — |
| $\nu$ | 注水水位，$\nu=1/(2\lambda)$ | [第三部 2.1 · 注水](part3/02-classical-foundations.md#注水三步走并且给这三步命名) | 预备篇水位写 $\mu$ |
| $\nu_{\mathrm b}$ | 嵌套亏损（按比特计）：让信息结构变成部分嵌套还差多少比特 | [第四部 2.7 · 两条逃生通道](part4/02-team-decision-theory.md#两条逃生通道) | 第四部第 4、9 章沿用 |
| $\nu$ | 嵌套亏欠（按链路数计）：还差几条链路 | [第四部 3.7 · 纵轴必须可计算](part4/03-information-structure-phase-diagram.md#纵轴必须可计算) | 第四部第 1 章本部地图先预告；与上一行是同一缺口的两种度量 |

### ξ { #sym-xi }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\xi$ | 外生不确定性的样本路径（预测的价目表 $V(I)$ 里 $I(\xi;M)$ 的 $\xi$） | [第三部 5.2 · 第二级台阶](part3/05-price-of-prediction.md#第二级台阶信息松弛对偶把先知变成刻度尺) | 第二部第 1、5 章与第四部第 2 章引用 $V(I)$ 时沿用 |
| $\xi_i$ | 平均场模型里个体目标对名义值的偏差 | [第四部 7.5 · 异质版模型](part4/07-mean-field.md#异质版模型) | — |

### π { #sym-pi }

$\pi$ 默认是圆周率。下表是它作为记号的其他用法。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\pi(a\mid s)$；$\pi^\star$ | 策略：从状态到动作分布的映射；最优策略 | [预备篇 8.2 · 策略、回报与折扣因子](part0/08-reinforcement-learning.md#策略回报与折扣因子) | 第一部第 7 章 $\pi^\star$ 是从地图到通信决策的最优策略 |
| $\pi$ | 链 $T=\pi\circ\mathcal D\circ\mathcal C\circ\Phi(\mathcal E)$ 的最后一环：决策 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部第 3、7 章与第四部第 9 章沿用 |
| $\pi,\ \pi_i$；$\pi_T$ | 先验分布；任务 $T$ 自带的先验 | [第二部 2.4 · Blackwell 定理](part2/02-blackwell.md#24-blackwell-定理三种说法是同一件事) | 正文说明"本章 $\pi$ 一律指先验"；第二部第 5 章任务写成 $T=(A_T,L_T,\pi_T)$ |
| $\pi$ | 置换（GNN 的置换等变性 $\pi\star Z$） | [第三部 3.4 · 为什么置换等变是"对的"归纳偏置](part3/03-nonconvex-era.md#为什么置换等变是对的归纳偏置一个定理级的回答) | 置换矩阵写 $\boldsymbol{\Pi}$ |
| $\pi\in\Pi(M)$ | 可以使用预测消息 $M$ 的在线策略 | [第三部 5.4 · 定义与两条对偶形式](part3/05-price-of-prediction.md#定义与两条对偶形式) | 第三部第 9 章沿用 |
| $\pi$ | 通信协议（确定性通信复杂度 $D(f)$ 里对协议取最小） | [第三部 6.1 · 模型与矩形引理](part3/06-communication-lower-bounds.md#模型与矩形引理) | — |

### ρ { #sym-rho }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\rho$ | 电荷密度 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | — |
| $\rho$ | 名义信噪比 $P/N_0$ | [预备篇 4.8 · 三个数放在一起看](part0/04-information-theory-basics.md#三个数放在一起看) | 预备篇第 5 章、第一部第 10 章、第三部第 3、9 章沿用；多数章节信噪比写 $\gamma$ 或 $\mathrm{SNR}$ |
| $\rho(\cdot)$ | 矩阵的谱半径（Foschini–Miljanic 收敛判据 $\rho(\boldsymbol{\Gamma}\mathbf F)<1$） | [预备篇 6.5 · Foschini–Miljanic 迭代](part0/06-wireless-networks.md#foschinimiljanic-迭代分布式功控的经典) | 第四部第 6 章 $\rho(\mathcal G)$ 是图的谱量 |
| $\rho_t$ | PPO 的新旧策略概率比 | [预备篇 8.7 · Actor-Critic 与 PPO](part0/08-reinforcement-learning.md#actor-critic-与-ppo) | — |
| $\rho(d),\ \rho(\tau)$ | 空间或时间相关系数 | [第一部 1.6 · Q2 信道场的预测半径](part1/01-lie-of-randomness.md#q2-信道场的预测半径) | 第一部第 3、4 章沿用 |
| $\rho_1,\ \rho_2$ | 射线管波前的两个主曲率半径 | [第一部 2.4 · 高频渐近](part1/02-maxwell-foundations.md#高频渐近波怎样退化为射线) | 第一部第 5 章沿用 |
| $\rho_s$ | 粗糙面的散射损失因子 | [第一部 2.7 · 散射](part1/02-maxwell-foundations.md#散射波长作为环境细节的低通滤波器) | — |
| $\rho$ | Bernstein 椭圆参数（解析延拓域的大小） | [第一部 8.5 · 指数病态的骨架](part1/08-dimension-and-prediction.md#指数病态的骨架从两常数定理到稳定外推) | 定理 8.2：$\alpha(x)=1-\ln B(x)/\ln\rho$ |
| $\rho$ | 误配半径：决策者所用概率表与真实表的差距（猜想 1.3） | [第二部第 1 章 · 开放问题](part2/01-four-arrows.md#开放问题) | 第二部第 4、7 章沿用 |
| $\rho(a\mid z)$ | 随机化决策规则：看到读数 $z$ 时选动作 $a$ 的概率 | [第二部 2.6 · 定理 2.2](part2/02-blackwell.md#定理-22亏格控制一切任务上的风险差) | 第二部第 7 章为避撞改写 $\sigma$；第四部的决策规则写 $\gamma_i$ |
| $\rho_{\mathrm{feat}}$ | 泛化半径 $\Delta_{\mathrm{feat}}/L_{\mathrm{feat}}$ | [第二部 4.6 · 特征的几何尺度与泛化半径](part2/04-environment-generalization.md#定义特征的几何尺度与泛化半径) | 正文提醒不是误配半径 |
| $\rho_T,\ \rho_n$ | 决策后悔：用感知结果决策比全知决策多付的风险 | [第二部 5.2 · 第三轴为什么不独立](part2/05-cognitive-triangle.md#52-第三轴为什么不独立后悔是感知质量经任务映射后的函数) | 同章算例 5.1 的 $\rho$ 是功率份额（正文有提醒） |
| $\rho_{\mathrm{eff}}$ | 有效信噪比 | [第二部 5.5 · 同一条律](part2/05-cognitive-triangle.md#55-同一条律耐用品与易逝品从-t_mathrmcoh-到-t_mathrmenv) | — |
| $\rho$ | 采样误差的幂律指数：误差 $\propto S^{-\rho}$ | [第二部 6.7 · 问题的精确形式](part2/06-error-budget.md#问题的精确形式) | — |
| $\rho_A,\ \rho^\star$；$\rho_{\mathrm{up}},\ \rho_{\mathrm{lo}}$ | 竞争比、最优竞争比及其上下界 | [第三部 1.2 · 山三 · 不确定](part3/01-three-mountains.md#山三--不确定不知道下一秒会发生什么) | 第三部第 8 章沿用 |
| $\rho(f),\ \bar\rho$ | 非凸度 | [第三部 7.2 · 第一击](part3/07-price-of-layering.md#第一击原子性对偶间隙从零变正) | — |
| $\rho$ | 网络函数计算的汇点（接收节点） | [第三部第 8 章 · 章首](part3/08-computing-network-capacity.md) | 同章信源节点写 $\sigma_i$ |
| $\rho$ | M/G/1 队列的负载 $\lambda\mathbb E[S]$ | [第三部 9.3 · 缺失定理一 · V(I)](part3/09-research-agenda.md#缺失定理一--vi信息的价值函数) | — |
| $\rho_{ji}$ | 回归系数（Radner 定理的线性方程组） | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | 同章 2.6 节的 $\rho$ 是噪声标准差（正文有提醒） |
| $\rho$ | 一阶自回归干扰的相关系数 | [第四部 3.5 · 工程常识变成相边界](part4/03-information-structure-phase-diagram.md#工程常识变成相边界) | — |
| $\rho$ | 平均场博弈与平均场控制的分歧比 $J^{\mathrm{MFG}}/J^{\mathrm{MFC}}$ | [第四部 7.3 · 分歧比](part4/07-mean-field.md#分歧比一个闭式与一个不等式) | 第四部第 9 章沿用 |

### σ { #sym-sigma }

$\sigma$ 最常见的用法是标准差（$\sigma^2$ 为方差，如噪声方差 $\sigma^2$）。下表只列其他用法和有专名的标准差。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\sigma_{\mathrm{SF}},\ \sigma_{\mathrm{dB}}$ | 阴影衰落的标准差（dB） | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $\sigma_\tau$ | 均方根时延扩展 | [预备篇 2.6 · 时延扩展](part0/02-wireless-channel-basics.md#时延扩展多径在时间上铺多宽) | 预备篇第 3 章写 $\tau_{\mathrm{rms}}$（正文有提醒） |
| $\sigma_i$ | 矩阵的奇异值 | [预备篇 5.4 · SVD](part0/05-mimo.md#svd线性代数给出的答案) | 第一部第 8 章 $\sigma_j$ 是 $\mathrm D\Phi$ 的奇异值 |
| $\sigma$ | 电导率 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | 第一部第 6 章 Calderón 问题的电导率写 $\gamma$ |
| $\sigma_h$ | 表面高度起伏的均方根（粗糙度） | [第一部 2.7 · 散射](part1/02-maxwell-foundations.md#散射波长作为环境细节的低通滤波器) | — |
| $\sigma_e^2$ | 信道估计误差方差 | [第一部 9.1 · 知道天气才能定价](part1/09-exchange-and-universality.md#知道天气才能定价信道知识的经典价值理论) | 第二部第 4 章沿用 |
| $\sigma(S),\ \sigma(a^\star)$ | 由统计量生成的 σ-代数 | [第二部 3.2 · 记号](part2/03-task-knowledge-lattice.md#记号把第-2-章的向量再用一次) | — |
| $\sigma_i$ | 网络函数计算的信源节点 | [第三部 8.2 · 最小例子](part3/08-computing-network-capacity.md#最小例子反向蝴蝶上的算术和与足迹尺寸这一个量) | 同章汇点写 $\rho$ |
| $\sigma$ | Witsenhausen 反例初始状态的标准差（经典参数 $k\sigma=1$） | [第四部 1.2 · 反例的精确设置](part4/01-one-counterexample.md#12-反例的精确设置三件套齐全结论塌了) | — |
| $\sigma$；$\bar\sigma_T$ | 相关均衡：联合动作上的分布；$T$ 轮后的经验联合分布 | [第四部 6.2 · 三级均衡](part4/06-learning-dynamics.md#三级均衡) | — |

### τ { #sym-tau }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\tau$；$\tau_l,\ \bar\tau,\ \tau_{\max}$ | 时延；第 $l$ 条径的时延；平均时延；最大时延 | [预备篇 2.6 · 时延扩展](part0/02-wireless-channel-basics.md#时延扩展多径在时间上铺多宽) | — |
| $\tau_{\mathrm{rms}}$ | 均方根时延扩展 | [预备篇 3.6 · 三种实现方式](part0/03-digital-communications.md#三种实现方式) | 预备篇第 2 章写 $\sigma_\tau$ |
| $\tau_c$；$\tau_p$ | 相干块长度 $T_cB_c$（符号数）；导频长度 | [预备篇 5.9 · 导频污染](part0/05-mimo.md#导频污染唯一不随-m-消失的损伤) | 第一部第 1 章沿用 |
| $\tau$ | 轨迹 $(s_0,a_0,s_1,\dots)$ | [预备篇 8.7 · REINFORCE 推导](part0/08-reinforcement-learning.md#reinforce-推导对数导数戏法) | — |
| $\tau_i$ | TCP 流 $i$ 的往返时延 | [第三部 2.5 · TCP Reno](part3/02-classical-foundations.md#tcp-reno从-aimd-反解出-alpha2) | — |
| $\tau$ | 时隙长度 | [第三部 4.2 · 问题 P](part3/04-sequential-uncertainty.md#问题-p边缘节点的能量时延卸载调度) | — |
| $\tau$ | 停时 | [第三部 5.1 · 第一级台阶](part3/05-price-of-prediction.md#第一级台阶先知不等式价目表的两个端点) | — |
| $\tau$ | 每个协作用户的导频开销（可用符号比例 $1-\tau K/L$） | [第四部第 8 章 · 开放问题](part4/08-network-games.md#开放问题) | 第四部第 9 章 9.6 节沿用 |

### φ、ϕ { #sym-phi }

两个字形 $\phi$ 与 $\varphi$ 在全站混用。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\varphi,\ \phi_i$；$\Delta\varphi$ | 相位；相位差 | [预备篇 1.3 · 逐步推导 $d_F = 2D^2/\lambda$](part0/01-em-waves-antennas.md#逐步推导-d_f--2d2lambda) | — |
| $\varphi$ | 方位角（与俯仰角 $\theta$ 成对） | [预备篇 1.4 · 方向图](part0/01-em-waves-antennas.md#参数一方向图) | 第一部第 9 章 $\phi_\ell$ 是到达角与离开角（正文提醒不是相位） |
| $\phi,\ \varphi$ | 标准正态概率密度 | [预备篇 4.6 · 模型与推导主线](part0/04-information-theory-basics.md#模型与推导主线) | 第二部第 6 章沿用 |
| $\phi_i$ | Mercer 展开的本征函数（正交场型） | [第一部 10.3 · 互信息的算子表示](part1/10-research-agenda.md#互信息的算子表示) | — |
| $\varphi$ | 作用在后验分布上的凸函数（Blackwell 定理 (iii)） | [第二部 2.4 · Blackwell 定理](part2/02-blackwell.md#24-blackwell-定理三种说法是同一件事) | — |
| $\varphi_p$ | 第 $p$ 条径的发射方向 | [第二部 3.4 · 第一步引理](part2/03-task-knowledge-lattice.md#第一步引理两个任务的充分统计量显式解) | 第二部第 7 章沿用 |
| $\varphi_{\mathrm{feat}}$ | 信道的一个标量特征 | [第二部 4.6 · 特征的几何尺度与泛化半径](part2/04-environment-generalization.md#定义特征的几何尺度与泛化半径) | — |
| $\varphi$ | 黄金比 $(1+\sqrt5)/2$ | [第三部 3.1 · 三个闭式临界值](part3/03-nonconvex-era.md#三个闭式临界值可用笔验证) | — |
| $\varphi_k$；$\varphi$ | nomographic 函数 $f=\psi(\sum_k\varphi_k(x_k))$ 的内函数（第三部第 6 章）；$f=\varphi(\sum_k\psi_k)$ 的外函数（第三部第 8 章） | [第三部 6.5 · 战场三](part3/06-communication-lower-bounds.md#战场三aircomp它改变的不是话费是货币单位) | 两章把内外函数的字母对调了 |
| $\varphi$ | 两个策略向量的夹角（MFG 与 MFC 的分歧） | [第四部 7.3 · 分歧比](part4/07-mean-field.md#分歧比一个闭式与一个不等式) | — |

### ψ、Ψ { #sym-psi }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\psi$ | 两副线极化天线的夹角（极化失配） | [预备篇 1.4 · 极化](part0/01-em-waves-antennas.md#参数四极化) | 同章 1.6 节的 $\psi$ 是阵元相位差（正文有提醒） |
| $\psi$ | 均匀线阵相邻阵元的相位差 $kd\sin\theta+\beta$ | [预备篇 1.6 · 均匀线阵的阵因子](part0/01-em-waves-antennas.md#均匀线阵的阵因子逐步推导) | 第二部第 6 章沿用 |
| $\psi$；$\Psi$ | 阴影（dB 值）；阴影的线性值（多次衰减的乘积） | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $\psi(\mathbf r)$ | 程函（eikonal） | [第一部 2.4 · 高频渐近](part1/02-maxwell-foundations.md#高频渐近波怎样退化为射线) | 第一部第 5 章沿用 |
| $\psi$ | 方向余弦（传播方向与阵列轴夹角的余弦） | [第一部 4.5 · 波数–孔径–角谱乘积定理与 Landau…](part1/04-spatial-structure.md#波数孔径角谱乘积定理与-landau-相变) | — |
| $\psi$ | Channel Charting 的映射 $\mathcal H\to\mathbb R^d$ | [第一部 7.5 · Channel Charting](part1/07-channel-cartography.md#channel-charting有度量无定理) | — |
| $\psi(\mathbf v),\ \psi_T$ | Bayes 风险里对每个读数取的凹函数（最小期望损失） | [第二部 2.4 · 证明的准备](part2/02-blackwell.md#证明的准备把-bayes-风险写成一堆向量上的凹函数之和) | 第二部第 3、5 章沿用 |
| $\Psi(\sigma)$ | 离散判决环的期望判决损失 | [第二部 6.2 · 它在哪里断掉](part2/06-error-budget.md#它在哪里断掉离散判决) | — |
| $\psi$；$\psi_k$ | nomographic 函数的外函数（第三部第 6 章）；内函数（第三部第 8 章） | [第三部 6.5 · 战场三](part3/06-communication-lower-bounds.md#战场三aircomp它改变的不是话费是货币单位) | 见 [φ](#sym-phi) |
| $\Psi(p)$ | 期望势函数 $\mathbb E_{s\sim p}[\Phi(s)]$ | [第四部 6.6 · 一步之差](part4/06-learning-dynamics.md#66-一步之差mwu-的两个变体) | — |

### ω { #sym-omega }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\omega$ | 角频率 $2\pi f$ | [预备篇 1.1 · 辐射功率](part0/01-em-waves-antennas.md#辐射功率larmor-公式与-f4-定律) | — |
| $\omega$ | 地图预测模型的多径残差 | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | — |
| $\omega(z)$ | 调和测度（两常数定理） | [第一部 8.5 · 指数病态的骨架](part1/08-dimension-and-prediction.md#指数病态的骨架从两常数定理到稳定外推) | — |
| $\omega(t)$ | 时隙 $t$ 的随机状态（drift-plus-penalty 的"$\omega$-only 策略"） | [第三部 4.1 · 一句「不知道未来」，四种严格化](part3/04-sequential-uncertainty.md#一句不知道未来四种严格化) | — |

### Γ { #sym-Gamma }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Gamma(\cdot)$ | Gamma 函数 | [预备篇 2.4 · 有视距时](part0/02-wireless-channel-basics.md#有视距时莱斯分布与-k-因子) | — |
| $\boldsymbol{\Gamma}$ | 目标 SINR 组成的对角阵 $\mathrm{diag}(\gamma_i)$ | [预备篇 6.5 · Foschini–Miljanic 迭代](part0/06-wireless-networks.md#foschinimiljanic-迭代分布式功控的经典) | — |
| $\Gamma,\ \Gamma_\perp,\ \Gamma_\parallel$；$\Gamma_{\mathrm{TE}},\ \Gamma_{\mathrm{TM}}$ | 反射系数（按极化分） | [第一部 2.5 · 反射与透射](part1/02-maxwell-foundations.md#反射与透射边界条件的闭式推论) | 第一部第 5 章、第二部第 6 章环一沿用 |
| $\Gamma$ | S-V 模型的簇间衰减常数（簇内写 $\gamma$） | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | — |
| $\Gamma$ | 两常数定理里观测数据所在的边界子集 $\Gamma\subset\partial\Omega$ | [第一部 8.5 · 指数病态的骨架](part1/08-dimension-and-prediction.md#指数病态的骨架从两常数定理到稳定外推) | — |
| $\Gamma(e\to e';f)$ | 泛化差：模型 $f$ 从环境 $e$ 换到 $e'$ 后风险的变化 | [第二部 4.1 · 记号](part2/04-environment-generalization.md#记号环境类源与目标风险差) | 第二部第 7 章沿用 |
| $\Gamma$ | 必要条件熵：两节点强协调里，公共随机率 $R_0\ge\Gamma$ 时容量域退化为经验协调的 $R\ge I(X;Y)$ | [第四部 4.2 · 分级](part4/04-coordination-information-theory.md#423-分级经验协调不用买公共随机性强协调要买) | 原文记作 $H(Y\dagger X)$ |
| $\Gamma$；$\Gamma^N_m$ | 策略式博弈 $(\mathcal N,\{A_i\},\{u_i\})$；$N$ 人、每人至多 $m$ 个动作的博弈族 | [第四部 4.5 · 三条定理](part4/04-coordination-information-theory.md#452-三条定理) | 第四部第 8 章沿用 |

### Δ { #sym-Delta }

$\Delta$ 作前缀时表示差量（$\Delta d$、$\Delta t$、$\Delta f$、$\Delta\varphi$ 等），首见 [预备篇 1.3 · 逐步推导 $d_F = 2D^2/\lambda$](part0/01-em-waves-antennas.md#逐步推导-d_f--2d2lambda)。下表是有专名的用法。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Delta f$ | OFDM 子载波间隔 | [预备篇 3.7 · 正交化，把一条宽路拆成 N 条窄路](part0/03-digital-communications.md#第二步正交化把一条宽路拆成-n-条窄路) | 5G NR 的 $\Delta f=15\cdot2^{\mu}$ kHz 见预备篇第 6 章 |
| $\Delta_a$ | 老虎机次优臂的间隙 $\mu^\star-\mu_a$ | [预备篇 8.1 · UCB](part0/08-reinforcement-learning.md#ucb给不确定性发奖金) | 第三部第 4 章写 $\Delta_i$ |
| $\Delta$ | 阵元间距、空间采样间隔（第一部第 4 章 $\Delta=\pi/\kappa=\lambda/2$） | [预备篇 9.2 · 近场给了什么新能力](part0/09-new-landscape.md#近场给了什么新能力距离域聚焦) | — |
| $\Delta r$ | 距离分辨率 $c/(2B)$ | [第一部 6.1 · 第一层](part1/06-inverse-problem.md#第一层回声直觉一切良态) | — |
| $\Delta$ | 拉普拉斯算子（$(\Delta-q)v=0$） | [第一部 6.2 · 唯一性定理及其证明骨架](part1/06-inverse-problem.md#唯一性定理及其证明骨架) | — |
| $\Delta U(\varepsilon)$ | 地图效能损失：地图带误差 $\varepsilon$ 时通信效用少了多少 | [第一部 7.6 · 诚实盘点](part1/07-channel-cartography.md#诚实盘点三句话与三个基本问题) | 第二部第 1–3 章沿用 |
| $\Delta R$ | 有限反馈造成的速率损失 | [第一部 9.2 · 汇率表的第一行](part1/09-exchange-and-universality.md#汇率表的第一行反馈比特换复用增益) | 第二部第 1 章沿用 |
| $\Delta C(R_{\mathrm{env}})$；$\Delta C(q)$ | 知识汇率：花 $R_{\mathrm{env}}$ 比特描述环境能换来多少容量增益；第二部第 5 章改以知识存量 $q$ 为自变量 | [第一部 9.4 · "CKM 的香农曲线"](part1/09-exchange-and-universality.md#ckm-的香农曲线一条尚不存在的曲线) | 第一部 Q3 的核心记号，第二部第 1、5、7 章沿用 |
| $\Delta(\mathcal E,\mathcal F)$ | Le Cam 距离 $\max\{\delta(\mathcal E,\mathcal F),\delta(\mathcal F,\mathcal E)\}$ | [第二部 1.5 · 目标形态](part2/01-four-arrows.md#15-目标形态带汇率的数据处理不等式) | 第二部第 2 章沿用 |
| $\mathcal H\Delta\mathcal H$ | 假设类的对称差（域适应界里的 $d_{\mathcal H\Delta\mathcal H}$） | [第二部 4.1 · 一条立刻能写下的界，以及它为什么没用](part2/04-environment-generalization.md#一条立刻能写下的界以及它为什么没用) | — |
| $\Delta_{\mathrm{feat}}$ | 特征的分辨单元：特征变多少才算"变了" | [第二部 4.6 · 特征的几何尺度与泛化半径](part2/04-environment-generalization.md#定义特征的几何尺度与泛化半径) | — |
| $\Delta(s)$ | 相邻 DFT 波束的增益差（dB） | [第二部 6.4 · 先把 DFT 码本的几何算清楚](part2/06-error-budget.md#先把-dft-码本的几何算清楚) | — |
| $\Delta(x)$ | 两个频带的期望代价之差（学习动力学） | [第四部 6.6 · 一步之差](part4/06-learning-dynamics.md#66-一步之差mwu-的两个变体) | — |
| $\Delta_N$ | 平均场里有限 $N$ 个体造成的涨落 | [第四部 7.5 · 异质版模型](part4/07-mean-field.md#异质版模型) | — |

### Θ { #sym-Theta }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Theta_{\mathrm{HPBW}}$ | 半功率波束宽度 | [预备篇 5.3 · 波束的几何](part0/05-mimo.md#波束的几何宽度码本与扫描) | 预备篇第 1 章写 $\theta_{3\mathrm{dB}}$ |
| $\Theta(\cdot)$；$\tilde\Theta(\cdot)$ | 渐近同阶；忽略对数因子的同阶 | [预备篇 5.7 · 2026 年 8 月](part0/05-mimo.md#2026-年-8-月一个二十年悬案的候选解) | 与参数集 $\Theta$ 同字母，看它后面跟的是不是函数括号 |
| $\boldsymbol{\Theta}$ | RIS 相移矩阵 $\mathrm{diag}(e^{j\theta_n})$ | [预备篇 9.3 · 级联信道模型](part0/09-new-landscape.md#级联信道模型) | — |
| $\Theta$；$\Theta_\varepsilon$ | 参数（状态）集；精度 $\varepsilon$ 下环境等价类的集合 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部各章与第四部第 2 章沿用 |

### Λ { #sym-Lambda }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Lambda$ | S-V 模型的簇到达率（簇内径到达率写 $\lambda$） | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | — |
| $\Lambda_\gamma,\ \Lambda_q$ | Dirichlet-to-Neumann 映射：边界上"加电压、测电流"的算子 | [第一部 6.2 · 从信道观测到边界数据](part1/06-inverse-problem.md#从信道观测到边界数据) | 同章 radio SLAM 一节的 $\Lambda$ 是对数似然（正文有提醒） |
| $\Lambda(\mathcal E)$ | 任务格：实验 $\mathcal E$ 下全部任务类充分统计量组成的格 | [第二部 3.4 · 任务格](part2/03-task-knowledge-lattice.md#34-任务格从任务类到划分的单调映射) | 第二部第 7 章沿用 |
| $\Lambda$；$\Lambda_c,\ \Lambda_\ell$ | 认知回路的无量纲数 $\kappa T_{\mathrm{env}}/q_{\mathrm{sat}}$：一个环境相干期内全力感知能把知识池灌满几遍；$\Lambda_c$ 是值得感知的门槛 | [第二部第 5 章 · 章首](part2/05-cognitive-triangle.md)（定义见 [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型)） | 第二部第 6、7 章沿用；第二部第 6 章另有拉格朗日函数 $\Lambda(b,\mu)$ |
| $\Lambda(\mathcal N)$ | 网络 $\mathcal N$ 的割集族 | [第三部 8.2 · 割集上界](part3/08-computing-network-capacity.md#割集上界一次不跳步的计数) | — |

### Π { #sym-Pi }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Pi$；$\Pi(M),\ \Pi(\varepsilon),\ \Pi(R)$ | 策略类或协议类：受限的决策者类；可用预测消息 $M$ 的在线策略类；达到 $\varepsilon$-最优的协议类 | [第二部第 1 章 · 开放问题](part2/01-four-arrows.md#开放问题) | 第三部第 5、6、9 章沿用 |
| $\boldsymbol{\Pi}$ | 置换矩阵 | [第三部 3.4 · 为什么置换等变是"对的"归纳偏置](part3/03-nonconvex-era.md#为什么置换等变是对的归纳偏置一个定理级的回答) | — |
| $\Pi(\mathcal N)$ | 网络的 Steiner 树填充数 | [第三部 8.3 · 已知紧的只有三类](part3/08-computing-network-capacity.md#已知紧的只有三类) | — |
| $\Pi$ | 协议记录：双方发出的全部消息按顺序连成的随机变量 | [第四部 5.2 · 通信复杂度的三级共享](part4/05-shared-world-model.md#52-通信复杂度的三级共享无共享共享随机共享模型) | — |
| $\Pi_i$ | 玩家 $i$ 的收益 | [第四部 8.4 · 无政府的代价](part4/08-network-games.md#84-无政府的代价smoothness-是一台可搬运的证明机器) | — |

### Φ { #sym-Phi }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Phi$；$\hat\Phi,\ \Phi_\theta$ | 环境→信道映射 $h=\Phi(E)$；$\hat\Phi$ 是引擎对它的近似，$\Phi_\theta$ 是参数取 $\theta$ 时的引擎 | [第一部第 5 章 · 章首](part1/05-deterministic-revival.md) | 第一部导读页先出现；第 1、2 章只用文字"确定性泛函"，第 2 章把同一映射记作 $\mathcal M$；第二部第 1 章链 $T=\pi\circ\mathcal D\circ\mathcal C\circ\Phi(\mathcal E)$ 的第一环 |
| $\boldsymbol{\Phi}$ | GNN 表示的功率分配映射（置换等变） | [第三部 3.4 · 为什么置换等变是"对的"归纳偏置](part3/03-nonconvex-era.md#为什么置换等变是对的归纳偏置一个定理级的回答) | — |
| $\Phi_T(\varepsilon)$ | 模型差 $\varepsilon$ 时协商任务 $T$ 要多付的罚项（猜想 5.10） | [第四部 5.8 · 猜想](part4/05-shared-world-model.md#猜想) | — |
| $\Phi$ | 势函数：任一玩家单方面改动作时，他自己收益的变化恰等于 $\Phi$ 的变化（精确势）；$\Phi$ 一般不是社会福利 | [第四部 6.4 · 给整个系统装一个"高度表"](part4/06-learning-dynamics.md#直觉给整个系统装一个高度表) | 第四部第 8 章 8.3 节沿用 |

### Ω { #sym-Omega }

单位"欧姆"也写 $\Omega$。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\Omega$；$\Omega_A$；$\lvert\Omega\rvert$ | 立体角；主瓣占据的立体角；角谱支撑的测度 | [预备篇 1.4 · 方向性与增益，以及 dBi 的准确含义](part0/01-em-waves-antennas.md#参数二方向性与增益以及-dbi-的准确含义) | 第一部第 4 章的 $\mathcal A\lvert\Omega\rvert$ 是空间自由度 |
| $\Omega(\cdot)$ | 渐近下界 | [预备篇 8.1 · regret](part0/08-reinforcement-learning.md#regret给学得慢定价) | — |
| $\Omega$ | Nakagami 分布的平均功率 | [第一部 3.2 · 相量和与中心极限定理](part1/03-statistical-lineage.md#相量和与中心极限定理瑞利分布的真正出身) | — |
| $\Omega\subset\mathbb R^n$ | 区域（Calderón 问题、两常数定理） | [第一部 6.2 · 从信道观测到边界数据](part1/06-inverse-problem.md#从信道观测到边界数据) | — |
| $\Omega_k$ | 第 $k$ 个理想扇区波束覆盖的方向集 | [第二部 3.4 · 第一步引理](part2/03-task-knowledge-lattice.md#第一步引理两个任务的充分统计量显式解) | — |

### C { #sym-C }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $C$；$C_{\mathrm{WF}},\ C_\epsilon$ | 信道容量；注水容量、中断容量 | [预备篇 1.5 · 物理意义与行为分析](part0/01-em-waves-antennas.md#物理意义与行为分析) | 第三部第 8 章 $\mathcal C_{\mathrm{cod}}$ 是计算容量 |
| $\mathcal C$ | 数字调制的星座 | [预备篇 3.2 · 用"位置"编码信息](part0/03-digital-communications.md#直觉用位置编码信息) | 第二部的 $\mathcal C$ 是链上的压缩环节 |
| $\mathcal C$ | 链 $T=\pi\circ\mathcal D\circ\mathcal C\circ\Phi(\mathcal E)$ 的压缩（编码）环节 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $C_0$ | 没有环境知识时的基线容量（持有 $q$ 比特知识时容量为 $C_0+\Delta C(q)$） | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | 第二部第 6、7 章沿用 |
| $C(\varepsilon)$；$C_{\mathcal F}(\varepsilon)$ | 协同的最小话费：达到 $\varepsilon$-最优所需的最少通信比特 | [第三部 1.2 · 山二 · 分布式](part3/01-three-mountains.md#山二--分布式不知道别的节点知道什么) | 第三部第 6、9 章与第四部第 3–5 章沿用 |
| $\mathcal C_{\mathrm{cod}}(\mathcal N,f)$ | 网络 $\mathcal N$ 计算函数 $f$ 的编码容量 | [第三部 8.2 · 割集上界](part3/08-computing-network-capacity.md#割集上界一次不跳步的计数) | — |
| $C(a),\ C_i(a)$；$C^\star$ | 社会代价与玩家 $i$ 的代价；社会最优代价 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | 第三部第 7 章 PoL 里的 $C_{\mathcal L}(I),\ C^\star(I)$ 是分层方案与联合最优的代价 |

### D { #sym-D }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\mathbf D$ | 电位移矢量 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | — |
| $D$ | 天线或阵列的最大尺寸，远场距离 $2D^2/\lambda$ | [预备篇 1.3 · 贴着电视墙看，和站在马路对面看](part0/01-em-waves-antennas.md#直觉贴着电视墙看和站在马路对面看) | — |
| $D$ | 天线的方向性（最大辐射强度与各向同性之比） | [预备篇 1.4 · 方向性与增益，以及 dBi 的准确含义](part0/01-em-waves-antennas.md#参数二方向性与增益以及-dbi-的准确含义) | 同章 $D$ 也指孔径尺寸，正文因此把抛物面直径另记为 $D_a$ |
| $D(p\Vert q)$ | KL 散度 | [预备篇 4.4 · 定义与非负性](part0/04-information-theory-basics.md#定义与非负性) | 第四部第 5、6 章沿用 |
| $D$；$R(D)$ | 失真；率失真函数 | [预备篇 4.9 · 率失真](part0/04-information-theory-basics.md#率失真容量的镜像) | 第二部第 3 章沿用（间接率失真） |
| $D$ | 同频小区的复用距离，$D/R=\sqrt{3N}$ | [预备篇 6.1 · 复用因子与复用距离](part0/06-wireless-networks.md#定义复用因子与复用距离) | 同章 6.8 节的 $D$ 是任务数据量（正文有提醒） |
| $D$ | 卸载任务的数据量（比特） | [预备篇 6.8 · MEC](part0/06-wireless-networks.md#mec把算力放到网络边缘) | — |
| $\mathcal D$ | DQN 的经验回放池 | [预备篇 8.6 · DQN 三件套](part0/08-reinforcement-learning.md#dqn-三件套) | — |
| $\mathcal D$ | 采样域（外推从这里出发） | [第一部 8.7 · Q2 的形式化](part1/08-dimension-and-prediction.md#q2-的形式化预测半径与边界曲线) | — |
| $\mathcal D$ | 链上的解码（重建）环节 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $D_S,\ D_T$ | 源域、目标域的数据分布 | [第二部 4.3 · 设定与 $\mathcal{H}\Delta\mathcal{H}$ 距离](part2/04-environment-generalization.md#设定与-mathcalhdeltamathcalh-距离) | — |
| $\bar D(\varepsilon)$ | 平均时延（Berry–Gallager） | [第三部 1.4 · Berry–Gallager 平方根律](part3/01-three-mountains.md#一berrygallager-平方根律无线资源领域的孤本) | — |
| $D(f)$ | 函数 $f$ 的确定性通信复杂度 | [第三部 6.1 · 模型与矩形引理](part3/06-communication-lower-bounds.md#模型与矩形引理) | — |

### E、𝓔 { #sym-E }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\mathbf E$ | 电场强度 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | — |
| $E_s,\ E_b$ | 每符号能量、每比特能量 | [预备篇 3.2 · 三个必须讲透的星座](part0/03-digital-communications.md#三个必须讲透的星座) | — |
| $E_l,\ E_o$ | 本地计算能耗、卸载能耗 | [预备篇 6.8 · MEC](part0/06-wireless-networks.md#mec把算力放到网络边缘) | — |
| $\mathcal E$；$E$ | 环境：全部几何边界、逐点材质与辐射条件；第一部第 8 章起 $\mathcal E$ 是环境状态空间、$E$ 是其中一个环境 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | 第一部第 5 章写 $h=\Phi(E)$；第二部起花体 $\mathcal E$ 改指**实验**（第二部第 1 章 1.2 节有提醒） |
| $\mathcal E,\ \mathcal F$；$\mathcal E_k$ | 统计实验：对每个状态 $\theta$ 给出读数的分布 $P_\theta$ | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部第 1 章定义 1.1 里不带下标的 $\mathcal E$ 仍是环境 |

### H、𝓗 { #sym-H }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\mathbf H$ | 磁场强度 | [预备篇 1.1 · Maxwell 四方程](part0/01-em-waves-antennas.md#maxwell-四方程逐条读懂它在说什么) | 预备篇第 5 章起粗体 $\mathbf H$ 是信道矩阵 |
| $H(f),\ H(t,f)$ | 频率响应、时变传递函数 | [预备篇 2.6 · 相干带宽](part0/02-wireless-channel-basics.md#相干带宽推出它与时延扩展互为倒数) | — |
| $H(X)$；$H_b(p)$ | 熵；二元熵函数 | [预备篇 4.1 · 平均惊讶度](part0/04-information-theory-basics.md#熵平均惊讶度) | 第二部、第四部把二元熵写成 $h(\cdot)$ |
| $\mathbf H$ | MIMO 信道矩阵，$\mathbf y=\mathbf H\mathbf x+\mathbf n$ | [预备篇第 5 章 · 章首](part0/05-mimo.md) | — |
| $H_n$ | 汉克尔函数（柱面谐波） | [第一部 4.4 · 散射几何的自由度](part1/04-spatial-structure.md#散射几何的自由度从-buccifranceschetti-到-miller) | — |
| $H^s$ | Sobolev 空间（光滑性约束） | [第一部 6.3 · Alessandrini](part1/06-inverse-problem.md#alessandrini数据误差换重建误差的汇率) | — |
| $\mathcal H$ | 信道空间：第一部导读页的 $\Phi:\mathcal E\to\mathcal H$，Channel Charting 的 $\psi:\mathcal H\to\mathbb R^d$ | [第一部 7.5 · Channel Charting](part1/07-channel-cartography.md#channel-charting有度量无定理) | — |
| $\mathcal H$ | 假设类（学习论）；$\mathcal H\Delta\mathcal H$ 距离 | [第二部第 1 章 · 开放问题](part2/01-four-arrows.md#开放问题)（定义见 [第二部 4.3 · 设定与 $\mathcal{H}\Delta\mathcal{H}$ 距离](part2/04-environment-generalization.md#设定与-mathcalhdeltamathcalh-距离)） | — |
| $\mathcal H_2,\ \mathcal H_\infty$ | 控制论里两种衡量闭环性能的系统范数 | [第四部第 3 章 · 章首](part4/03-information-structure-phase-diagram.md) | — |

### h { #sym-h }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $h,\ \mathbf h$ | 信道系数、信道矢量 | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $h_t,\ h_r$ | 发射、接收天线高度 | [预备篇 2.2 · 双径模型](part0/02-wireless-channel-basics.md#双径模型为什么室外指数常常是-4) | — |
| $h(X)$ | 微分熵 | [预备篇 4.1 · 连续变量](part0/04-information-theory-basics.md#连续变量微分熵) | — |
| $h$ | 刃峰绕射里障碍物高出收发连线的高度 | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | 第一部第 5 章沿用 |
| $h(\cdot)$ | 二元熵函数（预备篇写 $H_b$） | [第二部第 1 章 · 章首](part2/01-four-arrows.md) | 第四部第 4、9 章沿用（最小协调速率 $1-h(\epsilon)$） |
| $h\in\mathcal H$ | 假设（分类器） | [第二部 4.3 · 设定与 $\mathcal{H}\Delta\mathcal{H}$ 距离](part2/04-environment-generalization.md#设定与-mathcalhdeltamathcalh-距离) | — |

### K { #sym-K }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $K$ | 莱斯 $K$ 因子：直射分量与散射分量的功率之比 | [预备篇 2.4 · 有视距时](part0/02-wireless-channel-basics.md#有视距时莱斯分布与-k-因子) | 第一部第 9 章 $K=\kappa/(1-\kappa)$ |
| $\mathbf K$ | 协方差矩阵 | [预备篇 5.5 · 容量公式的推导](part0/05-mimo.md#容量公式的推导) | — |
| $K$ | 用户数（设备数、小区数） | [预备篇 5.9 · 两块基石](part0/05-mimo.md#两块基石) | — |
| $K$ | 地图预测用到的近邻数据点数 | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | — |
| $K$ | Mercer 展开的相关核（积分算子） | [第一部 10.3 · 互信息的算子表示](part1/10-research-agenda.md#互信息的算子表示) | — |
| $\mathbf K$ | 行随机矩阵：把一台仪器的读数随机翻译成另一台的读数（garbling） | [第二部 1.3 · 两种退化，两种知识](part2/01-four-arrows.md#13-两种退化两种知识本部的组织原则) | 第二部各章与第四部第 2 章沿用 |
| $K_{\mathrm{GK}}$ | Gács–Körner 公共信息 | [第二部 3.3 · 划分的格](part2/03-task-knowledge-lattice.md#33-划分的格shannon-1953-的信息格) | 第四部第 4 章展开 |
| $K$ | 批处理的任务数 | [第三部 7.2 · 第三击](part3/07-price-of-layering.md#第三击批处理规模效应杀死支撑价格) | — |

### L { #sym-L }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $PL(d)$ | 路径损耗（dB） | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $L$ | 抽头数、可分辨路径数 | [预备篇 2.8 · 时变冲激响应](part0/02-wireless-channel-basics.md#时变冲激响应) | 第一部第 1 章路径求和的上限也是 $L$ |
| $L(\cdot)$；$\mathcal L$ | 拉格朗日函数 | [预备篇 5.4 · 功率怎么分](part0/05-mimo.md#功率怎么分注水的完整推导) | 第二部第 6 章写 $\Lambda(b,\mu)$ |
| $L$ | 线孔径（阵列）长度，自由度 $2L/\lambda$ | [预备篇第 5 章 · 通往前沿](part0/05-mimo.md#通往前沿) | 第一部第 4 章沿用 |
| $L$ | 任务的计算量（CPU 周期），计算密度 $\lambda=L/D$ | [预备篇 6.8 · MEC](part0/06-wireless-networks.md#mec把算力放到网络边缘) | — |
| $L$ | 环境几何的特征尺度：$\lambda/L$ 决定哪些细节被信道看见 | [第一部 2.1 · 冻结的城市](part1/02-maxwell-foundations.md#冻结的城市一个思想实验) | 第二部第 4 章"泛化半径 $\lambda/4$ 对 $L$" |
| $L_T(\theta,a)$；$\lVert L_T\rVert$ | 任务 $T$ 的损失；损失的量程 $\sup L_T-\inf L_T$ | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部各章与第四部第 1 章沿用 |
| $L_{\mathrm{feat}}$ | 特征的几何灵敏度：环境每位移一米，特征变多少 | [第二部 4.6 · 特征的几何尺度与泛化半径](part2/04-environment-generalization.md#定义特征的几何尺度与泛化半径) | — |
| $L$ | 知识分层的层数 | [第二部 5.6 · 多时间尺度](part2/05-cognitive-triangle.md#56-多时间尺度t_mathrmenv-不止一个知识应分层折旧) | — |
| $\bar L$ | NUM 里最长路径的链路数 | [第三部 2.3 · 收敛条件](part3/02-classical-foundations.md#收敛条件一个完全由拓扑决定的稳定性判据) | — |
| $L$ | $L$-光滑：梯度的 Lipschitz 常数 | [第三部 9.3 · 缺失定理二 · C(ε)](part3/09-research-agenda.md#缺失定理二--cεε-最优性的比特成本) | — |

### N、𝒩 { #sym-N }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $N,\ N_t,\ N_r$ | 阵元数；发射、接收天线数 | [预备篇 1.4 · 方向性与增益，以及 dBi 的准确含义](part0/01-em-waves-antennas.md#参数二方向性与增益以及-dbi-的准确含义) | — |
| $\mathcal N(\mu,\sigma^2)$ | 高斯分布 | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | 第三部第 8 章的 $\mathcal N$ 是网络，第四部第 8 章是玩家集合 |
| $N_0$ | 噪声功率谱密度 | [预备篇 3.2 · 能量归一化](part0/03-digital-communications.md#能量归一化为什么是-1sqrt10) | — |
| $N$ | 频率复用因子（每簇的小区数） | [预备篇 6.1 · 复用因子与复用距离](part0/06-wireless-networks.md#定义复用因子与复用距离) | — |
| $N_{\mathrm{eff}}$（第一部） | 每个分辨单元里的有效路径数：路径功率的参与比 $(\sum a_n^2)^2/\sum a_n^4$，普适性相图的序参量 | [第一部 9.7 · 收束](part1/09-exchange-and-universality.md#收束普适性相图与知识的价格地图) | 第四部第 7 章的 $N_{\mathrm{eff}}$ 形式相同、对象不同 |
| $\mathcal N$ | 网络：有向图、信源与汇点 | [第三部 8.2 · 最小例子](part3/08-computing-network-capacity.md#最小例子反向蝴蝶上的算术和与足迹尺寸这一个量) | — |
| $N_{\mathrm{eff}}$（第四部） | 干扰耦合的有效人数：耦合权重的参与比 $1/\sum_n a_n^2$（定义 7.3） | [第四部第 7 章 · 章首](part4/07-mean-field.md)（定义见 [第四部 7.7 · 打破匿名与 $1/N$](part4/07-mean-field.md#打破匿名与-1n耦合是局部的)） | 与第一部第 9 章同名，对象从多径换成了干扰邻居 |
| $\mathcal N$ | 玩家集合 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | — |

### Q { #sym-Q }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $Q(x)$ | 标准正态的右尾概率（Q 函数） | [预备篇 2.3 · 相关距离](part0/02-wireless-channel-basics.md#相关距离阴影不是白噪声) | — |
| $Q^\pi(s,a),\ Q^\star$ | 动作价值函数 | [预备篇 8.3 · 价值函数](part0/08-reinforcement-learning.md#价值函数给状态标价) | — |
| $\mathbf P,\ \mathbf Q$；$P_\theta,\ Q_\theta$ | 实验的条件概率表（行是状态、列是读数）及其第 $\theta$ 行 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $Q(t)$ | 队列积压 | [第三部 4.2 · 问题 P](part3/04-sequential-uncertainty.md#问题-p边缘节点的能量时延卸载调度) | — |
| $Q$ | 团队二次代价 $\tfrac12u^{\top}Qu$ 的耦合矩阵（元素 $q_{ij}$） | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | — |
| $Q$ | Youla 参数：闭环对它是仿射的 | [第四部 3.1 · 抬桌子过门](part4/03-information-structure-phase-diagram.md#31-抬桌子过门两种可解一条赛跑) | — |

### q { #sym-q }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $q(\mathbf r)$ | 散射势 | [第一部第 6 章 · 章首](part1/06-inverse-problem.md) | — |
| $q$ | BSC 翻转概率（第二部的写法） | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 预备篇写 $\varepsilon$ |
| $q,\ q^\star,\ q_{\mathrm{sat}}$ | 知识存量（比特）；稳态知识量；饱和值 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | 第二部第 6、7 章沿用 |
| $q_i$ | TCP 丢包概率 | [第三部 2.5 · TCP Reno](part3/02-classical-foundations.md#tcp-reno从-aimd-反解出-alpha2) | 同章 $q_l(\cdot)$ 是供给函数（正文有提醒） |
| $q(m\mid\xi)$ | 预测方案：从未来样本路径到消息的信道 | [第三部 5.4 · 定义与两条对偶形式](part3/05-price-of-prediction.md#定义与两条对偶形式) | — |
| $q_{ij}$ | 团队代价耦合矩阵 $Q$ 的元素 | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | — |

### R { #sym-R }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $R_r$ | 辐射电阻 | [预备篇 1.1 · 辐射功率](part0/01-em-waves-antennas.md#辐射功率larmor-公式与-f4-定律) | — |
| $R,\ R_b$ | 速率、比特率 | [预备篇 3.1 · 每一层的"量纲"](part0/03-digital-communications.md#每一层的量纲) | — |
| $R_{\mathrm{env}}$ | 描述环境所花的比特率（知识汇率 $\Delta C(R_{\mathrm{env}})$ 的横轴） | [预备篇 4.9 · 本章概念在全站的角色索引](part0/04-information-theory-basics.md#本章概念在全站的角色索引)（定义见 [第一部 9.4 · "CKM 的香农曲线"](part1/09-exchange-and-universality.md#ckm-的香农曲线一条尚不存在的曲线)） | — |
| $R$ | 小区半径 | [预备篇 6.1 · 复用因子与复用距离](part0/06-wireless-networks.md#定义复用因子与复用距离) | — |
| $R$ | MDP 的奖励函数 | [预备篇 8.2 · 五元组定义](part0/08-reinforcement-learning.md#五元组定义) | 预备篇第 8 章的回报写 $G_t$ |
| $R_{\mathcal E}(\theta,\rho)$；$r_T$ | 风险：用规则 $\rho$ 时的期望损失；任务 $T$ 上的 Bayes 风险 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $R_{\mathrm{ceil}}$ | Q1 天花板：$d_{\mathrm{eff}}\log_2(1/\varepsilon)$ 比特 | [第二部 3.5 · 顶与底](part2/03-task-knowledge-lattice.md#35-顶与底q1-天花板与任务地板) | 第二部第 5、7 章沿用 |
| $R_e(f)$ | 模型 $f$ 在环境 $e$ 下的风险 | [第二部第 4 章 · 章首](part2/04-environment-generalization.md) | — |
| $\mathrm{Reg}_T$ | 遗憾（regret） | [第三部 1.2 · 山三 · 不确定](part3/01-three-mountains.md#山三--不确定不知道下一秒会发生什么) | — |
| $R^{\mathrm{pub}}_\varepsilon,\ R^{\mathrm{priv}}_\varepsilon$ | 允许公共随机性、私有随机性时的随机通信复杂度 | [第三部 6.1 · 随机性把 n 打成 O(1)](part3/06-communication-lower-bounds.md#随机性把-n-打成-o1为后文埋一颗雷) | 第四部第 4、5 章沿用 |
| $R_0$ | 公共随机率 | [第四部 4.2 · 模型与三个定义](part4/04-coordination-information-theory.md#421-模型与三个定义) | — |

### T、𝒯 { #sym-T }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $T_0$ | 标准噪声温度 290 K | [预备篇 1.5 · 物理意义与行为分析](part0/01-em-waves-antennas.md#物理意义与行为分析) | — |
| $T_c$ | 相干时间 | [预备篇 2.4 · 极坐标变换得到包络分布](part0/02-wireless-channel-basics.md#第二步极坐标变换得到包络分布) | 第二部第 5 章的环境相干期写 $T_{\mathrm{env}}$ |
| $T_s$ | 符号周期（采样间隔） | [预备篇 2.7 · 四象限分类](part0/02-wireless-channel-basics.md#27-四象限分类判据与系统含义) | — |
| $T$ | 轮数、时隙数（遗憾与学习的时间跨度） | [预备篇 8.1 · 生活里的两难](part0/08-reinforcement-learning.md#生活里的两难) | — |
| $\mathcal T$ | Bellman 最优算子 | [预备篇 8.3 · 最优 Bellman 方程与压缩映射](part0/08-reinforcement-learning.md#最优-bellman-方程与压缩映射) | 第二部的 $\mathcal T$ 是任务类 |
| $T_\perp$ | 透射系数 | [第一部 2.5 · 反射与透射](part1/02-maxwell-foundations.md#反射与透射边界条件的闭式推论) | — |
| $T=(A_T,L_T)$ | 任务：动作集与损失 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部第 5 章加上先验：$T=(A_T,L_T,\pi_T)$ |
| $\mathcal T$ | 任务类 | [第二部 1.7 · 本部地图、三张价目表，与怎么读这一部](part2/01-four-arrows.md#17-本部地图三张价目表与怎么读这一部) | — |
| $T_{\mathrm{env}}$ | 环境相干期：环境知识过期的时间尺度 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | 第二部第 6、7 章沿用 |

### V { #sym-V }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $V^\pi(s),\ V^\star$ | 状态价值函数 | [预备篇 8.3 · 价值函数](part0/08-reinforcement-learning.md#价值函数给状态标价) | — |
| $V_{\mathrm{oc}}$ | 天线端口的开路电压 | [第一部 1.2 · 从场到端口](part1/01-lie-of-randomness.md#从场到端口把电磁量翻译成通信量) | — |
| $V(I)$ | 预测的价目表：手握 $I$ 比特关于未来的信息时，最优在线策略的性能 | [第一部 9.4 · "CKM 的香农曲线"](part1/09-exchange-and-universality.md#ckm-的香农曲线一条尚不存在的曲线)（定义见 [第三部第 5 章 · 章首](part3/05-price-of-prediction.md)） | 第二部第 1、5 章与第四部第 2 章引用 |
| $V$ | drift-plus-penalty 的权衡参数：性能差 $O(1/V)$、队长 $O(V)$ | [第三部 4.1 · 一句「不知道未来」，四种严格化](part3/04-sequential-uncertainty.md#一句不知道未来四种严格化) | 与价值函数无关 |
| $V_0$ | 信息松弛里先知策略的期望价值 | [第三部 5.2 · 第二级台阶](part3/05-price-of-prediction.md#第二级台阶信息松弛对偶把先知变成刻度尺) | — |
| $V_n$ | $n$ 维单位球的体积 | [第三部 6.2 · Tsitsiklis–Luo 1987](part3/06-communication-lower-bounds.md#tsitsiklisluo-1987第一次给连续优化数比特) | — |
| $V(R)$ | 预测消息率为 $R$ 时的最优期望竞争比 | [第三部 9.3 · 缺失定理一 · V(I)](part3/09-research-agenda.md#缺失定理一--vi信息的价值函数) | 第三部第 5 章 $V(I)$ 的比值版 |

### W { #sym-W }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\mathbf w,\ \mathbf W$ | 波束赋形权向量；预编码或合并矩阵 | [预备篇 1.6 · 波束赋形](part0/01-em-waves-antennas.md#波束赋形把阵因子写成向量内积) | — |
| $W$ | 带宽（第一部第 8 章的 $W_{\mathrm{train}}$） | [第一部 8.6 · 频率轴](part1/08-dimension-and-prediction.md#频率轴平方罚与指数罚的缝合) | 多数章节带宽写 $B$ |
| $W_1$ | Wasserstein-1 距离（"搬沙子"距离） | [第二部第 4 章 · 章首](part2/04-environment-generalization.md) | — |
| $W_i$ | TCP 拥塞窗口 | [第三部 2.5 · TCP Reno](part3/02-classical-foundations.md#tcp-reno从-aimd-反解出-alpha2) | — |
| $W_{C,f}$ | 割 $C$ 上函数 $f$ 的最坏等价类数（计算网络的割集上界） | [第三部 8.3 · 更糟的](part3/08-computing-network-capacity.md#更糟的上界本身错了四年) | — |
| $W$ | 公共随机性：两端共享、与输入独立的随机变量 | [第四部 4.2 · 模型与三个定义](part4/04-coordination-information-theory.md#421-模型与三个定义) | 第四部第 7 章的 $W_i$ 是个体动力学里的独立噪声（布朗运动） |
| $W(a),\ W^\star$ | 社会福利与社会最优 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | — |

## 三、一个量，几种写法 { #same }

同一个量在不同章换了字母。读跨章引用时，先确认两边写的是不是同一个东西。

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $\varepsilon_r$；$\eta$ | 相对介电常数（第一部起为复数，含电导损耗） | [预备篇 1.1 · 从方程组到波动方程](part0/01-em-waves-antennas.md#从方程组到波动方程五步推导) | 第一部第 2 章写 $\varepsilon_r$，第 5 章 Fresnel 公式写 $\eta$ |
| $k,\ k_0,\ \kappa,\ \beta$ | 自由空间波数 $2\pi/\lambda$（rad/m） | [预备篇 1.2 · 三个量的铁三角](part0/01-em-waves-antennas.md#三个量的铁三角) | 预备篇第 1 章写 $k$；第一部第 2、5 章 $k_0$，第 4 章 $\kappa$，第 6、8 章 $k$，第 1 章 Q1 写 $\beta$（第一部第 1 章有提醒）；第一部第 8、9 章的 $\kappa$ 与第 8 章的 $\beta$ 都不是波数；预备篇第 1 章的 Boltzmann 常数也写 $k$ |
| $d_F$；$d_R$ | 远场距离 $2D^2/\lambda$（Fraunhofer 距离，亦称 Rayleigh 距离） | [预备篇 1.3 · 逐步推导 $d_F = 2D^2/\lambda$](part0/01-em-waves-antennas.md#逐步推导-d_f--2d2lambda) | 预备篇第 1 章写 $d_F$，第 9 章写 $d_R$（正文注明是同一个量） |
| $\theta_{3\mathrm{dB}}$；$\Theta_{\mathrm{HPBW}}$ | 半功率波束宽度 | [预备篇 1.4 · 方向图](part0/01-em-waves-antennas.md#参数一方向图) | 预备篇第 1 章写 $\theta_{3\mathrm{dB}}$，第 5 章写 $\Theta_{\mathrm{HPBW}}$ |
| $\mathrm{SNR}$；$\gamma$；$\rho$；$S$ | 信噪比 | [预备篇 1.5 · 物理意义与行为分析](part0/01-em-waves-antennas.md#物理意义与行为分析) | 预备篇第 3 章起常写 $\gamma,\ \bar\gamma$，第 4、5 章与第一部第 10 章写 $\rho$，第三部第 6 章写 $S$ |
| $B$；$W$ | 带宽 | [预备篇 1.5 · 物理意义与行为分析](part0/01-em-waves-antennas.md#物理意义与行为分析) | 多数章节写 $B$，第一部第 8 章写 $W$ |
| $n$；$\alpha$；$\gamma$ | 路径损耗指数 | [预备篇 2.2 · 对数距离模型](part0/02-wireless-channel-basics.md#对数距离模型把所有环境装进一个-n) | 预备篇第 2 章写 $n$，第 6 章与第四部第 7 章写 $\alpha$，第四部第 8 章算例 8.3 写 $\gamma$ |
| $f_m$；$f_d$ | 最大多普勒频率 $v/\lambda$ | [预备篇 2.5 · 频移的推导](part0/02-wireless-channel-basics.md#频移的推导) | 预备篇第 2 章写 $f_m$（同章 $f_d=v\cos\theta/\lambda$ 是单条径的多普勒频移），第 3 章写 $f_d$；第一部第 8 章的 $\nu_D$ 是归一化后的值 |
| $\theta$；$\alpha$ | 来波与运动方向的夹角（Clarke 模型） | [预备篇 2.5 · 频移的推导](part0/02-wireless-channel-basics.md#频移的推导) | 预备篇第 2 章写 $\theta$，第一部第 3 章写 $\alpha$ |
| $\sigma_\tau$；$\tau_{\mathrm{rms}}$ | 均方根时延扩展 | [预备篇 2.6 · 时延扩展](part0/02-wireless-channel-basics.md#时延扩展多径在时间上铺多宽) | 预备篇第 2 章写 $\sigma_\tau$，第 3 章写 $\tau_{\mathrm{rms}}$（第 3 章正文有提醒） |
| $H_b(\cdot)$；$h(\cdot)$ | 二元熵函数 | [预备篇 4.1 · 两个必须会算的例子](part0/04-information-theory-basics.md#两个必须会算的例子) | 预备篇写 $H_b$，第二部、第四部写 $h$ |
| $\varepsilon$；$q$；$p,\ r,\ \alpha$ | BSC 翻转概率 | [预备篇 4.2 · 条件作用永不增加熵](part0/04-information-theory-basics.md#条件作用永不增加熵) | 预备篇第 4 章写 $\varepsilon$，第二部第 1 章写 $q$，第 2 章写 $p,q,r$ 或 $\alpha$ |
| $\delta$；$\epsilon$；$\beta$ | BEC 擦除概率 | [预备篇 4.5 · 两个必会的容量](part0/04-information-theory-basics.md#两个必会的容量) | 预备篇第 4 章写 $\delta$，第二部第 1 章写 $\epsilon$，第 2 章写 $\epsilon$ 或 $\beta$ |
| $\mu$；$\nu$；$1/\lambda$ | 注水水位 | [预备篇 4.8 · CSIT 与时间注水](part0/04-information-theory-basics.md#第二部csit-与时间注水) | 预备篇第 4、7 章与第一部第 9 章写 $\mu$，第三部第 2 章写 $\nu=1/(2\lambda)$ |
| $\nu_i$；$\mu_i$ | 非负约束 $P_i\ge0$ 的拉格朗日乘子 | [预备篇 5.4 · 功率怎么分](part0/05-mimo.md#功率怎么分注水的完整推导) | 预备篇第 5 章写 $\nu_i$，第 7 章与第三部第 2 章写 $\mu_i$ |
| $\lambda_i$；$\kappa_i$ | 特征值 | [预备篇 5.5 · 容量公式的推导](part0/05-mimo.md#容量公式的推导) | 多数章节写 $\lambda_i$，预备篇第 5、7 章另用 $\kappa_i$ |
| $\theta$；$\lambda$ | 凸组合系数 | [预备篇 7.2 · 凸集](part0/07-optimization-basics.md#凸集两点之间不出界) | 预备篇第 7 章写 $\theta$，第四部第 3 章写 $\lambda$ |
| $\alpha,\ \alpha_k$；$\gamma$；$\eta,\ \eta_t$；$\varepsilon$ | 步长、学习率 | [预备篇 7.6 · 价格迭代](part0/07-optimization-basics.md#价格迭代次梯度上升) | 预备篇第 7、8 章写 $\alpha$，第三部第 2 章 NUM 写 $\gamma$，第三部第 4 章投影梯度写 $\eta_t$，第四部第 6 章 Hedge 写 $\eta$、MWU 写 $\varepsilon$ |
| $\lambda_\ell$；$\mu_l$ | NUM 的链路价格 | [预备篇 7.6 · 这是第三部 NUM 的种子](part0/07-optimization-basics.md#这是第三部-num-的种子) | 预备篇第 7 章写 $\lambda_\ell$，第三部第 2 章 Kelly 的 NETWORK 问题写 $\mu_l$ |
| $\gamma$；$\delta$ | 折扣（贴现）因子 | [预备篇 8.2 · 五元组定义](part0/08-reinforcement-learning.md#五元组定义) | 预备篇第 8 章写 $\gamma$，第四部第 8 章重复博弈写 $\delta$ |
| $\sigma$；$\gamma$ | 电导率 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | 第一部第 1、2 章写 $\sigma$，第 6 章 Calderón 问题写 $\gamma$ |
| $\mathcal M$；$\Phi$ | 环境→信道映射 | [第一部 2.3 · 唯一性定理](part1/02-maxwell-foundations.md#唯一性定理映射为什么存在且唯一) | 第一部第 2 章写 $\mathcal M$，第 5 章起写 $\Phi$ |
| $\lambda$；$\lambda_{\mathrm d}$ | 地图采样点的空间密度 | [第一部 7.4 · 四个理论孤岛](part1/07-channel-cartography.md#四个理论孤岛关于地图有多准我们知道什么) | 第一部第 7 章写 $\lambda$，第二部第 6 章写 $\lambda_{\mathrm d}$ |
| $a(y),\ \rho(a\mid z)$；$\sigma_i$；$\gamma_i$ | 决策规则：把观测映成动作（可以随机化） | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部第 2 章写 $a(y)$、$\rho(a\mid z)$，第 7 章为避撞写 $\sigma_i$，第四部写 $\gamma_i$ |
| $\lambda$；$\mu$ | 强凸参数（曲率下界） | [第三部 6.2 · Arjevani–Shamir 2015](part3/06-communication-lower-bounds.md#arjevanishamir-2015数轮数) | 第三部第 6 章写 $\lambda$-强凸，第 9 章写 $\mu$-强凸 |

## 四、各部核心记号 { #core }

按部列出读这一部必须认得的记号，行按首次出现排序。单个字母的其他含义见第二节对应的表。

### 预备篇 { #core-part0 }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $c$ | 光速 $1/\sqrt{\mu_0\varepsilon_0}\approx3\times10^8$ m/s | [预备篇 1.1 · 从方程组到波动方程](part0/01-em-waves-antennas.md#从方程组到波动方程五步推导) | — |
| $\eta_0$ | 自由空间波阻抗，约 $120\pi\ \Omega$ | [预备篇 1.1 · 从方程组到波动方程](part0/01-em-waves-antennas.md#从方程组到波动方程五步推导) | 见 [η](#sym-eta) |
| $\lambda,\ f$ | 波长与频率，$\lambda=c/f$ | [预备篇 1.1 · 辐射功率](part0/01-em-waves-antennas.md#辐射功率larmor-公式与-f4-定律)（定义见 [预备篇 1.2 · 三个量的铁三角](part0/01-em-waves-antennas.md#三个量的铁三角)） | $\lambda$ 另有十几种含义，见 [λ](#sym-lambda) |
| $k$ | 波数 $2\pi/\lambda$ | [预备篇 1.2 · 三个量的铁三角](part0/01-em-waves-antennas.md#三个量的铁三角) | 各章写法不一，见[第三节](#same) |
| $d_F$ | 远场距离 $2D^2/\lambda$ | [预备篇 1.3 · 逐步推导 $d_F = 2D^2/\lambda$](part0/01-em-waves-antennas.md#逐步推导-d_f--2d2lambda) | 预备篇第 9 章写 $d_R$ |
| $\mathbf a(\theta)$ | 阵列响应（导向）矢量 | [预备篇 1.3 · 逐步推导 $d_F = 2D^2/\lambda$](part0/01-em-waves-antennas.md#逐步推导-d_f--2d2lambda) | — |
| $\theta_{3\mathrm{dB}}$ | 半功率波束宽度 | [预备篇 1.4 · 方向图](part0/01-em-waves-antennas.md#参数一方向图) | 预备篇第 5 章写 $\Theta_{\mathrm{HPBW}}$ |
| $D$；$G$ | 方向性；增益（dBi） | [预备篇 1.4 · 方向性与增益，以及 dBi 的准确含义](part0/01-em-waves-antennas.md#参数二方向性与增益以及-dbi-的准确含义) | 同章 $D$ 也指孔径尺寸，正文因此把抛物面直径另记为 $D_a$ |
| $A_e$ | 有效孔径 $\lambda^2G/(4\pi)$ | [预备篇 1.4 · 方向性与增益，以及 dBi 的准确含义](part0/01-em-waves-antennas.md#参数二方向性与增益以及-dbi-的准确含义) | — |
| $P_t,\ P_r$；$G_t,\ G_r$ | 发射、接收功率；收发天线增益（Friis 公式） | [预备篇 1.4 · 有效孔径 $A_e$](part0/01-em-waves-antennas.md#参数三有效孔径-a_e)（Friis 公式见 [预备篇 1.5 · 完整推导](part0/01-em-waves-antennas.md#完整推导五步不跳步)） | — |
| EIRP | 等效全向辐射功率 $P_tG_t$ | [预备篇 1.5 · 完整推导](part0/01-em-waves-antennas.md#完整推导五步不跳步) | — |
| $C$ | 信道容量，$C=B\log_2(1+\mathrm{SNR})$ | [预备篇 1.5 · 物理意义与行为分析](part0/01-em-waves-antennas.md#物理意义与行为分析) | 见 [C](#sym-C) |
| $PL(d)$ | 路径损耗（dB） | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $\sigma_{\mathrm{SF}}$ | 阴影衰落标准差（dB） | [预备篇 2.1 · 数学分解](part0/02-wireless-channel-basics.md#数学分解为什么-db-域是加法) | — |
| $f_c$ | 载频 | [预备篇 2.2 · 3GPP 模型](part0/02-wireless-channel-basics.md#3gpp-模型今天真正在用的公式) | — |
| $Q(x)$ | 标准正态右尾概率 | [预备篇 2.3 · 相关距离](part0/02-wireless-channel-basics.md#相关距离阴影不是白噪声) | 见 [Q](#sym-Q) |
| $T_c$ | 相干时间 | [预备篇 2.4 · 极坐标变换得到包络分布](part0/02-wireless-channel-basics.md#第二步极坐标变换得到包络分布)（定义见 [预备篇 2.5 · 相干时间](part0/02-wireless-channel-basics.md#相干时间)） | — |
| $K$ | 莱斯 $K$ 因子 | [预备篇 2.4 · 有视距时](part0/02-wireless-channel-basics.md#有视距时莱斯分布与-k-因子) | 见 [K](#sym-K) |
| $f_m$；$B_D$ | 最大多普勒频率 $v/\lambda$；多普勒扩展 $2f_m$ | [预备篇 2.5 · 频移的推导](part0/02-wireless-channel-basics.md#频移的推导) | 预备篇第 3 章最大多普勒写 $f_d$ |
| $\sigma_\tau$；$B_c$ | 均方根时延扩展；相干带宽 | [预备篇 2.6 · 时延扩展](part0/02-wireless-channel-basics.md#时延扩展多径在时间上铺多宽) | 预备篇第 3 章写 $\tau_{\mathrm{rms}}$ |
| $\mathrm{SINR}$ | 信干噪比 | [预备篇 2.7 · 四象限分类](part0/02-wireless-channel-basics.md#27-四象限分类判据与系统含义) | — |
| $h(t,\tau),\ H(t,f)$ | 时变冲激响应、时变传递函数 | [预备篇 2.8 · 信道的统一表示](part0/02-wireless-channel-basics.md#28-信道的统一表示httau-与-htf) | — |
| $E_b/N_0$ | 每比特能量与噪声功率谱密度之比 | [预备篇 3.2 · 能量归一化](part0/03-digital-communications.md#能量归一化为什么是-1sqrt10) | 与 SNR 差一个频谱效率因子（预备篇第 3 章"常见误解"） |
| $P_b$；$P_s$ | 误比特率；误符号率 | [预备篇 3.2 · Gray 映射](part0/03-digital-communications.md#gray-映射一个便宜到不该不用的技巧) | — |
| $\gamma,\ \bar\gamma$ | 瞬时与平均信噪比 | [预备篇 3.5 · 模型](part0/03-digital-communications.md#模型) | 见 [γ](#sym-gamma) |
| $H(X)$；$H_b(p)$ | 熵；二元熵函数 | [预备篇 4.1 · 平均惊讶度](part0/04-information-theory-basics.md#熵平均惊讶度) | 第二部起二元熵写 $h(\cdot)$ |
| $I(X;Y)$ | 互信息 | [预备篇 4.2 · 条件作用永不增加熵](part0/04-information-theory-basics.md#条件作用永不增加熵)（定义见 [预备篇 4.3 · 定义与三种等价写法](part0/04-information-theory-basics.md#定义与三种等价写法)） | — |
| $D(p\Vert q)$ | KL 散度 | [预备篇 4.4 · 定义与非负性](part0/04-information-theory-basics.md#定义与非负性) | — |
| $R(D)$ | 率失真函数 | [预备篇 4.9 · 率失真](part0/04-information-theory-basics.md#率失真容量的镜像) | — |
| $\mathbf y=\mathbf H\mathbf x+\mathbf n$；$N_t,\ N_r$ | MIMO 信道模型；收发天线数 | [预备篇 5.4 · 模型](part0/05-mimo.md#模型) | — |
| $\sigma_i$ | 信道矩阵的奇异值 | [预备篇 5.4 · SVD](part0/05-mimo.md#svd线性代数给出的答案) | — |
| $L(\cdot)$ | 拉格朗日函数 | [预备篇 5.4 · 功率怎么分](part0/05-mimo.md#功率怎么分注水的完整推导) | — |
| $g(\boldsymbol{\lambda},\boldsymbol{\nu})$；$p^\star,\ d^\star$ | 对偶函数；原问题与对偶问题的最优值 | [预备篇 7.3 · 拉格朗日函数与对偶函数](part0/07-optimization-basics.md#拉格朗日函数与对偶函数) | — |
| $(\mathcal S,\mathcal A,P,R,\gamma)$ | MDP 五元组：状态集、动作集、转移概率、奖励、折扣因子 | [预备篇 8.2 · 五元组定义](part0/08-reinforcement-learning.md#五元组定义) | — |
| $G_t$ | 回报：从 $t$ 起的折扣累计奖励 | [预备篇 8.2 · 策略、回报与折扣因子](part0/08-reinforcement-learning.md#策略回报与折扣因子) | — |
| $V^\pi(s),\ Q^\pi(s,a)$ | 状态价值、动作价值函数 | [预备篇 8.3 · 价值函数](part0/08-reinforcement-learning.md#价值函数给状态标价) | — |
| $d_R$ | 瑞利距离 | [预备篇 9.2 · 分界在哪里](part0/09-new-landscape.md#分界在哪里瑞利距离的完整推导) | 与预备篇第 1 章的 $d_F$ 是同一个量 |
| $\boldsymbol{\Theta}$ | RIS 相移矩阵 | [预备篇 9.3 · 级联信道模型](part0/09-new-landscape.md#级联信道模型) | — |

### 第一部 { #core-part1 }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $R_{\mathrm{env}}$；$\Delta C(R_{\mathrm{env}})$ | 描述环境所花的比特率；知识汇率 | [预备篇 4.9 · 本章概念在全站的角色索引](part0/04-information-theory-basics.md#本章概念在全站的角色索引)（定义见 [第一部 9.4 · "CKM 的香农曲线"](part1/09-exchange-and-universality.md#ckm-的香农曲线一条尚不存在的曲线)） | — |
| $\varepsilon(\mathbf r)$ | 逐点复介电常数：环境的主要载体 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | — |
| $k(\mathbf r),\ k_0$ | 局部波数；自由空间波数 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | 第一部各章波数字母不一，见[第三节](#same) |
| $\bar{\bar{\mathbf G}}$ | 并矢 Green 函数：把点源换进同一环境得到的场 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | — |
| $\mathcal E$；$E$ | 环境：全部几何边界、逐点材质与辐射条件；一个具体环境 | [第一部 1.2 · Maxwell 的裁决](part1/01-lie-of-randomness.md#maxwell-的裁决信道是环境的确定性泛函) | 第二部起 $\mathcal E$ 改指实验，见 [E](#sym-E) |
| $\mathbf h_{\mathrm{eff}}$；$V_{\mathrm{oc}}$ | 天线的矢量等效长度；端口开路电压 $\mathbf h_{\mathrm{eff}}\cdot\mathbf E$ | [第一部 1.2 · 从场到端口](part1/01-lie-of-randomness.md#从场到端口把电磁量翻译成通信量) | — |
| $J_0(2\pi d/\lambda)$ | 二维各向同性散射下的空间自相关 | [第一部 1.4 · Rayleigh 衰落是最大无知模型](part1/01-lie-of-randomness.md#rayleigh-衰落是最大无知模型) | 三维各向同性时是 sinc（第一部第 4 章） |
| $\mathcal M$ | 环境→信道映射（第一部第 2 章的写法） | [第一部 2.3 · 唯一性定理](part1/02-maxwell-foundations.md#唯一性定理映射为什么存在且唯一) | 第 5 章起写 $\Phi$ |
| $\Gamma_\perp,\ \Gamma_\parallel$；$T_\perp$ | 反射系数；透射系数 | [第一部 2.5 · 反射与透射](part1/02-maxwell-foundations.md#反射与透射边界条件的闭式推论) | — |
| $D_{s,h}$ | UTD 绕射系数 | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | — |
| $\nu$；$F(\nu)$ | 刃峰绕射参数；绕射损耗函数 | [第一部 2.6 · 绕射](part1/02-maxwell-foundations.md#绕射几何光学的失效与两次修复) | 见 [ν](#sym-nu) |
| $\Lambda,\ \lambda$；$\Gamma,\ \gamma$ | S-V 模型：簇到达率与簇内径到达率；簇间与簇内衰减常数 | [第一部 3.4 · Saleh–Valenzuela](part1/03-statistical-lineage.md#salehvalenzuela多径是成簇到达的) | — |
| $\kappa$ | 波数（第一部第 4 章的写法） | [第一部 4.1 · 从 2WT 到 2L/λ](part1/04-spatial-structure.md#从-2wt-到-2lλ时间的定理在空间重演) | 见 [κ](#sym-kappa) |
| $\eta_1,\ \eta_2,\ \eta_3$ | 线、面、体孔径的空间自由度 | [第一部 4.3 · λ/2 采样、相干距离与自由度密度](part1/04-spatial-structure.md#三位一体λ2-采样相干距离与自由度密度) | — |
| $\mathcal A\lvert\Omega\rvert$ | 以 $\lambda^2$ 计的孔径面积乘角谱支撑的测度：空间自由度 | [第一部 4.5 · 波数–孔径–角谱乘积定理与 Landau…](part1/04-spatial-structure.md#波数孔径角谱乘积定理与-landau-相变) | — |
| $\Phi$；$\hat\Phi$ | 环境→信道映射 $h=\Phi(E)$；引擎对它的近似 | [第一部第 5 章 · 章首](part1/05-deterministic-revival.md) | 第四部的 $\Phi$ 是势函数，见 [Φ](#sym-Phi) |
| $q(\mathbf r)$；$\Lambda_\gamma$ | 散射势；Dirichlet-to-Neumann 映射 | [第一部第 6 章 · 章首](part1/06-inverse-problem.md) | — |
| $\Delta r$ | 距离分辨率 $c/(2B)$ | [第一部 6.1 · 第一层](part1/06-inverse-problem.md#第一层回声直觉一切良态) | — |
| $\Delta U(\varepsilon)$ | 地图效能损失 | [第一部 7.6 · 诚实盘点](part1/07-channel-cartography.md#诚实盘点三句话与三个基本问题) | — |
| $d_{\mathrm{eff}}(E;\varepsilon)$ | 有效维度：$\mathrm D\Phi[E]$ 大于 $\varepsilon\sigma_1$ 的奇异值个数 | [第一部 8.2 · 证据链](part1/08-dimension-and-prediction.md#证据链信道为什么远比环境小)（定义见 [第一部 8.3 · Q1 的形式化](part1/08-dimension-and-prediction.md#q1-的形式化有效维度与环境等价类)） | — |
| $\mathrm D\Phi[E]$；$\sigma_j$ | 映射在 $E$ 处的线性化（Fréchet 导数）及其奇异值 | [第一部 8.3 · Q1 的形式化](part1/08-dimension-and-prediction.md#q1-的形式化有效维度与环境等价类) | — |
| $[E]_\varepsilon$ | 环境等价类：精度 $\varepsilon$ 下信道分不开的环境 | [第一部 8.3 · Q1 的形式化](part1/08-dimension-and-prediction.md#q1-的形式化有效维度与环境等价类) | 第二部的 $\Theta_\varepsilon$ 由它组成 |
| $\alpha(r)$；$r_{\max}$ | 预测精度指数；预测半径（外推的硬墙） | [第一部 8.4 · 插值与外推](part1/08-dimension-and-prediction.md#插值与外推一步之遥的数学相变) | 见 [α](#sym-alpha) |
| $N_{\mathrm{eff}}$ | 每个分辨单元里的有效路径数 | [第一部 9.7 · 收束](part1/09-exchange-and-universality.md#收束普适性相图与知识的价格地图) | 第四部第 7 章同名不同义，见 [N](#sym-N) |

### 第二部 { #core-part2 }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $T=\pi\circ\mathcal D\circ\mathcal C\circ\Phi(\mathcal E)$ | 链：环境 → 信道 → 压缩 → 重建 → 决策 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $T=(A_T,L_T)$；$\lVert L_T\rVert$ | 任务：动作集与损失；损失的量程 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第二部第 5 章加上先验 $\pi_T$ |
| $r_T$ | 任务 $T$ 上的 Bayes 风险 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | — |
| $\mathcal E=(P_\theta)_{\theta\in\Theta}$；$\mathbf P$ | 实验：每个状态下读数的分布；写成行随机矩阵 | [第二部 1.2 · 把链写成算子复合](part2/01-four-arrows.md#12-把链写成算子复合四个箭头四种互不换算的度量) | 第一部的 $\mathcal E$ 是环境 |
| $\mathbf K$；$\mathbf Q=\mathbf P\mathbf K$ | garbling：与状态无关的随机后处理 | [第二部 1.3 · 两种退化，两种知识](part2/01-four-arrows.md#13-两种退化两种知识本部的组织原则) | — |
| $\mathcal E\succeq\mathcal F$ | Blackwell 序：$\mathcal E$ 在一切任务上不输 $\mathcal F$ | [第二部 1.3 · 两种退化，两种知识](part2/01-four-arrows.md#13-两种退化两种知识本部的组织原则) | — |
| $\lVert\cdot\rVert_{\mathrm{TV}}$ | 总变差距离，取半 $L_1$ 约定 | [第二部 1.5 · 目标形态](part2/01-four-arrows.md#15-目标形态带汇率的数据处理不等式) | — |
| $\delta(\mathcal E,\mathcal F)$；$\Delta$；$\delta_k$ | Le Cam 亏格；Le Cam 距离；$k$-亏格 | [第二部 1.5 · 目标形态](part2/01-four-arrows.md#15-目标形态带汇率的数据处理不等式) | 见 [δ](#sym-delta) |
| $\mathcal T$；$\delta_{\mathcal T}$ | 任务类；任务限制亏格 | [第二部 1.7 · 本部地图、三张价目表，与怎么读这一部](part2/01-four-arrows.md#17-本部地图三张价目表与怎么读这一部) | — |
| $\rho$ | 误配半径（猜想 1.3） | [第二部第 1 章 · 开放问题](part2/01-four-arrows.md#开放问题) | — |
| $\psi(\mathbf v)$ | Bayes 风险里对每个读数取的凹函数 | [第二部 2.4 · 证明的准备](part2/02-blackwell.md#证明的准备把-bayes-风险写成一堆向量上的凹函数之和) | — |
| $\top,\ \bot$ | 信息格的顶与底 | [第二部 3.3 · 划分的格](part2/03-task-knowledge-lattice.md#33-划分的格shannon-1953-的信息格) | — |
| $\mathcal S_T$ | 任务（类）的充分统计量 | [第二部 3.4 · 任务格](part2/03-task-knowledge-lattice.md#34-任务格从任务类到划分的单调映射) | — |
| $\Lambda(\mathcal E)$ | 任务格 | [第二部 3.4 · 任务格](part2/03-task-knowledge-lattice.md#34-任务格从任务类到划分的单调映射) | — |
| $\Theta_\varepsilon$ | 精度 $\varepsilon$ 下的环境等价类集合 | [第二部 3.4 · 无线任务格的第一张 Hasse 图](part2/03-task-knowledge-lattice.md#无线任务格的第一张-hasse-图) | — |
| $R_{\mathrm{ceil}}$ | Q1 天花板 $d_{\mathrm{eff}}\log_2(1/\varepsilon)$ | [第二部 3.5 · 顶与底](part2/03-task-knowledge-lattice.md#35-顶与底q1-天花板与任务地板) | — |
| $W_1$ | Wasserstein-1 距离 | [第二部第 4 章 · 章首](part2/04-environment-generalization.md) | — |
| $\Gamma(e\to e';f)$ | 泛化差 | [第二部 4.1 · 记号](part2/04-environment-generalization.md#记号环境类源与目标风险差) | — |
| $I_{\mathrm{GMI}}(s)$ | 广义互信息（误配译码的可达率） | [第二部 4.2 · 译码度量与 GMI](part2/04-environment-generalization.md#定义译码度量与-gmi) | — |
| $\epsilon_S,\ \epsilon_T$；$d_{\mathcal H\Delta\mathcal H}$ | 源域、目标域误差；域间距离 | [第二部 4.3 · 设定与 $\mathcal{H}\Delta\mathcal{H}$ 距离](part2/04-environment-generalization.md#设定与-mathcalhdeltamathcalh-距离) | — |
| $\rho_{\mathrm{feat}}$；$L_{\mathrm{feat}},\ \Delta_{\mathrm{feat}}$ | 泛化半径；特征的几何灵敏度与分辨单元 | [第二部 4.6 · 特征的几何尺度与泛化半径](part2/04-environment-generalization.md#定义特征的几何尺度与泛化半径) | — |
| $\Lambda$；$\Lambda_c$ | 认知回路的无量纲数；值得感知的门槛 | [第二部第 5 章 · 章首](part2/05-cognitive-triangle.md)（定义见 [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型)） | — |
| $\rho_T$ | 决策后悔 | [第二部 5.2 · 第三轴为什么不独立](part2/05-cognitive-triangle.md#52-第三轴为什么不独立后悔是感知质量经任务映射后的函数) | — |
| $q,\ q^\star,\ q_{\mathrm{sat}}$ | 知识存量；稳态值；饱和值 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $\alpha,\ \alpha^\star$ | 感知占比；认知平衡点 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $\kappa$ | 知识获取速率 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $T_{\mathrm{env}}$ | 环境相干期 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $C_0$；$\Delta C(q)$ | 基线容量；知识带来的容量增益 | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $J(\alpha)$ | 长期吞吐 $(1-\alpha)[C_0+\Delta C(q^\star(\alpha))]$ | [第二部 5.4 · 模型](part2/05-cognitive-triangle.md#模型) | — |
| $(R,\epsilon,\rho)$ | 通信速率、感知损失、决策后悔的三元 region | [第二部 5.7 · 三元 region](part2/05-cognitive-triangle.md#57-三元-region分时凸包可达内部形状开放) | — |
| $\Psi(\sigma)$；$\kappa_{\mathrm{SE}}$ | 离散判决环的期望损失；谱效对错格的斜率 | [第二部 6.2 · 它在哪里断掉](part2/06-error-budget.md#它在哪里断掉离散判决) | — |
| $\Delta(s)$ | 相邻 DFT 波束的增益差 | [第二部 6.4 · 先把 DFT 码本的几何算清楚](part2/06-error-budget.md#先把-dft-码本的几何算清楚) | — |
| $b_i$；$\gamma_i$ | 第 $i$ 个预算项分到的比特；比特效率 | [第二部 6.7 · 问题的精确形式](part2/06-error-budget.md#问题的精确形式) | — |
| $\mathrm{PoL}_{\text{chain}}$ | 链上的分层代价（猜想 6.6） | [第二部 6.8 · 猜想 6.6](part2/06-error-budget.md#猜想-66链上的-pol) | 一般的 PoL 由第三部第 7 章定义 |
| $\mathfrak W$ | 无线实验族 | [第二部 7.3 · 精确陈述](part2/07-research-agenda.md#精确陈述) | — |

### 第三部 { #core-part3 }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $V(I)$；$I(\xi;M)$；$\Pi(M)$ | 预测的价目表；预测消息携带的关于未来的信息；可用该消息的在线策略类 | [第一部 9.4 · "CKM 的香农曲线"](part1/09-exchange-and-universality.md#ckm-的香农曲线一条尚不存在的曲线)（定义见 [第三部第 5 章 · 章首](part3/05-price-of-prediction.md)） | — |
| PoL | 分层的代价：分层方案比联合最优差几倍 | [第二部 6.8 · 猜想 6.6](part2/06-error-budget.md#猜想-66链上的-pol)（定义见 [第三部 7.4 · PoL](part3/07-price-of-layering.md#pol定义上界下界与分类纲领)） | — |
| $C_{\mathcal F}(\varepsilon)$ | 协同的最小话费：问题族 $\mathcal F$ 上达到 $\varepsilon$-最优的最少通信比特 | [第三部 1.2 · 山二 · 分布式](part3/01-three-mountains.md#山二--分布式不知道别的节点知道什么) | — |
| $\rho_A,\ \rho^\star$；$\rho_{\mathrm{up}},\ \rho_{\mathrm{lo}}$ | 竞争比、最优竞争比及其上下界 | [第三部 1.2 · 山三 · 不确定](part3/01-three-mountains.md#山三--不确定不知道下一秒会发生什么) | — |
| $\mathrm{Reg}_T$ | 动态遗憾 | [第三部 1.2 · 山三 · 不确定](part3/01-three-mountains.md#山三--不确定不知道下一秒会发生什么) | — |
| $\bar D(\varepsilon)$ | Berry–Gallager 平方根律里的平均时延 | [第三部 1.4 · Berry–Gallager 平方根律](part3/01-three-mountains.md#一berrygallager-平方根律无线资源领域的孤本) | — |
| PoA | 无政府的代价 | [第三部 1.4 · Pigou 与 4/3](part3/01-three-mountains.md#二pigou-与-43分权的代价被算成了一个数) | 第四部第 8 章展开 |
| $x_r,\ U_r$；$A x\le c$ | NUM：用户 $r$ 的速率与效用；链路容量约束 | [第三部 2.2 · Kelly 的观念转换](part3/02-classical-foundations.md#22-kelly-的观念转换把网络写成一个凸优化) | — |
| $\lambda_r$；$\mu_l$ | 用户看到的路径价格；链路价格 | [第三部 2.2 · Kelly 的观念转换](part3/02-classical-foundations.md#22-kelly-的观念转换把网络写成一个凸优化) | 预备篇第 7 章链路价格写 $\lambda_\ell$ |
| $\bar L,\ \bar S,\ \bar\alpha$ | NUM 收敛条件里的最长路径链路数、最拥挤链路的源数、效用曲率上界 | [第三部 2.3 · 收敛条件](part3/02-classical-foundations.md#收敛条件一个完全由拓扑决定的稳定性判据) | — |
| $W_i,\ \tau_i,\ q_i$ | TCP 流的窗口、往返时延、丢包概率 | [第三部 2.5 · TCP Reno](part3/02-classical-foundations.md#tcp-reno从-aimd-反解出-alpha2) | — |
| $u_k,\ w_k$ | WMMSE 的两个辅助变量 | [第三部 3.3 · 合成](part3/03-nonconvex-era.md#第三步合成) | — |
| $V$ | drift-plus-penalty 的权衡参数 | [第三部 4.1 · 一句「不知道未来」，四种严格化](part3/04-sequential-uncertainty.md#一句不知道未来四种严格化) | 与价值函数无关，见 [V](#sym-V) |
| $\omega(t)$ | 时隙 $t$ 的随机状态 | [第三部 4.1 · 一句「不知道未来」，四种严格化](part3/04-sequential-uncertainty.md#一句不知道未来四种严格化) | — |
| $Q(t)$ | 队列积压 | [第三部 4.2 · 问题 P](part3/04-sequential-uncertainty.md#问题-p边缘节点的能量时延卸载调度) | — |
| $Z_i(t)$ | 虚拟队列（把时间平均约束变成队列稳定） | [第三部 4.3 · 核心推导](part3/04-sequential-uncertainty.md#核心推导drift-plus-penalty-的五步骨架) | — |
| EVPI | 完美信息的期望价值 | [第三部 5.1 · 第一级台阶](part3/05-price-of-prediction.md#第一级台阶先知不等式价目表的两个端点) | — |
| $V_0$ | 信息松弛里先知策略的期望价值 | [第三部 5.2 · 第二级台阶](part3/05-price-of-prediction.md#第二级台阶信息松弛对偶把先知变成刻度尺) | — |
| $D(f)$；$R^{\mathrm{pub}}_\varepsilon$ | 确定性通信复杂度；公共随机性下的随机通信复杂度 | [第三部 6.1 · 模型与矩形引理](part3/06-communication-lower-bounds.md#模型与矩形引理) | — |
| $C(\mathcal F_L;\varepsilon)$ | Tsitsiklis–Luo 的比特下界对象 | [第三部 6.2 · Tsitsiklis–Luo 1987](part3/06-communication-lower-bounds.md#tsitsiklisluo-1987第一次给连续优化数比特) | — |
| $\rho(f),\ \bar\rho$ | 非凸度 | [第三部 7.2 · 第一击](part3/07-price-of-layering.md#第一击原子性对偶间隙从零变正) | — |
| $(\lambda,\mu)$ | smoothness 框架的两个常数 | [第三部 7.3 · 借一把尺子](part3/07-price-of-layering.md#借一把尺子price-of-x-的最坏比值证法) | — |
| $\mathcal C_{\mathrm{cod}}(\mathcal N,f)$ | 网络计算函数 $f$ 的编码容量 | [第三部 8.2 · 割集上界](part3/08-computing-network-capacity.md#割集上界一次不跳步的计数) | — |
| $\hat{\mathcal N}$ | 三信源反例网络（割集上界不紧的例子） | [第三部 8.3 · 反例侧](part3/08-computing-network-capacity.md#反例侧缝隙可以宽到任意倍数) | — |
| $W_{C,f}$ | 割 $C$ 上函数 $f$ 的最坏等价类数 | [第三部 8.3 · 更糟的](part3/08-computing-network-capacity.md#更糟的上界本身错了四年) | — |
| $V(R)$ | 预测消息率为 $R$ 时的最优期望竞争比 | [第三部 9.3 · 缺失定理一 · V(I)](part3/09-research-agenda.md#缺失定理一--vi信息的价值函数) | — |
| $\mathcal S_\varepsilon$ | 目标值离最优不超过 $\varepsilon$ 的解集（重叠间隙性质） | [第三部 9.4 · 暗线](part3/09-research-agenda.md#暗线随机性如何决定可解性) | — |

### 第四部 { #core-part4 }

| 符号 | 含义 | 首次出现 | 同名异义提醒 |
|---|---|---|---|
| $k,\ \sigma$；$x_0$ | Witsenhausen 反例的两个参数；初始状态 $x_0\sim\mathcal N(0,\sigma^2)$ | [第四部 1.2 · 反例的精确设置](part4/01-one-counterexample.md#12-反例的精确设置三件套齐全结论塌了) | 经典参数 $k=0.2,\ \sigma=5$ |
| $\gamma_1,\ \gamma_2$；$\gamma_i$ | 决策规则 | [第四部 1.2 · 反例的精确设置](part4/01-one-counterexample.md#12-反例的精确设置三件套齐全结论塌了) | 见 [γ](#sym-gamma) |
| $J(\gamma_1,\gamma_2)$ | 团队期望代价 | [第四部 1.2 · 反例的精确设置](part4/01-one-counterexample.md#12-反例的精确设置三件套齐全结论塌了) | — |
| $\mathcal I$ | 信息结构：谁观测什么、谁的动作影响谁的观测 | [第四部 1.5 · 信息结构](part4/01-one-counterexample.md#15-信息结构把谁知道什么写成划分) | — |
| $d\le p$ | 两小区凸性判据：回传时延不超过耦合传播时延 | [第四部 1.6 · 无线的日常形态](part4/01-one-counterexample.md#16-无线的日常形态动作即信号的五个现场) | — |
| $Q$；$\delta_i$ | 团队二次代价的耦合矩阵与一次项 | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | — |
| $\rho_{ji}$ | Radner 定理里的回归系数 | [第四部 2.3 · 再叠上高斯，最优规则变成仿射](part4/02-team-decision-theory.md#232-第二步再叠上高斯最优规则变成仿射) | — |
| $\nu_{\mathrm b}$ | 嵌套亏损（按比特计） | [第四部 2.7 · 两条逃生通道](part4/02-team-decision-theory.md#两条逃生通道) | — |
| $Q$ | Youla 参数 | [第四部 3.1 · 抬桌子过门](part4/03-information-structure-phase-diagram.md#31-抬桌子过门两种可解一条赛跑) | — |
| $\mathcal S_{\mathcal I}$ | 信息结构给出的稀疏约束集 | [第四部 3.3 · 图论判据](part4/03-information-structure-phase-diagram.md#334-图论判据把谁看见谁画成图) | — |
| $\nu(\mathcal I;\mathcal G)$ | 嵌套亏欠（按链路数计） | [第四部 3.7 · 纵轴必须可计算](part4/03-information-structure-phase-diagram.md#纵轴必须可计算) | — |
| $W$；$R_0$ | 公共随机性；公共随机率 | [第四部 4.2 · 模型与三个定义](part4/04-coordination-information-theory.md#421-模型与三个定义) | — |
| $C_{\mathrm{Wyner}}(X;Y)$；$\Gamma$ | Wyner 公共信息；必要条件熵 | [第四部 4.2 · 分级](part4/04-coordination-information-theory.md#423-分级经验协调不用买公共随机性强协调要买) | — |
| $\mathrm{CC}$ | 到达某个解概念所需的通信复杂度 | [第四部 4.5 · 非耦合均衡程序](part4/04-coordination-information-theory.md#451-非耦合均衡程序) | — |
| $\mathrm{IC}(f,\mu)$ | 以共享先验 $\mu$ 为参数的信息复杂度 | [第四部 4.7 · 多方](part4/04-coordination-information-theory.md#47-多方广播是资源不是负担) | — |
| $\Pi$ | 协议记录 | [第四部 5.2 · 通信复杂度的三级共享](part4/05-shared-world-model.md#52-通信复杂度的三级共享无共享共享随机共享模型) | — |
| $\gamma$；$\beta$；$\alpha$ | 推测解码：每轮草稿数；单步接受率；期望接受率 | [第四部 5.5 · 推测解码](part4/05-shared-world-model.md#55-推测解码接受率-1-mathrmtvpq) | — |
| $\Phi_T(\varepsilon)$ | 模型差 $\varepsilon$ 时的协商罚项 | [第四部 5.8 · 猜想](part4/05-shared-world-model.md#猜想) | — |
| $\eta$；$\eta^\star$ | 学习率；分岔阈值 | [第四部 6.1 · 两个学下棋的人](part4/06-learning-dynamics.md#61-两个学下棋的人目标在动) | — |
| $\sigma$；$\bar\sigma_T$ | 相关均衡；经验联合分布 | [第四部 6.2 · 三级均衡](part4/06-learning-dynamics.md#三级均衡) | — |
| $\Phi$ | 势函数 | [第四部 6.4 · 给整个系统装一个"高度表"](part4/06-learning-dynamics.md#直觉给整个系统装一个高度表) | 第一部的 $\Phi$ 是环境→信道映射 |
| $\rho(\mathcal G)$；$\theta_1,\ \theta_2$ | 相图判据里图的谱量；三区的分界 | [第四部 6.9 · 三条轴，两条有先例，一条没有](part4/06-learning-dynamics.md#三条轴两条有先例一条没有) | — |
| $N_{\mathrm{eff}}$ | 干扰耦合的有效人数（定义 7.3） | [第四部第 7 章 · 章首](part4/07-mean-field.md) | 第一部第 9 章同名不同义 |
| $\mu,\ \mu_N$ | 群体分布；经验分布 | [第四部 7.1 · 高峰期的地铁口](part4/07-mean-field.md#71-高峰期的地铁口人多为什么反而简单) | — |
| $J^{\mathrm{MFG}},\ J^{\mathrm{MFC}}$ | 平均场博弈与平均场控制的代价 | [第四部 7.3 · MFG 的解](part4/07-mean-field.md#mfg-的解) | — |
| $\rho$ | MFG 与 MFC 的分歧比 | [第四部 7.3 · 分歧比](part4/07-mean-field.md#分歧比一个闭式与一个不等式) | — |
| $\Gamma=(\mathcal N,\{A_i\},\{u_i\})$ | 策略式博弈 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | — |
| $W(a),\ W^\star$ | 社会福利；社会最优 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | — |
| $\mathrm{NE}(\Gamma)$；PoA、PoS | 纯策略 Nash 均衡集；无政府的代价、稳定的代价 | [第四部 8.1 · 会议室里的音量战争](part4/08-network-games.md#81-会议室里的音量战争先把差多少定义清楚) | — |
| $\kappa$；$\kappa_{\mathrm{eff}}(N,B)$ | 耦合度；有效耦合度 | [第四部 8.9 · 协作增益的天花板](part4/08-network-games.md#89-协作增益的天花板耦合度-kappa-的第一个候选) | — |
| $C_{\mathrm{edge}}$ | 协作簇边缘用户的谱效天花板 | [第四部 8.9 · 协作增益的天花板](part4/08-network-games.md#89-协作增益的天花板耦合度-kappa-的第一个候选) | — |
