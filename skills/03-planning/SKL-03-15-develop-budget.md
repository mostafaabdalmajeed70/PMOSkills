---
skill_id: SKL-03-15
skill_name: Develop Budget
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A16 — Financial Management and Cost Baseline Record (Cost Baseline / BAC section)"
artifacts_updated:
  - "A14 — Integrated PM Plan (subsidiary reference)"
pmbok8_process_anchor: "Guide §2.4.2.3 Develop Budget · Figure 2-29"
performance_domains:
  - Finance
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-14 — Cost estimates in A16 must be complete"
  - "SKL-03-11 — Risk analysis complete (reserve basis)"
downstream_skills:
  - "SKL-05-xx — Monitor and Control Finances"
file_path: "skills/03-planning/SKL-03-15-develop-budget.md"
tests: 9
version: "1.0.0"
---

# SKL-03-15 — Develop Budget

**Skill ID:** SKL-03-15  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.4.2.3 Develop Budget · Figure 2-29  
**File path:** `skills/03-planning/SKL-03-15-develop-budget.md`

---

## Purpose

Aggregate approved work package cost estimates into an authorized project budget, determine contingency and management reserve levels, establish the cost baseline (BAC), and obtain formal budget approval to complete the Financial Management and Cost Baseline Record (A16).

---

## Scope

This skill covers budget aggregation, reserve determination, and cost baseline establishment. Cost estimation per work package was completed in SKL-03-14. Reserve justification from quantitative analysis comes from A20. The output is the approved budget and cost baseline in A16.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Cost estimates per work package | A16 Section 4 | Yes |
| Financial Management Plan | A16 Section 3 | Yes |
| Risk Management Record (qualitative analysis) | A19 | Yes |
| Quantitative Risk and Reserve Record | A20 | If produced |
| Schedule model (for time-phased budget) | A15 | Yes |
| Project Charter (authorized budget boundary) | A04 | Yes |

**Gate check:** All work package cost estimates in A16 Section 4 must be complete before budget aggregation begins.

---

## Instructions

### Step 1 — Aggregate work package estimates
1. Sum cost estimates from A16 Section 4 by WBS control account or work package group.
2. Produce a total project cost estimate (excluding reserves).
3. Validate that the sum is within or reconcilable with the charter budget boundary from A04.
4. If the sum exceeds the charter boundary, identify scope or estimation adjustments before proceeding — do not absorb the gap with reserve.

### Step 2 — Determine contingency reserve
1. From A19 (risk analysis), identify the basis for contingency reserve:
   - Percentage of total estimate (e.g., 10–15% of base estimate)
   - Expected Monetary Value (EMV) of identified cost risks
   - Quantitative analysis result from A20 (preferred for high-uncertainty projects)
2. Document the reserve basis and calculation method in A16.
3. Contingency reserve is within the project manager's authority to manage (per A06 thresholds).

### Step 3 — Determine management reserve
1. Management reserve covers unidentified risks (unknown unknowns).
2. Typical approach: 5–10% of total project cost (organizational policy may specify).
3. Management reserve is held by the sponsor or governance body — not within the PM's authority.
4. Document management reserve basis and authority in A16.

### Step 4 — Establish the cost baseline (BAC)
**Budget at Completion (BAC) = Sum of work package estimates + Contingency reserve**  
*(Management reserve is not included in the cost baseline — it is held separately)*

1. Record BAC in A16 Section 5.
2. The cost baseline is the approved, time-phased budget against which financial performance is measured.
3. Time-phase the baseline using the schedule model from A15 — allocate costs to the periods in which they will be incurred.

### Step 5 — Obtain budget approval
1. Present the budget (BAC + management reserve) to the sponsor or designated financial approval authority.
2. Confirm that the approved budget is within the charter boundary (A04) or that a charter amendment has been approved through A12.
3. Record approval authority, date, and approved amounts in A16.

### Step 6 — Enable Earned Value (if applicable)
1. If EV is the selected performance measurement method (from A16 Section 3), confirm that:
   - A cost baseline (BAC) exists
   - A schedule baseline exists in A15
   - Both are time-phased against the same calendar
2. Note: EV requires both baselines. Do not activate EV reporting in A17 without both.

### Step 7 — Update A14 subsidiary reference
Confirm A16 is referenced in the A14 Subsidiary Plan Index with baseline date and approved status.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Aggregated cost estimates | A16 | Section 4 (updated totals) |
| Contingency reserve | A16 | Section 5 — Cost Baseline |
| Management reserve | A16 | Section 5 — Cost Baseline |
| Cost baseline (BAC) | A16 | Section 5 — Cost Baseline |
| Budget approval record | A16 | Section 5 |
| Subsidiary reference | A14 | Subsidiary Plan Index |

---

## Constraints

- BAC = work package estimates + contingency reserve only. Management reserve is separate.
- Do not include management reserve in BAC — it is not part of the performance measurement baseline.
- Budget approval must come from the authority defined in A04 and A06, not the PM alone.
- If the total exceeds the charter budget boundary, resolve through A12 before baselining.
- EV activation requires both cost and schedule baselines.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / small | Analogous reserve (percentage); informal time-phasing |
| Large / formal | Risk-based contingency (A19/A20); fully time-phased S-curve |
| Adaptive | Budget per sprint/release cycle with velocity-based forecast |
| Regulatory / contractual | Budget structure must match contract cost categories; approval per contract terms |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Estimates not complete | Work packages with no cost data | Complete SKL-03-14 first |
| Reserve embedded in estimates | BAC includes padding in work package estimates | Clean estimates; set reserve explicitly |
| Management reserve in BAC | BAC inflated beyond performance baseline | Remove management reserve from BAC |
| Total exceeds charter boundary | Aggregated cost > A04 budget | Scope reduction, estimate revision, or charter amendment via A12 |
| EV activated without schedule baseline | A17 shows EV metrics but A15 not baselined | Complete schedule baseline in SKL-03-06b first |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — all work package estimates complete | All A16 Section 4 rows populated | Any work package missing estimate |
| T-2 | Aggregation correct | Sum of work packages = total base estimate | Arithmetic error or missing packages |
| T-3 | Contingency reserve documented with basis | Reserve amount and calculation method in A16 | Reserve amount with no basis |
| T-4 | Management reserve separate from BAC | BAC = base estimates + contingency only | Management reserve included in BAC |
| T-5 | Budget within charter boundary or amendment approved | Total ≤ A04 budget OR A12 charter amendment approved | Unexplained budget overrun |
| T-6 | BAC recorded in A16 Section 5 | BAC field populated with approval date and authority | BAC field blank |
| T-7 | Time-phasing completed | Budget allocated to schedule periods consistent with A15 | Lump-sum budget with no time allocation |
| T-8 | EV applicability confirmed | EV activated only when both cost and schedule baselines exist | EV metrics in A17 without A15 baseline |
| T-9 | A16 referenced in A14 as baselined | A14 Subsidiary Plan Index shows A16 status = Approved / Baselined | A14 not updated |

---

*Authority: PMBOK8 — Guide §2.4.2.3 Develop Budget · Figure 2-29*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Sponsor or designated financial governing body*
