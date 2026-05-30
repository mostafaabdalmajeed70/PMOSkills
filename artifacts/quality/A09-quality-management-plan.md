---
artifact_id: A09
name: Quality Management Plan
version: 1.0.0
status: "Definition · Active"
category: Quality
authority: "PMBOK8 Guide §2.7 · Process Groups PG §4.3 · Standard §3 (Quality Principle)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.7 · Plan Quality Management"
required_by_skills:
  - SKL-03-09
created_by_skills:
  - SKL-03-09
file_path: artifacts/quality/A09-quality-management-plan.md
---

# A09 — Quality Management Plan
**Artifact ID:** A09  
**Artifact Name:** Quality Management Plan  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.7 · Process Groups PG §4.3 (Plan Quality Management) · Standard §3 (Quality Principle)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/quality/A09-quality-management-plan.md`

---

## Definition

A09 defines the quality standards applicable to the project, how the team will achieve quality in deliverables and project management processes, and the approach to quality assurance (QA) and quality control (QC). It establishes acceptance criteria, quality metrics, and the audit and inspection schedule.

**PMI Source:** PMBOK8 Guide §2.7 — Delivery Performance Domain; PG §4.3 — Plan Quality Management.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Quality |
| **Type** | Subsidiary plan (component of A06 PM Plan) |
| **Lifecycle** | Created in Planning · Applied in Executing · Monitored in M&C |
| **Baseline?** | Yes — quality standards are baselined at planning approval |
| **Ownership** | Project Manager · Quality Assurance Lead |

---

## Purpose

- Define the quality standards and requirements applicable to project deliverables
- Establish acceptance criteria for all major deliverables
- Define the QA approach (process audits, reviews) and QC approach (inspections, testing)
- Document quality metrics and thresholds
- Assign quality roles and responsibilities
- Specify the cost of quality approach

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Quality Standards | Applicable standards (ISO, industry, organizational) | SKL-03-09 |
| §2 Quality Objectives | Measurable quality goals for this project | SKL-03-09 |
| §3 Deliverable Acceptance Criteria | Pass/fail criteria per major deliverable | SKL-03-09 · SKL-03-03 |
| §4 Quality Metrics | Measurable indicators (defect rate, rework %, test pass rate) | SKL-03-09 |
| §5 Quality Assurance Approach | Process audits, peer reviews, gate reviews | SKL-03-09 |
| §6 Quality Control Approach | Inspections, testing, sampling, checklists | SKL-03-09 |
| §7 Cost of Quality | Cost of conformance vs. non-conformance estimate | SKL-03-09 |
| §8 Quality Roles and Responsibilities | QA/QC owner, reviewers, approvers | SKL-03-09 |
| §9 Non-Conformance Process | How defects and failures are tracked and resolved | SKL-03-09 |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Applicable standards | Named standards (ISO 9001, industry standard, org standard) | Mandatory |
| Acceptance criteria | Pass/fail criteria per major deliverable | Mandatory |
| Quality metrics | ≦2 measurable metrics with thresholds | Mandatory |
| QA approach | At least one QA activity type defined | Mandatory |
| QC approach | At least one QC activity type defined | Mandatory |
| Quality roles | Named QA/QC owners | Mandatory |
| Non-conformance process | Process for handling failures and defects | Mandatory |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A04 — Project Charter | SKL-02-01 | Scope, objectives, success criteria |
| A05 — Context Register | SKL-01-02 | Org quality standards, OPA quality templates |
| A08 — Scope Documentation | SKL-03-03 | Deliverables list and requirements |
| A13 — Requirements Traceability Matrix | SKL-03-03 | Requirements linked to acceptance criteria |
| Stakeholder requirements | A07 | Quality expectations from key stakeholders |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Quality standards and acceptance criteria | SKL-04-01 · SKL-05-01 |
| Quality metrics | A17 (Performance Report §5 Quality) |
| QA/QC schedule | A06 PM Plan (integrated schedule) |
| Non-conformance process | A18 (Issue Log) |

---

## Quality Criteria

- Acceptance criteria defined for every major deliverable before execution begins
- Quality metrics are measurable with defined thresholds (not vague targets)
- Both QA (process) and QC (product) activities are planned
- Cost of quality estimated and documented
- A09 reviewed and updated at each phase gate

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A06 — PM Plan | A09 is a subsidiary plan of A06 |
| A08 — Scope Documentation | Deliverables list is input to acceptance criteria |
| A13 — RTM | Requirements ↔ acceptance criteria traceability |
| A17 — Performance Report | Quality metrics reported in §5 |
| A18 — Issue Log | Non-conformances tracked as issues |
| A21 — Lessons Learned | Quality failures and improvements archived |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.7 | Delivery Performance Domain — quality |
| Process Groups PG §4.3 | Plan Quality Management — inputs, tools, outputs |
| PMBOK8 Standard §3 | Quality principle — build quality in, don’t inspect it in |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 2 | Initial definition — Phase B1 |

---

*Owner: Project Manager · Quality Lead*  
*Change Control: Quality standard changes require PM + Sponsor (T2 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 2*
