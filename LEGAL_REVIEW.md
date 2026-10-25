# Legal review — approved pre-launch version

Approved: 25 October 2026. After receiving links to both revised documents and the disclosure of all five outstanding TODOs, the owner explicitly answered “Yes” to publication of this pre-launch version.

## Confirmed by the owner

- Public developer/contact name: Alexander Richter.
- Public email: majarichanders@outlook.com (provided by the owner; mailbox delivery has not been tested).
- App exclusively for the developer's own private use; no other users or commercial offering.
- App code does not exist yet. The notice therefore does not claim operational bank processing or verified production controls.

## Scope for approval

The owner approved publication of the **pre-launch legal-information website only**, with P1–P5 still open. This does not approve processing real bank data, establish security compliance, resolve the implementation tasks below, or guarantee Enable Banking acceptance.

The household exemption is described conditionally; no blanket GDPR exemption or unverified controller/processor relationship is asserted. No particular application hosting, encryption, retention period or implemented disconnect button is promised. No governing country, street address or company registration has been invented. Email correspondence and GitHub hosting are distinguished from the future bank-data application.

## All remaining public TODOs

| ID | Must be resolved before bank-data processing |
| --- | --- |
| P1 | Select actual data fields, permissions, purposes, recipients and necessary logs; implement minimisation. |
| P2 | Implement and test authorisation, redirects, expiry/renewal/cancellation, session termination and stopping background retrieval; document disconnection. |
| P3 | Identify actual providers/entities and roles, agreements, hosting/recipients, processing locations and international-transfer safeguards. |
| P4 | Implement and verify key/token storage and access, lifetimes, transport/storage protection, log redaction, rotation, backup protection and incident handling. |
| P5 | Define storage, retention periods/criteria, cache and log expiry, deletion and backup expiry; test and document. |

The former 16 placeholders have been replaced with the confirmed identity, sole-use scope and current non-implementation status. The five unresolved implementation tasks remain expressly marked **TODO** in the policy; terms refer to them. No missing implementation detail is treated as verified or silently removed.

## Publication procedure after explicit approval

1. Record the owner's approval of this specific pre-launch version, including publication with P1–P5 still open.
2. Set the website publication/effective date, replace draft banners with the continuing pre-launch status, and set all three HTML `data-status` values to `approved-prelaunch`. Preserve the statement that the application is not implemented and all five TODO disclosures.
3. Update the two readable review copies from the HTML if approval involves text edits; keep them consistent.
4. Run `python3 scripts/check.py --release`. Draft status is blocked. Only the five expressly disclosed pre-launch task IDs are allowed.
5. Commit only explicit website files, never the parent directory or any credentials. Configure Pages, push, watch deployment, then verify both public pages return HTTP 200 and contain approved text and contact details.
6. Before real bank-data processing, resolve P1–P5, revise the notice to the actual implementation and review again. The current checker deliberately accepts only the approved pre-launch scope; adapt it during that review.

Approval has been recorded, draft labels have been replaced, and both documents retain the pre-launch disclosures and five TODOs. Deployment status is available in the repository’s GitHub Actions history; public URL and content verification is performed after deployment.

## Primary references consulted

- Enable Banking API authentication and session deletion: https://enablebanking.com/docs/api/reference
- Enable Banking privacy information: https://enablebanking.com/privacy-policy/
- IMY on the personal/household exemption: https://www.imy.se/privatperson/dataskydd/introduktion-till-gdpr/nar-gdpr-inte-galler/
- European Commission on GDPR rights: https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en
- Your Europe on privacy-notice requirements: https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm
- GitHub Pages workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- GitHub Pages visitor IP logging: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection

Provider documentation does not prove that PrivateFinance follows it. In particular, session deletion only closes bank consent automatically where possible; do not promise universal immediate bank revocation.
