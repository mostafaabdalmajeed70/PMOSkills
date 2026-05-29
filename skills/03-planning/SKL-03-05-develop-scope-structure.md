---
skill_id: SKL-03-05
skill_name: Develop Scope Structure
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A08 — Scope and Requirements Decision Record (WBS / Scope Structure section)"
artifacts_updated:
  - "A15 — Schedule Model (work packages feed activity decomposition)"
  - "A16 — Financial Management and Cost Baseline Record (work packages feed cost estimates)"
pmbok8_process_anchor: "Guide §2.2.2.4 Develop Scope Structure · Figure 2-17"
performance_domains:
  - Scope
  - Schedule
  - Finance
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-04 — Project Scope Statement in A08 must be approved"
downstream_skills:
  - "SKL-03-06 — Plan Schedule Management"
  - "SKL-03-13 — Plan Financial Management"
  - "SKL-03-16 — Plan Resource Management"
file_path: "skills/03-planning/SKL-03-05-develop-scope-structure.md"
tests: 8
version: "1.0.0"
---

# SKL-03-05 — Develop Scope Structure

**Skill ID:** SKL-03-05  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.2.2.4 Develop Scope Structure · Figure 2-17  
**File path:** `skills/03-planning/SKL-03-05-develop-scope-structure.md`

---

## Purpose

Decompose the approved project scope statement into a hierarchical scope structure (WBS) with work packages that serve as the basis for schedule, cost, and resource planning. Complete the scope baseline by combining the approved scope statement, WBS, and WBS dictionary.

---

## Scope

This skill covers WBS decomposition and scope baseline completion. Scope statement was approved in SKL-03-04. Schedule planning (SKL-03-06), cost estimation (SKL-03-13), and resource estimation (SKL-03-16) all depend on this skill's output.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Approved Project Scope Statement | A08 | Yes |
| Approved Requirements baseline | A08 | Yes |
| Project Charter | A04 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Organizational WBS templates / OPA | A05 | If available |

**Gate check:** Project Scope Statement in A08 must be approved before WBS decomposition begins.

---

## Instructions

### Step 1 — Select decomposition approach
1. Review A06 and A09/A13 to confirm whether a predictive WBS, an adaptive release/feature structure, or a hybrid structure applies.
2. For predictive: decompose to work package level (lowest level planned and estimated).
3. For adaptive: develop a feature/capability hierarchy or product backlog structure organized by theme and epic; do not force a traditional WBS.
4. For hybrid: apply WBS to fixed-scope components; apply backlog structure to adaptive components.

### Step 2 — Build the hierarchical structure
1. Start with the project (Level 1).
2. Decompose into major deliverables or phases (Level 2).
3. Decompose each Level 2 element into sub-deliverables or work packages (Level 3+) until each work package is:
   - Assignable to one responsible party
   - Estimable for cost and duration
   - Completable within a single reporting period (or manageable sub-period)
4. Assign a unique WBS code to every element (e.g., 1.0, 1.1, 1.1.1).

### Step 3 — Create the WBS dictionary
For each work package, document:
- WBS code
- Description of work
- Acceptance criteria (reference A08 scope statement)
- Responsible party (to be confirmed in A25/A26)
- Estimated duration range (input to A15)
- Estimated cost range (input to A16)
- Dependencies (input to A15)
- Assumptions and constraints specific to this work package

### Step 4 — Validate completeness (100% rule)
1. Every deliverable in the approved scope statement must appear as a WBS element.
2. No work package should appear in the WBS without a traceable scope statement deliverable.
3. The sum of all work packages must equal 100% of the project scope — no more, no less.
4. Verify that out-of-scope items from A08 are not present anywhere in the WBS.

### Step 5 — Complete the scope baseline
The scope baseline = Approved Scope Statement + WBS + WBS Dictionary.
1. Mark the WBS section of A08 as baselined.
2. Record baseline date and approval authority.
3. Note: any future change to any element of the scope baseline requires A12 (change control).

### Step 6 — Feed downstream artifacts
1. Export work packages and dependency information to A15 (Schedule Model) as activity inputs.
2. Export work packages and cost range estimates to A16 (Financial Management Record) as estimation inputs.
3. Export work package responsibility assignments as inputs to A26 (Resource Capacity and Acquisition).

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| WBS and WBS Dictionary | A08 | WBS / Scope Structure section |
| Scope baseline (complete) | A08 | Scope Statement + WBS + WBS Dictionary |
| Work package inputs | A15 | Activity list inputs |
| Cost range inputs | A16 | Cost estimate inputs |

---

## Constraints

- The 100% rule is mandatory — the WBS must contain all scope, no more and no less.
- Work packages must be estimable and assignable — do not create work packages too large to plan.
- Scope baseline changes after this step require A12 entries.
- Do not decompose to activity level here — activities are decomposed in A15 (SKL-03-06 onward).

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / internal | Two-level WBS (deliverable → work package) is sufficient |
| Complex / large | Three or four levels with full WBS dictionary |
| Adaptive | Feature hierarchy / backlog structure replaces WBS; acceptance criteria at backlog item level |
| Regulatory | WBS must align with contract deliverable structure and reporting requirements |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Scope statement not approved | WBS built on draft scope | Stop; complete SKL-03-04 approval step |
| 100% rule violated | WBS missing a scope statement deliverable | Add missing element; re-validate |
| Work packages too large | Elements span multiple reporting periods without decomposition | Decompose further |
| Out-of-scope items in WBS | Item appears in WBS but not in scope statement | Remove or raise as change through A12 |
| WBS dictionary incomplete | Work packages lack descriptions or acceptance criteria | Complete dictionary before baselining |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — scope statement approved | A08 Project Scope Statement status = Approved | Status = Draft |
| T-2 | 100% rule — all scope statement deliverables present in WBS | Every deliverable has a WBS element | Missing deliverable |
| T-3 | 100% rule — no WBS element without scope statement source | Every WBS element traces to an approved deliverable | Orphan WBS element |
| T-4 | WBS codes assigned | Every element has a unique hierarchical code | Any element missing a code |
| T-5 | WBS dictionary complete | Every work package has: description, acceptance criteria reference, responsible party placeholder, estimate range | Any work package missing required fields |
| T-6 | Out-of-scope items absent | No WBS element matches an excluded item in A08 | Excluded item found in WBS |
| T-7 | Scope baseline dated and approved | A08 WBS section has baseline date and authority | Baseline date missing |
| T-8 | Work packages exported to A15 and A16 | A15 activity list and A16 cost inputs reference WBS work packages | Downstream artifacts not updated |

---

*Authority: PMBOK8 — Guide §2.2.2.4 Develop Scope Structure · Figure 2-17*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Sponsor or designated scope authority*
