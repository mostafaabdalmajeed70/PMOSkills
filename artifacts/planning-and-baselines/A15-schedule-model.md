# A15 — Schedule Model
**Artifact ID:** A15
**Artifact Name:** Schedule Model
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.3 · Scheduling-3E · EVM
**Source Type:** PMI-derived
**File Path:** `artifacts/planning-and-baselines/A15-schedule-model.md`

---

## Definition

The Schedule Model is the project's time baseline — a logical, time-phased model of all activities, milestones, durations, dependencies, resource assignments, and critical path. It serves as the reference against which schedule performance is measured using Earned Value (SV, SPI) and other schedule control techniques.

**PMI Source:** PMBOK8 Guide §2.3; Scheduling-3E; EVM.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Planning & Baselines |
| **Type** | Schedule baseline |
| **Lifecycle** | Created in Planning · Updated in Executing · Controlled in M&C · Final archived in Closing |
| **Baseline?** | Yes — Schedule Baseline. Changes require formal change request via SKL-05-02 |
| **Ownership** | Project Manager / Scheduler |

---

## Purpose

- Establish the approved time baseline for the project
- Define all activities, durations, dependencies, and milestones
- Support resource-loading and cost-phasing
- Enable schedule performance measurement (SV, SPI, EAC-T)
- Support adaptive projects with velocity tracking and release forecasting

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Schedule Management Plan | Scheduling method, tools, update frequency, variance thresholds | SKL-03-06 |
| §2 Activity List | All activities decomposed from WBS | SKL-03-06 |
| §3 Activity Attributes | Duration, resource, predecessor/successor, lead/lag | SKL-03-06 |
| §4 Milestone List | Key events, phase gates, contractual milestones | SKL-03-06 |
| §5 Network Diagram | PDM — Finish-to-Start, Start-to-Start, etc. | SKL-03-06 |
| §6 Schedule Baseline | Approved schedule with critical path highlighted | SKL-03-06 |
| §7 EVM Section | PV curve, SV, SPI, EAC-T calculations | SKL-05-04 |
| §8 Velocity / Release Forecast (adaptive) | Sprint velocity, release burn-up, forecast date | SKL-07-02 |

---

## Key Metrics

| Metric | Formula | Threshold |
|--------|---------|----------|
| Schedule Variance (SV) | EV − PV | SV < 0 = behind schedule |
| Schedule Performance Index (SPI) | EV ÷ PV | SPI < 0.9 = escalate |
| Estimate at Completion (Time) | BAC ÷ SPI (simplified) | Compared to baseline finish |
| Float / Slack | LS − ES or LF − EF | Critical path = 0 float |

---

## Inputs

| Input | Source |
|-------|--------|
| A08 §4 — WBS | SKL-03-05 |
| A26 — Resource estimates | SKL-03-17 |
| A04 — Project Charter (constraints) | SKL-02-01 |
| A05 — Context Register (calendars, holidays) | SKL-01-03 |
| A19 — Risk Register (schedule risks) | SKL-03-10 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Schedule baseline | SKL-05-04 (Control Schedule) · SKL-05-02 (Change Control) |
| PV (Planned Value) curve | SKL-05-01 (Monitor & Control) · SKL-05-05 (Control Costs) |
| Critical path | SKL-04-01 · SKL-05-04 |
| Milestone schedule | A14 (PMP assembly) · Stakeholder reporting |

---

## Quality Criteria

- 100% WBS activities represented (no orphan work packages)
- Critical path identified and documented
- All external dependencies and constraints captured
- Resource leveling applied where over-allocation exists
- Schedule baseline formally approved
- Variance thresholds defined in §1

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A08 — Scope Document | WBS is primary schedule input |
| A16 — Financial Management Record | Schedule phasing drives cost phasing |
| A26 — Resource Record | Resource assignments loaded in schedule |
| A19 — Risk Management Record | Schedule risks managed here |
| A17 — Performance Report | SV/SPI reported per period |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.3.2.1–2.3.2.5 | Plan through Control Schedule |
| PMBOK8 Guide Figures 2-21 to 2-24 | Schedule management process flows |
| Scheduling-3E | Scheduling methodology, CPM, resource leveling |
| EVM | SV, SPI, EAC-T formulas |

---

*Owner: Project Manager / Scheduler · Version Control: Semantic versioning · Change Control: T2 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch D*
