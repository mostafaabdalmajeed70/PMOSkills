# A16 — Financial Management Record
**Artifact ID:** A16
**Artifact Name:** Financial Management Record
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.4 · EVM · Process-Groups §3.3
**Source Type:** PMI-derived
**File Path:** `artifacts/planning-and-baselines/A16-financial-management-record.md`

---

## Definition

The Financial Management Record is the cost baseline authority — containing the cost management plan, activity cost estimates, cost baseline (Budget at Completion), funding requirements, and all EVM performance data (CPI, EAC, TCPI) accumulated during execution and control.

**PMI Source:** PMBOK8 Guide §2.4; EVM standard; Process-Groups §3.3.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Planning & Baselines |
| **Type** | Cost baseline + EVM record |
| **Lifecycle** | Created in Planning · Updated in Executing · Controlled in M&C · Final archived in Closing |
| **Baseline?** | Yes — Cost Baseline (BAC). Changes require formal change request via SKL-05-02 |
| **Ownership** | Project Manager / Finance Lead |

---

## Purpose

- Establish the approved cost baseline (BAC) for project control
- Record all cost estimates and basis of estimate
- Support Earned Value Management (CPI, EAC, TCPI, VAC)
- Provide financial forecasting through project lifecycle
- Feed the Final Performance Report (A17) at closure

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Cost Management Plan | Estimation method, control thresholds, EVM approach, reporting frequency | SKL-03-13 |
| §2 Cost Estimates | Bottom-up estimates per WBS work package, basis of estimate, confidence range | SKL-03-14 |
| §3 Cost Baseline (BAC) | Time-phased budget, S-curve, contingency reserves, management reserves | SKL-03-15 |
| §4 Funding Requirements | Period-by-period funding tranches, funding reconciliation | SKL-03-15 |
| §5 EVM / CPI / EAC Section | AC, EV, PV per period; CPI, SPI; EAC, ETC, TCPI, VAC | SKL-05-05 |

---

## Key EVM Metrics

| Metric | Formula | Threshold |
|--------|---------|----------|
| Cost Variance (CV) | EV − AC | CV < 0 = over budget |
| Cost Performance Index (CPI) | EV ÷ AC | CPI < 0.9 = escalate |
| Estimate at Completion (EAC) | BAC ÷ CPI (typical) | Compare to original BAC |
| To-Complete Performance Index (TCPI) | (BAC − EV) ÷ (BAC − AC) | TCPI > 1.1 = difficult to recover |
| Variance at Completion (VAC) | BAC − EAC | Negative = projected overrun |

---

## Inputs

| Input | Source |
|-------|--------|
| A08 §4 — WBS | SKL-03-05 |
| A15 — Schedule Model | SKL-03-06 |
| A26 — Resource Estimates | SKL-03-17 |
| A05 — Context Register (rates, historical costs) | SKL-01-02 |
| A19 — Risk Register (cost risks, contingency) | SKL-03-11 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Cost baseline (BAC + S-curve) | SKL-05-05 (Control Costs) · SKL-05-02 (Change Control) |
| EAC / CPI / TCPI | SKL-05-01 (Monitor & Control) · A17 (Performance Report) |
| Funding requirements | Sponsor / Finance authority |

---

## Quality Criteria

- Estimates developed from WBS (bottom-up preferred)
- Basis of estimate documented per work package
- Contingency reserves linked to identified risks (A19)
- Management reserves separate from cost baseline
- BAC formally approved before execution
- EVM thresholds (CPI/SPI) defined in §1

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A08 — Scope Document | WBS drives cost estimates |
| A15 — Schedule Model | Time-phasing of cost baseline |
| A19 — Risk Management Record | Contingency reserves tied to risks |
| A17 — Performance Report | CPI/EAC reported each period |
| A27 — Closure Record | Final cost performance summary |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.4.2.1–2.4.2.4 | Plan Financial through Control Finances |
| PMBOK8 Guide Figures 2-27 to 2-30 | Financial management process flows |
| EVM Standard | Full EVM metric definitions and formulas |

---

*Owner: Project Manager / Finance Lead · Version Control: Semantic versioning · Change Control: T2–T3 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch D*
