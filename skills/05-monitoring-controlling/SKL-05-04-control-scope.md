---
skill_id: SKL-05-04
skill_name: Control Scope
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A08 — Scope Baseline Record"
artifacts_updated:
  - "A12 — Integrated Change Log (scope change requests)"
  - "A17 — Integrated Performance Reporting Record (scope section)"
  - "A18 — Issue, Impediment and Action Log (scope issues)"
pmbok8_anchor: "Guide §2.4.2.5 Control Scope · Process Groups Practice Guide §5.5"
performance_domains:
  - Scope
  - Delivery
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-03-03 — A08 scope baseline must be approved"
  - "SKL-05-03 — A12 change control process must be active"
downstream_skills:
  - "SKL-05-05 — Control Schedule (scope changes affect schedule)"
  - "SKL-05-06 — Control Costs (scope changes affect cost)"
file_path: "skills/05-monitoring-controlling/SKL-05-04-control-scope.md"
tests: 8
---

# SKL-05-04 — Control Scope

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A08 — Scope Baseline Record
**PMBOK8 Anchor:** Guide §2.4.2.5 · Process Groups Practice Guide §5.5

---

## Purpose

Control Scope monitors project and product scope against the approved A08 scope baseline, detects unauthorized scope additions (gold plating and scope creep), manages scope change requests through A12, and ensures the A08 baseline is updated only after formal approval. This skill is the primary defense against uncontrolled scope expansion.

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Scope baseline | A08 | WBS, WBS Dictionary, scope statement | Approved |
| Work package status | A08 / A18 | WBS status + issue log | Current |
| Change requests | A12 | Pending items | Current |
| Requirements traceability | A09 | RTM | Current |
| Deliverable acceptance records | A10 | Acceptance log | Current |
| Performance report | A17 | Scope section | Current |

---

## Steps

### Step 1 — Compare Delivered Work to Scope Baseline
At each reporting period, review the status of all active work packages in A08 against the approved WBS and WBS Dictionary:
- Is each work package delivering exactly what the WBS Dictionary defines?
- Are any work packages producing deliverables not in the WBS?
- Are any requirements in A09 RTM not traceable to a WBS work package?

### Step 2 — Detect Scope Creep and Gold Plating
Identify unauthorized scope additions:

| Type | Definition | Detection method |
|---|---|---|
| Scope creep | Gradual, undocumented addition of features or work | WBS Dictionary review; deliverable comparison |
| Gold plating | Team adds unrequested enhancements to deliverables | Deliverable review against acceptance criteria in A10 |
| Requirements drift | Requirements added informally without RTM update | A09 RTM audit; stakeholder interview |

For every instance detected, log in A18 as a scope issue and flag for A12 change request.

### Step 3 — Process Scope Change Requests
For every scope change request in A12:
- Verify the request is documented with full description and requestor in A12
- Perform impact assessment per SKL-05-03 (scope, schedule, cost, quality, risk dimensions)
- Route to appropriate authority per A06
- If approved: update A08 WBS and WBS Dictionary; update A09 RTM; update A10 acceptance criteria as needed
- If rejected: record rationale; notify requestor

### Step 4 — Verify Scope Delivery Progress
Review deliverable completion against A08 WBS completion criteria:
- Work packages with status = Complete must have corresponding A10 acceptance record
- Work packages past due without completion must be logged in A18 with impact assessment
- Track WBS completion % and trend in A17 scope section

### Step 5 — Update A17 Scope Section
Record scope control findings in A17:
- % of WBS work packages complete
- Scope creep or gold plating instances identified
- Change requests submitted, approved, and rejected this period
- Cumulative approved scope change (additive and reductive)
- Scope delivery forecast vs. plan

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Scope performance information | A17 | Scope section |
| Scope change requests | A12 | Pending items |
| Updated scope baseline | A08 | WBS + WBS Dictionary (approved changes only) |
| Scope issues | A18 | Issue log |
| Updated RTM | A09 | Requirement status |

---

## Operating Rules

1. No scope addition is permitted without an Approved A12 entry — verbal authorizations are not scope approvals.
2. Gold plating is treated the same as scope creep — both require documentation and either A12 approval or removal.
3. Every completed work package must have a corresponding A10 acceptance record before being marked Complete in A08.
4. A09 RTM must remain synchronized with A08 WBS at all times.
5. Scope delivery forecast must be updated in A17 at every reporting period.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Scope creep undetected | Deliverables larger than WBS Dictionary definition with no A12 entry | Immediate WBS Dictionary audit; log in A18; raise A12 for each addition found |
| Gold plating normalized | Team considers enhancements standard practice; no documentation | Team briefing; retrospective review of delivered work; log additions in A12 retroactively |
| A08 updated without A12 Approved | WBS changes with no A12 cross-reference | Retroactive A12 entry; assess authorization; sponsor notification if above PM threshold |
| A09 RTM not updated after scope change | Requirements in A09 reference outdated WBS codes after approved change | Reconcile A09 RTM against current A08 WBS; update all affected requirement-to-WBS links |
| Completed work packages without A10 acceptance | A08 shows work package complete; A10 has no acceptance record | Retroactive acceptance verification; A10 entry required before work package is closed |
| Scope forecast not updated | A17 scope section shows no forecast revision despite late work packages | Immediate scope delivery forecast update; assess impact on project completion date |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Scope baseline approved | A08 WBS and WBS Dictionary approved before Control Scope begins | Control Scope active with no approved A08 baseline |
| T-2 | WBS Dictionary audit | All active work packages reviewed against WBS Dictionary at each period | Period passes with no WBS Dictionary review |
| T-3 | Scope creep detection | Unauthorized scope additions identified within same reporting period | Scope addition undetected for more than one reporting period |
| T-4 | A12 for scope changes | All scope changes have A12 change request before baseline update | Scope change made without A12 Approved entry |
| T-5 | A09 RTM synchronized | A09 RTM updated after every approved scope change | A09 RTM out of sync with current A08 WBS |
| T-6 | A10 acceptance for completed work | Every Work Package marked Complete has an A10 acceptance record | Work package Complete status without A10 entry |
| T-7 | Scope issues in A18 | Scope creep, gold plating, or delivery gaps logged in A18 | Scope issue discovered but not in A18 |
| T-8 | A17 scope section updated | A17 includes scope performance and forecast at every period | A17 scope section not updated for one or more periods |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.4.2.5 · Process Groups Practice Guide §5.5*
*Source type: PMI-derived*
