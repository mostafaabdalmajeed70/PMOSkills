# A18 — Issue Log
**Artifact ID:** A18
**Artifact Name:** Issue Log
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.1.6.3 · AUTHORITY-ROUTING.md
**Source Type:** PMI-derived
**File Path:** `artifacts/monitoring-and-decisions/A18-issue-log.md`

---

## Definition

The Issue Log is the active register of all project issues — problems, conflicts, and impediments that have already occurred and require resolution. Unlike risks (A19), issues are current events, not future uncertainties. Issues are logged, assigned, tracked to resolution, and escalated per the T1–T4 threshold model when they cannot be resolved at the current authority level.

**PMI Source:** PMBOK8 Guide §2.1.6.3 — Direct and Manage Project Work; AUTHORITY-ROUTING.md.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Monitoring & Decisions |
| **Type** | Living issue register |
| **Lifecycle** | Opened at first issue · Maintained throughout execution · Closed at project closure |
| **Baseline?** | No — living record |
| **Ownership** | Project Manager / Issue Owner per entry |

---

## Purpose

- Provide a single auditable register of all active and resolved project issues
- Ensure every issue has an owner, a resolution path, and a target resolution date
- Trigger escalation when issues exceed the project manager's resolution authority
- Prevent issues from falling through the cracks or being resolved informally without documentation
- Feed the Performance Report (A17 §9) and Lessons Learned (A21)

---

## Issue Entry Schema

| Field | Description |
|-------|-------------|
| **Issue ID** | Unique ID — format: I-NNN (e.g., I-001) |
| **Date Raised** | Date issue was identified |
| **Raised By** | Name and role of person who identified the issue |
| **Description** | Clear statement of the issue |
| **Category** | Technical / Resource / Stakeholder / External / Process / Governance |
| **Impact** | Effect on scope / schedule / cost / quality / team if unresolved |
| **Severity** | Critical / High / Medium / Low |
| **Authority Threshold** | T1 / T2 / T3 / T4 per AUTHORITY-ROUTING.md |
| **Owner** | Named individual responsible for resolution |
| **Target Resolution Date** | Agreed date for resolution |
| **Resolution Actions** | Steps being taken or taken |
| **Status** | Open / In Progress / Escalated / Resolved / Closed |
| **Resolution Date** | Actual date resolved |
| **Resolution Description** | How the issue was resolved |
| **Change Request Triggered?** | CR-NNN reference if a change request was raised as a result |
| **Notes** | Additional context |

---

## Issue vs. Risk Distinction

| Attribute | Issue (A18) | Risk (A19) |
|-----------|------------|----------|
| Timing | Has already occurred | May occur in the future |
| Certainty | Certain — it exists now | Uncertain — probability < 100% |
| Response type | Resolution actions | Response strategies |
| Register | A18 — Issue Log | A19 — Risk Management Record |
| Relationship | A realized risk becomes an issue | Unresolved issues may create new risks |

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Active Issues | All open and in-progress issues using schema above | SKL-04-01 (ongoing) |
| §2 Escalated Issues | Issues escalated to T2–T4 authority, with decision record | SKL-04-01 · AUTHORITY-ROUTING.md |
| §3 Resolved Issues | Closed issues with resolution details retained for audit | SKL-04-01 (ongoing) |
| §4 Issue Statistics | Open / resolved / escalated counts per period | SKL-05-01 (reporting input) |

---

## Inputs

| Input | Source |
|-------|--------|
| Issue reports from team / stakeholders | Any project participant |
| Realized risks from A19 | SKL-05-06 |
| Performance variance triggers from A17 | SKL-05-01 |
| Escalation thresholds | AUTHORITY-ROUTING.md |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Open issue list | A17 §9 (Performance Report) |
| Escalated issues | Sponsor / Governing body (T3/T4) |
| Change requests triggered | A12 (Change Log) |
| Resolved issues record | A21 (Lessons Learned) · A27 (Closure Record) |

---

## Quality Criteria

- Every issue has a unique I-NNN ID and a named owner
- Target resolution dates set within 2 status cycles of issue being raised
- Issues at or above T2 threshold escalated within defined timeframe
- No issue remains in "Open" status without an active resolution action
- Issue log reviewed at every status cycle
- Resolved issues retained (not deleted) for audit and lessons learned

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A19 — Risk Record | Realized risks become issues; unresolved issues may create risks |
| A17 — Performance Report | Open issues reported each cycle |
| A12 — Change Log | Issue resolution may trigger change requests |
| A21 — Lessons Learned | Issue patterns captured as lessons |
| A27 — Closure Record | Issue resolution summary at closure |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.1.6.3 | Direct and Manage Project Work · Figure 2-5 |
| AUTHORITY-ROUTING.md | T1–T4 escalation thresholds |
| Process-Groups §4.3 | Direct and Manage Project Work outputs |

---

*Owner: Project Manager / Issue Owner per entry · Version Control: Living record · Escalation: T1–T4 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch E*
