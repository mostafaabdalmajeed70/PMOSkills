---
skill_id: SKL-05-06
skill_name: Control Costs
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A16 — Financial Management and Cost Baseline Record"
artifacts_updated:
  - "A12 — Integrated Change Log (cost change requests)"
  - "A17 — Integrated Performance Reporting Record (cost/EVM section)"
  - "A18 — Issue, Impediment and Action Log (cost overrun issues)"
pmbok8_anchor: "Guide §2.1.6.9 Control Costs · Process Groups Practice Guide §5.7 · PMI Practice Standard for EVM"
performance_domains:
  - Finance
  - Measurement
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-03-10 — A16 cost baseline must be approved"
  - "SKL-05-03 — A12 change control process must be active"
downstream_skills:
  - "SKL-06-01 — Close Project or Phase (final cost reconciliation)"
file_path: "skills/05-monitoring-controlling/SKL-05-06-control-costs.md"
tests: 9
---

# SKL-05-06 — Control Costs

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A16 — Financial Management and Cost Baseline Record
**PMBOK8 Anchor:** Guide §2.1.6.9 · Process Groups Practice Guide §5.7 · PMI Practice Standard for EVM

---

## Purpose

Control Costs monitors project expenditure against the A16 cost baseline using Earned Value Management (EVM), identifies cost variances, forecasts final cost at completion, manages contingency reserve consumption, and ensures cost baseline changes are processed through A12. This skill produces the definitive financial performance picture reported in A17.

---

## EVM Reference Formulas

| Metric | Formula | Interpretation |
|---|---|---|
| Planned Value (PV) | Budgeted cost of scheduled work | What we planned to spend |
| Earned Value (EV) | Budgeted cost of work performed | What the work done is worth |
| Actual Cost (AC) | Actual cost of work performed | What we actually spent |
| Cost Variance (CV) | EV − AC | Positive = under budget |
| Schedule Variance (SV) | EV − PV | Positive = ahead of schedule |
| CPI | EV ÷ AC | <1.0 = over budget |
| SPI | EV ÷ PV | <1.0 = behind schedule |
| EAC (typical) | BAC ÷ CPI | Forecast final cost |
| ETC | EAC − AC | Cost to complete from now |
| VAC | BAC − EAC | Positive = under budget at completion |
| TCPI (to BAC) | (BAC − EV) ÷ (BAC − AC) | CPI required to finish within BAC |

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Cost baseline (BAC) | A16 | §4 cost baseline | Approved |
| Actual costs | A16 | Actuals section | Current period |
| EV data | A15 + A16 | EV calculated from schedule + cost | Current |
| Reserve balance | A16 | Reserve section | Current |
| Change requests | A12 | Pending items | Current |
| Performance report | A17 | Cost section | Current period |

---

## Steps

### Step 1 — Collect Cost Actuals
Gather all actual costs incurred in the current period from A16 actuals section:
- Labor costs (by resource from A25/A26)
- Material costs
- External/vendor costs (from A31)
- Reserve drawdowns (from A16 reserve section)
Ensure actuals are reconciled with finance system. Record in A16.

### Step 2 — Calculate EVM Metrics
Using PV from A15, EV from % complete, and AC from A16:
- Calculate CV, SV, CPI, SPI for current period
- Calculate cumulative CV, SV, CPI, SPI (period-to-date)
- Calculate EAC using primary formula (BAC ÷ CPI) and confirm with secondary formula if CPI varies significantly from 1.0
- Calculate ETC, VAC, TCPI
- Record all metrics in A16 EVM log and mirror in A17

### Step 3 — Assess Variance Against Thresholds
Compare CPI and CV against thresholds from A17 plan section:

| CPI range | Status | Required action |
|---|---|---|
| ≥0.95 | Green | Monitor; no action |
| 0.85–0.94 | Amber | Corrective action plan required |
| <0.85 | Red | A12 change request required; sponsor notification |

For VAC negative (forecast over budget):
- Document likely cause in A17
- Assess whether reserve is sufficient to cover VAC
- Raise A12 if cost baseline revision is required

### Step 4 — Manage Contingency Reserve
Review A16 reserve section:
- Total reserve authorized (as approved)
- Amount consumed to date (by risk event, from A19 cross-references)
- Remaining reserve balance
- Reserve burn rate vs. remaining project duration

If reserve burn rate projects exhaustion before project end:
- Log in A18 as a High priority cost issue
- Notify sponsor per A06 threshold
- Raise A12 change request for additional contingency if needed

### Step 5 — Process Cost Change Requests
For each cost change request in A12:
- Assess impact on BAC and EAC
- Route to appropriate authority per A06
- If approved: update A16 cost baseline; recalculate EAC; update A17
- If rejected: record rationale

### Step 6 — Update A17 Cost Section
Record cost control findings in A17:
- Current period and cumulative CPI and SPI
- CV and SV summary
- EAC, ETC, VAC
- TCPI (to BAC and to EAC if re-baselined)
- Reserve status and burn rate
- Cost change requests this period (submitted, approved, rejected)

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| EVM performance information | A17 | Cost section |
| Updated cost actuals | A16 | Actuals section |
| EAC and VAC forecasts | A16 + A17 | Forecast section |
| Reserve status | A16 | Reserve section |
| Cost change requests | A12 | Pending items |
| Cost overrun issues | A18 | Issue log |

---

## Operating Rules

1. Cost baseline may only be updated after A12 Approved entry — no informal BAC adjustments.
2. EAC must be recalculated every reporting period using current CPI — static EAC is not acceptable.
3. Reserve consumption must cross-reference A19 Risk ID for every drawdown.
4. TCPI must be reported when CPI falls below 0.90 — it establishes whether recovery is mathematically feasible.
5. Actuals must be reconciled with the finance system before being entered in A16 — unreconciled estimates are not actuals.
6. Sponsor notification is required when cumulative reserve consumption exceeds the A06 threshold.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Actuals not reconciled with finance system | A16 actuals differ from finance system records | Reconcile immediately; correct A16; determine reconciliation cadence for future periods |
| EAC not updated each period | A17 shows static EAC despite CPI movement | Recalculate EAC using current CPI; update A17; reissue if stakeholders have the old figure |
| Reserve consumed without A19 cross-reference | A16 reserve section shows drawdown with no Risk ID | Retroactive A19 cross-reference; enforce policy for future reserve draws |
| TCPI not reported when CPI < 0.90 | A17 shows CPI below 0.90 without TCPI | Calculate and add TCPI to current and future A17 reports; escalate if TCPI > 1.10 (recovery unlikely) |
| Cost change made without A12 entry | A16 BAC changed informally | Retroactive A12 entry; assess authorization compliance; sponsor notification if above PM threshold |
| Reserve exhaustion not escalated | A16 reserve balance at zero or forecast to exhaust before project end with no sponsor notification | Immediate sponsor notification; A12 change request for additional reserve; A18 issue |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Cost baseline approved | A16 cost baseline approved before Control Costs begins | Control Costs active with no approved A16 baseline |
| T-2 | Actuals reconciled | A16 actuals match finance system at each period end | A16 actuals differ from finance system by more than rounding |
| T-3 | EVM calculated each period | CPI, SPI, CV, SV calculated and in A17 each period | Any period with no EVM calculation |
| T-4 | EAC updated | EAC recalculated every period using current CPI | EAC unchanged for two or more periods of CPI movement |
| T-5 | Reserve cross-referenced | Every reserve drawdown in A16 references A19 Risk ID | Reserve draw with no Risk ID cross-reference |
| T-6 | Threshold actions | CPI amber or red triggers corrective action or A12 | CPI below threshold with no documented action |
| T-7 | TCPI reported | TCPI calculated and in A17 when CPI < 0.90 | CPI < 0.90 with no TCPI in A17 |
| T-8 | Cost changes via A12 | All cost baseline changes have A12 Approved entry | BAC changed without A12 entry |
| T-9 | Reserve alerts escalated | Reserve exhaustion risk notified to sponsor per A06 threshold | Reserve near exhaustion with no sponsor notification |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.1.6.9 · Process Groups Practice Guide §5.7 · PMI Practice Standard for Earned Value Management*
*Source type: PMI-derived*
