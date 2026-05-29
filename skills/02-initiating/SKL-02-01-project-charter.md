# SKL-02-01 — Project Charter Creation
**Skill ID:** SKL-02-01  
**Skill Name:** Project Charter Creation  
**Version:** 1.0.0-draft  
**Lifecycle Pack:** 02-Initiating  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/02-initiating/SKL-02-01-project-charter.md`

---

## Purpose

Produce a formally authorized Project Charter (A04) that grants the project its official existence, names the project manager with delegated authority, establishes the high-level scope boundary, and enables the project to consume organizational resources.

This skill must be executed **once per project** — and once per phase in multi-phase predictive projects — before planning work begins.

---

## Scope

**In scope:**
- Drafting the Project Charter from required inputs
- Validating that the charter contains all mandatory fields
- Routing the draft for sponsor approval
- Linking the charter to its source business case and feasibility record

**Out of scope:**
- Business case creation → use SKL-01-02
- Detailed planning → use SKL-03-01
- Stakeholder identification → use SKL-02-02 (triggered by this skill's output)
- Governance structure → use SKL-02-04 (triggered by this skill's output)

---

## Authority and Governance

| Field | Value |
|-------|-------|
| **Primary PMI Source** | PMBOK8 |
| **Exact Section** | Guide §2.1.6.1 Initiate Project or Phase · Guide Figure 2-3 · Guide §4.5.1 |
| **Purpose of Citation** | Establish the charter as the formal authorization record for the project |
| **Source Type** | PMI-derived |
| **Governance Layer** | Project Governance |
| **Artifact Produced** | A04 — Project Charter |
| **Owner** | Sponsor (prepares with PM input) |
| **Approval Authority** | Sponsor or designated project initiating authority |
| **Threshold Band** | T3 — changes to authority boundaries, major funding, or initiation basis |
| **Escalate When** | Enterprise-level commitment or regulatory exposure involved |

---

## Performance Domains and Principles

**Performance Domains:** Governance · Stakeholders  
**Focus Area:** Initiating

| Principle | Application in This Skill |
|-----------|--------------------------|
| P1 Adopt a Holistic View | Charter must reflect full project context: organizational, strategic, environmental, and stakeholder dimensions |
| P2 Focus on Value | Charter anchors the project to the business case value rationale and defines success criteria |
| P4 Be an Accountable Leader | Charter formally assigns the PM with named authority — accountability starts here |

---

## PMBOK 8 Process: Initiate Project or Phase

### Inputs (per PMBOK8 Guide Figure 2-3)

| Input | Source | Mandatory? | Notes |
|-------|--------|-----------|-------|
| Business case | A01 — Business Case | Yes | Provides the value rationale, strategic alignment, and economic feasibility |
| Benefits management plan | A02 — Benefits and Value Measurement Record | Recommended | Benefits baseline established prior to or alongside the charter |
| Agreements | Pre-existing contracts or MOUs | Conditional | Required when the project is triggered by an external contract or agreement |
| Enterprise environmental factors (EEFs) | A05 — Context Register (or org systems) | Yes | Regulatory constraints, organizational culture, market conditions |
| Organizational process assets (OPAs) | A05 — Context Register (or org systems) | Yes | Templates, policies, past lessons, standards |
| Feasibility and viable options record | A03 | Recommended | Provides the selected option basis for the charter |
| Intake and prioritization decision record | A10 | Conditional | Required for portfolio-governed projects |

### Tools and Techniques (per PMBOK8 Guide Figure 2-3)

| Tool / Technique | When to Use |
|-----------------|------------|
| Expert judgment | Always — PM, sponsor, and key stakeholders apply domain knowledge |
| Data gathering — Brainstorming | When project purpose or scope boundary needs refinement with key parties |
| Data gathering — Focus groups | When multiple stakeholders have competing priorities that must be reconciled |
| Interpersonal and team skills — Conflict management | When disagreements about scope, authority, or success criteria arise during drafting |
| Meetings | Kickoff meeting or charter review session with sponsor and key parties |

### Outputs (per PMBOK8 Guide Figure 2-3)

| Output | Artifact ID | Description |
|--------|------------|-------------|
| **Project charter** | A04 | The formal authorization document — primary output of this skill |
| **Assumption log** | Part of A05 | Initial assumptions captured during charter development |

---

## Instructions

Execute this skill in the following sequence. The PM typically drafts the charter; the sponsor owns and approves it.

### Step 1 — Confirm Prerequisites

Before drafting, verify all of the following:

- [ ] Business case (A01) has been reviewed and approved
- [ ] Authorization decision has been made (approve / proceed)
- [ ] A project manager has been nominated
- [ ] At least one sponsor has been identified
- [ ] EEFs and OPAs are accessible (A05 or equivalent)

If any item is missing, **do not proceed**. Return to SKL-01-02 (Business Case) or SKL-01-01 (Intake Decision) as appropriate.

### Step 2 — Populate the Charter Fields

Complete all mandatory fields. Refer to the **Core Fields** section below for the complete field list with guidance on each.

Apply the following constraints:
- Keep the charter **concise** — it is an authorization record, not a plan
- Do **not** reproduce the full business case inside the charter
- Do **not** include detailed scope, WBS, or schedule — those are planning outputs
- Include only enough scope boundary to establish what the project is and what it is not
- Name the PM explicitly with the extent of their delegated authority

### Step 3 — Apply the Waste Test

Before routing for approval, check:

- [ ] Does this charter add a unique authorization record beyond what is in the business case?
- [ ] Does it avoid duplicating detailed planning content?
- [ ] Is it shorter than the business case?
- [ ] Does it name the PM and sponsor explicitly?

**If the charter repeats the complete business case and full plan set → FAIL.** Simplify before routing.

### Step 4 — Route for Approval

| Situation | Authority |
|-----------|-----------|
| Standard project | Sponsor |
| Regulated or enterprise-scale project | Sponsor + designated governing body |
| Program-initiated project | Program governance board |
| Externally contracted project | Sponsor + contract authority |

Record the approval in the charter itself or in A35 (Governance and Decision Authority Record).

### Step 5 — Trigger Downstream Skills

Once the charter is signed, immediately trigger:

| Skill | What It Does |
|-------|-------------|
| SKL-02-02 | Identify Stakeholders — uses charter as primary input |
| SKL-02-03 | Create Context Register — consolidates EEFs and OPAs |
| SKL-02-04 | Set Up Governance — uses charter authority model |
| SKL-02-05 | Make Initial Tailoring Decision — uses charter complexity factors |

---

## Core Fields — Project Charter (A04)

| Field | Mandatory? | Guidance |
|-------|-----------|---------|
| **Project title** | Yes | Unique, unambiguous name |
| **Project purpose and business need** | Yes | 1–3 sentences linking to the business case value rationale |
| **Strategic alignment** | Yes | Reference to the strategic objective or portfolio item this project serves |
| **High-level scope boundary** | Yes | What is in scope and what is explicitly out of scope; not a WBS |
| **High-level milestones** | Yes | 3–6 major milestones only; not a full schedule |
| **Budget boundary or range** | Yes | Approved funding ceiling or indicative range from the business case |
| **Named sponsor** | Yes | Full name and role; may be multiple sponsors for large projects |
| **Named project manager** | Yes | Full name, role, and explicit statement of delegated authority |
| **PM authority limits** | Yes | What the PM can and cannot decide without escalation |
| **Initial success criteria** | Yes | How the project will be judged successful; linked to the business case |
| **Key stakeholders** | Recommended | Names or groups of high-influence stakeholders; full register is A07 |
| **Known constraints** | Recommended | Budget cap, regulatory deadline, technical limitations |
| **Known assumptions** | Recommended | Captured here and transferred to A05 Assumption Log |
| **Approval signature** | Yes | Sponsor signature (wet or digital) and date |

---

## Tailoring Guidance

| Context | Tailoring Decision |
|---------|-------------------|
| Small, low-risk internal project | Single-page charter with all mandatory fields; merge with a brief feasibility note |
| Agile or adaptive project | Charter remains mandatory but may be intentionally brief; governance may shift toward self-governance per PMBOK8 §2.1.7 |
| Multi-phase predictive project | Issue a new charter at each major phase gate, or re-authorize via A35 gate record |
| Externally contracted project | Charter must align with contractual scope boundary; legal review may be required |
| Regulated environment | Charter may need compliance sign-off beyond sponsor approval; record in A06 Tailoring Decision Record |

**Do not tailor away:**
- PM authority statement (P4 — non-negotiable for accountability)
- Sponsor identification and signature
- Link to business case and success criteria (P2)

---

## Failure Cases

| Failure | Indicator | Corrective Action |
|---------|-----------|-----------------|
| Charter drafted without approved business case | Business case pending or not found | Stop; return to SKL-01-02 |
| Charter contains full plan content | Document exceeds 5–6 pages and includes WBS, schedule, or risk register | Remove planning content; route those to Pack 03 skills |
| PM authority not stated | PM named but no scope of authority documented | Clarify with sponsor and restate explicitly |
| Sponsor not identified or not signing | Charter approved by PM or delegated to PM | Escalate; sponsor signature is mandatory |
| Charter replicates the business case verbatim | Same narrative text appears in both documents | Summarize business case rationale in 2–3 sentences; cite A01 by reference |
| Phase gate charter not issued in multi-phase project | Phase 2 starts without re-authorization | Issue phase charter or use A35 gate record with formal proceed decision |

---

## Outputs Produced by This Skill

| Output | Location | Notes |
|--------|---------- |-------|
| Signed Project Charter | `artifacts/templates/A04-project-charter.md` (filled) | Primary deliverable |
| Assumption Log entries | A05 (Context Register) | Transfer assumptions captured during charter drafting |
| Downstream skill trigger list | Internal record | Document which Pack 02 skills are immediately triggered |

---

## Integration Points

| Connected Artifact or Skill | Relationship |
|----------------------------|-------------|
| A01 Business Case | Input — charter derives authority from the approved business case |
| A02 Benefits Record | Input — charter references success criteria and benefit measures |
| A03 Feasibility Record | Input — charter reflects the selected option from feasibility analysis |
| A05 Context Register | Bidirectional — EEFs and OPAs feed the charter; assumptions from the charter feed A05 |
| A06 Tailoring Decision Record | Downstream — charter triggers the initial tailoring assessment |
| A07 Stakeholder Register | Downstream — charter provides the initial stakeholder list for A07 |
| A35 Governance Record | Downstream — charter authority model feeds the governance setup |
| A14 Integrated Plan | Downstream — all planning builds on the charter as its foundation |

---

## Tests

### Test T-1: Minimum Valid Charter
**Given:** An approved business case and a nominated PM  
**When:** SKL-02-01 is executed  
**Then:** The output must contain all 9 mandatory fields, must be signed by the sponsor, and must not reproduce the full business case

### Test T-2: Waste Test Pass
**Given:** A draft charter with full planning content included  
**When:** Waste test is applied in Step 3  
**Then:** The skill must return FAIL and require removal of planning content before routing

### Test T-3: Missing Business Case Prerequisite
**Given:** No approved business case exists  
**When:** Step 1 prerequisite check is run  
**Then:** The skill must halt and return "Return to SKL-01-02 — Business Case not approved"

### Test T-4: Adaptive Tailoring
**Given:** An adaptive (Agile) project context  
**When:** Charter is drafted with tailoring applied  
**Then:** The charter must still include PM authority, sponsor, and success criteria — but may omit detailed milestone dates

### Test T-5: Multi-phase Gate Charter
**Given:** A predictive project entering Phase 2  
**When:** SKL-02-01 is executed for phase re-authorization  
**Then:** The output must reference the prior charter and the gate decision (A35) and must state the new phase scope boundary

---

## Examples

### Example A — Internal IT Project (Predictive, Low Risk)

> **Project Title:** Customer Data Migration — Phase 1  
> **Purpose:** Migrate legacy customer records to the new CRM platform to eliminate data duplication and improve service response times, as justified in Business Case A01-2026-017.  
> **Scope Boundary:** In scope — migration of records from System A and System B. Out of scope — CRM user training and reporting module configuration.  
> **Budget Boundary:** Not to exceed USD 120,000 without sponsor re-authorization.  
> **Named Sponsor:** [Name], VP Operations  
> **Named PM:** [Name], authority to approve changes within 10% of baseline cost and 5-day schedule variance without escalation.  
> **Success Criteria:** 100% of records migrated with zero data loss; system go-live by Q3 2026.  
> **Approved:** [Sponsor Signature] [Date]

### Example B — Adaptive Software Product

> **Project Title:** Mobile Loyalty App — MVP Release  
> **Purpose:** Deliver a minimum viable product loyalty application to capture early market share per strategic initiative S-2026-04.  
> **Scope Boundary:** In scope — core loyalty points, redemption flow, and user account. Out of scope — partner integrations and analytics dashboard (future releases).  
> **Budget Boundary:** Sprint funding approved for 3 months at USD 45,000/month; continuation subject to sprint review outcomes.  
> **Named Sponsor:** [Name], Chief Digital Officer  
> **Named PM / Product Lead:** [Name], authority to reprioritize backlog items within approved release scope without escalation.  
> **Success Criteria:** App live in app stores with 500 active users within 60 days of launch; NPS ≥ 35.  
> **Approved:** [Sponsor Signature] [Date]

---

## Companion References

| Alias | Source | Relevant Section |
|-------|--------|-----------------|
| PMBOK8 | PMBOK Guide 8th Edition | §2.1.6.1 Initiate Project or Phase · Figure 2-3 |
| PMBOK8 | The Standard for Project Management | §3.5 P4 Be an Accountable Leader · §3.3 P2 Focus on Value |
| Process-Groups | Process Groups Practice Guide | Initiating Process Group |
| PMI-BA | Business Analysis Practice Guide | Project initiation and needs analysis |
| Forms-Book | PMI Practice Standard Forms | Project Charter template reference |

---

*Source Type: PMI-derived*  
*Governance Layer: Project Governance*  
*Authority: PMBOK8 §2.1.6.1 · Figure 2-3 · Standard §3.5*  
*Linked Artifact: A04 — Project Charter*  
*Related Skills: SKL-01-02 · SKL-02-02 · SKL-02-03 · SKL-02-04 · SKL-02-05*
