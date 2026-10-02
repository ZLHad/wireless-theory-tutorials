# 理论地基·四部曲

**从环境到群体：无线智能网络缺失的四层理论地基。**

作者：Zhang Linghao（National University of Singapore & Nanjing University of Posts and Telecommunications）

联系：<zhangczssx@gmail.com> · <zhanglinghao@u.nus.edu>

在线阅读：<https://zlhad.top/wireless-theory-tutorials/>

这是一本开放的中文电子书，写给学过高数、线性代数、概率和信号与系统的本科高年级学生与研究生，也写给想找研究方向的人。预备篇从本科水平讲起，把读懂前沿所需的无线通信基础讲透；四部沿着"环境 → 信道 → 任务 → 网络 → 群体"这条线，先讲清已有的经典理论，再指出 AI 原生无线网络底下还没有定理的地方。

全书 46 章、约 61 万汉字，另有导览篇 6 页和符号表、术语表、开放问题总表三份附录。书里不出习题，篇幅都花在三件事上：把概念和推导讲透，把各部分之间的联系讲清楚，把前沿还缺什么摆出来。

## 内容

| 篇 / 部 | 讲什么 |
|---|---|
| 导览篇 · 领域画像 | 领域地图、学习路径、开篇之作、时间线与标准、贯穿全书的八条线索、方向的生命周期 |
| 预备篇 · 基础教程（11 章） | 电磁波与天线、无线信道、数字通信、信息论、MIMO、无线网络、优化、强化学习，以及 6G 的新概念图景 |
| 第一部 · 环境的科学（10 章） | 信道从哪里来：环境到信道的映射、统计建模谱系、信道地图、有效维度与预测半径 |
| 第二部 · 链的定理（7 章） | 信道知识怎样变成业务价值：Blackwell 排序、任务-知识格、环境泛化、认知回路、误差预算 |
| 第三部 · 网络的优化论（9 章） | 资源分配的基本限：非凸优化、时序决策、预测的价目表、通信复杂度、分层的代价 |
| 第四部 · 群体的决策论（9 章） | 许多智能体怎样协同：团队决策、信息结构相图、协作的信息论、学习动力学、平均场、网络博弈 |

第一次读，建议从导览篇的[学习路径](https://zlhad.top/wireless-theory-tutorials/guide/02-learning-paths.html)开始：那里给了三种读法和七条按方向深读的路线。

## 状态标签

书里每个结论都标明来历：【已解决】是文献中的定理，【本站演算】是本书自己的推导或数值计算（都已复算），【开放】是还没有定理的问题，【表述待核】【预印本·未评审】提醒你引用前回原文核对。完整说明见首页的"诚实声明与状态标签"。

## 本地构建

```bash
pip install -r requirements.txt
mkdocs serve -f site/mkdocs.yml
```

然后打开 <http://127.0.0.1:8000>。推送到 `main` 分支后，GitHub Actions 会构建站点并发布到 GitHub Pages（见 `.github/workflows/deploy.yml`）。

## 仓库结构

- `site/`：MkDocs 站点。正文在 `site/docs/`，配置在 `site/mkdocs.yml`。
- `charts/`：83 张统计图的数据与生成脚本，输出到 `site/docs/assets/charts/`，用法见 `charts/README.md`。
- `notation-glossary/`：符号表、术语表与开放问题总表的源文件和生成工具，用法见 `notation-glossary/README.md`。

统计图和三份附录都是生成的：改它们要改源文件，再按各自的 README 重新生成。重新生成需要的额外依赖在 `requirements-tools.txt`。

## 反馈

发现错误或有建议，欢迎[提 Issue](https://github.com/ZLHad/wireless-theory-tutorials/issues)，也可以发邮件给作者（地址见上）。

## 许可

- **正文与图**（`site/docs/` 中的文字与图片、`charts/` 生成的图）采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans) 许可，法律文本见 `LICENSE`：转载和改编请署名，不得用于商业目的，改编后的作品须以相同许可发布。
- **代码**（`charts/` 与 `notation-glossary/tools/` 中的脚本，`site/docs/javascripts/` 与 `site/docs/stylesheets/` 中本书自己写的脚本和样式）采用 MIT 许可，见 `LICENSE-CODE`。
- **第三方组件**：随站点分发的 MathJax 3.2.2（Apache-2.0）和 Mermaid 11.16.1（MIT）保留各自的许可证，见 `THIRD_PARTY_NOTICES.md`。

## 引用

```bibtex
@misc{zhang2026sibuqu,
  author       = {Zhang, Linghao},
  title        = {理论地基·四部曲：从环境到群体，无线智能网络缺失的四层理论地基},
  year         = {2026},
  howpublished = {\url{https://zlhad.top/wireless-theory-tutorials/}}
}
```
