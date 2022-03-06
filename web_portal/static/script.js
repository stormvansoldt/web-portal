ThemeChanger.theme_meta.light[1] = [
    ["--font-dark", "black"],
    ["--font-light", "#f0f0f0"],
    ["--bg-bnt", "#adadad"],
    ["--bg-body", "#9299a5"],
    ["--bg-sub-body", "#8c93a0"],
    ["--bg-panel", "#848a94"],
];
ThemeChanger.theme_meta.dark[1] = [
    ["--font-dark", "var(--font-light)"],
    ["--font-light", "#bcbcbc"],
    ["--bg-bnt", "#003d4b"],
    ["--bg-body", "#002b36"],
    ["--bg-sub-body", "#073540"],
    ["--bg-panel", "#083b47"],
];
ThemeChanger.theme_picker_parent = document.querySelector("main");
ThemeChanger.selected_theme_css_class = "green";

document.getElementById("themeToggleBnt").addEventListener("click", _ => {
    ThemeChanger.toggle_theme_picker();
});

ThemeChanger.on_load();