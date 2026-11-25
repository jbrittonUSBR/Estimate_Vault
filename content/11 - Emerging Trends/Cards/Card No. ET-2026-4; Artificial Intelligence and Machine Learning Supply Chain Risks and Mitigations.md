---
title: "Artificial Intelligence and Machine Learning Supply Chain Risks and Mitigations"
card: "ET-2026-4"
author: "Australian Signals Directorate (ASD)"
outlet: "HSIN"
published: 2026-04-03
url: "https://media.defense.gov/2026/Mar/04/2003882809/-1/-1/0/AI_ML_SUPPLY_CHAIN_RISKS_AND_MITIGATIONS.PDF"
query: ""
imported: 2026-04-03
type: news-card

KIQ: []
---
(U) Australian Signals Directorate (ASD). "Artificial intelligence and machine learning Supply chain risks and mitigations." 2025. [Artificial intelligence and machine learning Supply chain risks and mitigations](https://media.defense.gov/2026/Mar/04/2003882809/-1/-1/0/AI_ML_SUPPLY_CHAIN_RISKS_AND_MITIGATIONS.PDF) Accessed April 3, 2026. 

(U) The National Security Agency (NSA), alongside several international cyber organizations, has released a publication intended for organizations and staff that deploy or develop artificial intelligence (AI) and machine learning (ML) systems and components. The guidance provides broad mitigation advice, highlighting aspects unique to AI and ML, as well as resources for organizations looking to apply their own, tailored protective measures.

(U) Executive Summary: This guidance addresses AI and ML supply chain risks and mitigations for organizations deploying or developing AI and ML systems. It highlights the importance of securing the supply chain, which includes components like training data, models, software, infrastructure, hardware, and third-party services. The purpose is to inform questions and requirements for vendors when sourcing third-party AI and ML systems, and to guide in-house development by addressing key risks and mitigations based on risk assessments.

(U) Main risks include: low-quality or biased data leading to ineffective models; data poisoning causing degraded performance or malicious responses; training data exposure through model inversion or extraction, risking privacy; model serialization attacks embedding malicious code; model poisoning via availability, targeted, or backdoor methods; stego-malware hiding in models; evasion attacks on ML-based security; vulnerabilities in AI software libraries from typo-squatting or deserialization; infrastructure/hardware risks from drivers and protocols; and third-party service vulnerabilities from poor hygiene or shared resources. These can compromise confidentiality, availability, and integrity, exposing data, degrading functionality, or executing code.

(U) Key mitigations recommended: use trusted sources and verification methods like checksums for data and models; quarantine and test external data; preprocess and sanitize data to reduce bias and poisoning; employ ensemble methods for consistency checks; obfuscate sensitive data with anonymization; validate models with secure formats, performance testing, explainability, and adversarial training; maintain AIBOMs/SBOMs for transparency; monitor inputs/outputs; refine models to disrupt malware; scan software and audit components; secure infrastructure with signed drivers and segmentation; assess third-party vendors thoroughly, include security in contracts, and define shared responsibilities. Organizations should integrate AI/ML into broader cyber supply chain management, conduct assessments, threat modelling, and maintain incident response plans.

(U) Overall conclusions: AI and ML introduce distinct challenges like poisoned data and backdoors, but adopting secure practices reduces the attack surface and enhances resilience when combined with defense-in-depth strategies.

(U) Key Judgments: No dedicated â€œKey Judgments,â€ â€œKey Findings,â€ or â€œKey Takeawaysâ€ section exists in the document. The following represent the most critical judgments and findings drawn directly from the text (with section references):

- Data poisoning is a prevalent threat, with adversarial actors already modifying AI training data, leading to degraded performance, bias, or malicious responses.
- Training data exposure risks privacy through attacks like model inversion and membership inference, even post-model training.
- Model poisoning, including backdoors, can embed hidden triggers causing abnormal behavior while maintaining normal performance.
- Serialized ML models are vulnerable to attacks embedding malicious code, as demonstrated by uploads to sharing platforms in 2025.
- Evasion attacks allow malicious inputs to bypass ML-based security mechanisms, requiring resilience in model design.
- AI software dependencies increase attack surface, with vulnerabilities in libraries enabling deserialization attacks or malware installation.
- Third-party services introduce risks from shared resources or incidents, potentially compromising customer systems due to ambiguous responsibilities.
- Organizations must maintain AIBOMs/SBOMs and verify components to ensure supply chain integrity throughout the lifecycle.
- Preventative measures like data sanitization and model verification are more effective than detection for mitigating data and model risks.
- Integrating AI/ML requires ongoing risk assessments, threat modelling, and vendor due diligence to address unique threats.

(U) Document Metadata: 
- **Title**: Artificial Intelligence and Machine Learning Supply Chain Risks and Mitigations  
- **Issuing Organisations**: Commonwealth of Australia (cyber.gov.au) in collaboration with the Canadian Centre for Cyber Security, Singapore Cyber Security Agency, Republic of Korea National Intelligence Service, Japan National Cyber Security Office, New Zealand National Cyber Security Centre, United Kingdom National Cyber Security Centre, and United States National Security Agency (NSA)  
- **Publication Date**: 2025  

(U) This document is publicly available via the provided link on the U.S. Department of Defense media site. It includes case studies of real-world incidents (e.g., 2025 data poisoning and leaks) and references established frameworks such as the NIST AI Risk Management Framework and MITRE ATLAS.