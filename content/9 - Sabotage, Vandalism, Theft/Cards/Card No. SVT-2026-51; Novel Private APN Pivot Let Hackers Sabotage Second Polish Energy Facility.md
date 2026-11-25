---
title: "Novel Private APN Pivot Let Hackers Sabotage Second Polish Energy Facility."
card: "SVT-2026-51"
author: "Eduard Kovacs"
outlet: "SecurityWeek"
published: 2026-08-10
url: "https://www.securityweek.com/novel-private-apn-pivot-let-hackers-sabotage-second-polish-energy-facility/"
query: ""
imported: 2026-08-10
type: news-card

KIQ: []
---
(U) Eduard Kovacs. "Novel Private APN Pivot Let Hackers Sabotage Second Polish Energy Facility." SecurityWeek, August 10, 2026. https://www.securityweek.com/novel-private-apn-pivot-let-hackers-sabotage-second-polish-energy-facility/. Accessed August 10, 2026.

![[RSVT 2026.2]]
![[RSVT 2026.4]]

(U) Poland’s computer emergency response team (**CERT.PL**) revealed details of a sophisticated cyberattack from December 2025 targeting a combined heat and power (CHP) plant. According to researchers, the incident marks the **first known instance of hackers utilizing a private APN (Access Point Name) as a lateral attack vector** to breach an operational technology (OT) network.
### **Key Takeaways**

- **The Target:** The secondary attack—unfolding in parallel with a broader wave of Russian-linked Sandworm attacks against roughly 30 Polish energy sites—targeted a smaller CHP facility supplying heat to approximately 50,000 residents.
- **The Novel Attack Chain:**
    1. **Initial Compromise:** Attackers gained internet-level access via an un-secured Fortinet VPN/firewall at a separate wind farm substation.
    2. **Cellular Router Pivot:** From there, they compromised a Teltonika cellular router and used an SSH tunnel to pivot directly into a Distribution System Operator's (DSO) **private APN**.
    3. **APN Misconfiguration:** Due to a lack of proper client isolation within the private mobile network, the attackers were able to scan and talk to devices across completely different facilities.
    4. **PLC Gateway:** They discovered a WAGO PFC200 programmable logic controller at the CHP plant that was exposed via the private APN and still running on **default administrator credentials**.
    5. **OT Sabotage:** Using the WAGO controller as a bridge, the threat actors accessed the plant's SCADA environment, targeted Siemens PLCs (models S7-300, S7-1200, and S7-1500), switched them into "STOP" mode, and locked them out with custom passwords.
- **Impact and Destruction:** The attack successfully forced the shutdown of a steam turbine and a water treatment system, halting the cogeneration process. Although operators quickly restored manual control and prevented heat or power outages to residents, the hackers permanently destroyed the WAGO gateway controller by corrupting its partition table to cover their tracks.
- **Global Warning:** CERT.PL warned that the vulnerable configuration—where private cellular APNs blindly trust connected industrial equipment without strict client isolation—is widely replicated across critical infrastructure networks globally.