'use strict';
const themeButton = document.getElementById('theme');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
let manualTheme = null;
function refreshThemeButton() {
  const dark = manualTheme ? manualTheme === 'dark' : systemTheme.matches;
  const label = dark ? 'Switch to light theme' : 'Switch to dark theme';
  themeButton.textContent = dark ? 'Light theme' : 'Dark theme';
  themeButton.setAttribute('aria-label', label);
}
if (themeButton) {
  themeButton.hidden = false;
  themeButton.addEventListener('click', () => {
    const dark = manualTheme ? manualTheme === 'dark' : systemTheme.matches;
    manualTheme = dark ? 'light' : 'dark';
    document.documentElement.dataset.theme = manualTheme;
    refreshThemeButton();
  });
  systemTheme.addEventListener('change', refreshThemeButton);
  refreshThemeButton();
}
