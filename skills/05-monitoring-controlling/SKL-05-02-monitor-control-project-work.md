---
skill_id: SKL-05-02
skill_name: Monitor and Control Project Work
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A17 — Integrated Performance Reporting Record"
artifacts_updated:
  - "A12 — Integrated Change Log (change requests raised)"
  - "A18 — Issue, Impediment and Action Log (issues identified)"
  - "A19 — Risk Management Record (forecast-based risk review)"
pmbok8_anchor: "Guide §2.1.6.7 Monitor and Control Project Work · Process Groups Practice Guide §5"
performance_domains:
  - Measurement
  - Delivery
  - Governance
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-04-01 — Work performance data must be flowing from Direct and Manage Project Work"
  - "SKL-03-15 — A17 performance reporting plan must be complete"
downstream_skills:
  - "SKL-05-03 — Perform Integrated Change Control"
  - "SKL-05-04 — Control Scope"
  - "SKL-05-05 — Control Schedule"
  - "SKL-05-06 — Control Costs"
file_path: "skills/05-monitoring-controlling/SKL-05-02-monitor-control-project-work.md"
tests: 9
---

# SKL-05-02 — Monitor and Control Project Work

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A17 — Integrated Performance Reporting Record
**PMBOK8 Anchor:** Guide §2.1.6.7 · Process Groups Practice Guide §5

---

## Purpose

Monitor and Control Project Work is the overarching surveillance skill for the project. It tracks progress against all baselines (scope, schedule, cost, quality, risk), identifies variances, forecasts outcomes, and triggers corrective actions or change requests. All performance findings are consolidated in A17 and distributed through A28.

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Work performance data | — | From SKL-04-01 Direct and Manage | Current |
| Schedule baseline | A15 | §3 baseline section | Approved |
| Cost baseline | A16 | §4 BAC section | Approved |
| Scope baseline | A08 | WBS + WBS Dictionary | Approved |
| Risk register | A19 | §6 register | Current |
| Issue log | A18 | Full log | Current |
| Quality metrics | A20 | Measurement results | Current |
| Performance reporting plan | A17 | Plan section | Complete |

---

## Steps

### Step 1 — Collect Work Performance Data
Gather raw work performance data from all executing processes (SKL-04-01 through SKL-04-09):
- Deliverable completion status (% complete per work package)
- Resource utilization actuals
- Cost actuals (from A16)
- Schedule actuals (from A15)
- Quality results (from A20)
- Issue and risk status updates

### Step 2 — Calculate Work Performance Information
Transform raw data into work performance information for A17:
- **Schedule variance (SV):** EV − PV
- **Cost variance (CV):** EV − AC
- **Schedule performance index (SPI):** EV ÷ PV
- **Cost performance index (CPI):** EV ÷ AC
- **Estimate at completion (EAC):** BAC ÷ CPI (or other approved formula)
- **Estimate to complete (ETC):** EAC − AC
- **Variance at completion (VAC):** BAC − EAC
- Quality pass/fail rates vs. targets
- Issue count by status and priority
- Risk exposure trend

Record all calculations in A17 current period section.

### Step 3 — Assess Variance Against Thresholds
Compare performance information against control thresholds defined in A17 plan section:

| Variance type | Green threshold | Amber threshold | Red threshold |
|---|---|---|---|
| SPI | ≥0.95 | 0.85–0.94 | <0.85 |
| CPI | ≥0.95 | 0.85–0.94 | <0.85 |
| SV% | ≤5% behind | 5–10% behind | >10% behind |
| CV% | ≤5% over | 5–10% over | >10% over |
| Issue count | Stable | +10% from prior | +20% or critical open |

*(Thresholds are defaults; project-specific thresholds from A06 override.)*

For each indicator in Amber or Red:
- Document the variance, trend, and likely cause in A17
- Identify corrective, preventive, or defect repair action needed

### Step 4 — Update Forecasts
Update forward-looking projections in A17:
- Revised EAC (cost forecast)
- Revised finish date (schedule forecast)
- Revised scope delivery confidence
- Benefits realization forecast (if A02 exists)

### Step 5 — Raise Change Requests and Issues
For each variance requiring a baseline change:
- Raise a change request in A12 with: type (corrective / preventive / defect repair), description, impacted baselines, recommended action
- Log significant variances as issues in A18 if they require cross-functional action
- Flag new risks identified during monitoring to A19

### Step 6 — Prepare and Distribute Performance Report
Issue A17 performance report per the A28 delivery schedule:
- Confirm distribution list matches A28
- Apply sensitivity classification per A28
- Record issuance in A28 delivery log
- Archive copy in A17 with period date and version stamp

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Work performance information | A17 | Current period section |
| Forecasts (EAC, schedule) | A17 | Forecast section |
| Performance report (distributed) | A17 + A28 | Report + delivery log |
| Change requests | A12 | Pending items |
| Issues raised | A18 | Issue log |
| Risk updates triggered | A19 | Risk register |

---

## Operating Rules

1. A17 must be updated at every reporting period without exception — even periods where all indicators are Green.
2. Variance thresholds must be documented in A17 plan section before first performance report is issued.
3. EVM calculations must use data from A15 and A16 — no standalone spreadsheet data.
4. Every Amber or Red indicator must have an associated corrective/preventive action or a change request.
5. Performance reports are distributed per A28 — ad hoc distribution outside the plan must still be logged.
6. Forecast data is always clearly labelled as forecast (not actuals) in A17.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Performance report not issued at period end | A17 has no current period entry; stakeholders have no update | Issue overdue report immediately; identify reason for gap; update A28 if schedule needs adjustment |
| EVM calculations use stale data | A17 shows EAC unchanged despite new actuals in A16 | Recalculate using current A16 actuals; reissue corrected report |
| Variance identified but no action raised | A17 shows Red CPI/SPI with no corresponding A12 or A18 entry | Raise A12 change request or A18 issue immediately; assess if corrective action window has been lost |
| Threshold definitions absent | A17 plan section has no thresholds; all variances treated equally | Define thresholds retrospectively; confirm with sponsor; document in A17 plan section |
| Forecast not updated | EAC remains at BAC despite consistent CPI below 1.0 | Recalculate EAC; update A17; issue revised forecast to affected stakeholders |
| Distribution list out of date | Stakeholder added or removed without A28 update | Audit A28 distribution list against A07; reconcile and reissue if stakeholders were missed |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | A17 updated each period | A17 current period section populated at every reporting period | Any reporting period with no A17 entry |
| T-2 | EVM data sourced from A15/A16 | A17 EVM values traceable to A15 (PV/EV) and A16 (AC) | A17 shows EVM values with no A15/A16 cross-reference |
| T-3 | Thresholds defined | A17 plan section contains Green/Amber/Red thresholds | A17 plan section has no threshold definitions |
| T-4 | Red/Amber triggers action | Every Red or Amber indicator has a corresponding A12 or A18 entry | Red or Amber indicator with no action logged |
| T-5 | Forecast updated | EAC and revised finish date updated every reporting period | EAC unchanged for two or more consecutive periods of variance |
| T-6 | Change requests in A12 | Corrective/preventive actions requiring baseline change are in A12 | Baseline changed without A12 change request |
| T-7 | Report distribution per A28 | A28 delivery log shows report sent to all A28-listed stakeholders | Stakeholder on A28 list did not receive report |
| T-8 | Issues in A18 | Variances requiring cross-functional resolution logged in A18 | Significant variance with no A18 issue entry |
| T-9 | Risks flagged to A19 | New risks identified during monitoring entered in A19 | Risk identified during monitoring not recorded in A19 |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.1.6.7 · Process Groups Practice Guide §5*
*Source type: PMI-derived*
