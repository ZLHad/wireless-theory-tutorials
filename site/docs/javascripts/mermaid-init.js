// 用本地 vendored mermaid 渲染图，完全离线可用。
//
// 为什么不用 Material 自带的图集成：Material 9.x 会在运行时从 unpkg.com 动态加载
// mermaid；该请求失败时，它已经把 <pre class="mermaid"> 里的图源取走，页面上只剩
// 一个空 div（图彻底消失且无提示）。因此 mkdocs.yml 里把 superfences 的输出类名改成
// mermaid-src，Material 不再认领这些块，改由本文件渲染。
//
// 渲染后把图源存在 data-mmd-src 上，切换明/暗配色时按新主题重画，
// 避免暗色页面上残留亮色主题的图。
(function () {
  function currentTheme() {
    var scheme = document.body && document.body.getAttribute("data-md-color-scheme");
    return scheme === "slate" ? "dark" : "default";
  }

  // 配色跟站点走（深红主色、暖灰中性色），字体与正文一致；明暗两套。
  // 统计图已改用 matplotlib 生成的 SVG，这里只管流程图与时序图。
  var FONT = '"PingFang SC", "Noto Sans SC", "Microsoft YaHei", "Helvetica Neue", sans-serif';
  var LIGHT = {
    darkMode: false, background: "#ffffff", fontFamily: FONT, fontSize: "15px",
    primaryColor: "#fbf4f2", primaryTextColor: "#2b2321", primaryBorderColor: "#c98b83",
    secondaryColor: "#f4efe9", secondaryTextColor: "#2b2321", secondaryBorderColor: "#bfae9f",
    tertiaryColor: "#faf8f6", tertiaryTextColor: "#2b2321", tertiaryBorderColor: "#e3d6d2",
    lineColor: "#8d7f7b", textColor: "#2b2321", titleColor: "#8e1b1b",
    clusterBkg: "#fcfaf9", clusterBorder: "#e3d6d2", edgeLabelBackground: "#ffffff",
    noteBkgColor: "#fff6e0", noteTextColor: "#3a2f1c", noteBorderColor: "#e2c98c",
    actorBkg: "#fbf4f2", actorBorder: "#c98b83", actorTextColor: "#2b2321", actorLineColor: "#b9aaa6",
    signalColor: "#6f625e", signalTextColor: "#2b2321", sequenceNumberColor: "#ffffff",
    labelBoxBkgColor: "#fbf4f2", labelBoxBorderColor: "#c98b83", labelTextColor: "#2b2321"
  };
  var DARK = {
    darkMode: true, background: "#1e2029", fontFamily: FONT, fontSize: "15px",
    primaryColor: "#2c2f3a", primaryTextColor: "#ece6e4", primaryBorderColor: "#c78a84",
    secondaryColor: "#33313a", secondaryTextColor: "#ece6e4", secondaryBorderColor: "#9c8c84",
    tertiaryColor: "#262830", tertiaryTextColor: "#ece6e4", tertiaryBorderColor: "#4b4d58",
    lineColor: "#a9a0a0", textColor: "#ece6e4", titleColor: "#ef9a9a",
    clusterBkg: "#24262f", clusterBorder: "#4b4d58", edgeLabelBackground: "#1e2029",
    noteBkgColor: "#3b3526", noteTextColor: "#f1e6c8", noteBorderColor: "#8a7a4a",
    actorBkg: "#2c2f3a", actorBorder: "#c78a84", actorTextColor: "#ece6e4", actorLineColor: "#6d6a72",
    signalColor: "#cfc6c4", signalTextColor: "#ece6e4", sequenceNumberColor: "#1e2029",
    labelBoxBkgColor: "#2c2f3a", labelBoxBorderColor: "#c78a84", labelTextColor: "#ece6e4"
  };

  function init() {
    var theme = currentTheme();
    window.mermaid.initialize({
      startOnLoad: false,
      theme: "base",
      look: "neo",
      securityLevel: "loose",
      flowchart: { htmlLabels: true, useMaxWidth: true, curve: "basis" },
      themeVariables: theme === "dark" ? DARK : LIGHT
    });
  }

  // Chrome 的 MathML 只认 mathvariant="normal"：KaTeX 把 \mathcal{E}、\mathbb{E} 输出成
  // <mi mathvariant="script">E</mi> 这类写法，Chrome 会画成普通斜体 E，和正文里的 ℰ、𝔼 对不上。
  // 渲染后把这些字母换成对应的 Unicode 数学字母（ℰ、ℝ 这类落在"字母式符号"区的单独列出）。
  var MATH_VARIANTS = {
    "script": [0x1D49C, 0x1D4B6, { B: 0x212C, E: 0x2130, F: 0x2131, H: 0x210B, I: 0x2110, L: 0x2112, M: 0x2133, R: 0x211B, e: 0x212F, g: 0x210A, o: 0x2134 }],
    "double-struck": [0x1D538, 0x1D552, { C: 0x2102, H: 0x210D, N: 0x2115, P: 0x2119, Q: 0x211A, R: 0x211D, Z: 0x2124 }],
    "fraktur": [0x1D504, 0x1D51E, { C: 0x212D, H: 0x210C, I: 0x2111, R: 0x211C, Z: 0x2128 }]
  };
  function fixMathVariants(root) {
    Array.prototype.forEach.call(root.querySelectorAll("mi[mathvariant]"), function (mi) {
      var m = MATH_VARIANTS[mi.getAttribute("mathvariant")];
      var t = mi.textContent;
      if (!m || t.length !== 1) return;
      var c = t.charCodeAt(0), cp;
      if (m[2][t]) cp = m[2][t];
      else if (c >= 65 && c <= 90) cp = m[0] + (c - 65);
      else if (c >= 97 && c <= 122) cp = m[1] + (c - 97);
      else return;
      mi.textContent = String.fromCodePoint(cp);
      mi.setAttribute("mathvariant", "normal");
    });
  }

  // 渲染前先把 \mathcal{X}、\mathbb{X} 换成 Unicode 数学字母，mermaid 量尺寸时用的就是真实字形；
  // 落在"字母式符号"区的那几个（ℰ、ℝ 等）KaTeX 会改回 mathvariant，留给上面的渲染后处理。
  function toMathAlphabet(src) {
    return src.replace(/\\(mathcal|mathbb)\{([A-Za-z])\}/g, function (m, kind, ch) {
      var v = MATH_VARIANTS[kind === "mathcal" ? "script" : "double-struck"];
      if (v[2][ch]) return m;
      var c = ch.charCodeAt(0);
      return String.fromCodePoint(c <= 90 ? v[0] + (c - 65) : v[1] + (c - 97));
    });
  }

  // 手机上流程图常缩到原尺寸的四成左右，字太小。缩到 80% 以下的图可以点一下看原尺寸（横向滚动），再点一下复原。
  var ZOOM_BELOW = 0.8;

  function naturalWidth(box) {
    var svg = box.querySelector("svg");
    var vb = svg && svg.viewBox && svg.viewBox.baseVal;
    return vb && vb.width ? vb.width : 0;
  }

  function markZoomable(box) {
    if (box.classList.contains("mmd-zoomed")) return;
    var w = naturalWidth(box);
    // 藏在折叠块里的图宽度是 0，量不准，先不标
    box.classList.toggle("mmd-zoomable", w > 0 && box.clientWidth > 0 && box.clientWidth < w * ZOOM_BELOW);
  }

  function toggleZoom(box) {
    var svg = box.querySelector("svg");
    if (!svg) return;
    if (box.classList.contains("mmd-zoomed")) {
      box.classList.remove("mmd-zoomed");
      svg.style.width = "";
      svg.style.maxWidth = box.getAttribute("data-mmd-maxw") || "";
      markZoomable(box);
    } else if (box.classList.contains("mmd-zoomable")) {
      box.setAttribute("data-mmd-maxw", svg.style.maxWidth);
      box.classList.add("mmd-zoomed");
      svg.style.maxWidth = "none";
      svg.style.width = naturalWidth(box) + "px";
    }
  }

  window.addEventListener("resize", function () {
    Array.prototype.forEach.call(document.querySelectorAll(".mermaid-rendered"), markZoomable);
  });

  var seq = 0;

  function draw(src, mount) {
    seq += 1;
    return window.mermaid
      .render("mmd-" + seq, toMathAlphabet(src))
      .then(function (res) {
        var box = document.createElement("div");
        box.className = "mermaid-rendered";
        box.setAttribute("data-mmd-src", src);
        box.innerHTML = res.svg;
        fixMathVariants(box);
        mount.replaceWith(box);
        if (res.bindFunctions) res.bindFunctions(box);
        markZoomable(box);
        box.addEventListener("click", function (e) {
          if (e.target.closest && e.target.closest("a")) return;  // 图里的链接照常跳转
          toggleZoom(box);
        });
      })
      .catch(function (err) {
        // 渲染失败时保留图源文本，至少读者还能看到内容
        if (mount.setAttribute) mount.setAttribute("data-mmd", "error");
        console.error("mermaid render failed:", err);
      });
  }

  function renderAll() {
    if (!window.mermaid) return;
    var blocks = document.querySelectorAll("pre.mermaid-src:not([data-mmd])");
    if (!blocks.length) return;
    init();
    Array.prototype.forEach.call(blocks, function (pre) {
      var code = pre.querySelector("code") || pre;
      pre.setAttribute("data-mmd", "1");
      draw(code.textContent, pre);
    });
  }

  function redrawForTheme() {
    if (!window.mermaid) return;
    var done = document.querySelectorAll(".mermaid-rendered[data-mmd-src]");
    if (!done.length) return;
    init();
    Array.prototype.forEach.call(done, function (box) {
      draw(box.getAttribute("data-mmd-src"), box);
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(renderAll);
  } else {
    document.addEventListener("DOMContentLoaded", renderAll);
  }

  // 跟随 Material 的明/暗配色切换重画
  var lastScheme = null;
  new MutationObserver(function () {
    var s = document.body.getAttribute("data-md-color-scheme");
    if (s !== lastScheme) {
      lastScheme = s;
      redrawForTheme();
    }
  }).observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
})();
