# PrivateFinance legal website

A dependency-free, responsive static legal-information website. System light/dark themes, an accessible per-page theme switch, English documents, keyboard navigation, print styles and relative project-repository URLs. No cookies, browser storage, analytics, external fonts or bank integration.

**Status: pre-launch legal website approved by the owner on 25 October 2026.** See [LEGAL_REVIEW.md](LEGAL_REVIEW.md) for the five remaining implementation TODO items. The application does not exist yet. Approval covers publication of this pre-launch legal website with the five implementation tasks disclosed; it does not authorise processing bank data or guarantee registration acceptance. See the repository Actions history for deployment status.

## Files

- `index.html` — document landing page
- `privacy/index.html` — Privacy Policy
- `terms/index.html` — Terms of Service
- `assets/style.css` — responsive design and themes
- `assets/theme.js` — optional theme toggle, no persistence or network access
- `.github/workflows/deploy.yml` — automatic deployment on main, gated by release checks
- `scripts/check.py` — dependency-free document/link/public-file checks and draft release guard
- `.gitignore` — common secret and personal-data file exclusions
- `PRIVACY_REVIEW.md`, `TERMS_REVIEW.md` — readable copies of the current HTML text for approval

## Local review

From this directory:

```bash
python3 scripts/check.py
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://localhost:8080/ and follow both document links. For project-prefix testing, copy only the public website files into a fresh temporary directory under `privatefinance-legal/`, then serve that temporary root. Never serve the application parent directory, which may contain credentials. No installation or build is required.

The theme follows the OS unless overridden using the button. No preference is stored; navigation or reload follows the OS again. Without JavaScript the OS theme and all navigation remain usable.

## Before publishing

Review [LEGAL_REVIEW.md](LEGAL_REVIEW.md) and obtain explicit approval of the pre-launch legal text with all five TODO tasks disclosed. Record the publication date and replace draft markers with the approved pre-launch status as documented there. Keep P1–P5 visible until the app implementation has been verified; none of these tasks is resolved by publishing the legal website. The release check accepts this approved pre-launch scope and rejects draft status or unexpected TODOs:

```bash
python3 scripts/check.py --release
```

Keep app credentials, transaction data and all private files outside this repository. `.gitignore` cannot stop someone from pasting secrets into an HTML file or forcibly adding ignored files. The workflow uploads only explicitly staged website directories and checks their file allowlist; it does not upload this README or review notes. The pattern scan is an additional check, not a security audit.

## GitHub Pages publication (after legal approval)

Repository: https://github.com/rillenz/privatefinance-legal

1. Verify `gh auth status` in WSL.
2. Commit the approved website on `main` using an explicit file list.
3. Activate Pages in repository Settings → Pages → Source: **GitHub Actions**. With sufficient permission, use `gh api --method POST repos/rillenz/privatefinance-legal/pages -f build_type=workflow` (or PATCH for an existing Pages site).
4. Push `main`; the workflow validates, stages only public files, uploads the Pages artifact, then deploys it. Inspect `gh run list` and `gh run watch RUN_ID --exit-status`.
5. Verify the actual responses and content, not just the workflow result:

```bash
curl --fail --location --show-error --output /tmp/privatefinance-privacy.html --write-out '%{http_code}\n' https://rillenz.github.io/privatefinance-legal/privacy/
curl --fail --location --show-error --output /tmp/privatefinance-terms.html --write-out '%{http_code}\n' https://rillenz.github.io/privatefinance-legal/terms/
```

Confirm the documents have the right headings, approved pre-launch text, correct contact details, all five acknowledged TODOs and no draft/awaiting-approval labels. Verify navigation, stylesheet and script under the project prefix. If permission or authentication fails, stop and report the actual error; do not claim publication.

Public addresses (verify after each deployment):

- https://rillenz.github.io/privatefinance-legal/privacy/
- https://rillenz.github.io/privatefinance-legal/terms/

GitHub Pages handles HTTPS. Its infrastructure logs visitor IPs for security; see the policy's hosting section. The absence of application analytics is not a claim that GitHub has no hosting logs.

## Maintenance

Edit the HTML/CSS directly. Reassess the policy whenever users, purpose, providers, retention or controls change. Re-review legal changes before pushing to main: subsequent pushes automatically deploy after the release check passes. Keep review notes current and never replace the project repository with the parent application directory.
