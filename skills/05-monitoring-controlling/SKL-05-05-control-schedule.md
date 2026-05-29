---
skill_id: SKL-05-05
skill_name: Control Schedule
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A15 — Schedule Baseline Record"
artifacts_updated:
  - "A12 — Integrated Change Log (schedule change requests)"
  - "A17 — Integrated Performance Reporting Record (schedule section)"
  - "A18 — Issue, Impediment and Action Log (schedule delays)"
pmbok8_anchor: "Guide §2.1.6.9 Control Schedule · Process Groups Practice Guide §5.6 · Practice Standard for Scheduling"
performance_domains:
  - Delivery
  - Measurement
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-03-09 — A15 schedule baseline must be approved"
  - "SKL-05-03 — A12 change control process must be active"
downstream_skills:
  - "SKL-05-06 — Control Costs (schedule and cost are linked via EVM)"
file_path: "skills/05-monitoring-controlling/SKL-05-05-control-schedule.md"
tests: 9
---

# SKL-05-05 — Control Schedule

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A15 — Schedule Baseline Record
**PMBOK8 Anchor:** Guide §2.1.6.9 · Process Groups Practice Guide §5.6 · Practice Standard for Scheduling

---

## Purpose

Control Schedule monitors schedule progress against the A15 baseline using EVM and critical path analysis, identifies schedule variances, applies schedule compression or recovery techniques when required, and manages baseline changes through A12. It feeds schedule performance into A17 and ensures that no schedule baseline change occurs without formal approval.

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Schedule baseline | A15 | Baseline section | Approved |
| Activity actuals | A15 | Actuals section | Current |
| EV data | A15 + A16 | EV = % complete × PV; AC from A16 | Current |
| Resource actuals | A26 | Utilization actuals | Current |
| Change requests | A12 | Pending items | Current |
| Performance report | A17 | Schedule section | Current period |

---

## Steps

### Step 1 — Update Schedule Actuals
Collect actual start, actual finish, and remaining duration for all in-progress activities from A15:
- Update A15 actuals section with: actual start date, actual finish date (if complete), remaining duration, and % complete
- Calculate Earned Value (EV) for each completed or in-progress work package: EV = Planned Value (PV) × % complete

### Step 2 — Calculate Schedule Performance
For each work package and at summary level, calculate:
- **SV (Schedule Variance):** EV − PV
- **SPI (Schedule Performance Index):** EV ÷ PV
- **Negative SV** = behind schedule; **SPI < 1.0** = behind schedule
- **Forecast finish date:** re-compute from current critical path using updated actuals

Record in A15 performance section and mirror in A17.

### Step 3 — Critical Path Analysis
Re-run critical path analysis using updated actuals:
- Identify activities on the critical path with negative float
- Identify near-critical path activities (float < defined threshold, typically 5 days or 10%)
- Compare current critical path to baseline critical path — identify path changes
Document critical path status in A15 and A17.

### Step 4 — Apply Schedule Recovery Techniques
For activities behind schedule or on a slipping critical path, apply one or more recovery techniques:

| Technique | Description | Best for |
|---|---|---|
| Crashing | Add resources to critical path activities to reduce duration | When resources are available and cost increase is acceptable |
| Fast-tracking | Overlap sequential activities that were originally planned in sequence | When activities have low dependency risk |
| Scope reduction | Remove low-priority scope from the current phase | When neither crashing nor fast-tracking is viable |
| Re-sequencing | Re-order non-critical activities to free up resources for the critical path | When resource contention is the cause |

Document technique selected, rationale, expected recovery, and owner in A15 recovery log. Raise A12 if technique changes the schedule baseline.

### Step 5 — Process Schedule Change Requests
For each schedule change request in A12:
- Assess impact on cost baseline (A16), scope (A08), and risk (A19)
- Route to appropriate authority per A06
- If approved: update A15 schedule baseline; update A17 forecast
- If rejected: record rationale

### Step 6 — Update A17 Schedule Section
Record schedule control findings:
- Current SV and SPI (summary and work package level)
- Critical path float trend
- Forecast finish date vs. baseline finish date
- Recovery actions taken and their expected impact
- Change requests submitted, approved, and rejected

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Schedule performance information | A17 | Schedule section |
| Updated schedule actuals | A15 | Actuals section |
| Forecast finish date | A15 + A17 | Forecast section |
| Schedule change requests | A12 | Pending items |
| Schedule delays | A18 | Issue log |
| Recovery log | A15 | Recovery section |

---

## Operating Rules

1. Schedule baseline may only be updated after A12 Approved entry — no informal date adjustments.
2. Critical path must be re-analysed at every reporting period — not just when slippage is suspected.
3. Recovery technique selection must be documented in A15 with expected result and owner assigned.
4. Schedule forecast must be updated every period and labelled as forecast (not actuals) in A17.
5. Near-critical path activities (within threshold float) must be monitored and reported in A17.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Schedule baseline not updated via A12 | A15 baseline dates changed informally with no A12 Approved entry | Retroactive A12 entry; assess authorization compliance |
| Critical path not re-analysed each period | A15 shows no critical path analysis entry for one or more periods | Perform immediate critical path analysis; determine if path has shifted |
| SPI below threshold with no recovery action | A17 shows SPI < 0.85 for two or more periods with no A15 recovery log entry | Immediate recovery planning; document technique; assign owner; reassess in next period |
| Fast-tracking applied without risk assessment | Fast-tracking implemented without reviewing dependency risk in A19 | Retroactive risk assessment; log dependency risk in A19; monitor closely |
| Forecast finish not updated | A17 shows same forecast finish date despite actuals slippage | Recalculate critical path; update A15 and A17 forecast; communicate to affected stakeholders |
| Schedule recovery action has no owner | A15 recovery log shows technique selected but no responsible party | Assign owner immediately; set due date; follow up in next reporting period |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Schedule baseline approved | A15 baseline section approved before Control Schedule begins | Control Schedule active with no approved A15 baseline |
| T-2 | Actuals updated each period | A15 actuals section updated at every reporting period | Any period without A15 actuals update |
| T-3 | EVM calculated | SV and SPI calculated and recorded every period | A17 shows period with no SV or SPI entry |
| T-4 | Critical path re-analysed | Critical path analysis run and documented at every period | Period passes with no critical path documentation in A15 |
| T-5 | Recovery action for SPI < threshold | Every period with SPI below A17 threshold has a recovery action in A15 | SPI below threshold for two periods with no recovery log entry |
| T-6 | Recovery action has owner | Every A15 recovery log entry has a named owner and target date | Recovery action without owner or date |
| T-7 | Schedule change via A12 | Schedule baseline changes have A12 Approved entry | Schedule baseline date changed without A12 entry |
| T-8 | Forecast updated | A17 forecast finish date updated every period | Forecast finish unchanged for two periods despite actuals slippage |
| T-9 | Delays in A18 | Activities delayed beyond threshold logged as A18 issues | Activity more than 10% of duration late with no A18 entry |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.1.6.9 · Process Groups Practice Guide §5.6 · PMI Practice Standard for Scheduling*
*Source type: PMI-derived*
