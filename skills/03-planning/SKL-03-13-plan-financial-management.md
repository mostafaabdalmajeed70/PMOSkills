---
skill_id: SKL-03-13
skill_name: Plan Financial Management
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A16 — Financial Management and Cost Baseline Record (Financial Management Plan section)"
artifacts_updated:
  - "A14 — Integrated PM Plan (subsidiary reference)"
pmbok8_process_anchor: "Guide §2.4.2.1 Plan Financial Management · Figure 2-27"
performance_domains:
  - Finance
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-02-01 — A04 must be baselined"
  - "SKL-03-05 — Scope baseline (WBS) must be complete"
downstream_skills:
  - "SKL-03-14 — Estimate Costs"
  - "SKL-03-15 — Develop Budget"
file_path: "skills/03-planning/SKL-03-13-plan-financial-management.md"
tests: 8
version: "1.0.0"
---

# SKL-03-13 — Plan Financial Management

**Skill ID:** SKL-03-13  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.4.2.1 Plan Financial Management · Figure 2-27  
**File path:** `skills/03-planning/SKL-03-13-plan-financial-management.md`

---

## Purpose

Establish the financial management approach for the project — defining how costs will be estimated, how the budget will be structured, how reserves will be managed, and how financial performance will be controlled and reported — and record it in the Financial Management Plan section of A16.

---

## Scope

This skill covers the planning approach only. Cost estimation is SKL-03-14. Budget development is SKL-03-15. This skill's output is the Financial Management Plan section of A16 (Section 3).

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Project Charter (budget boundary) | A04 | Yes |
| Scope baseline (WBS) | A08 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Context Register (OPA — financial policies) | A05 | Yes |
| Delivery approach and lifecycle | A09 / A13 | Yes |

**Gate check:** Scope baseline (WBS) in A08 must be complete before financial management is planned — cost estimation requires a work structure to estimate against.

---

## Instructions

### Step 1 — Confirm financial governance context
1. From A04, extract the authorized budget boundary and any pre-set financial constraints.
2. From A05, identify organizational financial policies, approval thresholds, procurement rules, and reporting requirements.
3. From A06, identify tailoring decisions that affect financial management formality.

### Step 2 — Select cost estimation approach
1. Determine the cost estimation method(s): analogous, parametric, bottom-up, or three-point.
2. For bottom-up: confirm the WBS from A08 is the basis for estimation.
3. For adaptive approaches: determine whether estimation is per sprint/iteration (velocity-based) or per feature/epic.
4. Define the level of precision required (e.g., ±10%, ±25%, order of magnitude).

### Step 3 — Define budget structure and reporting
1. Define how costs will be classified (labor, materials, equipment, overhead, contingency, management reserve).
2. Define the budget reporting frequency and format consistent with A17.
3. Define how budget consumption is tracked (actual vs. planned, earned value if applicable).
4. Confirm EV metrics applicability: EV is appropriate only when a formal cost and schedule baseline both exist.

### Step 4 — Define reserve management approach
1. Determine how contingency reserve will be set (percentage, expected monetary value, risk-based from A19/A20).
2. Determine how management reserve will be set and who holds authority to release it.
3. Define the drawdown process: who approves reserve use, what triggers drawdown, how it is logged.
4. Confirm reserve decision linkage to A19 (risk-based) and A20 (quantitative justification if needed).

### Step 5 — Define financial control approach
1. Define cost variance thresholds that trigger review, corrective action, and escalation — consistent with A06.
2. Define the re-baseline trigger: what financial change requires a formal budget rebaseline in A16.
3. Confirm that financial baseline changes route through A12.
4. Define the financial reporting cadence and audience — consistent with A28.

### Step 6 — Write the Financial Management Plan section of A16
Populate Section 3 of A16 (Financial Management Approach) with all decisions from Steps 1–5.

### Step 7 — Register A16 as subsidiary in A14
Add or confirm A16 reference in the A14 Subsidiary Plan Index.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Financial Management Plan | A16 | Section 3 — Financial Management Approach |
| Subsidiary reference | A14 | Subsidiary Plan Index |

---

## Constraints

- Do not estimate costs in this skill — that is SKL-03-14.
- Reserve amounts are not set here — they are set in SKL-03-15 (Develop Budget) based on SKL-03-11/SKL-03-14 outputs.
- Financial control thresholds must align with A06 — do not set independent limits.
- Reserve drawdown must reference A12 for formal decision capture.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / small | Brief financial approach note; analogous estimation; informal reserve |
| Formal / large | Full financial plan; bottom-up estimation; EV; formal reserve management |
| Adaptive | Per-sprint budget allocation; velocity-based cost forecasting |
| Regulatory / contractual | Cost classification and reporting must match contract requirements |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| WBS not complete | Cost approach planned without scope structure | Complete SKL-03-05 first |
| EV applied without dual baseline | EV metrics defined before schedule baseline exists | Defer EV decision to SKL-03-15 |
| Reserve approach undefined | No reserve management rules | Define approach in Step 4 |
| Financial changes not routed to A12 | Parallel change process | Update approach to reference A12 |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — scope baseline complete | A08 WBS = Baselined | WBS not baselined |
| T-2 | Estimation method selected | A16 Section 3 estimation method field populated | Field blank |
| T-3 | Cost classification defined | Budget cost categories listed | No classification |
| T-4 | Reserve management approach defined | Contingency and management reserve approach documented | Reserve approach absent |
| T-5 | Reserve drawdown authority named | Who approves drawdown is documented | Authority blank |
| T-6 | Variance thresholds defined | At least cost variance threshold documented | No thresholds |
| T-7 | Financial change routing references A12 | A12 named in control approach | Parallel or undefined process |
| T-8 | A16 referenced in A14 subsidiary index | A14 Subsidiary Plan Index row for A16 present | A14 not updated |

---

*Authority: PMBOK8 — Guide §2.4.2.1 Plan Financial Management · Figure 2-27*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Sponsor or designated financial authority*
