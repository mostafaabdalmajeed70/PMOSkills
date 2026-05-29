---
skill_id: SKL-04-07
skill_name: Manage Communications
pack: "04 — Executing"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A28 — Communications and Reporting Record (delivery log)"
artifacts_updated:
  - "A17 — Integrated Performance Reporting Record (reports issued)"
  - "A07 — Stakeholder Register (engagement updates from interactive communications)"
pmbok8_anchor: "Guide §2.5.2.5 Manage Communications · Figure 2-37"
performance_domains:
  - Stakeholders
  - Governance
focus_area: Executing
upstream_prerequisites:
  - "SKL-03-08 — A28 communications plan must be complete"
downstream_skills:
  - "SKL-05-09 — Monitor Communications"
file_path: "skills/04-executing/SKL-04-07-manage-communications.md"
tests: 8
---

# SKL-04-07 — Manage Communications

**Pack:** 04 — Executing
**Status:** Draft · Untested
**Primary Artifact:** A28 — Communications and Reporting Record
**PMBOK8 Anchor:** Guide §2.5.2.5 · Figure 2-37

---

## Purpose

Manage Communications executes the delivery plan defined in A28 — creating, distributing, storing, and retrieving project information according to the planned methods, frequencies, and formats for each stakeholder. This skill ensures the right information reaches the right people at the right time in the right format.

---

## Communication Methods

| Method | Description | When to use |
|---|---|---|
| Interactive | Real-time two-way exchange (meetings, calls, video) | Decisions, negotiations, complex topics |
| Push | Information sent to recipients without requesting response (email, reports, memos) | Status updates, distribution of documents |
| Pull | Information stored for stakeholder to access on demand (intranet, dashboards, repositories) | Reference materials, large audiences, self-service |

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Communications plan | A28 | Plan section | Complete |
| Performance data | A17 | Current period | Current |
| Stakeholder access levels | A28 | Sensitivity/access section | Current |
| Engagement events | A07 | Delivery log entries | Current |

---

## Steps

### Step 1 — Review A28 Delivery Schedule
Confirm all scheduled communications for the current period. For each item check:
- Stakeholder or group
- Communication type and topic
- Method (Interactive / Push / Pull)
- Format and language requirements
- Sender responsibility
- Sensitivity classification

### Step 2 — Create Communication Packages
Prepare each communication item per A28 specifications:
- Match content depth to stakeholder information need (executive summary vs. detailed technical data)
- Apply format template if specified
- Confirm sensitivity level and distribution list
- Attach or reference A17 data for performance communications

### Step 3 — Distribute Communications
Deliver via the planned channel. For each delivery, record in A28 delivery log:
- Stakeholder or group
- Communication type
- Method used
- Date and time sent
- Sender
- Status: Sent / Delivered / Confirmed receipt

### Step 4 — Manage Feedback and Responses
For Interactive communications:
- Capture decisions, commitments, and action items
- Record in A28 delivery log with outcomes
- Update A07 SEAM if engagement level changes
- Log issues arising from communication events in A18

### Step 5 — Issue Performance Reports
Issue all scheduled performance reports:
- Reference A17 data — do not create standalone data
- Confirm distribution matches A28 audience specification
- Record issuance in A28 delivery log

### Step 6 — Manage Communication Records
Store all communications per A28 storage and retrieval requirements:
- Apply retention period from A05 OPA
- Ensure records are retrievable by authorized parties
- Protect confidential communications per sensitivity classification

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Delivery log (all communications sent) | A28 | Delivery log |
| Performance reports issued | A17 | Reporting section |
| A07 updates from interactive comms | A07 | Engagement section |
| Issues from communications | A18 | Issue log (if applicable) |

---

## Operating Rules

1. Every scheduled communication must have an A28 delivery log entry whether sent on time, delayed, or cancelled.
2. Delayed communications must note the reason and rescheduled delivery date.
3. Performance reports must reference A17 data — standalone data not traceable to A17 is not acceptable.
4. No communication distributes information at a sensitivity level above the stakeholder's classified access level per A28.
5. Interactive communication outcomes that include decisions or commitments must be recorded within 24 hours.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Missing delivery log entries | Stakeholder asks why they did not receive a communication | Audit A28 delivery log; identify gaps; re-send if needed |
| Report data not from A17 | Performance report contains data not in A17 | Retract; reissue with A17-sourced data |
| Access level breach | Information distributed to unauthorized stakeholder | Immediate notification; A18 issue; A06 escalation |
| Interactive decisions undocumented | Team acts on verbal decisions with no record | Immediate A28 entry; confirm with participants |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | A28 plan exists | A28 communications plan complete before managed communications begin | Managed communications without A28 plan |
| T-2 | Delivery log complete | Every planned communication has an A28 delivery log entry | Planned communication with no delivery log entry |
| T-3 | Delays recorded | Delayed communications have reason and rescheduled date in A28 | Delayed entry with no explanation |
| T-4 | Access levels respected | No information distributed above stakeholder's classified access level | Distribution breach identified |
| T-5 | Interactive feedback captured | Interactive communication responses recorded in A07 or A18 | Interactive communication with no response record |
| T-6 | Reports reference A17 | Performance reports cite A17 as the data source | Report issued with data not traceable to A17 |
| T-7 | Storage compliant | All communications stored and retrievable per A28 storage specification | Communications not retrievable per A28 spec |
| T-8 | Frequency maintained | Communications issued at A28-specified frequency | Stakeholder missing a scheduled communication for more than one period |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial build |

---

*Authority: PMBOK8 Guide §2.5.2.5 · Figure 2-37*
*Source type: PMI-derived*
