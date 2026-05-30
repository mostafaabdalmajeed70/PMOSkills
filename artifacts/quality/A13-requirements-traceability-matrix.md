---
artifact_id: A13
name: Requirements Traceability Matrix
version: 1.0.0
status: "Definition · Active"
category: Quality
authority: "PMBOK8 Guide §2.7 · Process Groups PG §4.2 · PMI Guide to Business Analysis §5"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.7 · Collect Requirements (outputs)"
required_by_skills:
  - SKL-03-03
  - SKL-03-09
  - SKL-05-03
created_by_skills:
  - SKL-03-03
file_path: artifacts/quality/A13-requirements-traceability-matrix.md
---

# A13 — Requirements Traceability Matrix
**Artifact ID:** A13  
**Artifact Name:** Requirements Traceability Matrix (RTM)  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.7 · Process Groups PG §4.2 (Collect Requirements) · PMI Guide to Business Analysis §5  
**Source Type:** PMI-derived  
**File Path:** `artifacts/quality/A13-requirements-traceability-matrix.md`

---

## Definition

A13 is the table that links each project requirement to its source (business need or stakeholder), the deliverable(s) that fulfill it, and the test or acceptance criterion that verifies it. It provides end-to-end traceability from strategic objective through requirement to delivered output and verification.

**PMI Source:** PMBOK8 Guide §2.7; PG §4.2 — Collect Requirements (output: Requirements Traceability Matrix); PMI Guide to Business Analysis §5.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Quality |
| **Type** | Traceability and verification record |
| **Lifecycle** | Created in Planning · Updated throughout Executing · Used in M&C (Control Scope) · Verified at Closing |
| **Baseline?** | Requirements baseline is governed; RTM is living |
| **Ownership** | Project Manager · Business Analyst |

---

## Purpose

- Trace every requirement to its originating business need or stakeholder
- Link requirements to the WBS deliverable(s) that fulfill them
- Link requirements to acceptance criteria and test cases
- Detect scope creep by flagging unlinked deliverables or requirements
- Support change impact analysis when requirements change
- Confirm all requirements are met before project closure

---

## RTM Schema

| Field | Description |
|---|---|
| **Req ID** | Unique requirement identifier (format: REQ-NNN) |
| **Requirement Statement** | Clear, unambiguous description of the requirement |
| **Source** | Business need, stakeholder, regulation, or contract clause |
| **Priority** | MoSCoW: Must / Should / Could / Won’t |
| **Category** | Functional / Non-Functional / Regulatory / Constraint |
| **Business Objective** | Strategic objective or benefit this requirement supports |
| **WBS Deliverable** | WBS ID(s) that fulfill this requirement |
| **Acceptance Criteria** | Pass/fail criteria for verification |
| **Test / Verification Method** | Test case ID, inspection, demonstration, or analysis |
| **Status** | Defined / In Development / Delivered / Verified / Accepted |
| **Change Log** | Record of changes to this requirement |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Req ID | Unique, formatted ID | Mandatory |
| Requirement Statement | Unambiguous, testable statement | Mandatory |
| Source | Named stakeholder or document | Mandatory |
| WBS Deliverable link | At least one WBS element linked | Mandatory |
| Acceptance Criteria | Pass/fail statement | Mandatory |
| Status | Current status from defined enum | Mandatory |
| Priority | MoSCoW assignment | Mandatory |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A07 — Stakeholder Register | SKL-02-02 | Stakeholder requirements and expectations |
| A04 — Project Charter | SKL-02-01 | Objectives and high-level scope |
| A08 — Scope Documentation | SKL-03-03 | Deliverables and WBS |
| A09 — Quality Management Plan | SKL-03-09 | Acceptance criteria standards |
| Stakeholder interviews, surveys | SKL-03-03 | Elicited requirements |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Requirements baseline | SKL-05-03 (Control Scope) |
| Acceptance criteria | A09 (Quality Plan) · SKL-05-01 |
| Verification record | A27 (Closure Record §2) |
| Change impact mapping | SKL-05-02 (Change Control) |

---

## Quality Criteria

- Every requirement has a unique ID and unambiguous statement
- Every requirement is traced to a WBS deliverable — untraceable requirements are incomplete
- Every requirement has defined acceptance criteria before execution begins
- RTM is updated within 48 hours of any approved scope change
- At project closure, all Must-have requirements show Status = Accepted

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A08 — Scope Documentation | WBS deliverables linked from RTM |
| A09 — Quality Management Plan | Acceptance criteria standards align |
| A12 — Change Log | Requirement changes logged in both A12 and A13 |
| A17 — Performance Report | Requirements status reported in §5 |
| A27 — Closure Record | All Must requirements verified before closure sign-off |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.7 | Delivery Performance Domain — requirements |
| Process Groups PG §4.2 | Collect Requirements — RTM as output |
| PMI Business Analysis Guide §5 | Requirements traceability and validation |
| PMBOK8 Guide §2.7.2 | Validate Scope — acceptance criteria |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 2 | Initial definition — Phase B1 |

---

*Owner: Project Manager · Business Analyst*  
*Change Control: Requirement changes require Change Request via SKL-05-02 (T1–T2 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 2*
