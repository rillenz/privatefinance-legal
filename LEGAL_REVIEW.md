# Legal review — approved local-application version

Approved and effective: 25 October 2026. The owner explicitly stated: “Ja, jag godkänner de uppdaterade juridiska texterna. Publicera dem.” Approval covers the full updated Privacy Policy and Terms of Service provided in `privatefinance-local/legal-review/`, with L1–L3 disclosed.

## Scope and evidence

- Alexander Richter, majarichanders@outlook.com; exclusively the developer's own private, non-commercial use.
- The local implementation now exists. The documents describe actual loopback binding, local self-signed HTTPS, server-side RSA handling, five-minute JWTs, a necessary temporary local session cookie, in-memory account handling and manual financial-data requests.
- API registration, active PRODUCTION/AIS and the exact callback were verified. The owner reports linking a bank account to Enable Banking; this does not itself verify authorisation and retrieval through the local app.
- Automated backend and simulated browser callback tests passed. No complete real own-account bank flow is claimed.
- The public legal website remains static, with no bank integration, cookies, browser storage, analytics or external runtime resources. It must not be confused with the separate local app's session cookie and API calls.
- No claim of disk encryption, guaranteed secure memory erasure or a completed independent security audit is made. No unverified legal entity, address, governing jurisdiction or controller/processor relationship has been invented.

## Remaining disclosed tasks

| ID | Approved open disclosure |
| --- | --- |
| L1 | Complete and document a live own-account authorisation, local certificate/callback, expiry and revocation test. |
| L2 | Review provider terms, entities/roles, processing locations and any required transfer safeguards. |
| L3 | Establish the exposed-key procedure and separately assess OS/browser protection. |

The former pre-launch P1–P5 have been replaced by implementation descriptions and these three specific remaining tasks. Publication does not mark them complete, authorise third-party/commercial use, or guarantee Enable Banking acceptance.

## Release controls

All three HTML pages are marked `approved-local-app`. Release checks require the approved local-implementation statement and precisely the known L1–L3 task IDs, and still reject draft/awaiting-approval labels. Relative links, fragments, the public-file allowlist, common credential patterns and JavaScript network/storage patterns are checked. Prose may mention browser storage APIs as part of the privacy explanation; the actual legal-site script is checked for their use.

Only explicit legal-site files are committed. No local-app source, bank keys, application configuration or financial information is included. GitHub Actions stages only the five public HTML/CSS/JS files. Deployment success and public HTTP/content checks are verified after push; see Actions history for the deployed revision.

## Primary references consulted

- Enable Banking API authentication and session deletion: https://enablebanking.com/docs/api/reference
- Enable Banking privacy information: https://auth.enablebanking.com/privacy
- IMY on the personal/household exemption: https://www.imy.se/privatperson/dataskydd/introduktion-till-gdpr/nar-gdpr-inte-galler/
- European Commission on GDPR rights: https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en
- Your Europe on privacy-notice requirements: https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm
- GitHub Pages workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- GitHub Pages visitor IP logging: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection

Provider documentation does not prove that PrivateFinance follows it. In particular, session deletion only closes bank consent automatically where possible; do not promise universal immediate bank revocation.
