(function () {
  var storageKey = "lbtwyk-lang";

  function preferredLang() {
    try {
      var saved = localStorage.getItem(storageKey);
      if (saved === "en" || saved === "zh") return saved;
    } catch (err) {}
    var nav = (navigator.language || "en").toLowerCase();
    return nav.indexOf("zh") === 0 ? "zh" : "en";
  }

  function setLang(lang) {
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute("lang", lang === "zh" ? "zh-CN" : "en");
    document.querySelectorAll("[data-set-lang]").forEach(function (btn) {
      btn.setAttribute("aria-pressed", btn.getAttribute("data-set-lang") === lang ? "true" : "false");
    });
    try {
      localStorage.setItem(storageKey, lang);
    } catch (err) {}
  }

  var queryLang = new URLSearchParams(window.location.search).get("lang");
  setLang(queryLang === "en" || queryLang === "zh" ? queryLang : preferredLang());

  document.querySelectorAll("[data-set-lang]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      setLang(btn.getAttribute("data-set-lang"));
    });
  });
})();
