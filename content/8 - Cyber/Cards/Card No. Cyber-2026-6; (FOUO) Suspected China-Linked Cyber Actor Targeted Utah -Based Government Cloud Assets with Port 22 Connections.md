---
title: "Suspected China-Linked Cyber Actor Targeted Utah-Based Government Cloud Assets with Port 22 Connections"
card: "Cyber-2026-6"
author: "SIAC"
outlet: "HSIN"
published: 2026-04-02
url: ""
query: ""
imported: 2026-04-02
type: news-card
---tags:
  - Cyber
  - China

KIQ: ["[[RCYR 2026.1]]", "[[RCYR 2026.2]]", "[[RCYR 2026.3]]", "[[RCYR 2026.4]]", "[[RCYR 2026.6]]"]
---
(U//FOUO) SIAC. "Suspected China-Linked Cyber Actor Targeted Utah-Based Government Cloud Assets with Port 22 Connections." Serial: SIAC 260401-1702216, April 2, 2026. HSIN. Accessed April 7, 2026. 

![[RCYR 2026.1]]
![[RCYR 2026.2]]

(U//FOUO) A review of network logs from 12 March 2025 through 12 March 2026 identified prolonged interactions between Utah-based cloud computing assets and an Internet Protocol (IP) address, 27.128.171[.]39, suspected to be controlled by a China-linked cyber actor. Over this twelve-month period, the threat actor targeted commercial cloud infrastructure belonging to Utah-based, government-related cyber assets with 1,805 distinct network connection events, exclusively targeting destination Port 22 Secure Shell (SSH)a . 
(U//FOUO) The timing of this network activity directly correlates with a Department of Homeland Security (DHS) Network Defender Bulletin (NDB) DHS-IA-NDB-2026-005761 . According to DHS, China-linked cyber actors compromised a US telecommunications provider in September 2025, exfiltrating sensitive data and subsequently using compromised infrastructure to conduct further malicious cyber activity in October 2025. The network activity against Utah assets aligns with this established operational timeline. There is currently no indication of any breaches or compromises identified with the activity found in these network logs. 
(U//FOUO) The Utah Statewide Information and Analysis Center (SIAC) assesses it is very likelyb that the China-linked actor initiated a widespread, aggressive scanning and exploitation campaign against US infrastructure simultaneously with the telecom breach mentioned above. This assessment is made with high confidence based on the September 2025 surge against Utah cloud assets matching the timeline of the initial telecommunications compromise reported by DHS.

(U//FOUO) This threat actor explicitly targeted commercial cloud environments used by Utah-based, government related cyber assets. The threat actor interacted with workloads across three specific environments:
- (U//FOUO) Government Related Transparency Web Application Server: Targeted heavily via Port 22 connections, specifically interacting with a public transparency web application server (364 events), an internal governance application server (309 events across various internal IPs), and an automated email reporting server (29 events).
- (U//FOUO) Government Related Financial/Audit Server: Targeted via Port 22 connections, interacting with a specialized AI/GPU computing instance (508 events), internal audit management servers (228 events), and secondary scanning/reconnaissance virtual machines (89 events).
- (U//FOUO) Government Related Water Development Project: Specifically interacted with the â€œutdrone-mission-form-serverâ€ (48 events).
	- (U//FOUO) This pattern closely resembles the major activity spike reported in SIAC report titled: â€œ(U//FOUO) Malicious Foreign Internet Protocol Addresses Conduct SSH Brute Force Attacks Against Water Related Utah Assetsâ€SIAC-250717-10152362 . 

(U//FOUO) The SIAC assesses it is likely the threat actor was seeking sensitive financial data, internal audit data, or specific governmental operational information, rather than conducting untargeted, opportunistic scanning. This assessment is made with medium confidence based on the targeted focus on transparency, financial/audit, and specialized drone mission servers, though the exact intent behind the connections can be interpreted in various ways.