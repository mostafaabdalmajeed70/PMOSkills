---
skill_id: SKL-01-01
skill_name: Establish PM Governance Framework
pack: "01 — Organizational Setup"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A05 — Context Register (Governance section)"
artifacts_updated:
  - "A06 — Project Management Plan (governance reference)"
  - "A04 — Project Charter (authority thresholds reference)"
pmbok8_process_anchor: "PMBOK8 Standard §3 Principles · Guide §2.1 Project Integration Management · AUTHORITY-ROUTING.md"
performance_domains:
  - Governance
  - Stakeholders
focus_area: Organizational Setup
upstream_prerequisites:
  - "A01 — Business Case or equivalent authorization trigger must exist"
downstream_skills:
  - "SKL-01-02 — Define Artifact and Document Control Standards"
  - "SKL-01-03 — Configure Project Repository and Tool Environment"
  - "SKL-02-01 — Initiate Project or Phase"
file_path: "skills/01-organizational-setup/SKL-01-01-establish-pm-governance-framework.md"
tests: 9
---

# SKL-01-01 — Establish PM Governance Framework

**Skill ID:** SKL-01-01  
**Pack:** 01 — Organizational Setup  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** PMBOK8 Standard §3 Principles · Guide §2.1 · AUTHORITY-ROUTING.md  
**File path:** `skills/01-organizational-setup/SKL-01-01-establish-pm-governance-framework.md`

---

## Purpose

Establish the governance framework that will govern all project activity in this repository — defining authority levels, decision rights, escalation thresholds, role accountability, and the operating rules that all downstream skills and artifacts must respect. The output is the Governance section of A05 (Context Register), which becomes the single authority reference for all project governance decisions.

---

## Scope

This skill covers organizational-level governance setup only. It does not initiate a specific project (SKL-02-01), define scope (SKL-03-02 through SKL-03-05), or configure tooling (SKL-01-03). It runs once per organizational setup or when a significant governance restructuring occurs. It may be re-run at program level or for projects with unique governance requirements.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Business case or authorization trigger | A01 | Yes |
| Organizational structure information | EEF (Enterprise Environmental Factors) | Yes |
| PMI PMBOK8 Standard — Governance Principles | PMBOK8 Standard §3.8 | Yes |
| Authority Routing reference | AUTHORITY-ROUTING.md | Yes |
| Existing OPA (policies, templates, standards) | A05 prior version or organizational source | If available |

**Gate check:** A01 (Business Case) or equivalent authorization trigger must exist before this skill runs. If no authorization exists, stop and obtain organizational or sponsor authorization.

---

## Instructions

### Step 1 — Identify Governance Stakeholders
1. Identify the sponsor, governing body, PMO (if applicable), and key decision-making authorities.
2. Confirm who holds ultimate project authorization authority (charter sign-off).
3. Confirm who holds authority to approve scope changes, budget changes, schedule changes, and exceptions.
4. Confirm who holds authority to close the project or phase.
5. Document all identified authorities in A05 Governance section.

### Step 2 — Define Authority Thresholds
1. Open AUTHORITY-ROUTING.md and extract the authority threshold matrix.
2. For each decision type (scope change, cost change, schedule change, risk acceptance, contract award, exception), assign:
   - **PM authority level** — decisions the PM can make independently
   - **Sponsor authority level** — decisions requiring sponsor approval
   - **Governing body / steering committee level** — decisions requiring escalation beyond sponsor
3. Express thresholds in measurable terms where possible (e.g., cost variance >10% BAC requires sponsor approval).
4. Record all thresholds in A05 Governance section.

### Step 3 — Define Decision Rights and RACI for Governance
1. For each governance decision type, define who is:
   - **Responsible** — prepares the decision package
   - **Accountable** — makes the final call
   - **Consulted** — must be consulted before decision
   - **Informed** — notified after decision
2. Align RACI assignments with authority thresholds from Step 2.
3. Record governance RACI in A05 Governance section.

### Step 4 — Define Escalation Path
1. Map the escalation path for each decision type:
   - Level 1: PM resolves independently
   - Level 2: PM escalates to sponsor
   - Level 3: Sponsor escalates to steering committee or governing body
   - Level 4: Program-level or organizational executive escalation
2. Define escalation triggers — what conditions require moving from Level N to Level N+1.
3. Define escalation timeframe — maximum hours/days before escalation is mandatory.
4. Document the escalation path in A05 Governance section.

### Step 5 — Define Governance Meeting Cadence
1. Identify governance review touchpoints:
   - Project status reviews (frequency, attendees, format)
   - Phase gate reviews (entry/exit criteria, decision authority)
   - Exception reviews (trigger, timing, participants)
   - Steering committee or board reviews (if applicable)
2. Document cadence, participants, and decision scope for each meeting type in A05.

### Step 6 — Define Compliance and Audit Requirements
1. Identify any regulatory, legal, contractual, or organizational compliance obligations that apply to project governance.
2. Define audit or review obligations (internal audit, PMO review, external compliance check).
3. Record compliance requirements and their governance implications in A05.

### Step 7 — Align with PMBOK8 Governance Principles
1. Confirm that the established governance framework is consistent with PMBOK8 Standard §3 Principles, specifically:
   - Principle 3: Effectively engage with stakeholders
   - Principle 4: Focus on value
   - Principle 8: Navigate complexity
   - Principle 9: Optimize risk responses
   - Principle 11: Embrace adaptability and resiliency
   - Principle 12: Enable change to achieve the envisioned future state
2. Note any deliberate deviations with rationale in A05.

### Step 8 — Finalize and Baseline A05 Governance Section
1. Review the complete Governance section of A05 with the sponsor and key governance stakeholders.
2. Obtain formal sign-off or acknowledgment.
3. Record the baseline date and version in A05.
4. Distribute to all project managers and team leads who will operate under this framework.

---

## Outputs

| Output | Artifact | Section | Notes |
|---|---|---|---|
| Governance framework | A05 | Governance section | Authority thresholds, decision rights, escalation path, cadence, compliance |
| Authority reference | AUTHORITY-ROUTING.md | Full document | Pre-existing — confirm alignment, update if needed |
| Governance reference | A06 | Governance reference section | Subsidiary pointer only — A05 is the authority |

---

## Constraints

- Authority thresholds must be measurable — vague statements like "significant changes" are not acceptable.
- All downstream skills must reference A05 for authority and escalation decisions — no parallel governance documents.
- This skill does not define project-specific scope, schedule, or cost — those are Planning skills.
- Governance RACI must not conflict with the project-level RACI in A25.
- Compliance obligations must be stated explicitly — they cannot be implied.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / single-PM project | Streamlined governance: two authority levels (PM and sponsor). Single escalation path. Minimal cadence. |
| Large / multi-phase project | Full four-level authority matrix. Formal phase gate governance. Steering committee cadence. |
| Program-level setup | Add program governance layer above project sponsor. Define inter-project authority and conflict resolution rules. |
| Regulated environment | Add compliance section with specific regulatory references, audit schedule, and sign-off requirements. |
| Adaptive / agile project | Governance adapts: product owner holds acceptance authority; sprint reviews serve as governance touchpoints. |
| Hybrid project | Split governance: predictive components use threshold-based escalation; adaptive components use product owner authority. |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| No authorization trigger | No A01 or equivalent — governance built in a vacuum | Stop; obtain organizational authorization before proceeding |
| Thresholds are vague | "Significant changes" — no measurable definition | Rewrite all thresholds with numeric or categorical precision |
| RACI conflicts with A25 | PM is Accountable in governance but not in team RACI | Reconcile A05 governance RACI with A25 team RACI |
| Escalation path not defined | Disputes held at PM level beyond PM authority | Add escalation path with explicit triggers and timeframes |
| Compliance obligations not identified | Regulatory requirement discovered mid-project | Re-run Step 6; update A05; assess downstream impact |
| Governance framework not distributed | Project team unaware of authority thresholds | Distribute A05 to all PMs and team leads; confirm receipt |
| Authority thresholds not aligned with AUTHORITY-ROUTING.md | Conflicting decision rules in two documents | Reconcile; A05 governs project; AUTHORITY-ROUTING.md governs repo |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Authorization trigger exists | A01 or equivalent exists and is accessible | No authorization trigger; governance built without mandate |
| T-2 | Authority thresholds defined and measurable | All decision types have numeric or categorical thresholds | Any threshold is vague or missing |
| T-3 | Governance RACI complete | Every governance decision type has R, A, C, I assigned | Any decision type with no RACI entry |
| T-4 | Escalation path documented | All four escalation levels defined with triggers and timeframes | Escalation path absent or incomplete |
| T-5 | Governance cadence documented | All meeting types have frequency, participants, and decision scope | Any meeting type with no documented cadence |
| T-6 | PMBOK8 principles alignment confirmed | Step 7 review completed; deviations documented | Principles alignment check skipped |
| T-7 | A05 Governance section baselined | A05 has version, baseline date, and sign-off | A05 Governance section in draft without sign-off |
| T-8 | No conflict with AUTHORITY-ROUTING.md | A05 thresholds consistent with repo-level routing rules | Conflicting authority statements in two documents |
| T-9 | Framework distributed | All PMs and team leads have received A05 Governance section | Framework exists but not distributed |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Standard §3 Principles · Guide §2.1 Project Integration Management · AUTHORITY-ROUTING.md*  
*Source type: PMI-derived*  
*Owner: PMO / Organizational governance authority*  
*Approval authority: Sponsor or governing body*
