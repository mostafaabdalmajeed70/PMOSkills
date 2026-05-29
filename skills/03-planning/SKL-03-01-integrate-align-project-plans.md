---
skill_id: SKL-03-01
skill_name: Integrate and Align Project Plans
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A14 — Integrated Project Management Plan"
artifacts_updated:
  - "All subsidiary planning records (cross-referenced and confirmed)"
pmbok8_process_anchor: "Guide §2.1.6.2 Integrate and Align Project Plans · Figure 2-4"
performance_domains:
  - Governance
  - All domains (integrative)
focus_area: Planning
upstream_prerequisites:
  - "SKL-02-01 — A04 baselined"
  - "SKL-02-02 — A07 identification complete"
  - "SKL-03-02 through SKL-03-17 — All applicable subsidiary planning skills complete"
downstream_skills:
  - "SKL-04-xx — Manage Project Execution (primary input)"
  - "All Pack 05 monitoring skills"
file_path: "skills/03-planning/SKL-03-01-integrate-align-project-plans.md"
tests: 10
version: "1.0.0"
---

# SKL-03-01 — Integrate and Align Project Plans

**Skill ID:** SKL-03-01  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.1.6.2 Integrate and Align Project Plans · Figure 2-4  
**File path:** `skills/03-planning/SKL-03-01-integrate-align-project-plans.md`

---

## Purpose

Assemble all approved subsidiary planning records into a coherent, internally consistent Integrated Project Management Plan (A14) — verifying alignment across scope, schedule, finance, risk, resources, stakeholders, and communications before authorizing the transition to execution.

---

## Scope

This is the final Pack 03 skill. It does not produce subsidiary plan content — all subsidiary records must be complete before this skill runs. Its sole output is a baselined A14 that references all applicable subsidiary records and confirms their alignment.

---

## Inputs Required

| Input | Artifact | Status required |
|---|---|---|
| Project Charter | A04 | Approved |
| Tailoring Decision Record | A06 | Approved |
| Stakeholder Register and Engagement Strategy | A07 | Baselined |
| Scope and Requirements Decision Record | A08 | Baselined (scope baseline complete) |
| Delivery Approach and Team Operating Agreement | A09 | Approved |
| Development Approach and Lifecycle Decision Record | A13 | Approved |
| Schedule Model and Baseline Record | A15 | Baselined |
| Financial Management and Cost Baseline Record | A16 | Baselined (BAC approved) |
| Risk Management Record | A19 | Active (responses planned) |
| Resource Capacity and Acquisition Record | A26 | Approved |
| Team Operating and Responsibility Record | A25 | Approved |
| Communications and Reporting Record | A28 | Approved |

**Gate check:** Every applicable subsidiary record in the table above must be in the required status before A14 can be baselined. Any record in Draft status must be resolved before this skill proceeds.

---

## Instructions

### Step 1 — Confirm all subsidiary records are in required status
1. Review every subsidiary record in the input table above.
2. For any record not in required status, stop and resolve before proceeding.
3. Document which subsidiary plans are applicable for this project (some may be waived per A06 tailoring).

### Step 2 — Populate the A14 Subsidiary Plan Index
1. Add or confirm every applicable subsidiary record in A14 Section 3 (Subsidiary Plan Index).
2. Record artifact ID, file location, version, status, and owner for each entry.
3. For any subsidiary plan waived by A06 tailoring, record the waiver rationale in the Notes column.

### Step 3 — Validate internal consistency across plans
Check alignment across the following pairs:

| Check | Plan A | Plan B | Alignment test |
|---|---|---|---|
| Scope ↔ Schedule | A08 WBS work packages | A15 activity list | Every WBS work package has activities in A15 |
| Schedule ↔ Finance | A15 time-phased schedule | A16 time-phased budget | Cost allocation periods match schedule periods |
| Finance ↔ Risk | A16 contingency reserve | A19 risk analysis | Reserve is consistent with A19/A20 risk justification |
| Risk ↔ Schedule | A19 risk responses | A15 schedule buffers | Schedule buffers reference A19 risk IDs |
| Resources ↔ Schedule | A26 resource availability | A15 resource assignments | Resource assignments do not exceed A26 availability |
| Stakeholders ↔ Communications | A07 engagement strategies | A28 communication entries | Every A07 stakeholder has at least one A28 entry |
| Governance ↔ Tailoring | A14 control thresholds | A06 governance thresholds | A14 thresholds match A06 — no independent limits |

For each check, document: Aligned / Gap found / Gap resolved.

### Step 4 — Populate A14 Baseline Summary
1. Record scope baseline reference (A08 version and date).
2. Record schedule baseline reference (A15 BAC-equivalent: planned dates and milestones).
3. Record cost baseline reference (A16 BAC amount and date).
4. Record benefits baseline reference (A02 if applicable).

### Step 5 — Populate A14 Control Thresholds
1. Transfer approved variance thresholds from A06 into A14 Section 6.
2. Confirm every domain (scope, schedule, finance, risk, resources) has a threshold entry.
3. No threshold in A14 may differ from A06 without a documented rationale.

### Step 6 — Populate A14 Governance Calendar
1. Define the governance and review event schedule for the project lifecycle.
2. Confirm that reporting cadence in A14 Section 7 matches A28 communication plan entries.

### Step 7 — Obtain A14 approval
1. Present A14 to the sponsor or designated approval authority for formal approval.
2. Record approval authority, date, and any conditions in A14.
3. Mark A14 status as Approved / Baselined.

### Step 8 — Declare Pack 03 complete
1. Update SKILL-REGISTRY.md — mark SKL-03-01 as Draft · Untested.
2. Confirm Pack 03 completion criteria are met: A14 baselined with all applicable subsidiary references.
3. Pack 04 (Executing) skills may now begin.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Integrated Project Management Plan (baselined) | A14 | All sections |
| Pack 03 completion declaration | SKILL-REGISTRY.md | Pack 03 status |

---

## Constraints

- This skill cannot run until all applicable subsidiary planning skills are complete — it assembles, it does not create.
- A14 must not re-state content from subsidiary records — it indexes and references only.
- Every gap found in Step 3 must be resolved before A14 is approved — do not baseline with open alignment gaps.
- Thresholds in A14 must match A06 exactly — no independent limits.
- Pack 04 may not begin until A14 is approved.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / small | A14 may be a one-page plan index with key decisions summarized — subsidiary records remain the source of truth |
| Complex / large | Full A14 with all sections populated; formal sponsor sign-off; gate review required |
| Adaptive | A14 references the product backlog, release roadmap, and team operating agreement as primary planning artifacts |
| Regulatory | A14 may require external approval or audit review before execution authorization |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Subsidiary records in Draft status | Cannot baseline A14 | Resolve all draft subsidiary records first |
| Alignment gaps not resolved | Conflicting data across plans | Resolve each gap; document resolution |
| A14 re-states subsidiary content | A14 becomes a duplicate planning document | Remove duplicated content; reference instead |
| Control thresholds differ from A06 | A14 has independent limits | Align with A06 — update A14 |
| Pack 04 started before A14 approved | Execution without an integrated plan | Stop execution activities; complete A14 approval |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — all applicable subsidiary records in required status | All records in Approved or Baselined status | Any record in Draft |
| T-2 | Subsidiary Plan Index complete | All applicable records listed in A14 Section 3 with file, version, status, owner | Any applicable record missing |
| T-3 | Scope ↔ Schedule alignment confirmed | Every WBS work package has A15 activities | Orphan WBS elements with no activities |
| T-4 | Schedule ↔ Finance alignment confirmed | Cost allocation periods consistent with A15 schedule periods | Misaligned time-phasing |
| T-5 | Finance ↔ Risk alignment confirmed | A16 contingency reserve consistent with A19/A20 justification | Reserve with no risk basis |
| T-6 | Resources ↔ Schedule alignment confirmed | A26 availability consistent with A15 resource assignments | Over-allocation not flagged |
| T-7 | Stakeholders ↔ Communications alignment confirmed | Every A07 stakeholder has at least one A28 entry | Orphan stakeholders |
| T-8 | A14 thresholds match A06 | Every A14 threshold matches its A06 equivalent | Any discrepancy without documented rationale |
| T-9 | A14 approved by correct authority | Approval authority, name, and date recorded | A14 unapproved or self-approved by PM |
| T-10 | A14 does not re-state subsidiary content | A14 references records; no duplicated fields | A14 contains plan content that belongs in subsidiary records |

---

*Authority: PMBOK8 — Guide §2.1.6.2 Integrate and Align Project Plans · Figure 2-4*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Sponsor or designated project governing body*
