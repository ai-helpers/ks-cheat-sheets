# 5 values-based Principles for trustworthy, human-centric AI

## Table of Contents (ToC)

- [Table of Contents (ToC)](#table-of-contents-toc)
- [Six Responsible AI Principles](#six-responsible-ai-principles)
  - [Privacy \& Security](#privacy--security)
  - [Inclusiveness](#inclusiveness)
  - [Fairness](#fairness)
  - [Transparency](#transparency)
  - [Books](#books)
    - [Python modules - Github](#python-modules---github)
    - [Teams](#teams)
  - [Reliability, Safety \& Robustness](#reliability-safety--robustness)
    - [Python modules](#python-modules)
  - [Accountability](#accountability)
- [References](#references)

## Six Responsible AI Principles

### Privacy & Security

Privacy and security entail whether an AI system protects individuals' personal data and prevents
unauthorised access, manipulation, or misuse. This spans data collection, storage, and usage
practices, as well as cybersecurity safeguards across the AI lifecycle. Organisations must ensure
their usage of AI tools or systems complies with data protection laws.

Example governance risks:

- Regulatory penalties: Mishandling personal data can trigger formal investigations, audits and
substantial fines, under both Hong Kong law and in other jurisdictions.41
- System compromise: Insecure AI models and infrastructure are targets for adversarial attacks,
hacks, data breaches, and model inversion techniques.42
- Reputational loss: Perceived misuse, leakage, or unauthorised use of user data can erode
public trust and damage stakeholder relationships.

### Inclusiveness

Inclusiveness asks whether AI systems are accessible, usable and beneficial across demographic,
linguistic, cultural and disability dimensions, and whether they avoid creating new digital divides.

Example governance risks:

- Market share loss: If products don't work in minority languages, fail to cater to disability
needs, exclude certain demographics by design, or underperform in certain markets.
- Monolingual bias: Over-reliance on English training data can degrade performance for
Cantonese and Putonghua users.
- Regulatory non-compliance: May contravene ESG-related standards, such as those found in
HKEX's Corporate Governance Code.43
- Innovation blind spots: May overlook use cases, risks, or opportunities relevant to broader
populations.

### Fairness

Fairness asks whether an AI system treats individuals without discrimination and avoids unjustified
disparate impact across protected or vulnerable groups. In practice, this covers training data
representativeness, model design choices, and outcome monitoring.

Example governance risks:

- Legal exposure: Algorithmic discrimination can lead to liability issues under Hong Kong's anti-discrimination ordinances and infringe on the right to equality protected under Article 25 of the Basic Law or the HK Bill of Rights.
- Reputational licence: Perceived injustice can trigger media backlashes, activist litigation
and regulator intervention.
- Capital allocation: Using AI models can potentially distort credit, hiring or pricing
decisions, embedding systemic bias in business outcomes.

### Transparency

Transparency covers both model explainability (stakeholders can understand how outputs were
produced), and organisational disclosure (being open about AI usage, limitations and governance).
This includes internal traceability, user-facing explanations, documentation of design choices, and
openness about limitations and risks.44

Example governance risks:

- Litigation exposure if decisions cannot be explained to regulators or the Court. Many
jurisdictions increasingly require data transparency and model explainability in high-risk
domains; non-compliance can result in sanctions, service rollbacks, or product bans.45
- Consumer confidence: Knowing whether and how AI technologies are used will enable
consumers to make informed decisions, ensure trust, and prevent backlash. Consumers may
reject products and services if they cannot understand their outputs or challenge their
decisions.
- Accountability gaps: The intrinsic opaqueness of AI models means that they can be hard to
debug, especially if key technical staff leave. This can make it difficult to identify root causes of
errors or harms, hindering redress and oversight.

### Books

- [Interpretable ML Book](https://christophm.github.io/interpretable-ml-book/)

#### Python modules - Github

- [Github - shap](https://github.com/shap/shap)
- [Github - Shapash](https://github.com/MAIF/shapash)
  - [Documentation](https://maif.github.io/shapash/)
- [Github - shapiq: Shapley Interactions for Machine Learning](https://github.com/mmschlk/shapiq)
  - [Arxiv](https://arxiv.org/pdf/2410.01649)
- [Github - LIME](https://github.com/marcotcr/lime)
- [Github - MLI resources](https://github.com/h2oai/mli-resources/tree/master)
- [Github - Skope Rules](https://github.com/scikit-learn-contrib/skope-rules)
- [Github - Eli5](https://github.com/eli5-org/eli5)
- [Github - AIX360](https://github.com/Trusted-AI/AIX360)
- [Github - InterpretML](https://github.com/interpretml/interpret)
- [Doc - ModEva](https://modeva.ai/_build/html/index.html)

#### Teams

- [TADJ](https://lnkd.in/eecHfhdc)
- [Explicon](https://lnkd.in/egrDzTk9)

### Reliability, Safety & Robustness

Reliability and safety entail whether an AI system performs as intended under expected and
unexpected conditions, while avoiding harm and unintended side effects. This covers issues of
technical robustness, fault tolerance, risk containment, and safe deployment across diverse
environments and user contexts.

Example governance risks:

- Operational disruption: Unreliable models can hallucinate, drift, malfunction, or fail
under stress, leading to system downtime, service degradation, or cascading failures.38
- Legal exposure: Unsafe AI systems may breach product liability or duty-of-care obligations or
consumer protection statutes.39
- Trust erosion: Safety failures, especially in high-stakes use cases, can undermine user
trust, investor confidence, and long-term adoption.40

#### Python modules

- [Reliability - PiML](https://selfexplainml.github.io/PiML-Toolbox/_build/html/guides/testing/reliability.html)
- [Github - MAPIE](https://github.com/scikit-learn-contrib/MAPIE)

### Accountability

Accountability ensures that clear ownership, oversight, and redress mechanisms are in place for
the design, deployment, and impact of AI systems. In other words, that identifiable humans, and
ultimately the board, remain answerable for AI-generated outcomes, with clear mechanisms to
trace responsibilities, remedy harms, and learn from incidents. It includes assigning responsibility
across functions, tracking decisions, and ensuring consequences for misuse or failure.

Example governance risks:

- Incident under-reporting and ethical drift: If escalation routes are unclear, this can amplify
harm and delay remediation. Lack of accountability can lead to unmonitored deployment,
scope creep, or misalignment with organisational values.46
- Vendor risk transfer: If relying on external models without contractual recourse, residual
liabilities may land on the organisation for unanticipated failures.47
- Organisational blind spots: When no one owns AI outcomes end-to-end, risks can fall between
the cracks and go unaddressed.

## References

- [OECD]()
  - [OECD Working Party on Artificial Intelligence Governance (AIGO)](https://oecd.ai/en/network-of-experts)
  - [Inclusive growth, sustainable development and well-being (Principle 1.1)](https://oecd.ai/en/dashboards/ai-principles/P5)
  - [Respect for the rule of law, human rights and democratic values, including fairness and privacy (Principle 1.2)](https://oecd.ai/en/dashboards/ai-principles/P6)
  - [Transparency and explainability (Principle 1.3)](https://oecd.ai/en/dashboards/ai-principles/P7)
  - [Robustness, security and safety (Principle 1.4)](https://oecd.ai/en/dashboards/ai-principles/P8)
  - [Accountability (Principle 1.5)](https://oecd.ai/en/dashboards/ai-principles/P9)
- [Github - TrustyAI examples](https://github.com/trustyai-explainability/trustyai-explainability-python-examples/tree/main)
