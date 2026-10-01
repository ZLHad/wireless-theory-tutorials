window.MathJax = {
  // boldsymbol 靠自动加载时不会注册进解析器，\boldsymbol 会显示成红字；启动时直接加载
  loader: { load: ["[tex]/boldsymbol"] },
  tex: {
    packages: { "[+]": ["boldsymbol"] },
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex|toc-math" },
  startup: {
    ready() {
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(markWideMath);
    }
  }
};

// 手机上，比所在段落还宽的行内公式会把整页撑宽、左右晃（MathJax 3 不会给行内公式折行）。
// 排版后量一遍，只给这些公式挂 math-wide 类，让它自己横向滚动；表格里的不管，表格本身能横向滚动。
function markWideMath() {
  document.querySelectorAll(".md-typeset span.arithmatex").forEach((el) => {
    if (el.closest("table")) return;
    el.classList.remove("math-wide");
    // 公式常在 strong、em 这类行内元素里，它们没有宽度，要和最近的块级容器比
    const box = el.closest("p, li, dd, dt, blockquote, figcaption, summary, h1, h2, h3, h4, h5, h6, div");
    const mjx = el.querySelector("mjx-container");
    if (box && mjx && mjx.getBoundingClientRect().width > box.clientWidth + 1) el.classList.add("math-wide");
  });
}
let wideTimer = null;
window.addEventListener("resize", () => {
  clearTimeout(wideTimer);
  wideTimer = setTimeout(markWideMath, 200);
});

// 目录（页面右侧和窄屏抽屉里的"本页目录"）直接搬标题文字，公式会以 \( \) 源码的样子出现；
// 给含公式的目录项挂上 toc-math 类，让 MathJax 一起排版（一个目录项里可以有几处公式）。
function tagTocMath() {
  document.querySelectorAll(".md-nav--secondary .md-ellipsis").forEach((el) => {
    if (el.textContent.indexOf("\\(") !== -1) el.classList.add("toc-math");
  });
}
tagTocMath();

// 初次载入由 MathJax 启动时自己排版；这里只负责即时导航换页后的新公式。
// 排在 startup.promise 之后、只排版还没排过的公式，避免与启动排版重叠：
// 重叠时第二遍会把读屏用的隐藏 MathML 再渲染一份。
document$.subscribe(() => {
  if (!(window.MathJax && MathJax.startup && MathJax.startup.promise)) return;
  MathJax.startup.promise = MathJax.startup.promise
    .then(() => {
      tagTocMath();
      const pending = [...document.querySelectorAll(".arithmatex, .toc-math")]
        .filter((el) => !el.querySelector("mjx-container"));
      if (!pending.length) return;
      if (MathJax.startup.output && MathJax.startup.output.clearCache) {
        MathJax.startup.output.clearCache();
      }
      MathJax.typesetClear();
      MathJax.texReset();
      return MathJax.typesetPromise(pending);
    })
    .then(markWideMath)
    .catch((err) => console.error("MathJax typeset failed:", err));
});
