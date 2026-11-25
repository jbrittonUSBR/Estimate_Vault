---
title: "Potential Abuse of Knowledge Base Articles for Phishing."
card: "Insider-2026-1"
author: "E-ISAC"
outlet: "Serial: 000026904"
published: 2026-05-15
url: "https://www.eisac.com/portal/article/PotentialAbuseofKnowledgeBaseArticlesforPhishing-5186"
query: ""
imported: 2026-05-15
type: news-card

KIQ: []
---
(TLP: Amber) E-ISAC. "Potential Abuse of Knowledge Base Articles for Phishing." Serial: 000026904, May 15, 2026. https://www.eisac.com/portal/article/PotentialAbuseofKnowledgeBaseArticlesforPhishing-5186. Accessed May 27, 2026. 

![[RCYR 2026.2]]

(TLP: Amber) This morning, we received a user report of a phishing email containing a link to what appeared to be a legitimate company knowledge base (KB) article hosted on a FreshDesk instance. At this time, it is unclear whether the link originated from a compromised FreshDesk instance belonging to the legitimate company, or if a threat actor created a fraudulent FreshDesk environment designed to impersonate the organization. Analysis revealed that the KB site contained only a single article. The article hosted content that was designed to appear legitimate but ultimately redirected users to a malicious credential harvesting page. This represents a relatively novel delivery method in our environment, as we have not previously observed phishing campaigns leveraging KB article platforms in this manner. 

**Observed Tactics:**

- Abuse of trusted SaaS platform (FreshDesk) to lend legitimacy
- Minimal content footprint (single KB article) to reduce detection surface
- Use of embedded/redirection links to deliver credential harvesting payload

**Indicator(s) of Compromise (IOCs):**

- techciscosystemsincsonicsolutionsemerson[.]capitroia[.]cfd

**Additional Notes:**

- The KB article mimics a secure document delivery notification (e.g., SharePoint-themed messaging)
- Includes a “View or Download Document” call-to-action that initiates the redirect chain