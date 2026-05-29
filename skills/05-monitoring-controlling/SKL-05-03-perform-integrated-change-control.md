---
skill_id: SKL-05-03
skill_name: Perform Integrated Change Control
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A12 — Integrated Change Log"
artifacts_updated:
  - "A08 — Scope Baseline Record (if scope baseline updated)"
  - "A15 — Schedule Baseline Record (if schedule baseline updated)"
  - "A16 — Financial Management and Cost Baseline Record (if cost baseline updated)"
  - "A17 — Integrated Performance Reporting Record (updated after approved changes)"
pmbok8_anchor: "Guide §2.1.6.8 Perform Integrated Change Control · Process Groups Practice Guide §5.4"
performance_domains:
  - Governance
  - Delivery
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-05-02 — Change requests must flow from Monitor and Control Project Work"
  - "SKL-03-02 — A12 Change Management Plan must be complete"
downstream_skills:
  - "SKL-05-04 — Control Scope"
  - "SKL-05-05 — Control Schedule"
  - "SKL-05-06 — Control Costs"
file_path: "skills/05-monitoring-controlling/SKL-05-03-perform-integrated-change-control.md"
tests: 9
---

# SKL-05-03 — Perform Integrated Change Control

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A12 — Integrated Change Log
**PMBOK8 Anchor:** Guide §2.1.6.8 · Process Groups Practice Guide §5.4

---

## Purpose

Perform Integrated Change Control reviews all change requests, evaluates their impact on project baselines and objectives, routes them for approval at the correct authority level, and updates all affected artifacts after approval. No baseline may be changed without an Approved entry in A12.

---

## Change Request Types

| Type | Description | Typical trigger |
|---|---|---|
| Corrective action | Action to realign project performance with the plan | Variance identified in A17 |
| Preventive action | Action to reduce risk of future performance deviation | Risk response in A19 |
| Defect repair | Fix to a non-conforming deliverable | Quality audit or inspection result |
| Scope change | Addition, removal, or modification of scope | Stakeholder request; regulatory change |
| Schedule change | Revision to the schedule baseline | Critical path slip; resource constraint |
| Cost change | Revision to the cost baseline or budget | Cost overrun; approved scope addition |

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Change requests | A12 | Pending items | Current |
| Change management plan | A12 | §1 plan section | Complete |
| Authority thresholds | A06 | §4 authority levels | Current |
| All baselines | A08, A15, A16 | Baseline sections | Approved |
| Performance report | A17 | Current period | Current |

---

## Steps

### Step 1 — Receive and Register Change Request
For every change request submitted to A12:
- Assign a unique Change ID
- Record: requestor, date submitted, type, description, affected baseline(s)
- Set status = Pending Review
- Confirm completeness — reject incomplete requests back to requestor for rework

### Step 2 — Assess Impact
For each Pending Review change request, perform an integrated impact assessment:

| Dimension | Assessment question | Source artifact |
|---|---|---|
| Scope | Does this add, remove, or modify scope? | A08 WBS |
| Schedule | Does this change the critical path or finish date? | A15 schedule model |
| Cost | Does this change BAC, EAC, or reserve? | A16 cost baseline |
| Quality | Does this affect quality standards or acceptance criteria? | A20 quality plan |
| Risk | Does this introduce new risks or close existing ones? | A19 risk register |
| Stakeholders | Does this affect stakeholder expectations or agreements? | A07 register |
| Resources | Does this change resource requirements? | A26 resource plan |

Document findings in A12 impact assessment section for each dimension affected.

### Step 3 — Determine Approval Authority
Using A06 authority thresholds, determine who must approve the change:

| Change value / impact | Approval authority |
|---|---|
| Within PM authority threshold | PM approves independently |
| Above PM threshold, within sponsor threshold | Sponsor approval required |
| Above sponsor threshold | Change Control Board (CCB) or governance body required |
| Contract-related change | Procurement/legal review + CCB |

Record the required approver(s) in A12.

### Step 4 — Route for Decision
Submit the change request and impact assessment to the required approver(s):
- Use the communication channel specified in A12 §1 change management plan
- Set a decision due date (from A12 plan — typically 5 business days default)
- Track decision status in A12

### Step 5 — Record Decision and Update Status
Record the decision in A12:
- **Approved:** proceed to baseline update
- **Rejected:** record rationale; notify requestor; no baseline change
- **Deferred:** set review date; retain in Pending Review status
- **Withdrawn:** close with reason

### Step 6 — Update Baselines and Artifacts
For every Approved change request, update all affected artifacts:

| Baseline affected | Artifact | Section to update |
|---|---|---|
| Scope | A08 | WBS, WBS Dictionary, scope statement |
| Schedule | A15 | Schedule model, milestones, critical path |
| Cost | A16 | BAC, cost estimates, EAC |
| Quality | A20 | Quality standards, acceptance criteria |
| Resources | A26 | Resource estimates, capacity |
| Risk | A19 | New or updated risks |

Record all artifact updates in A12 with the date updated and updated-by.

### Step 7 — Communicate and Reissue
- Notify all affected parties per A28 communications plan
- Reissue A17 performance report reflecting the updated baselines
- Update the A12 change register summary with cumulative approved change count, total cost impact, and total schedule impact

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Approved/rejected change decisions | A12 | Decision log |
| Updated scope baseline | A08 | Baseline section (if scope changed) |
| Updated schedule baseline | A15 | Baseline section (if schedule changed) |
| Updated cost baseline | A16 | Baseline section (if cost changed) |
| Reissued performance report | A17 | Current period |
| Change communications | A28 | Delivery log |

---

## Operating Rules

1. No baseline (scope, schedule, cost) may be changed without an Approved A12 entry.
2. Every change request, regardless of outcome, must remain in A12 permanently — no deletions.
3. PM may only approve changes within the PM authority threshold defined in A06.
4. Impact assessment is mandatory for every change request — undocumented impacts are not acceptable.
5. Approved changes must be reflected in all affected baselines before the next performance reporting period.
6. Withdrawn or deferred requests must have a documented reason in A12.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Baseline changed without A12 entry | Baseline discrepancy with no A12 Approved record | Retroactive A12 entry; assess authorization compliance; A06 review |
| Impact assessment skipped | A12 shows change Approved with no impact fields populated | Retroactive impact assessment; if baseline change already made, reconcile artifacts |
| PM approves above authority threshold | A12 shows PM approval on a high-value change without sponsor sign-off | Escalate retroactively to sponsor for ratification; update A06 authority record |
| Decision timeline exceeded | A12 shows pending review items older than the A12 plan deadline | Follow up with approver; escalate if no response; escalate to next authority level per A06 |
| Approved change not reflected in baseline | A12 shows Approved status but A08/A15/A16 not updated | Immediate baseline update; reissue A17 |
| Change request submitted with no impact details | A12 Pending item has description only, no impact fields | Return to requestor for completion; do not route for approval until impact assessment complete |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | A12 plan exists | A12 §1 change management plan complete before change requests are routed | Change requests processed without A12 plan |
| T-2 | All change requests registered | Every change request has a unique A12 Change ID with date and requestor | Change request actioned without A12 entry |
| T-3 | Impact assessment complete | Every A12 entry has all relevant impact dimensions assessed | A12 entry with blank impact fields |
| T-4 | Authority threshold respected | All approvals by the correct authority per A06 | PM approves above-threshold change without sponsor sign-off |
| T-5 | Decision timeline met | All change requests resolved within A12 plan deadline | Pending Review change older than deadline with no escalation |
| T-6 | Approved changes update baselines | All affected artifacts updated before next reporting period | Approved change with no corresponding artifact update |
| T-7 | Rejected/withdrawn reasons documented | Every non-approved change has documented reason | Rejection with no rationale |
| T-8 | A17 reissued after baseline change | A17 performance report reissued with updated baselines after each approved change | Stakeholders working from pre-change A17 after baseline update |
| T-9 | No deletions from A12 | A12 log has all change requests present with full history | Any deleted A12 entry |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.1.6.8 · Process Groups Practice Guide §5.4*
*Source type: PMI-derived*
