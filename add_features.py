import sys
import os

base_dir = r"c:\Projects Antigravity\Lesson_Mastadont_Coffe"
html_path = os.path.join(base_dir, "index.html")
css_path = os.path.join(base_dir, "style.css")

# --- 1. Modify HTML ---
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace header actions
old_header_actions = """            <div class="header-actions">
                <a href="#about" class="btn-nav">Найти нас</a>"""
new_header_actions = """            <div class="header-actions">
                <button id="lang-toggle" class="lang-switch">EN</button>
                <a href="#login" class="btn-nav btn-login hidden-mobile">Личный кабинет</a>
                <a href="#about" class="btn-nav hidden-mobile">Найти нас</a>"""
html_content = html_content.replace(old_header_actions, new_header_actions)

# Update burger layout (mobile): login button can be available in menu, or just left out, 
# but user just wanted "add another button". For mobile we can hide "Find us" and "Login" or just "Find us".
# Let's keep Login visible on mobile.
html_content = html_content.replace('<a href="#login" class="btn-nav btn-login hidden-mobile">', '<a href="#login" class="btn-nav btn-login">')

# Ensure translation script is included
if '<script src="i18n.js"></script>' not in html_content:
    html_content = html_content.replace('<script src="script.js"></script>', '<script src="i18n.js"></script>\n    <script src="script.js"></script>')

# Replace footer social icons
old_footer_social = """            <div class="footer-social">
                <a href="#" aria-label="Facebook">Fb</a>
                <a href="#" aria-label="Instagram">Ig</a>
                <a href="#" aria-label="Twitter">Tw</a>
                <a href="#" aria-label="VK">Vk</a>
                <a href="#" aria-label="Telegram">Tg</a>
            </div>"""

new_footer_social = """            <div class="footer-social">
                <a href="#" aria-label="Telegram">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13"></path><path d="M22 2L15 22L11 13L2 9L22 2Z"></path></svg>
                </a>
                <a href="#" aria-label="Instagram">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>
                <a href="#" aria-label="Facebook">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                </a>
            </div>"""
if old_footer_social in html_content:
    html_content = html_content.replace(old_footer_social, new_footer_social)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# --- 2. Modify CSS ---
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

new_css_additions = """
/* Features */
.lang-switch {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    padding: 0.5rem 0.8rem;
    border-radius: 20px;
    cursor: pointer;
    font-weight: 600;
    transition: var(--transition);
    font-size: 0.9rem;
}
.lang-switch:hover {
    border-color: var(--gold);
    color: var(--gold);
}
.btn-login {
    background-color: var(--gold);
    color: var(--dark-brown) !important;
}
.btn-login:hover {
    background-color: #fff;
}
.footer-social a {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 45px;
    height: 45px;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 50%;
    color: #fff;
    transition: var(--transition);
}
.footer-social a:hover {
    border-color: var(--gold);
    background-color: var(--gold);
    color: var(--dark-brown);
}
.footer-social svg {
    width: 20px;
    height: 20px;
}
@media (max-width: 768px) {
    .hidden-mobile { display: none !important; }
    .header-actions { gap: 0.8rem; }
    .btn-login { padding: 0.4rem 0.8rem; font-size: 0.75rem; }
}
"""
if ".lang-switch" not in css_content:
    css_content += new_css_additions
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

print("Modifications done")
