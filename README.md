# INCA Finance Ltd – website

Static website for INCA Finance Ltd (FCA FRN 480650), hosted on GitHub Pages.

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

- [ ] **Fees** (`fees.html`): typical fee amounts, the maximum fee, a worked example and when the fee is payable (including any non-refundable element)
- [x] **Insurance remuneration**: confirmed no fee; paid by insurer commission
- [ ] **Permissions** (`regulatory.html`): match the wording to the FCA Register entry for FRN 480650
- [ ] **Email address** (`build.py`): confirm or replace `info@incafinance.co.uk`
- [ ] **Opening hours** (`contact.html`)
- [ ] **City office address and team details** (`about.html`): optional
- [ ] **Privacy notice**: add the ICO registration number and retention periods, then have it reviewed
- [ ] Confirm that the initial consultation is free and without obligation (home and fees pages)
- [ ] Confirm the "30+ years' experience" claim (advisers' combined experience; the company was founded in 2006)
- [ ] Have the financial promotions approved and recorded by the person responsible for compliance
- [ ] Higher-resolution logo: the cube was redrawn as an SVG and "INCA Finance Ltd" is set as live text in grey (#58595B), matching the supplied logo. Replace `docs/assets/img/inca-mark.svg` if you have the original vector artwork

## Deliberately removed from the old site

- **"Financial planning"**: investment advice needs separate FCA permissions. Add it back only if FRN 480650 holds them.
- **"Find the best interest rates"**: absolute claims like this can be misleading under the financial promotion rules.
- **"The FCA does not regulate some investment mortgage contracts"**: replaced with specific warnings for buy-to-let, commercial and bridging finance.
