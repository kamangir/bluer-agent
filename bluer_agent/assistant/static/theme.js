// --- enter-to-submit ---
const textarea = document.getElementById("question-text");
const form = document.getElementById("main-form");

textarea.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        form.requestSubmit();
    }
});

// --- theme toggle ---
const toggleBtn = document.getElementById("theme-toggle");
const root = document.documentElement;

function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    toggleBtn.textContent = theme === "dark" ? "☀️" : "🌙";
}

const savedTheme = localStorage.getItem("theme") || "dark";
setTheme(savedTheme);

toggleBtn.addEventListener("click", () => {
    const current = root.getAttribute("data-theme");
    setTheme(current === "dark" ? "light" : "dark");
});

function syncSubjectToSaveForm() {
    const subjectInput = document.getElementById("subject");
    const hiddenInput = document.getElementById("save-subject");

    if (subjectInput && hiddenInput) {
        hiddenInput.value = subjectInput.value;
    }
}


(function () {
    // --- existing theme code can stay above/below this ---

    const KEYS = {
        pageX: "scroll:page:x",
        pageY: "scroll:page:y",
        // If you also want specific containers, add keys like:
        // sidebarY: "scroll:sidebar:y",
    };

    function savePageScroll() {
        try {
            sessionStorage.setItem(KEYS.pageX, String(window.scrollX || 0));
            sessionStorage.setItem(KEYS.pageY, String(window.scrollY || 0));
        } catch (_) { }
    }

    function restorePageScroll() {
        try {
            const x = parseInt(sessionStorage.getItem(KEYS.pageX) || "0", 10);
            const y = parseInt(sessionStorage.getItem(KEYS.pageY) || "0", 10);
            // rAF helps after layout/fonts settle
            requestAnimationFrame(() => window.scrollTo(x, y));
        } catch (_) { }
    }

    // Restore after navigation/refresh
    window.addEventListener("load", restorePageScroll);

    // Save before leaving and on actions that usually navigate
    window.addEventListener("beforeunload", savePageScroll);
    document.addEventListener("submit", savePageScroll, true);
    document.addEventListener(
        "click",
        (e) => {
            if (e.target && e.target.closest && e.target.closest("a")) savePageScroll();
        },
        true
    );

    // Optional: keep it updated while scrolling (useful if beforeunload is blocked)
    // (throttled)
    let t = null;
    window.addEventListener(
        "scroll",
        () => {
            if (t) return;
            t = setTimeout(() => {
                t = null;
                savePageScroll();
            }, 150);
        },
        { passive: true }
    );
})();
