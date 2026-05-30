---
artifact_id: A05
name: Context Register (EEF / OPA)
version: 1.0.0
status: "Definition · Active"
category: Governance
authority: "PMBOK8 Guide §2.1.3–2.1.4 · Standard §3 (Stewardship, Systems Thinking)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.1.3–2.1.4"
required_by_skills:
  - SKL-01-02
  - SKL-02-01
  - SKL-03-01
  - SKL-06-03
created_by_skills:
  - SKL-01-02
file_path: artifacts/governance/A05-context-register-eef-opa.md
---

# A05 — Context Register (EEF / OPA)
**Artifact ID:** A05  
**Artifact Name:** Context Register — Enterprise Environmental Factors and Organizational Process Assets  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.1.3–2.1.4 · Standard §3 (Stewardship · Systems Thinking)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/governance/A05-context-register-eef-opa.md`

---

## Definition

A05 is the project-level record of Enterprise Environmental Factors (EEF) and Organizational Process Assets (OPA) that influence, constrain, or enable the project. EEFs are external or internal conditions not under the project team's control. OPAs are organizational plans, processes, policies, procedures, and knowledge bases. Together they form the contextual operating environment for all project decisions.

**PMI Source:** PMBOK8 Guide §2.1.3 (Enterprise Environmental Factors) and §2.1.4 (Organizational Process Assets).

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Governance |
| **Type** | Context and constraints reference record |
| **Lifecycle** | Initiated in Org Setup (SKL-01-02) · Updated at each phase gate · Outputs feed into Lessons Learned (A21) |
| **Baseline?** | No — living reference record |
| **Ownership** | PMO / Project Manager |

---

## Purpose

- Document all internal and external conditions that constrain or enable the project
- Capture organizational policies, processes, templates, and historical data available to the team
- Provide the authoritative context input to planning, risk, communications, and procurement
- Enable consistent decision-making anchored to the project's operating environment
- Ensure project closure outputs (lessons learned, updated processes) are fed back into OPA

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Enterprise Environmental Factors — Internal | Org culture, governance, infrastructure, resource availability, PMIS, commercial databases | SKL-01-02 |
| §2 Enterprise Environmental Factors — External | Market conditions, regulatory environment, industry standards, geopolitical factors, financial market conditions | SKL-01-02 |
| §3 Organizational Process Assets — Processes & Policies | PM methodology, change control procedures, financial controls, quality standards, safety policies | SKL-01-02 |
| §4 Organizational Process Assets — Corporate Knowledge Base | Lessons learned repository, historical project data, process measurement database, templates | SKL-01-02 |
| §5 Project-Specific Constraints | Constraints specific to this project derived from EEF/OPA review | PM / SKL-02-01 |
| §6 OPA Update Log | Record of updates fed back into org knowledge base at closure | SKL-06-03 |

---

## EEF Categories

### Internal EEF

| Factor | Examples |
|---|---|
| Organizational culture and structure | PMO model, governance style, decision-making norms |
| Governance framework | Policies, authority thresholds, board structure |
| Infrastructure | Facilities, equipment, IT systems, PMIS tools |
| Resource capability | Skills inventory, availability calendars, capacity constraints |
| Stakeholder risk tolerance | Organizational appetite for risk and uncertainty |
| PMIS and data systems | Project management information systems available |

### External EEF

| Factor | Examples |
|---|---|
| Marketplace conditions | Competition, supply chain, vendor market conditions |
| Legal and regulatory requirements | Laws, regulations, industry standards, permits |
| Social and political factors | Community expectations, political stability, ESG requirements |
| Financial market conditions | Interest rates, exchange rates, inflation |
| Physical / environmental factors | Climate, geography, sustainability requirements |

---

## OPA Categories

### Processes, Policies, and Procedures

| OPA Type | Examples |
|---|---|
| Standard PM methodology | Lifecycle models, process frameworks, phase gate criteria |
| Change control procedures | Change request forms, CCB charter, escalation thresholds |
| Financial controls | Budget approval thresholds, procurement authority, audit requirements |
| Quality standards | QA/QC procedures, acceptance criteria norms, testing standards |
| Safety and compliance | HSE policies, regulatory compliance checklists |
| HR policies | Hiring procedures, performance management, training requirements |

### Corporate Knowledge Base

| Knowledge Type | Examples |
|---|---|
| Lessons learned repository | Historical LL entries by project type, phase, domain |
| Process measurement database | Historical estimates, velocity data, defect rates |
| Issue and risk databases | Historical risk registers, issue resolution records |
| Project files | Previous project plans, charters, closure reports |
| Financial databases | Historical cost data, actuals, budget variance records |
| Templates and standards | Standard forms, templates, checklists (feeds A06, A19, A07) |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| EEF Internal summary | Key internal conditions relevant to this project | Mandatory |
| EEF External summary | Key external conditions and constraints | Mandatory |
| OPA Processes & Policies | Relevant organizational standards and procedures | Mandatory |
| OPA Knowledge Base | Historical data, templates, LL entries relevant to this project | Mandatory |
| Project-Specific Constraints | Derived constraints from EEF/OPA review | Mandatory |
| OPA Update Log | Updated at closure with lessons and process improvements | Required at Closing |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| Organizational governance documents | PMO / Legal | Policies, standards, procedures |
| Historical project records | PMO Knowledge Base | Lessons learned, historical estimates |
| Regulatory and legal requirements | Legal / Compliance | Applicable regulations |
| Market and industry data | External sources | Benchmarks, standards, surveys |
| PMIS system documentation | IT / PMO | Available tools and capabilities |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Project constraints and assumptions | A04 (Charter) · A06 (PM Plan) |
| Risk context for risk planning | A19 (Risk Register) |
| Historical estimates for planning | A15 (Schedule) · A16 (Budget) |
| Template and standard library reference | All artifact definitions |
| OPA updates at closure | SKL-06-03 · Organizational knowledge base |

---

## Scope Boundaries

| In Scope | Out of Scope |
|---|---|
| Project-level EEF and OPA documentation | Organization-wide EEF/OPA management (PMO responsibility) |
| Constraints derived from EEF/OPA for this project | Process improvement across the organization |
| OPA update log at project close | Creating new organizational policies |

---

## Quality Criteria

- EEF and OPA documented before planning begins
- Internal and external EEF both addressed — not just one category
- OPA knowledge base queried for historical data before estimating
- Project-specific constraints derived and explicitly documented
- A05 reviewed and updated at each phase gate
- OPA Update Log populated at project closure (SKL-06-03) with new lessons and improved processes

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A01 — Business Case | EEF/OPA feed business case assumptions and cost basis |
| A04 — Project Charter | EEF/OPA inform charter constraints and PM authority level |
| A06 — PM Plan | Planning constrained by EEF/OPA |
| A07 — Stakeholder Register | Org culture (EEF) shapes stakeholder engagement approach |
| A19 — Risk Register | EEF/OPA are primary input to risk identification |
| A21 — Lessons Learned | A21 outputs feed back into OPA knowledge base |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.1.3 | Enterprise Environmental Factors — internal and external |
| PMBOK8 Guide §2.1.4 | Organizational Process Assets — processes, policies, knowledge base |
| PMBOK8 Standard §3 | Stewardship — responsible use of org resources and constraints |
| PMBOK8 Standard §3 | Systems Thinking — project as part of larger organizational system |
| Process Groups PG §3.1 | EEF/OPA as standard inputs to all process groups |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 1 | Initial definition — Phase B1 |

---

*Owner: PMO / Project Manager*  
*Change Control: EEF updates are informational; OPA changes require PMO authorization (T2 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 1*
