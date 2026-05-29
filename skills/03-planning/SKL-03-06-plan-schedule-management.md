---
skill_id: SKL-03-06
skill_name: Plan Schedule Management
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A15 — Schedule Model and Baseline Record (Schedule Management Plan section)"
artifacts_updated:
  - "A14 — Integrated PM Plan (subsidiary reference)"
pmbok8_process_anchor: "Guide §2.3.2.1 Plan Schedule Management · Figure 2-21"
performance_domains:
  - Schedule
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-05 — Scope baseline (WBS) in A08 must be complete"
  - "SKL-02-01 — A04 (charter) must be baselined"
downstream_skills:
  - "SKL-03-06b — Develop Schedule (activity sequencing, duration estimation, schedule model)"
file_path: "skills/03-planning/SKL-03-06-plan-schedule-management.md"
tests: 8
version: "1.0.0"
---

# SKL-03-06 — Plan Schedule Management

**Skill ID:** SKL-03-06  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.3.2.1 Plan Schedule Management · Figure 2-21  
**File path:** `skills/03-planning/SKL-03-06-plan-schedule-management.md`

---

## Purpose

Establish the schedule management approach — defining how the schedule will be developed, maintained, controlled, and reported — and record it in the Schedule Management Plan section of A15.

---

## Scope

This skill covers the planning approach only. Activity definition, sequencing, duration estimation, and schedule model development are separate skills (SKL-03-06b and forward). This skill's output is the Schedule Management Plan section of A15.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Scope baseline (WBS) | A08 | Yes |
| Project Charter | A04 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Delivery approach and lifecycle decision | A09 / A13 | Yes |
| Organizational scheduling OPAs | A05 | If available |

**Gate check:** Scope baseline in A08 must be complete before schedule management is planned — the WBS provides the work structure that the schedule is built upon.

---

## Instructions

### Step 1 — Confirm lifecycle approach
1. From A09/A13, confirm whether the schedule approach is predictive (CPM-based), adaptive (iteration/release roadmap), or hybrid.
2. Select the scheduling method consistent with the lifecycle approach.
3. Document the selection rationale if it differs from organizational standards in A05.

### Step 2 — Define scheduling method and tools
1. Select the scheduling method: Critical Path Method (CPM), rolling wave, resource-leveled, agile roadmap, or other.
2. Identify the scheduling tool or system to be used.
3. Define the time unit (days / weeks / sprints).
4. Define the project calendar and working hours basis.

### Step 3 — Define level of detail
1. For predictive: determine whether the schedule will be built at summary milestone, WBS-linked activity, or full activity list level.
2. For adaptive: determine whether a release roadmap, sprint cadence, or both will be maintained.
3. For hybrid: define the level of detail by component type.

### Step 4 — Define schedule control approach
1. Define schedule variance thresholds that trigger review, corrective action, and escalation — consistent with A06.
2. Define float management rules (how much float is acceptable before corrective action).
3. Define the re-baseline trigger: what schedule change requires a formal baseline update in A15.
4. Confirm that schedule baseline changes route through A12.
5. Define the milestone reporting approach for A17.

### Step 5 — Define schedule update and reporting cadence
1. Define how often the schedule is updated (weekly, sprint close, milestone).
2. Define how schedule status feeds A17 (performance reporting).
3. Confirm schedule communication requirements align with A28.

### Step 6 — Write the Schedule Management Plan section of A15
Populate Section 3 of A15 (Schedule Management Approach) with all decisions from Steps 1–5.

### Step 7 — Register A15 as subsidiary in A14
Add or confirm A15 reference in the A14 Subsidiary Plan Index.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Schedule Management Plan | A15 | Section 3 — Schedule Management Approach |
| Subsidiary reference | A14 | Subsidiary Plan Index |

---

## Constraints

- Do not develop the schedule model (activities, durations, dependencies) in this skill — that is SKL-03-06b.
- Variance thresholds must be consistent with A06 — do not set independent control limits.
- Schedule change routing must reference A12.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / short-duration | Milestone list with informal schedule updates is sufficient |
| Predictive / formal | Full CPM schedule with critical path, float tracking, and formal re-baseline process |
| Adaptive | Sprint cadence + release roadmap; velocity-based forecasting |
| Regulatory / contractual | Schedule must align with contract milestones; changes require contract authority |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| WBS not complete | Schedule planned without scope structure | Complete SKL-03-05 first |
| Scheduling method contradicts lifecycle | CPM imposed on adaptive project | Align method with A09/A13 lifecycle decision |
| No variance thresholds | Schedule monitored with no defined action triggers | Add thresholds aligned with A06 |
| Schedule changes not routed to A12 | Parallel change process created | Update approach to reference A12 |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — scope baseline complete | A08 WBS section = Baselined | WBS not baselined |
| T-2 | Lifecycle approach confirmed | A09 or A13 confirms scheduling approach | Approach field empty |
| T-3 | Scheduling method selected and documented | A15 Section 3 Scheduling method field populated | Field blank |
| T-4 | Time unit and calendar defined | Both fields populated in A15 Section 3 | Either field blank |
| T-5 | Variance thresholds defined | At least schedule variance and float erosion thresholds documented | No thresholds |
| T-6 | Re-baseline trigger defined | Explicit trigger condition documented | Trigger absent |
| T-7 | Schedule change routing references A12 | A12 named in the control approach | Parallel or undefined change process |
| T-8 | A15 referenced in A14 subsidiary index | A14 Subsidiary Plan Index row for A15 present | A14 not updated |

---

*Authority: PMBOK8 — Guide §2.3.2.1 Plan Schedule Management · Figure 2-21*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Project manager within thresholds*
