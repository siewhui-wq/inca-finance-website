#!/usr/bin/env python3
"""Build the INCA Finance static site.

Edit pages in src/pages/*.html and shared parts in src/partials/.
Firm details live in SITE below - change them once and every page updates.
Run:  python3 build.py      -> writes finished pages into docs/ (served by GitHub Pages)
"""
import re, pathlib, datetime

SITE = {
    "FIRM": "INCA Finance Ltd",
    "FRN": "480650",
    "COMPANY_NO": "05988620",
    "REG_OFFICE": "2nd Floor, Premier House, 309 Ballards Lane, London N12 8LY",
    "OFFICE": "63 St Mary Axe, London EC3A 8AA",
    "COMPLIANCE_EMAIL": "Compliance@incafinance.co.uk",
    "PHONE": "0777 9279 021",
    "PHONE_TEL": "+447779279021",
    "EMAIL": "info@incafinance.co.uk",          # CONFIRM before go-live
    "DOMAIN": "https://www.incafinance.co.uk",
    "YEAR": str(datetime.date.today().year),
    "UPDATED": datetime.date.today().strftime("%-d %B %Y"),
}
# Shows a "draft - pending compliance sign-off" bar on every page. Set False to go live.
DRAFT = False

NAV = [("index.html", "Home"), ("mortgages.html", "Mortgages"), ("insurance.html", "Insurance"),
       ("about.html", "About us"), ("fees.html", "Fees")]

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "src", ROOT / "docs"


def fill(text):
    return re.sub(r"\{\{(\w+)\}\}", lambda m: SITE.get(m.group(1), m.group(0)), text)


def nav_html(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append('<li><a class="btn btn-primary" href="contact.html">Book an appointment</a></li>')
    return "\n".join(items)


def build():
    head = (SRC / "partials/header.html").read_text()
    foot = (SRC / "partials/footer.html").read_text()
    draft = (SRC / "partials/draft.html").read_text() if DRAFT else ""
    for page in sorted((SRC / "pages").glob("*.html")):
        raw = page.read_text()
        meta = dict(re.findall(r"^@(\w+):\s*(.+)$", raw, re.M))
        body = re.sub(r"^@\w+:.*\n", "", raw, flags=re.M)
        html = (head.replace("[[TITLE]]", meta.get("title", SITE["FIRM"]))
                    .replace("[[DESC]]", meta.get("description", ""))
                    .replace("[[PATH]]", "" if page.name == "index.html" else page.name)
                    .replace("[[NAV]]", nav_html(page.name))
                    .replace("[[DRAFT]]", draft)
                    .replace("[[RISK]]", meta.get("risk", "")))
        html += body + foot
        (OUT / page.name).write_text(fill(html))
        print("built", page.name)
    # sitemap
    urls = "".join(f"<url><loc>{SITE['DOMAIN']}/{'' if p.name=='index.html' else p.name}</loc></url>"
                   for p in sorted((SRC / "pages").glob("*.html")) if p.name != "404.html")
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    (OUT / "robots.txt").write_text(("User-agent: *\nDisallow: /\n" if DRAFT else "User-agent: *\nAllow: /\n")
                                    + f"Sitemap: {SITE['DOMAIN']}/sitemap.xml\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "CNAME").write_text(SITE["DOMAIN"].split("//")[1] + "\n")


if __name__ == "__main__":
    build()
