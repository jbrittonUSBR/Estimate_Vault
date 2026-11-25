---
title: "[0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)"
card: "Ballistic-2026-19"
author: "Seclists.org Staff"
outlet: "Seclists.org"
published: "October 6, 2026"
url: "https://seclists.org/fulldisclosure/2026/Oct/8"
query: "\"Ballistic attack\" OR ((shooting OR sabotage OR attack) AND (transformer OR substation OR \"power line\" OR \"high voltage\"))"
imported: 2026-10-08
type: news-card
KIQ: []
---

(U) Seclists.org Staff. "[0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)." Seclists.org, October 6, 2026. https://seclists.org/fulldisclosure/2026/Oct/8. Accessed October 8, 2026.

# [0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)

[Source](https://seclists.org/fulldisclosure/2026/Oct/8)

(U) Global — Researchers with 0day Rubbish disclosed a failing-open authentication flaw and an un-sandboxed ScalaDTransform code-execution path in StreamSets Transformer 3.17.0 (IBM), with verified remote code execution as root in a container under the deployment-conditional `auth-mode none` state; the advisory details dual CVSS readings (8.1 High / 9.8 Critical) and notes no exploit was demonstrated against shipped defaults.

**Query:** `"Ballistic attack" OR ((shooting OR sabotage OR attack) AND (transformer OR substation OR "power line" OR "high voltage"))`
