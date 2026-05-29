---
skill_id: SKL-03-02
skill_name: Plan Scope Management
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A08 — Scope and Requirements Decision Record (Scope Management Plan section)"
artifacts_updated:
  - "A14 — Integrated PM Plan (subsidiary reference)"
pmbok8_process_anchor: "Guide §2.2.2.1 Plan Scope Management · Figure 2-14"
performance_domains:
  - Scope
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-02-01 — A04 must be baselined"
  - "SKL-02-02 — A07 Identification section must exist"
downstream_skills:
  - "SKL-03-03 — Elicit and Analyze Requirements"
  - "SKL-03-04 — Define Scope"
file_path: "skills/03-planning/SKL-03-02-plan-scope-management.md"
tests: 8
version: "1.0.0"
---

# SKL-03-02 — Plan Scope Management

**Skill ID:** SKL-03-02  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.2.2.1 Plan Scope Management · Figure 2-14  
**File path:** `skills/03-planning/SKL-03-02-plan-scope-management.md`

---

## Purpose

Establish the scope management approach for the project — defining how scope will be defined, validated, and controlled — and record it in the Scope Management Plan section of A08 (Scope and Requirements Decision Record).

---

## Scope

This skill covers the Plan Scope Management process only. It does not elicit requirements (SKL-03-03), define scope (SKL-03-04), or develop the scope structure/WBS (SKL-03-05). Its output is the Scope Management Plan section of A08 and a subsidiary reference in A14.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Project Charter | A04 | Yes |
| Context Register (EEF/OPA) | A05 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Stakeholder Register (Identification section) | A07 | Yes |
| Delivery approach and lifecycle decision | A09 / A13 | Yes |

**Gate check:** A04 must be approved and baselined before this skill runs. If A04 is not baselined, stop and complete SKL-02-01.

---

## Instructions

### Step 1 — Review charter and context
1. Read A04 to extract the authorized scope boundary, high-level deliverables, and stated constraints.
2. Read A05 for organizational standards, templates, and precedents that govern scope management.
3. Read A06 for tailoring decisions that affect how formal or lightweight the scope approach should be.

### Step 2 — Select scope definition approach
1. Determine whether a predictive (WBS-driven), adaptive (backlog-driven), or hybrid scope approach applies based on A09/A13.
2. For predictive: plan for a formal scope baseline using a WBS and project scope statement.
3. For adaptive: plan for a prioritized backlog with defined acceptance criteria per item.
4. For hybrid: identify which components are predictive and which are adaptive; document the boundary.

### Step 3 — Define scope validation approach
1. Determine who validates and accepts deliverables (customer, sponsor, product owner, or designated authority).
2. Define when validation occurs (at phase gates, sprint reviews, milestone completions, or continuous).
3. Define acceptance criteria standards — what constitutes a formally accepted deliverable.
4. Record the validation authority in A07 if not already captured.

### Step 4 — Define scope control approach
1. Determine the scope change process: who can request, who assesses, who approves.
2. Confirm that scope changes route through A12 (Change and Exception Decision Log).
3. Define the re-baseline trigger: what level of scope change requires a formal baseline update to A08.
4. Confirm alignment with A06 thresholds.

### Step 5 — Define requirements management linkage
1. Confirm that requirements will be elicited and documented in A08 by SKL-03-03.
2. Confirm that requirements traceability will be maintained within A08.
3. Identify any regulatory or contractual requirements that impose specific requirements management obligations.

### Step 6 — Write the Scope Management Plan section of A08
Populate the Scope Management Plan section of A08 with:
- Scope definition approach (predictive / adaptive / hybrid)
- Scope validation approach (who, when, acceptance criteria standard)
- Scope control approach (change process, re-baseline triggers)
- Requirements management linkage
- Tailoring rationale (reference A06)

### Step 7 — Register A08 as subsidiary in A14
Add or confirm A08 reference in the A14 Subsidiary Plan Index.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Scope Management Plan | A08 | Scope Management Plan section |
| Subsidiary reference | A14 | Subsidiary Plan Index |

---

## Constraints

- Do not combine scope definition, requirements elicitation, or WBS development in this skill — those are SKL-03-03, SKL-03-04, and SKL-03-05.
- The scope management approach must be consistent with the lifecycle approach in A09/A13.
- Scope change routing must reference A12 — do not design a parallel change process.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / low-risk | One-paragraph scope management note in A08 is sufficient; skip formal plan structure |
| Predictive | Full scope management plan with WBS, formal validation, and change control |
| Adaptive | Backlog management rules, definition of ready, definition of done, sprint review as validation |
| Hybrid | Map which components use each approach; document at the component level |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Charter not baselined | A04 missing or draft | Stop; complete SKL-02-01 first |
| Lifecycle approach not decided | A09/A13 empty | Resolve delivery approach before planning scope |
| Scope management approach contradicts A06 | Overly heavyweight for tailored project | Align with A06 tailoring decision |
| Validation authority not named | A07 has no acceptance authority identified | Update A07 stakeholder register |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — A04 baselined | A04 status = Approved | A04 in Draft status |
| T-2 | Lifecycle approach resolved | A09 or A13 confirms predictive/adaptive/hybrid | Approach field empty |
| T-3 | Scope Management Plan section populated in A08 | All six fields in Step 6 present | Any field blank without tailoring justification |
| T-4 | Scope definition approach matches lifecycle | Predictive → WBS planned; Adaptive → backlog planned | Mismatch with no documented rationale |
| T-5 | Validation authority named | A07 or A08 identifies acceptance authority | No named authority |
| T-6 | Scope change routing references A12 | A12 named as the change decision vehicle | Parallel or undefined change process |
| T-7 | Re-baseline trigger defined | Explicit trigger condition documented | Trigger absent or vague |
| T-8 | A08 referenced in A14 subsidiary index | A14 Subsidiary Plan Index row for A08 present | A14 not updated |

---

*Authority: PMBOK8 — Guide §2.2.2.1 Plan Scope Management · Figure 2-14*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Project manager within thresholds*
