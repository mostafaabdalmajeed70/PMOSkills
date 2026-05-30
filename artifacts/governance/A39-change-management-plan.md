---
artifact_id: A39
name: Change Management Plan
version: 1.0.0
status: "Definition · Active"
category: Governance
authority: "PMBOK8 Guide §2.4 · Process Groups PG §4.8 · Managing Change in Organizations PG §3"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.4 · Perform Integrated Change Control"
required_by_skills:
  - SKL-05-02
created_by_skills:
  - SKL-03-01
file_path: artifacts/governance/A39-change-management-plan.md
---

# A39 — Change Management Plan
**Artifact ID:** A39  
**Artifact Name:** Change Management Plan  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.4 · Process Groups PG §4.8 (Perform Integrated Change Control) · Managing Change in Organizations PG §3  
**Source Type:** PMI-derived  
**File Path:** `artifacts/governance/A39-change-management-plan.md`

---

## Definition

A39 defines the process for identifying, evaluating, approving, and implementing changes to the project baselines (scope, schedule, cost, quality). It establishes the Change Control Board (CCB) composition, authority thresholds, change request process, and baseline update procedures. It is a subsidiary plan within the Project Management Plan (A06).

**PMI Source:** PMBOK8 Guide §2.4 — Project Work Performance Domain; PG §4.8 — Perform Integrated Change Control; Managing Change in Organizations PG §3.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Governance |
| **Type** | Subsidiary plan (component of A06 PM Plan) |
| **Lifecycle** | Created in Planning · Applied throughout Executing and M&C · Closed at project close |
| **Baseline?** | Yes — change management process is governed |
| **Ownership** | Project Manager · PMO |

---

## Purpose

- Define the end-to-end process for raising, evaluating, approving, and implementing changes
- Establish the Change Control Board composition and authority levels
- Define change request categories and authority thresholds
- Protect project baselines from unauthorized changes
- Ensure all changes are logged and their impacts assessed before approval
- Align change control with AUTHORITY-ROUTING.md thresholds

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Change Control Philosophy | Project’s approach to change: baseline protection vs. agility | SKL-03-01 |
| §2 Change Control Board (CCB) | Composition, roles, quorum, meeting cadence | SKL-03-01 |
| §3 Authority Thresholds | T1–T4 authority levels per change category (aligned to AUTHORITY-ROUTING.md) | SKL-03-01 |
| §4 Change Request Process | Steps from submission to closure: log → assess → approve/reject → implement → close | SKL-03-01 |
| §5 Change Categories | Scope / Schedule / Cost / Quality / Risk / Contractual | SKL-03-01 |
| §6 Impact Assessment Requirements | What must be assessed per change type (cost impact, schedule impact, risk impact) | SKL-03-01 |
| §7 Baseline Update Procedure | How baselines are formally revised after approval | SKL-03-01 |
| §8 Emergency Change Process | Fast-track process for critical changes | SKL-03-01 |

---

## Change Request Process (Standard)

```
1. IDENTIFY — Anyone on the project may raise a change request
2. LOG — CR entered in A12 Change Log with unique ID (CR-NNN)
3. ASSESS — PM assesses impact on scope, schedule, cost, quality, risk
4. REVIEW — CCB reviews impact assessment
5. DECISION — Approve / Reject / Defer / Approve with conditions
6. IMPLEMENT — If approved: update affected baselines and plans
7. CLOSE — Update A12 with final status; notify stakeholders
```

---

## Authority Thresholds (§3)

| Threshold | Change Authority | Change Types |
|---|---|---|
| T1 | Project Manager | Minor scope clarifications; schedule adjustments within float |
| T2 | PM + Sponsor | Scope additions ≤ budget threshold; schedule changes > 5% |
| T3 | CCB (PM + Sponsor + PMO) | Major scope changes; budget overruns > threshold; strategic changes |
| T4 | Governing Body | Project redirection; fundamental objective change; early termination |

*Specific thresholds (dollar amounts, % variances) defined in A06 §1 per project.*

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| CCB composition | Named roles (not just titles) | Mandatory |
| Authority thresholds | T1–T4 linked to change categories | Mandatory |
| Change request process | All 7 steps documented | Mandatory |
| Impact assessment requirements | What is assessed per change type | Mandatory |
| Baseline update procedure | How baselines are revised post-approval | Mandatory |
| Emergency change process | Fast-track criteria and steps | Recommended |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A04 — Project Charter | SKL-02-01 | PM authority level |
| A05 — Context Register | SKL-01-02 | Org change control policies and CCB standards |
| A06 — PM Plan (baselines) | SKL-03-01 | What is being protected by change control |
| AUTHORITY-ROUTING.md | Repo governance | T1–T4 threshold reference |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Change control process | SKL-05-02 (Integrated Change Control) |
| CCB charter and authority | A12 (Change Log) |
| Authority thresholds | AUTHORITY-ROUTING.md alignment |
| Baseline update procedure | A06 (PM Plan) · A14 · A15 · A16 |

---

## Quality Criteria

- CCB members named with explicit authority before execution begins
- T1–T4 thresholds defined with specific values (not just descriptions)
- All changes — including approved verbal changes — logged in A12
- No baseline is updated without a logged and approved change request
- Emergency change process exists and is tested before it is needed

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A06 — PM Plan | A39 is a subsidiary plan of A06 |
| A12 — Change Log | A39 defines the process; A12 records the changes |
| A14 — WBS | Scope baseline protected by A39 |
| A15 — Schedule | Schedule baseline protected by A39 |
| A16 — Budget | Cost baseline protected by A39 |
| AUTHORITY-ROUTING.md | T1–T4 thresholds aligned |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.4 | Project Work Performance Domain |
| Process Groups PG §4.8 | Perform Integrated Change Control |
| PMBOK8 Standard §3 | Stewardship — baseline integrity |
| Managing Change PG §3 | Organizational change management principles |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 2 | Initial definition — Phase B1 |

---

*Owner: Project Manager · PMO*  
*Change Control: Changes to the change management plan itself require CCB approval (T3 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 2*
