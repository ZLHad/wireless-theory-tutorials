# 符号表与术语表的源文件

`site/docs/notation.md` 与 `site/docs/glossary.md` 由本目录的两份源文件生成，不要直接改生成结果（2026-09-24 建）。

## 源文件写法

- `notation_src.md`、`glossary_src.md` 是普通 Markdown，链接写成宏：`@[p0/04:788]` 表示"预备篇第 4 章第 788 行所在的小节"，生成器按构建出的标题锚点换成 `[预备篇 4.8 · CSIT 与时间注水](part0/04-...md#锚点)`。
- 变体：`@[p0/04:788|自定义文字]`；`@[p1/05]` 链到整章；`@[p1/05:0]` 链到章首；`@[p0/02:89^h2]` 强制链到二级标题。
- 表格行按"首次出现"列（术语表按"所属部 · 主讲"列）的阅读顺序自动排序。
- 行号以 2026-09-25 的正文为准。当天预备篇、第一部、第三部共 28 章插入了图、表与预备知识框，源文件里的行号宏已按新旧正文的逐行对应整体平移（符号表 271 处、术语表 141 处），平移后重新生成的两页与平移前逐字相同。2026-10-01 又在 35 章的"开放问题"一节前插入了"跨部连线"框，受影响的宏再平移一次（符号表 5 处、术语表 5 处），重新生成的两页仍与平移前逐字相同。同日的 P1 又在预备篇第 2–6、9 章插入提示框与小节，并新增第 10、11 章：用 `expansion-研究档案/scripts/p1/shift_by_diff.py`（按新旧正文逐行对应，一个文件多处插入也适用）平移了符号表 76 处、术语表 65 处，重新生成的两页除符号表开头的"46 章"外逐字相同；随后术语表预备篇一节新增 20 条（块衰落、EVM、信道色散、HARQ、级联信道、测量间隙、条件切换、MDT、可移动与流体天线、空间非平稳、无蜂窝、SBFD、OTFS/AFDM、上中频、非地面网络、携能通信、反向散射与环境物联网、保密容量、隐蔽通信与平方根律、人工噪声）。同日晚的图与公式改版重写了 91 张流程图、把 16 张时间线改成表格、83 张统计图改成 SVG 图片引用，35 章行数都变了：`shift_by_diff.py` 改进为等长的替换块也逐行对应、不等长的替换块按相似度（不低于 0.85）匹配，平移了符号表 264 处、术语表 199 处，重新生成的两页除术语表"Nash ⊂ CE ⊂ CCE"改成公式外逐字相同。2026-10-02 的 P2 在预备篇第 9、10 章，第二部第 4、5 章，第四部第 9 章插入小节与提示框，平移了符号表 5 处、术语表 10 处，重新生成的两页逐字相同。正文再增删行后，重新生成前先用 `tools/firstpat.py`、`tools/tfirst.py` 核对行号；已生成的页面不受影响，链接锚点由 `mkdocs.yml` 的 `validation.anchors: warn` 在构建时校验。
- 公式照正文原样抄写。粗体希腊字母也用 `\boldsymbol`，不要换成 `\pmb` 或 `\mathbf`，否则符号表里的字形会和正文对不上（`\boldsymbol` 曾经渲染不出来，2026-09-25 起 `mathjax-config.js` 已显式加载它）。

## 重新生成

需要 Python 3、PyYAML 和站点的构建依赖（见仓库根目录的 `requirements.txt`）。工具默认处理本仓库的 `site/`；在别处的副本上跑时，用环境变量 `SIBUQU_SITE`、`SIBUQU_DOCS` 指定站点目录和正文目录。

```bash
cd tools
python3 symscan.py                     # 扫描正文 → scan.json
cd ../../site && mkdocs build && cd -
python3 anchors.py ../../site/site      # 构建结果 → anchors.json
python3 gen.py ../notation_src.md ../../site/docs/notation.md
python3 gen.py ../glossary_src.md ../../site/docs/glossary.md
python3 lint.py ../../site/docs/notation.md ../../site/docs/glossary.md
cd ../../site && mkdocs build   # 须 0 警告
python3 ../notation-glossary/tools/linkcheck.py site notation.html glossary.html
```

## 开放问题总表

`site/docs/open-problems.md` 由 `tools/openq.py` 生成（2026-09-25 建）。它不用行号宏：链接按标题文字从构建结果里取锚点，各章条目数每次从章末"开放问题"一节重新统计，所以正文增删行不影响它，改了标题或条目后重跑即可。第一节末的"从定理到判据"表（16 条缺失定理各补判据形式、改变的设计决策、运行期是否因果可行、复杂环境下的验证路径四列，2026-10-02 加）写在脚本的 `CRITERIA` 里，要改就改脚本再重跑；表格外面套了 `<div class="criteria-table" markdown>`，列宽由 `docs/stylesheets/extra.css` 里同名的规则定：

```bash
cd tools
cd ../../site && mkdocs build && cd -
python3 openq.py ../../site/docs ../../site/site ../../site/docs/open-problems.md
```

其余脚本是抽取时用的检索工具：`sym2.py`（某个字母在各章各节的用法）、`symq.py`、`cands.py`（每章候选记号）、`gscan.py` + `gterms.txt`（术语的首次出现与定义处）、`cg.py`（带上下文的检索）。
