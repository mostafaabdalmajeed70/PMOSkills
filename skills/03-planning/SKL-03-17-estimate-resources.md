---
skill_id: SKL-03-17
skill_name: Estimate Resources
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A26 — Resource Capacity and Acquisition Record (Resource Estimates section)"
artifacts_updated:
  - "A15 — Schedule Model (resource-loaded schedule)"
  - "A16 — Financial Management and Cost Baseline Record (resource cost feeds)"
pmbok8_process_anchor: "Guide §2.6.2.2 Estimate Resources · Figure 2-42"
performance_domains:
  - Resources
  - Schedule
  - Finance
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-16 — Resource Management Plan section of A26 must be complete"
  - "SKL-03-06b — Schedule activities must be defined (activity durations in A15)"
downstream_skills:
  - "SKL-04-xx — Acquire Resources"
file_path: "skills/03-planning/SKL-03-17-estimate-resources.md"
tests: 8
version: "1.0.0"
---

# SKL-03-17 — Estimate Resources

**Skill ID:** SKL-03-17  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.6.2.2 Estimate Resources · Figure 2-42  
**File path:** `skills/03-planning/SKL-03-17-estimate-resources.md`

---

## Purpose

Estimate the type, quantity, and characteristics of resources required for each activity or work package, populate the Resource Estimates section of A26, and feed resource assignments into A15 (schedule) and resource costs into A16 (finance).

---

## Scope

This skill covers resource estimation per activity or work package. Resource management approach was established in SKL-03-16. Acquisition execution is in Pack 04 (Acquire Resources). This skill feeds both the schedule model (A15) and the cost baseline (A16).

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Resource Management Plan | A26 Section 3 | Yes |
| Activity list / work packages | A15 / A08 WBS | Yes |
| Activity duration estimates | A15 | Yes |
| Resource rates and availability | A05 OPA / A26 | Yes |
| Scope baseline | A08 | Yes |

**Gate check:** Resource Management Plan in A26 Section 3 must be complete. Activity durations in A15 must be defined (SKL-03-06b output) before resource-loaded estimates can be produced.

---

## Instructions

### Step 1 — Select estimation method
From A26 Section 3, confirm the estimation method:
- **Bottom-up:** Estimate resource needs per individual activity; roll up to work package and project level.
- **Analogous:** Use resource data from similar past projects (A05 OPA).
- **Parametric:** Use a resource-driving parameter (e.g., hours per unit, resources per sprint).
- **Expert judgment:** Structured input from subject matter experts for unique or novel work.

### Step 2 — Estimate resources per activity or work package
For each activity in A15 or work package in A08:
1. Identify required resource types (role/skill, equipment, material).
2. Estimate quantity of each resource type.
3. Estimate duration of resource need (start–end alignment with A15 activity dates).
4. Identify resource skill requirements (must match or exceed role profile in A25).
5. Document estimation basis and assumptions.

### Step 3 — Check availability and confirm resource calendar
1. Cross-reference estimated resource needs against availability data in A26 Section 5.
2. Flag any resource type that is unavailable or over-allocated during the required period.
3. Update A26 Section 5 (Resource Calendar and Availability) with confirmed assignments.

### Step 4 — Build the resource-loaded schedule
1. Assign confirmed resources to activities in A15 Section 6 (Resource Assignments).
2. For predictive projects: confirm resources are assigned to critical path activities first.
3. For adaptive projects: confirm team capacity per sprint is consistent with velocity assumptions.

### Step 5 — Feed resource costs to A16
1. Apply resource rates (from A05 or A26) to estimated quantities and durations.
2. Calculate resource cost per work package.
3. Pass resource cost data to A16 Section 4 (Cost Estimates) as labor and equipment cost inputs.
4. Confirm alignment with cost estimates already in A16 (no double-counting with SKL-03-14).

### Step 6 — Identify resource risks
1. Flag any resource with low availability confidence (single point of failure, critical skill, long lead time).
2. Enter resource-related risks in A19 Risk Register.
3. For external resources requiring acquisition, initiate A26 Section 6 (Acquisition Log) entries.

### Step 7 — Populate A26 Resource Estimates section
Complete A26 Section 4 (Resource Estimates) with all estimate rows, bases, and cost rate linkages.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Resource estimates per activity/WP | A26 | Section 4 — Resource Estimates |
| Resource assignments | A15 | Section 6 — Resource Assignments |
| Resource cost inputs | A16 | Section 4 — Cost Estimates (resource rows) |
| Resource risks | A19 | Risk Register |
| Acquisition log stubs | A26 | Section 6 — Acquisition Log |

---

## Constraints

- Every activity or work package with labor or equipment requirements must have a resource estimate.
- Resource assignments must be consistent with availability in A26 Section 5 — do not assign unavailable resources.
- Resource costs passed to A16 must not duplicate estimates already entered in SKL-03-14.
- Resource skill requirements must be compatible with role profiles in A25.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Small / stable team | Role-level estimates with hours per work package; no detailed rate calculation |
| Large / multi-vendor | Full resource estimate per activity; rate-based cost calculation; acquisition log entries |
| Adaptive | Team capacity per sprint (story points × velocity or hours per person-sprint) |
| External / contracted | Estimate scope of work for contractor; cost estimate as fixed-price or time-and-materials basis |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Resource Management Plan incomplete | Estimation method not defined | Complete SKL-03-16 first |
| Activity durations not defined | Cannot calculate resource-hours | Complete A15 activity list and duration estimation (SKL-03-06b) |
| Over-allocation not flagged | Resources assigned beyond availability | Check A26 Section 5 against estimates |
| Resource costs not passed to A16 | A16 cost estimates exclude labor | Add resource cost rows to A16 Section 4 |
| Resource risks not in A19 | Single points of failure unregistered | Add resource risk entries to A19 |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — Resource Management Plan complete | A26 Section 3 populated | Section blank |
| T-2 | All activities/WPs have resource estimates | Every A15 activity or A08 WP has a A26 estimate row | Any activity missing resource estimate |
| T-3 | Resource types and quantities documented | Type, quantity, duration all populated per estimate row | Any field blank without tailoring justification |
| T-4 | Estimation basis documented | Source, method, assumptions recorded per estimate | Estimate with no basis |
| T-5 | Resource assignments in A15 | A15 Section 6 populated with confirmed resource assignments | A15 resource assignments blank |
| T-6 | Resource costs in A16 | A16 Section 4 has resource cost rows from A26 | Resource costs absent from A16 |
| T-7 | Over-allocation flagged | Any over-allocated resource flagged in A26 Section 7 | Silent over-allocation |
| T-8 | Resource risks in A19 | Low-availability or single-point-of-failure resources have A19 entries | Known resource risks absent |

---

*Authority: PMBOK8 — Guide §2.6.2.2 Estimate Resources · Figure 2-42*  
*Source type: PMI-derived*  
*Owner: Project manager with resource management support*  
*Approval authority: Project manager; functional authority for shared resources*
