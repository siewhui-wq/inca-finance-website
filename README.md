# INCA Finance Ltd – website

Static website for INCA Finance Ltd (FCA FRN 480650), hosted on GitHub Pages.

## Where it lives

- Repository: https://github.com/siewhui-wq/inca-finance-website (public)
- Draft site: https://siewhui-wq.github.io/inca-finance-website/ (GitHub Pages, `main` branch, `/docs` folder)
- Working copy: `~/Downloads/inca` on Siew Hui's Mac, opened in GitHub Desktop. Changes go live when she clicks **Push origin**

## How it's organised

| Folder / file | What it is |
|---|---|
| `src/pages/` | One file per page: the content you edit |
| `src/partials/` | Shared header, footer (including the FCA status and risk warnings) and draft banner |
| `build.py` | Firm details (FRN, phone, email, address) live at the top. Run `python3 build.py` to rebuild |
| `docs/` | The finished site that GitHub Pages serves. Don't edit it by hand; rebuild instead |

## Publishing on GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings → Pages**, choose *Deploy from a branch*, then select `main` and `/docs`.
3. To use the www.incafinance.co.uk domain, add it under **Custom domain**, which creates `docs/CNAME`. At your DNS provider, point `www` to `<your-github-username>.github.io` with a CNAME record, and the apex domain to GitHub's A records. Then tick **Enforce HTTPS**.
4. Set `DRAFT = False` in `build.py` and rebuild **only after compliance sign-off**. Draft mode shows a yellow banner and blocks search engines in `robots.txt`.

## Go-live checklist (compliance)

Every item is highlighted in yellow on the site until it's filled in.

- [x] **Fees**: amounts are not published (not required by the FCA). The site says a fee is charged and refers clients to the Terms of Business
- [x] **Insurance remuneration**: confirmed no fee; paid by insurer commission
- [x] **Permissions**: wording taken from the Terms of Business (30 Oct 2026). Double-check it against the FCA Register
- [ ] **Email address** (`build.py`): confirm or replace `info@incafinance.co.uk`
- [x] **Opening hours**: 9am to 9pm
- [x] **Trading address**: 63 St Mary Axe, London EC3A 8AA (from the Terms of Business)
- [x] **Team section**: removed
- [x] **ICO registration number**: Z1389227
- [ ] **Privacy notice**: have it reviewed (retention wording taken from the Terms of Business)
- [x] Free initial consultation: confirmed in the Terms of Business
- [x] **Insurance products**: income protection, landlord and business insurance stay on the site (decided 4 Nov 2026), although the Terms of Business list only life, mortgage term assurance, critical illness and buildings/contents
- [ ] Confirm the "30+ years' experience" claim (advisers' combined experience; the company was founded in 2006)
- [ ] Have the financial promotions approved and recorded by the person responsible for compliance
- [ ] Higher-resolution logo: the cube was redrawn as an SVG and "INCA Finance Ltd" is set as live text in grey (#58595B), matching the supplied logo. Replace `docs/assets/img/inca-mark.svg` if you have the original vector artwork

## Deliberately removed from the old site

- **"Financial planning"**: investment advice needs separate FCA permissions. Add it back only if FRN 480650 holds them.
- **"Find the best interest rates"**: absolute claims like this can be misleading under the financial promotion rules.
- **"The FCA does not regulate some investment mortgage contracts"**: replaced with specific warnings for buy-to-let, commercial and bridging finance.
