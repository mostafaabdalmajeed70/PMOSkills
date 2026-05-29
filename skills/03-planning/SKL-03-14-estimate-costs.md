---
skill_id: SKL-03-14
skill_name: Estimate Costs
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A16 — Financial Management and Cost Baseline Record (Cost Estimates section)"
artifacts_updated:
  - "A19 — Risk Management Record (cost risk entries)"
  - "A15 — Schedule Model (resource-cost linkage)"
pmbok8_process_anchor: "Guide §2.4.2.2 Estimate Costs · Figure 2-28"
performance_domains:
  - Finance
  - Risk
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-13 — Financial Management Plan section of A16 must be complete"
  - "SKL-03-05 — Scope baseline (WBS) must be complete"
downstream_skills:
  - "SKL-03-15 — Develop Budget"
file_path: "skills/03-planning/SKL-03-14-estimate-costs.md"
tests: 9
version: "1.0.0"
---

# SKL-03-14 — Estimate Costs

**Skill ID:** SKL-03-14  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.4.2.2 Estimate Costs · Figure 2-28  
**File path:** `skills/03-planning/SKL-03-14-estimate-costs.md`

---

## Purpose

Produce cost estimates for each work package in the WBS, document the estimation basis, flag cost-related risks, and populate the Cost Estimates section of A16 — providing the input required for budget development in SKL-03-15.

---

## Scope

This skill covers cost estimation per work package. Financial management approach was established in SKL-03-13. Budget aggregation, reserve setting, and baseline development are in SKL-03-15.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Financial Management Plan section | A16 | Yes |
| Scope baseline (WBS + Dictionary) | A08 | Yes |
| Resource estimates | A26 | Yes |
| Schedule model (activity durations) | A15 | Yes |
| Risk register (cost-related risks) | A19 | Yes |
| Context Register (OPA — historical cost data) | A05 | If available |

**Gate check:** Financial Management Plan in A16 Section 3 must be complete before estimation begins — the estimation method and cost classification are defined there.

---

## Instructions

### Step 1 — Confirm estimation method and inputs
1. From A16 Section 3, confirm the estimation method: analogous, parametric, bottom-up, or three-point.
2. From A08 WBS dictionary, extract all work packages to be estimated.
3. From A26, extract resource types, rates, and quantities for each work package.
4. From A15, extract duration data per activity to calculate time-dependent costs.

### Step 2 — Estimate cost per work package
Apply the selected estimation method:

| Method | Application |
|---|---|
| **Analogous** | Use historical cost of similar work packages from A05 OPA. Apply scaling factors. Document comparison basis. |
| **Parametric** | Identify a cost-driving parameter (e.g., cost per unit, cost per hour). Multiply by quantity. Document the parameter source and validity range. |
| **Bottom-up** | Estimate each resource, material, and equipment item individually. Sum to work package level. Most accurate but most effort-intensive. |
| **Three-point (PERT)** | For each work package: O = optimistic, M = most likely, P = pessimistic. Expected cost E = (O + 4M + P) / 6. Document all three values. |

### Step 3 — Classify costs
1. For each work package estimate, classify costs into the categories defined in A16 Section 3 (e.g., labor, materials, equipment, overhead).
2. Identify direct costs (traceable to a work package) and indirect costs (allocated across the project).
3. Do not include contingency or management reserve here — those are set in SKL-03-15.

### Step 4 — Document estimation basis
For every work package estimate, record:
- Estimation method used
- Data source (OPA reference, vendor quote, rate card, analogous project)
- Assumptions made
- Confidence level or range (e.g., ±10%, ±25%)

### Step 5 — Identify cost risks
1. For any work package with a confidence level below the threshold defined in A16, flag as a cost risk.
2. Enter cost risk entries in A19 (Risk Management Record) with a reference back to the work package.
3. Flag candidates for quantitative analysis in A20 if the cost risk is material.

### Step 6 — Link to schedule
1. Confirm that time-dependent costs (labor, equipment rental) are consistent with durations in A15.
2. Note any schedule dependency that affects cost (resource availability windows, escalation clauses).

### Step 7 — Populate A16 Cost Estimates section
Enter all estimates in A16 Section 4 (Cost Estimates). Confirm the section is complete and internally consistent before passing to SKL-03-15.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Cost estimates per work package | A16 | Section 4 — Cost Estimates |
| Cost risk entries | A19 | Risk Register |
| Schedule-cost linkage notes | A15 | Notes / Resource Assignments |

---

## Constraints

- Do not include contingency or management reserve in cost estimates — reserve is set in SKL-03-15.
- Every work package in the WBS must have a corresponding cost estimate.
- Do not use a single project-level estimate without WBS-level decomposition (unless analogous estimation is the approved method and A06 permits it).
- Three-point estimates must document all three values (O, M, P) — single-point estimates must be justified.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / internal | Analogous or parametric estimation with documented basis |
| Large / formal | Bottom-up with three-point estimation for high-risk packages |
| Adaptive | Per-sprint cost based on team velocity and fully loaded resource rate |
| Regulatory | Cost classification must align with contract cost categories |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Financial Management Plan not complete | Estimation method not defined | Complete SKL-03-13 first |
| Work packages without estimates | Some WBS elements skipped | Estimate all work packages |
| Reserve included in estimates | Estimates inflated with contingency | Remove reserve; add in SKL-03-15 |
| No estimation basis documented | Single number with no source | Document method, source, and confidence for every estimate |
| Cost risks not in A19 | Low-confidence estimates not risk-registered | Add cost risk entries to A19 |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — Financial Management Plan complete | A16 Section 3 populated | Section blank |
| T-2 | All WBS work packages estimated | Every work package in A08 has a cost estimate in A16 | Any work package missing estimate |
| T-3 | Estimation method matches A16 plan | Method used matches method selected in SKL-03-13 | Inconsistent method |
| T-4 | Estimation basis documented | Source, method, assumptions, confidence documented per estimate | Any estimate with no basis |
| T-5 | Three-point estimates contain O, M, P | All three values present for every three-point estimate | Single-point value only |
| T-6 | Reserve not included in work package estimates | No estimate contains padding labelled "contingency" or "buffer" | Reserve embedded in estimates |
| T-7 | Cost classification applied | Each estimate has a cost category label | Unclassified estimates |
| T-8 | Low-confidence estimates flagged in A19 | Cost risk entries in A19 for below-threshold confidence estimates | Known cost risks absent from A19 |
| T-9 | Schedule-cost linkage confirmed | Time-dependent costs consistent with A15 activity durations | Inconsistency between A15 and A16 |

---

*Authority: PMBOK8 — Guide §2.4.2.2 Estimate Costs · Figure 2-28*  
*Source type: PMI-derived*  
*Owner: Project manager with cost estimation support*  
*Approval authority: Project manager; sponsor for estimates exceeding the approved budget boundary*
