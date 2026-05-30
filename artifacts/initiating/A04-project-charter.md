---
artifact_id: A04
name: Project Charter
version: 1.0.0
status: "Definition · Active"
category: Initiating
authority: "PMBOK8 Guide §2.1 · Process Groups Practice Guide §3.1 · Standard §3 (Stewardship)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.1 · Figure 2-2"
required_by_skills:
  - SKL-02-01
  - SKL-03-01
  - SKL-07-01
created_by_skills:
  - SKL-02-01
file_path: artifacts/initiating/A04-project-charter.md
---

# A04 — Project Charter
**Artifact ID:** A04  
**Artifact Name:** Project Charter  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.1 · Process Groups Practice Guide §3.1 · Standard §3 (Stewardship Principle)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/initiating/A04-project-charter.md`

---

## Definition

A04 is the document that formally authorizes a project or phase and grants the project manager the authority to apply organizational resources. It is the first formal artifact created, produced in SKL-02-01 (Initiate Project or Phase), and serves as the foundational input to all subsequent planning, execution, and governance activities.

**PMI Source:** PMBOK8 Guide §2.1 — Project Management Processes; Process Groups Practice Guide §3.1 — Develop Project Charter.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Initiating |
| **Type** | Formal authorization document |
| **Lifecycle** | Created in Initiating · Referenced throughout all phases · Closed in Closing |
| **Baseline?** | No — but changes require sponsor authorization |
| **Ownership** | Sponsor (authorizes) · Project Manager (drafts) |

---

## Purpose

- Formally authorize the project or phase to begin
- Grant the project manager authority to use organizational resources
- Establish the project's purpose, objectives, and constraints at a high level
- Link the project to the business case (A01) and strategic objectives
- Provide the first high-level identification of stakeholders, risks, and assumptions
- Serve as the single authoritative reference for project scope boundaries throughout the lifecycle

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Project Identification | Project name, ID, sponsor, PM, date | SKL-02-01 |
| §2 Purpose and Justification | Why the project is being undertaken; link to business case | SKL-02-01 |
| §3 Objectives | SMART objectives with measurable success criteria | SKL-02-01 |
| §4 High-Level Scope | What is in scope and out of scope at initiation | SKL-02-01 |
| §5 High-Level Risks | Initial risk statement (refined in A19) | SKL-02-01 |
| §6 High-Level Schedule Milestones | Key milestones and target dates | SKL-02-01 |
| §7 High-Level Budget | Approved funding range or estimate | SKL-02-01 |
| §8 Stakeholder List | Initial key stakeholders (refined in A07) | SKL-02-01 |
| §9 Assumptions and Constraints | Assumptions on which the project is predicated | SKL-02-01 |
| §10 Project Manager Authority | Explicit authority level granted to PM | SKL-02-01 |
| §11 Approval and Signatures | Sponsor sign-off; formal authorization | SKL-02-01 |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Project Name | Official project title | Mandatory |
| Project ID | Unique identifier (format: PROJ-NNN) | Mandatory |
| Sponsor | Name and role of authorizing sponsor | Mandatory |
| Project Manager | Assigned PM name and contact | Mandatory |
| Authorization Date | Date charter was signed | Mandatory |
| Purpose Statement | 2–3 sentences on why the project exists | Mandatory |
| Objectives | ≥1 SMART objective with measurable criteria | Mandatory |
| High-Level Scope | In/out scope boundary statement | Mandatory |
| High-Level Budget | Approved or estimated funding envelope | Mandatory |
| Approval Signatures | Sponsor + PM | Mandatory |
| Business Case Reference | Link or reference to A01 | Mandatory if A01 exists |
| Assumptions | ≥1 assumption documented | Recommended |
| Initial Risks | ≥1 high-level risk identified | Recommended |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A01 — Business Case | Pre-authorization / Sponsor | Justification and strategic alignment |
| A05 — Context Register (EEF/OPA) | SKL-01-02 | Org standards, historical information |
| A02 — Benefits Record | Sponsor / Portfolio | Benefit metrics to be achieved |
| Expert judgment | Sponsor, PMO, PM | Authority and resource constraints |
| Agreements / Contracts | Legal / Procurement | If project is externally initiated |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Formal project authorization | All subsequent skills and artifacts |
| PM authority level | A06 (PM Plan) · AUTHORITY-ROUTING.md |
| Initial stakeholder list | A07 (Stakeholder Register) |
| Initial risk statement | A19 (Risk Register) |
| Scope boundaries | A08 (Scope) |
| Success criteria | A17 (Performance Report) · A27 (Closure) |

---

## Scope Boundaries

| In Scope | Out of Scope |
|---|---|
| High-level project authorization | Detailed scope definition (see A08) |
| SMART objectives at initiation level | Detailed WBS or deliverable breakdown (see A14) |
| Initial stakeholder identification | Full stakeholder analysis and SEAM (see A07) |
| Initial risk identification | Quantitative risk analysis (see A19) |
| Funding authorization | Detailed budget (see A16) |

---

## Quality Criteria

- Charter is signed by an authorized sponsor before any project work begins
- All mandatory fields populated — no blank or TBD objectives
- Objectives are SMART and measurable — generic statements are not acceptable
- Charter references A01 Business Case or provides standalone justification
- PM authority level is explicit — ambiguous authority is a governance risk
- High-level scope boundaries prevent scope creep from day one
- Charter reviewed and re-confirmed at each phase gate

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A01 — Business Case | Charter is authorized by and linked to A01 |
| A05 — Context Register | EEF/OPA inform charter constraints and standards |
| A06 — PM Plan | Charter is primary input to integrated PM plan |
| A07 — Stakeholder Register | Initial stakeholder list from charter §8 |
| A08 — Scope Documentation | Charter scope statement seeds A08 |
| A19 — Risk Register | Charter initial risks seed A19 |
| A27 — Closure Record | Charter objectives used to confirm project completion |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.1 | Project Management Processes — Initiating |
| Process Groups PG §3.1 | Develop Project Charter — inputs, tools, outputs |
| PMBOK8 Standard §3 | Stewardship principle — fiduciary authority |
| PMI Lexicon | "Project Charter" — formal document authorizing project |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 1 | Initial definition — Phase B1 |

---

*Owner: Sponsor (authorizes) · Project Manager (maintains)*  
*Change Control: Charter changes require sponsor authorization (T2–T3 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 1*
