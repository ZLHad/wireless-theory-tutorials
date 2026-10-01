# 统计图

站点里的 83 张统计图（折线、柱状、象限图）由本目录生成，输出到 `site/docs/assets/charts/`，每张一份浅色、一份深色 SVG。正文用两行图片引用，Material 按配色方案只显示其中一张；`loading=lazy` 让另一张和还没滚到的图不提前下载：

```markdown
![图的标题](../assets/charts/p0-03-3.svg#only-light){ .chart loading=lazy }
![图的标题](../assets/charts/p0-03-3-dark.svg#only-dark){ .chart loading=lazy }
```

这些图原先写在正文里，用 mermaid 的 xychart / quadrantChart 画，2026-10-01 改为 matplotlib 生成：mermaid 的统计图没有图例，公式只能写纯文本，坐标轴也不能取对数。数据原样保留，没有重新计算。

## 文件

- `src/<id>.mmd`：每张图的数据，沿用 mermaid 的写法（`x-axis`、`y-axis`、`line [...]`、`bar [...]`、象限图的点坐标）。改数据就改这里。
- `src/index.json`：图的 id 与所在页面的对照。id 的写法是"部-章-块号"，例如 `p0-03-3` 是预备篇第 3 章原来的第 3 号 mermaid 块，`g-04-1` 是导览篇第 4 页的。
- `ov_A.py`（导览篇与预备篇）、`ov_B.py`（第一、二部）、`ov_C.py`（第三、四部）：标注规格，包括标题、轴名、图例、刻度、参照线、象限文字与点名的位置。公式用 LaTeX，写法跟正文一致。
- `chartlib.py`：绘图库。`draw_xy`、`draw_quadrant` 的说明里列出了全部可用的规格键。
- `build.py`：生成脚本。

## 生成

需要 Python 3 和 matplotlib（站点里的图用 matplotlib 3.8.2 生成）。中文字体按顺序取本机装了的第一种：冠黑体（Hiragino Sans GB）、苹方、思源黑体、Noto Sans CJK SC、微软雅黑；公式字体用 Computer Modern。文字一律转成路径，看图的机器不需要装这些字体。站点里的图是用冠黑体画的，换一种字体重画，字形会略有不同。

```bash
cd charts
python3 build.py            # 全部重画
python3 build.py --png p0-03-3   # 只画一张，另出 prev/p0-03-3.png 预览
```

## 规矩

- 横轴的排点规则跟原来的 mermaid 一样：数值区间 `a --> b` 时，n 个点等距铺满 [a, b]；类别轴时各类别等距排开。图注里"每格翻倍""按对数等距排开"一类说法依赖这一点，不要随手改成真实数值轴。只有类别本身是等差数列（或图注本来就要求真实比例）时，才在规格里写 `xnumeric=True`。
- 图例顺序必须与 `src` 里序列的顺序一致，因为图注里常用"第一条""第二条"指认曲线。
- mathtext 只支持 LaTeX 的子集：`\tfrac`、`\lVert`、`\rVert`、`\le`、`\ge` 不能用，分别换成 `\frac`、`\|`、`\leq`、`\geq`；`$…$` 里不能放中文。对数坐标轴的刻度要在规格里用 `yticks` 显式写成 `$10^{-k}$`，否则 matplotlib 默认的刻度文字会缺字形。
- 改完先用 `--png` 出预览看一遍，再跑全部，然后照常构建站点。
