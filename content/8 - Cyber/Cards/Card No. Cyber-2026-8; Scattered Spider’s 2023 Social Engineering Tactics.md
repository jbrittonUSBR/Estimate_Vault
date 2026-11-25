---
title: "Scattered Spider’s 2023 Social Engineering Tactics"
card: Cyber-2026-8
author: 
outlet: HSIN
published: 2026-01-01
url: ""
query: ""
imported: 2026-01-01
type: news-card

KIQ: ["[[RCYR 2026.1]]", "[[RCYR 2026.2]]", "[[RCYR 2026.3]]", "[[RCYR 2026.4]]", "[[RCYR 2026.5]]", "[[RCYR 2026.6]]"]
---
(U//FOUO) SNCTC. "Cyber Awareness Advisory: Scattered Spiderâ€™s 2023 Social Engineering Tactics." April 2, 2026. HSIN. Accessed April 9, 2026. 

![[RCYR 2026.1]]
![[RCYR 2026.2]]

(U//FOUO) Scattered Spider is a financially-motivated threat group comprised of young, native English-speaking threat actors from the United States and the United Kingdom commonly associated with the Coma . Scattered Spider typically sets their sights on an industry sector and targets third-party vendors within that sector as a strategic entry point into the vendorâ€™s clients. The group uses social engineering techniques, posing as the compromised third-party vendors to obtain credentials, install remote access tools, and bypass MFA. b Scattered Spider supplements the gaps in their skillset through third-party tools and affiliate partnerships with ransomware-as-a-service (RaaS)c operations.

(U//FOUO) Social Engineering Techniques: Scattered Spider uses various social engineering tactics, such as SIM swapping, SMS phishing, and MFA fatigue attacks. After performing recon on their chosen target, the group impersonates an employee of a victim organization through SIM swapping, tricking the victimâ€™s telecommunications provider into transferring the phone number to a phone under the threat actorsâ€™ control.8 The group may also use SMS phishing (smishing) by sending fake text messages to trick people into issuing a password reset or confirming a MFA request.9 After a successful SIM swap or smishing attempt, the group may then use MFA fatigue attacks to bombard the victim with MFA token requests until the victim, out of confusion or frustration, accepts the request.

(U//FOUO) Once Scattered Spider successfully takes over a victimâ€™s phone number, they use this access to contact the victim organizationâ€™s third-party service desk and request an account reset to gain access to the victim organizationâ€™s Single Sign-On (SSO) account. Scattered Spider relies on VoIP (Voice Over Internet Protocol) services to mimic internal phone numbers and spoof email addresses or third-party accounts during these account takeover attempts. During the course of the call, Scattered Spider imitates a real victim employee or contractor using differing tactics:
- (U) The threat actor may impose a false sense of urgency by imposing time constraints to pressure the agent.
- (U) The threat actor may feign knowledge of systems used by the organization or reference believable events to downplay their request (e.g., â€œCanâ€™t you just go into Okta<sup>USBUS</sup> and reset like you did last week for Mike in Ops?â€)
- (U) The threat actor may engage in polite small talk referencing local events or weather to build rapport and prove trustworthiness with the agent.