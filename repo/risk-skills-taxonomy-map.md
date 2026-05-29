# Risk Skills Taxonomy Map

**Purpose:** Provide a repo-ready crosswalk for the four risk-management skills aligned to PMBOK8 and the repository artifact model.

**Authority order:** PMBOK8, PMI companion guides, repository artifact model.

## Scope

This map covers the current risk-management skill chain:
- SKL-03-11 — Perform Risk Analysis
- SKL-03-12 — Plan Risk Responses
- SKL-04-01 — Implement Risk Responses
- SKL-05-01 — Monitor Risks

## Taxonomy Table

| Skill | Canonical purpose | PMBOK8 anchor | Supporting PMI sources | Primary artifacts | Main roles | Main outputs | Loop / handoff |
|---|---|---|---|---|---|---|---|
| **SKL-03-11 — Perform Risk Analysis** | Analyze identified risks iteratively to understand probability, impact, timing, exposure, and where justified overall effects. | Risk Performance Domain, Perform Risk Analysis in §2.7.2 Processes | Risk-PPP §4.4, §4.5; Process-Groups quantitative-analysis guidance where applicable | **A19 Risk Management Record**; **A20 Quantitative Risk and Reserve Decision Record** when quantitative decision support is required | Project manager, risk owner, SMEs, analysts | Updated risk assessments, prioritization, quantified exposure insight when justified | Feeds SKL-03-12 |
| **SKL-03-12 — Plan Risk Responses** | Select and agree suitable responses for threats and opportunities, assign owners, define triggers, and integrate actions into plans. | Plan Risk Responses, Figure 2-51 | Risk-PPP §4.6; Process-Groups §5.22 | **A19 Risk Management Record**; **A12 Change and Exception Decision Log**; **A16 Financial Management and Cost Baseline Record** | Risk owner, response owner, project manager, sponsor or delegated authority | Agreed response strategies, triggers, contingency or fallback plans, reserve implications, decision requests | Feeds SKL-04-01 |
| **SKL-04-01 — Implement Risk Responses** | Execute agreed responses, mobilize response owners, activate contingent actions when triggers occur, and convert realized risks into active issue control. | §2.7.2.5, Figure 2-52 | Risk-PPP §4.7, §7.2.5 | **A19 Risk Management Record**; **A18 Issue, Impediment, and Action Log**; **A12 Change and Exception Decision Log**; **A16 Financial Management and Cost Baseline Record** | Risk owner, risk response owner, project manager, sponsor / governing authority | Executed actions, issue conversion, reserve-use traceability, secondary-risk capture, monitoring handoff | Feeds SKL-05-01 |
| **SKL-05-01 — Monitor Risks** | Track identified risks, monitor trigger conditions and response effectiveness, detect emergent, secondary, and residual risks, and improve the risk process itself. | §2.7.2.6, Figure 2-53 | Risk-PPP §4.8, Figure 4-5, §7.2.6; Process-Groups §7.10 | **A19 Risk Management Record**; **A18 Issue, Impediment, and Action Log**; **A12 Change and Exception Decision Log**; **A16 Financial Management and Cost Baseline Record**; lessons learned records | Risk owner, project manager, response owner, team and functional leads, sponsor for escalations | Work performance information, updated risk and issue records, escalation or change decisions, reserve sufficiency findings, audit and lessons learned outputs | Loops back to SKL-03-11, SKL-03-12, or SKL-04-01 |

## Artifact Relationship Model

- **A19 Risk Management Record** is the central control artifact across all four skills.
- **A18 Issue, Impediment, and Action Log** becomes active when a risk event occurs and requires issue control.
- **A12 Change and Exception Decision Log** captures material change decisions, exceptions, escalations, and governance actions.
- **A16 Financial Management and Cost Baseline Record** supports reserve planning, reserve usage traceability, and monitoring of adequacy.
- **A20 Quantitative Risk and Reserve Decision Record** is optional and used when quantitative analysis materially supports a decision.

## Lifecycle Logic

The intended control flow is:
1. Analyze risks.
2. Plan responses.
3. Implement approved responses.
4. Monitor effectiveness and changed exposure.
5. Loop back into analysis, response planning, or further implementation when monitoring reveals changed, emergent, secondary, or residual risk.

## Naming Standard

Use these canonical repository names:
- **SKL-03-11 — Perform Risk Analysis**
- **SKL-03-12 — Plan Risk Responses**
- **SKL-04-01 — Implement Risk Responses**
- **SKL-05-01 — Monitor Risks**

Retained alias:
- **SKL-05 — Monitor Risk** (acceptable shorthand, but not the preferred canonical title)

## Reuse Notes

This file is designed for direct inclusion in a Skills repository, knowledge-base index, or MCP/agent documentation set. It can also serve as the source table for README navigation or a risk-domain landing page.
