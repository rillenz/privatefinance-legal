# Privacy Policy

Approved pre-launch version - effective 25 October 2026. Application not implemented.

## Purpose and current status

PrivateFinance is a planned personal finance application developed by Alexander Richter exclusively for his own private, non-commercial use with his own bank accounts. It is not offered to other users, households or businesses.

The application has not yet been implemented. There is currently no PrivateFinance application collecting, retrieving or storing bank information. This notice describes the current development stage and intended functionality; it does not claim that planned features or security controls already exist.

This public website provides legal information only. It has no bank connection features and does not receive bank credentials, balances or transactions.

## Developer and privacy context

Alexander Richter
Email: majarichanders@outlook.com (mailto:majarichanders@outlook.com)

Alexander Richter is the developer and intended sole user. The GDPR household exemption may be relevant to his own processing carried out exclusively in a personal or household capacity. This is not a blanket exemption for Enable Banking, banks, GitHub or email providers, whose own processing must be considered separately.

If the app is offered to others or its purpose changes, privacy responsibilities, any applicable lawful bases and this notice must be reassessed before that change. No commercial service or general public access is authorised by this notice.

## Planned account information

The planned purpose is to display the developer's own accounts, balances and transactions using Enable Banking. Depending on the bank, granted permissions and implemented features, relevant information may include:

- Account identifiers such as IBANs, account names, holder details, currencies, bank names and other account metadata.

- Balances, balance types and timestamps.

- Transactions, amounts, currencies, dates, status, descriptions, references and counterparty information.

- Connection and consent metadata, account/session identifiers, expiry information and necessary technical error information.

These are possible categories, not a record of data already collected. Transaction details may also concern other people or reveal sensitive information. The intended purpose is personal financial organisation, not unrelated profiling or advertising.

TODO P1 — Before bank-data processing: select and document the exact fields, permissions, purposes, recipients and necessary logs; limit collection to the implemented personal-finance features.

## Authentication and approval

The planned connection uses Enable Banking to facilitate the bank's supported authentication and authorisation process. The user must approve the requested account access, and the bank may require strong customer authentication, for example BankID. No bank access is granted by visiting this website or reading these documents.

PrivateFinance must not collect bank passwords, BankID security codes or equivalent authentication secrets. Those belong only in the bank's or identity provider's genuine authentication interface. They must not be sent through this website or by email.

For use in Enable Banking's restricted production mode, the intended accounts must be linked to the application. Linking an account does not replace the API authorisation required to retrieve its data. Availability, permitted scope and access duration depend on the bank and provider.

TODO P2 — Before bank-data processing: implement and test bank redirects, requested permissions, expiry, renewal, cancellation, session invalidation and the stopping of background retrieval. Document the actual disconnection steps.

## Enable Banking and other providers

Enable Banking is the planned API provider for authorised account information. Its processing and the bank's own processing are governed by their applicable information and terms. See Enable Banking's account-information privacy notice (https://auth.enablebanking.com/privacy) and the relevant bank's privacy information.

No application hosting provider, database service, deployment region or international-transfer arrangement has yet been selected for PrivateFinance. This must not be read as a promise of local-only or EEA-only processing. The legal website's intended hosting is addressed separately below.

TODO P3 — Before bank-data processing: document the actual provider entities and roles, applicable agreements, any app hosting or other recipients, processing locations and any international transfers and required safeguards.

## Private keys, tokens and protection

Enable Banking authenticates application API requests with JWTs signed using the application's private RSA key. These application credentials are separate from the user's bank login and approval.

The implementation requirements are to keep private signing keys and API/session credentials out of frontend code, public repositories, URLs and ordinary logs; limit access to the components that require them; and replace exposed credentials and terminate affected sessions as appropriate. Private RSA keys must not be delivered to a browser.

These are requirements for the future application, not verified statements about an existing implementation. No claim is made about encryption at rest, a particular key vault, backup protection or a completed security audit.

TODO P4 — Before bank-data processing: implement and verify credential storage and access, token lifetimes, transport and storage protection, log redaction, key rotation, backup protection and incident handling. Record the actual controls in this notice.

## Minimisation, retention and deletion

No retention period or application storage architecture has been set because the app has not been built. Whether retrieved information will remain transient or be saved, and how copies, caches, logs and backups will be handled, must be decided before real bank data is processed.

The implementation should retrieve only necessary information and retain it only for the documented personal-finance purpose. Authorisation expiry and deletion of information already retrieved are different events.

TODO P5 — Before bank-data processing: define and test storage locations, retention periods or criteria, cache and log expiry, deletion of retained information and expiry of backup copies. Update this notice with the actual arrangements.

## Withdrawing access

Bank access can be withdrawn through the bank's consent or connected-services controls where available; contact the bank if those controls cannot be found. Enable Banking also offers session deletion, which closes bank consent automatically where possible. Deleting an application session must not be assumed to revoke every bank-side consent immediately.

PrivateFinance has no implemented disconnect or deletion interface yet. Its future procedure must be tested before use, as identified in TODO P2 and TODO P5. Stopping access does not by itself erase data already retrieved.

Where a processing activity relies on GDPR consent, withdrawal does not affect the lawfulness of processing based on that consent before withdrawal. Bank-access approval should not be treated as a blanket GDPR legal basis for every subsequent use.

## Rights where GDPR applies

Where GDPR applies, and subject to its conditions, individuals may have rights to information, access, rectification, erasure, restriction, portability and objection. Where consent is the legal basis, it may be withdrawn. A complaint may be made to the competent supervisory authority, including Sweden's IMY (https://www.imy.se/en/) where relevant.

These rights are conditional and do not by themselves make the GDPR applicable to exempt personal or household processing. Each provider's obligations require a separate assessment.

Privacy questions or requests concerning this project may be sent to Alexander Richter at majarichanders@outlook.com (mailto:majarichanders@outlook.com). Requests will need to be assessed according to the activity and applicable law. Do not send bank credentials, private keys or full transaction histories in an initial message.

## This website and correspondence

This static website uses no analytics, tracking scripts, advertising, cookies or browser storage. Fonts, styling and the optional theme script are served with the site. A manually chosen theme is not stored and lasts only for the current page.

The website is intended for GitHub Pages hosting. GitHub states that it logs visitors' IP addresses for security. See GitHub's Pages documentation (https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection) and GitHub's privacy statement (https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). External websites are contacted when their links are followed.

The contact link opens your email application; this website does not contain a contact form. If you choose to email the project, your address and message will be processed by the email services involved and may be retained in correspondence. No fixed correspondence-retention period has been established. Share only what is necessary for the question and do not send financial records or authentication secrets.

## Contact and updates

Alexander Richter
Email: majarichanders@outlook.com (mailto:majarichanders@outlook.com)

This version concerns a project under development, not an operational banking application. It must be updated before processing bank data and before any material change in users, purpose or providers. The implementation tasks marked above remain open.

Effective date: 25 October 2026. Publication does not mean that the application is ready or that its security has been verified.

