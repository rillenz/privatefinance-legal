# Privacy Policy

Approved local-application version — effective 25 October 2026. Open tasks L1–L3 remain disclosed; publication does not complete them.

## Purpose and scope

PrivateFinance is a minimal local personal-finance application developed by Alexander Richter exclusively for his own private, non-commercial use with his own accounts. It is not offered to other users or businesses. The app can request authorised account information through Enable Banking; it does not initiate payments.

The app has been implemented locally and its API registration has been checked. The complete live bank-authorisation, callback and revocation flow has not yet been verified with the developer's accounts. A successful registration check does not establish that these bank interactions work.

The public legal website and the local app are separate. The legal website does not receive bank credentials, balances or transactions. The local app communicates with Enable Banking only for requested operations and session termination.

## Developer and privacy context

Alexander Richter

Email: majarichanders@outlook.com

The developer is the sole intended user. The GDPR household exemption may be relevant to his processing exclusively in a personal or household capacity. This is not a blanket exemption for banks, Enable Banking, GitHub or email providers. If the users, purpose or operating model changes, responsibilities and any applicable lawful bases must be reassessed before that change.

## Account information and minimisation

When the developer approves a connection, information may include account identifiers and IBANs, names/descriptions, products, currency, bank and consent metadata, balances and their dates/types, and transactions including amounts, currencies, dates, descriptions, status, references and counterparty details. Transaction descriptions can concern others or reveal sensitive information.

The API returns account metadata during authorisation. The app retains the account identifiers and descriptive fields needed to identify permitted accounts, rather than retaining the complete account response. Displayed balance and transaction responses are reduced to fields needed by the interface. The app does not perform advertising, unrelated profiling, financial scoring or automated decisions with legal or similarly significant effects.

Balances and transactions are fetched only when requested. Transactions are requested for a chosen UTC date range, defaulting to 30 days, and one API page at a time. The UI indicates whether another page is available. No automatic financial-data refresh is implemented.

## Authentication and authorisation

The developer chooses a bank and is redirected through Enable Banking to the supported bank-authentication process. The bank may require strong customer authentication such as BankID. Bank passwords and BankID security codes must be entered only in genuine bank or identity-provider interfaces; PrivateFinance does not provide fields to collect them.

The app supports private-user redirect authentication. It requests balances and transactions for accounts approved by the user. In restricted production mode, those accounts must also be linked to the registered application in Enable Banking. Account linking and API authorisation are separate steps.

The backend validates a random, browser-session-bound, expiring state and exchanges the returned authorisation code for a session. The code and provider session identifier are not sent to frontend JavaScript. The callback response redirects to a clean local URL without the code or state.

TODO L1 — Before relying on real account access, complete and document a live own-account test of authorisation, the local HTTPS certificate and callback, expiry and revocation. Current automated tests use a simulated provider.

## Providers and processing locations

The app process runs locally; no third-party app-hosting or database service is configured. Outgoing account-information API requests go to Enable Banking, which interacts with the bank. The bank's and Enable Banking's own terms and notices govern their processing. See https://auth.enablebanking.com/privacy and the relevant bank's privacy information.

No claim is made that all processing is local or confined to a particular country. Provider processing locations, roles and transfer arrangements are not established merely by the app running locally.

TODO L2 — Review the applicable provider terms and privacy information for this registration, record the relevant entities/roles and processing locations, and establish any required transfer safeguards before real bank-data processing. No controller/processor relationship is assumed without assessment.

## Keys, tokens and local access protection

The private application RSA key is read by the backend from a configured private file outside the served assets. In the checked WSL configuration, private-file ownership and restrictive permissions are verified before loading. The key is not embedded in frontend code, stored in this repository or sent to the browser. API requests use RS256-signed JWTs with a five-minute lifetime. Provider session IDs remain in backend memory; the browser uses separate random local handles.

The app explicitly binds IPv4 and IPv6 loopback, rejects non-loopback peers and unexpected Host/Origin values, and implements CSRF and framing protection. Loopback restricts network access; it does not isolate the app from other programs or users on the same computer. The app has no separate user login.

The local HTTPS connection uses a separate self-signed certificate, generated for localhost for 90 days. The browser must explicitly accept it or trust it through a separately reviewed setup. No system-wide trust change is installed automatically. Outgoing API HTTPS uses the runtime's normal certificate validation. These statements describe the implementation and local checks, not an independent security audit or a guarantee of absolute security.

The application writes no bank-data, token, credential or callback-query logs. Only fixed startup/shutdown and generic status messages are written to the terminal. Keys are files protected by permissions; no file-encryption, full-disk-encryption, swap or crash-dump protection has been verified.

TODO L3 — Establish the developer's procedure for an exposed key, including disabling/replacing the affected application credentials through Enable Banking and withdrawing affected bank access. OS and browser protection require their own assessment.

## Storage, retention and deletion

There is no bank-data database, file-based transaction history, export or application backup. API tokens are created for requests and not persisted. Account/connection metadata and pagination state remain in backend memory; displayed financial information also exists in the browser page's memory. The app sends no-store headers and uses no localStorage, sessionStorage or service worker.

The browser uses one temporary Secure, HttpOnly, SameSite=Lax local session cookie. The local session expires after eight hours. A bank session is requested for no more than one day, subject to a lower bank maximum; a bank-side consent can have a different duration.

On local-session expiry, the app attempts provider-session deletion. When deletion is confirmed, connection records are removed. If revocation fails, further account reads are blocked, account metadata and pagination state are released, and records needed for retry can remain in backend memory beyond eight hours until revocation succeeds or the process exits.

Disconnecting clears the associated view and confirmed connection. The Hide details control clears the current account view but does not revoke bank access. Reloading clears the current view but may keep the connection active in backend memory. Closing a tab alone does not revoke access. Normal process shutdown attempts to delete known sessions; process exit releases its application memory but does not guarantee erasure from RAM, browser internals, operating-system swap, crash dumps or screenshots.

## Withdrawing access

Use Disconnect or Disconnect all in the app. The backend calls Enable Banking's session-deletion endpoint. On failure the UI blocks further reading and offers a retry. The bank's consent controls should also be used if access remains shown or the outcome is uncertain. Enable Banking closes bank-side consent automatically only where supported.

A crash, forced exit, network failure or uncertain code-exchange outcome can leave bank consent active. Bank controls may then be required even if the local app no longer has its session ID. Deleting a session does not itself erase information already processed by the bank or provider.

Where processing relies on GDPR consent, withdrawing consent does not affect earlier lawful processing. Bank access authorisation does not automatically establish the GDPR lawful basis for every use.

## Rights where GDPR applies

Where applicable and subject to legal conditions, individuals may have rights to information, access, rectification, erasure, restriction, portability and objection, withdrawal of consent where that is the basis, and a complaint to a competent supervisory authority such as Sweden's IMY. Listing these rights does not make GDPR applicable to exempt household processing.

Send project privacy questions or requests to Alexander Richter at majarichanders@outlook.com. Do not send credentials, private keys or full financial histories in an initial message.

## Public website and correspondence

The separate GitHub Pages legal website has no analytics, advertising, external fonts, tracking scripts, cookies or browser storage. GitHub logs visitor IP addresses for security under its own privacy information: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection and https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement .

Unlike that legal website, the local app uses the necessary temporary session cookie described above. External legal links in the app contact the relevant website when followed. No external runtime assets are loaded.

The contact link opens the user's email application. Correspondence is handled by the email services involved and may be retained in the mailbox; no fixed correspondence retention period has been established. Share only information necessary for the question.

## Updates and status

This version is effective from 25 October 2026. It describes the local implementation but leaves L1–L3 open. Those tasks must not be represented as completed by publishing these documents. Review this notice before material changes in users, purposes, providers or actual processing.
