---
title: "OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat"
card: ET-2026-25
author: Shresta Bellary Seetharam, Nabeel Mohamed, Billy Melicher, Oleksii Starov
outlet: Unit 42
published: 2026-06-23
url: https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
query: ""
imported: 2026-06-23
type: news-card

KIQ: []
---
(U) Shresta Bellary Seetharam, Nabeel Mohamed, Billy Melicher, Oleksii Starov. "OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat." Unit 42, June 23, 2026. https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/. Accessed June 25, 2026.

![[RETT 2026.1]]
![[RETT 2026.2]]

(U) OpenClaw, an AI agent platform, relies on a third-party skill marketplace called ClawHub where markdown-driven packages execute with broad local system access, creating a new attack vector in the AI software supply chain that malicious actors have rapidly exploited. In early 2026, researchers identified hundreds of malicious skills—including infostealers like Atomic macOS Stealer delivered via Base64-encoded droppers, evasion techniques such as file padding to bypass scanners, and novel agentic abuses like affiliate link injection and Solana meme token front-running—with initial analyses showing roughly 17% of skills carrying malicious payloads. Although ClawHub implemented screening tools like VirusTotal and its own ClawScan, evolving threats continued to slip through until reported and removed, prompting OpenClaw to partner with NVIDIA for enhanced analysis. The incidents highlight how AI agents can semantically hijack natural language instructions to gain unauthorized control over systems, differing from traditional supply chain attacks by leveraging agent authority rather than code exploits. Security experts recommend rigorous provenance verification, line-by-line code reviews, and behavioral monitoring for organizations adopting such AI tools to mitigate these emerging risks.
