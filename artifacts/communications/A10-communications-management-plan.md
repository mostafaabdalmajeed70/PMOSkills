---
artifact_id: A10
name: Communications Management Plan
version: 1.0.0
status: "Definition · Active"
category: Communications
authority: "PMBOK8 Guide §2.5 · Process Groups PG §4.6 · Standard §3 (Stakeholders Principle)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.5 · Plan Communications Management"
required_by_skills:
  - SKL-03-08
  - SKL-04-07
  - SKL-05-09
created_by_skills:
  - SKL-03-08
file_path: artifacts/communications/A10-communications-management-plan.md
---

# A10 — Communications Management Plan
**Artifact ID:** A10  
**Artifact Name:** Communications Management Plan  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.5 · Process Groups PG §4.6 (Plan Communications Management) · Standard §3 (Stakeholders Principle)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/communications/A10-communications-management-plan.md`

---

## Definition

A10 defines the approach, methods, frequency, and responsibilities for all project communications. It translates stakeholder information needs (from A07) into a structured communications matrix that specifies what is communicated, to whom, when, by whom, and through what channel.

**PMI Source:** PMBOK8 Guide §2.5 — Stakeholder Performance Domain; PG §4.6 — Plan Communications Management.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Communications |
| **Type** | Subsidiary plan (component of A06 PM Plan) |
| **Lifecycle** | Created in Planning · Applied in Executing · Monitored in M&C |
| **Baseline?** | Yes — communications plan is baselined; tailored as stakeholder needs change |
| **Ownership** | Project Manager |

---

## Purpose

- Define the information needs of all stakeholders
- Establish a communications matrix mapping who receives what, when, and how
- Define communication formats, channels, and technology
- Assign communication responsibilities
- Establish a feedback and escalation path for communications
- Ensure communications are timely, accurate, and fit for purpose

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Communications Principles | Project communication norms, preferred channels, escalation rules | SKL-03-08 |
| §2 Stakeholder Information Needs | What each stakeholder needs to know, when, and why (from A07) | SKL-03-08 |
| §3 Communications Matrix | Full table: message · audience · frequency · format · channel · owner | SKL-03-08 |
| §4 Communication Technologies | Tools and platforms used (email, PMIS, meetings, dashboards) | SKL-03-08 |
| §5 Escalation Path | Communication escalation trigger and routing | SKL-03-08 |
| §6 Meeting Management | Standard meeting types, cadence, facilitation rules | SKL-03-08 |
| §7 Communication Monitoring | How communications effectiveness is assessed | SKL-05-09 |

---

## Communications Matrix Schema (§3)

| Field | Description |
|---|---|
| Communication ID | COMM-NNN |
| Message / Report | What is being communicated |
| Purpose | Why this communication is needed |
| Audience | Recipient(s) (link to A07 Stakeholder ID) |
| Frequency | Daily / Weekly / Monthly / At milestone / Ad hoc |
| Format | Report / Dashboard / Email / Presentation / Meeting |
| Channel | Email / PMIS / Video call / Physical meeting / Portal |
| Owner | Person responsible for producing and distributing |
| Feedback Mechanism | How recipients respond or confirm receipt |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Communications matrix | At least one entry per key stakeholder group | Mandatory |
| Communication channels | Named tools/platforms | Mandatory |
| Owners per communication | Named person per communication row | Mandatory |
| Escalation path | Defined trigger and routing | Mandatory |
| Stakeholder linkage | A07 stakeholder IDs referenced | Mandatory |
| Monitoring approach | At least one method to assess effectiveness | Recommended |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A07 — Stakeholder Register (SEAM) | SKL-02-02 · SKL-03-07 | Information needs and engagement strategies |
| A04 — Project Charter | SKL-02-01 | Sponsor and key stakeholder identification |
| A05 — Context Register | SKL-01-02 | Communication tools and org standards |
| A06 — PM Plan | SKL-03-01 | Project lifecycle — shapes communication frequency |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Communications matrix | A28 (Comms Record) · SKL-04-07 |
| Meeting schedule | A06 PM Plan |
| Communication monitoring criteria | SKL-05-09 |

---

## Quality Criteria

- Every key stakeholder in A07 has ≥1 communication entry in the matrix
- Owners are named (not left as "PM" generically)
- Communication frequency matches stakeholder engagement needs
- Escalation path is defined with a clear trigger condition
- A10 reviewed and updated when stakeholder register changes materially

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A06 — PM Plan | A10 is a subsidiary plan of A06 |
| A07 — Stakeholder Register | Stakeholder information needs drive communications matrix |
| A28 — Communications Record | A10 is the plan; A28 is the execution log |
| A29 — Meeting Records | Meeting management §6 governs A29 |
| A17 — Performance Report | A10 defines how A17 is distributed |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.5 | Stakeholder Performance Domain — communications |
| Process Groups PG §4.6 | Plan Communications Management |
| PMBOK8 Standard §3 | Engage stakeholders principle |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 2 | Initial definition — Phase B1 |

---

*Owner: Project Manager*  
*Change Control: Changes to communications plan require PM authorization (T1–T2 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 2*
