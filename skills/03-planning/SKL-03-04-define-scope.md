---
skill_id: SKL-03-04
skill_name: Define Scope
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A08 — Scope and Requirements Decision Record (Project Scope Statement section)"
artifacts_updated:
  - "A06 — Tailoring Decision Record (scope-driven tailoring updates)"
pmbok8_process_anchor: "Guide §2.2.2.3 Define Scope · Figure 2-16"
performance_domains:
  - Scope
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-03 — Requirements baseline in A08 must be approved"
downstream_skills:
  - "SKL-03-05 — Develop Scope Structure (WBS)"
file_path: "skills/03-planning/SKL-03-04-define-scope.md"
tests: 8
version: "1.0.0"
---

# SKL-03-04 — Define Scope

**Skill ID:** SKL-03-04  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.2.2.3 Define Scope · Figure 2-16  
**File path:** `skills/03-planning/SKL-03-04-define-scope.md`

---

## Purpose

Produce a detailed project scope statement that describes in-scope deliverables, out-of-scope exclusions, assumptions, constraints, and acceptance criteria — serving as the authoritative scope boundary for all downstream planning and control.

---

## Scope

This skill covers scope statement definition only. Requirements elicitation was completed in SKL-03-03. WBS decomposition follows in SKL-03-05. Scope baseline (scope statement + WBS + WBS dictionary) is completed when SKL-03-05 is done.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Approved requirements baseline | A08 | Yes |
| Project Charter | A04 | Yes |
| Context Register | A05 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Feasibility and Viable Options Record | A03 | If exists |

**Gate check:** Requirements in A08 must be approved before scope is defined. Defining scope before requirements approval produces an ungrounded scope statement.

---

## Instructions

### Step 1 — Review approved requirements
1. Read the approved requirements baseline in A08.
2. Group requirements by deliverable or product component to identify logical scope boundaries.
3. Identify any requirements flagged as deferred or out of scope in SKL-03-03 — these become candidates for the out-of-scope exclusions list.

### Step 2 — Draft in-scope deliverables
1. List each major deliverable or product component explicitly.
2. For each deliverable, write a clear description sufficient for a stakeholder to confirm whether it is included.
3. Reference the requirement ID(s) that each deliverable satisfies.
4. For adaptive approaches, the in-scope section describes the product vision and high-level capability set; detailed features remain in the backlog.

### Step 3 — Define explicit exclusions
1. List items that are explicitly out of scope — do not assume exclusions are implied.
2. Include items that stakeholders may assume are in scope unless excluded (common scope creep sources).
3. Reference any requirements that were deferred and the reason for deferral.

### Step 4 — Document assumptions and constraints
1. List planning assumptions that the scope statement depends on (resource availability, technology readiness, regulatory timeline, etc.).
2. List constraints that limit scope definition options (budget ceiling, regulatory mandates, technology standards, contractual obligations).
3. Cross-reference A05 (Context Register) — do not duplicate entries; reference instead.

### Step 5 — Define acceptance criteria
1. For each major deliverable, specify the minimum criteria that must be met for the deliverable to be formally accepted.
2. Acceptance criteria must be measurable — avoid subjective language ("good quality", "user-friendly").
3. Name the acceptance authority for each deliverable (consistent with A08 scope management plan).

### Step 6 — Validate scope statement against requirements
1. Verify every approved requirement is traceable to at least one in-scope deliverable.
2. Verify no deliverable is included that has no requirement source — remove or raise as a change.
3. Confirm exclusions do not contradict charter commitments (A04).

### Step 7 — Obtain approval and update A06 if needed
1. Present scope statement to sponsor or designated approval authority.
2. If the scope statement reveals complexity or tailoring decisions not captured in A06, update A06 before approval.
3. Record approval authority name and date in A08 Project Scope Statement section.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Project Scope Statement | A08 | Project Scope Statement section |
| Tailoring updates (if triggered) | A06 | Tailoring Decision Record |

---

## Constraints

- Do not proceed to WBS development (SKL-03-05) without an approved scope statement.
- Acceptance criteria must be measurable — reject vague criteria before approval.
- Do not add deliverables with no requirement source without raising a change through A12.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / internal | One-page scope statement with bullet list of deliverables and exclusions is sufficient |
| Predictive / formal | Structured scope statement with full acceptance criteria and explicit assumption/constraint list |
| Adaptive | Product goal + high-level capability set; individual acceptance criteria live at backlog item level |
| Regulatory / contractual | Scope statement must reference specific contractual clauses; acceptance criteria must match contract terms |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Requirements not approved | Scope written before requirements approval | Stop; complete SKL-03-03 approval step first |
| Deliverable without requirement source | Extra deliverable added without a requirement | Remove or raise as change through A12 |
| Requirement not traceable to deliverable | Approved requirement has no corresponding deliverable | Add deliverable or reclassify requirement as out of scope |
| Vague acceptance criteria | "System shall perform well" | Replace with measurable criteria before approval |
| Exclusions not explicit | Out-of-scope items assumed rather than stated | List all material exclusions explicitly |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — requirements approved | A08 requirements section status = Approved | Requirements in Draft |
| T-2 | In-scope deliverables listed | At least one explicit deliverable per major requirement group | Scope statement contains only vague product description |
| T-3 | Explicit exclusions documented | Out-of-scope list present with at least one entry | No exclusions section or "N/A" without rationale |
| T-4 | Every deliverable traces to a requirement | Each deliverable has at least one A08 requirement ID reference | Deliverable with no requirement source |
| T-5 | Every approved requirement traces to a deliverable | No orphan approved requirements | Requirement with no deliverable mapping |
| T-6 | Acceptance criteria are measurable | All acceptance criteria use quantifiable or verifiable language | Any criterion uses subjective language |
| T-7 | Assumptions and constraints documented | At least one assumption and one constraint listed, or explicit statement that none apply | Section blank |
| T-8 | Approval documented | Approval authority name and date in A08 | Scope statement unapproved |

---

*Authority: PMBOK8 — Guide §2.2.2.3 Define Scope · Figure 2-16*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Sponsor, product owner, or customer representative*
