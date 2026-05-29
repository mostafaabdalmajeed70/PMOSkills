---
skill_id: SKL-03-03
skill_name: Elicit and Analyze Requirements
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A08 — Scope and Requirements Decision Record (Requirements section)"
artifacts_updated:
  - "A07 — Stakeholder Register (requirements-driven updates)"
  - "A19 — Risk Management Record (requirements-related risks)"
pmbok8_process_anchor: "Guide §2.2.2.2 Elicit and Analyze Requirements · Figure 2-15"
performance_domains:
  - Scope
  - Stakeholders
focus_area: Planning
upstream_prerequisites:
  - "SKL-03-02 — Scope Management Plan section of A08 must be complete"
  - "SKL-02-02 — A07 Identification section must be complete"
downstream_skills:
  - "SKL-03-04 — Define Scope"
  - "SKL-03-08 — Plan Communications Management (requirements inform communication needs)"
file_path: "skills/03-planning/SKL-03-03-elicit-analyze-requirements.md"
tests: 9
version: "1.0.0"
---

# SKL-03-03 — Elicit and Analyze Requirements

**Skill ID:** SKL-03-03  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.2.2.2 Elicit and Analyze Requirements · Figure 2-15  
**File path:** `skills/03-planning/SKL-03-03-elicit-analyze-requirements.md`

---

## Purpose

Elicit, document, and analyze stakeholder requirements to produce a requirements baseline in A08 that is traceable, prioritized, and approved by the appropriate authority before scope definition begins.

---

## Scope

This skill covers elicitation and analysis only. Scope definition (project scope statement) and WBS decomposition are SKL-03-04 and SKL-03-05. Requirements management plan was established in SKL-03-02.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Project Charter | A04 | Yes |
| Scope Management Plan section | A08 | Yes |
| Stakeholder Register (identification) | A07 | Yes |
| Context Register (OPA — templates, lessons) | A05 | Yes |
| Feasibility and Viable Options Record | A03 | If exists |

**Gate check:** SKL-03-02 must be complete. Scope management approach must be decided before elicitation begins to ensure requirements are captured in the right format.

---

## Instructions

### Step 1 — Identify elicitation participants
1. From A07, identify stakeholders with requirements input authority: product owners, customers, subject matter experts, regulatory bodies, end users.
2. Confirm availability and elicitation method for each participant.
3. For adaptive approaches, confirm that the product owner holds requirements authority.

### Step 2 — Select and apply elicitation techniques
Apply one or more of the following based on stakeholder availability and project context:

| Technique | Best for |
|---|---|
| Interviews | High-influence individual stakeholders |
| Focus groups | Group of homogeneous end users |
| Facilitated workshops / JAD | Cross-functional groups needing consensus |
| Observation / job shadowing | Process-embedded or tacit requirements |
| Questionnaires / surveys | Large dispersed stakeholder groups |
| Prototyping | Unclear or evolving requirements |
| Benchmarking | External standards or competitor comparison |
| Document analysis | Existing contracts, regulations, system specs |

Record elicitation session outputs as raw requirement statements before analysis.

### Step 3 — Analyze and classify requirements
1. For each raw requirement, classify into: Business / Stakeholder / Solution / Transition / Project / Quality / Compliance.
2. Identify conflicts between requirements from different stakeholders; resolve through facilitation or escalation.
3. Assess completeness — identify gaps or unstated assumptions.
4. Assess feasibility — flag requirements that may be technically, financially, or schedule-constrained.
5. For adaptive approaches, express requirements as user stories or backlog items with acceptance criteria.

### Step 4 — Prioritize requirements
1. Apply a prioritization method: MoSCoW (Must / Should / Could / Won't), weighted ranking, or product owner priority queue.
2. Document the priority basis and authority who assigned priority.
3. Flag requirements that are deferred or out of scope for this project phase.

### Step 5 — Build traceability
1. Assign a unique ID to each requirement.
2. Trace each requirement to its source stakeholder (A07 reference) and to its parent business need or charter objective (A04 reference).
3. For predictive approaches, traceability will extend forward to WBS elements (SKL-03-05) and test/acceptance items.

### Step 6 — Obtain requirements approval
1. Present requirements baseline to the acceptance authority identified in A08 Scope Management Plan section.
2. Resolve open items before approval.
3. Document approval in A08 with authority name and date.

### Step 7 — Update linked artifacts
1. Update A07 if requirements elicitation revealed new stakeholders, changed influence levels, or new communication needs.
2. Flag any requirements-related risks in A19 (regulatory requirements not met, feasibility concerns, conflicting priorities).
3. Confirm A08 requirements section is complete and approved.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Requirements baseline | A08 | Requirements section |
| Stakeholder updates (if any) | A07 | Stakeholder entries |
| Requirements-related risks | A19 | Risk Register |

---

## Constraints

- Do not begin defining scope (project scope statement) until requirements are approved.
- For adaptive approaches: requirements expressed as prioritized backlog items with acceptance criteria are sufficient — do not force a structured requirements document.
- Requirements conflicts must be resolved before approval — do not baseline conflicting requirements.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / internal | Informal workshop + structured requirement list sufficient |
| Regulatory / contractual | Formal elicitation, full traceability matrix, signed approval |
| Adaptive | Product backlog with prioritized user stories and Definition of Ready |
| Hybrid | Formal requirements for fixed components; backlog for adaptive components |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| Elicitation skipped | Requirements assumed from charter | Conduct at least one structured elicitation session |
| No traceability | Requirements cannot be linked to A07 or A04 | Assign IDs and trace to source before approval |
| Conflicting requirements baselined | Requirements contradict each other | Facilitate resolution before approval |
| No approval authority | Requirements signed off by wrong role | Verify acceptance authority in A08 scope management plan |
| Requirements scope creep | Requirements added after approval without A12 entry | Enforce change control via A12 |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — SKL-03-02 complete | A08 Scope Management Plan section populated | Section blank or missing |
| T-2 | Elicitation conducted | At least one structured elicitation technique applied and documented | No evidence of elicitation |
| T-3 | All A07 stakeholders with input authority engaged | Every input-authority stakeholder has a documented elicitation touchpoint | Gap in stakeholder coverage |
| T-4 | Requirements classified | Each requirement has a type label | Unclassified requirements present |
| T-5 | Requirements prioritized | Each requirement has an explicit priority | All requirements marked equal priority or priority absent |
| T-6 | Traceability to A07 and A04 | Every requirement has a source stakeholder ID and a charter objective reference | Orphan requirements present |
| T-7 | Conflicts resolved | No two approved requirements contradict each other | Conflicting requirements in approved baseline |
| T-8 | Approval documented | Approval authority name and date recorded in A08 | Requirements section marked unapproved |
| T-9 | Requirements-related risks in A19 | Feasibility flags or compliance risks entered in A19 | Known requirements risks not recorded |

---

*Authority: PMBOK8 — Guide §2.2.2.2 Elicit and Analyze Requirements · Figure 2-15*  
*Source type: PMI-derived*  
*Owner: Project manager and business analysis lead*  
*Approval authority: Sponsor, product owner, or customer representative per A08 scope management plan*
