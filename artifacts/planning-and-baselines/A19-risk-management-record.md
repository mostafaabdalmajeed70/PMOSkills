# A19 — Risk Management Record
**Artifact ID:** A19
**Artifact Name:** Risk Management Record
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.7 · Risk-PPP · Process-Groups §4.7
**Source Type:** PMI-derived
**File Path:** `artifacts/planning-and-baselines/A19-risk-management-record.md`

---

## Definition

The Risk Management Record is the single artifact that consolidates risk management plan, risk register (identification + analysis), risk response plan, and risk monitoring log across the full project lifecycle. It is continuously updated from initiation through closure.

**PMI Source:** PMBOK8 Guide §2.7; Risk-PPP; Process-Groups §4.7.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Planning & Baselines |
| **Type** | Living risk record |
| **Lifecycle** | Initiated in Planning · Continuously updated in Executing · Actively monitored in M&C · Archived in Closing |
| **Baseline?** | No — living document; no formal baseline. Response plan and thresholds are governed. |
| **Ownership** | Project Manager / Risk Owner per risk entry |

---

## Purpose

- Establish the risk management approach and appetite
- Identify, analyze, and prioritize project risks and opportunities
- Define response strategies for top risks
- Track response implementation and residual risk
- Provide the risk monitoring log throughout execution

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Risk Management Plan | Risk appetite, methodology, probability/impact scales, escalation thresholds, risk categories (RBS) | SKL-03-09 |
| §2 Risk Register — Identification | Risk ID, description, category, cause, potential impact, date identified, raised by | SKL-03-10 |
| §3 Risk Analysis | Probability, impact, risk score (P×I), priority ranking, qualitative ratings; quantitative (EMV/Monte Carlo) where applied | SKL-03-11 |
| §4 Risk Response Plan | Response strategy (Avoid/Transfer/Mitigate/Accept/Escalate for threats; Exploit/Share/Enhance/Accept for opportunities), response owner, triggers, fallback, residual risk | SKL-03-12 |
| §5 Response Log | Response actions taken, dates, actual cost, effectiveness rating | SKL-04-08 |
| §6 Risk Monitoring Log | Monitoring cycle, risk status updates, new risks identified, closed risks, re-analysis triggers | SKL-05-06 |

---

## Risk Entry Schema

| Field | Description |
|-------|-------------|
| Risk ID | Format: R-NNN (e.g., R-001) |
| Category | RBS category (Technical / External / Organizational / PM) |
| Description | Clear risk statement: "Due to [cause], [risk event] may occur, resulting in [impact]" |
| Probability | Low / Medium / High (or % where quantitative) |
| Impact | Low / Medium / High (or $ / days where quantitative) |
| Risk Score | P × I (matrix value) |
| Priority | Top / Watch / Low |
| Response Strategy | Avoid / Transfer / Mitigate / Accept / Escalate / Exploit / Share / Enhance |
| Response Owner | Named individual |
| Trigger | Observable early-warning indicator |
| Status | Open / In-Response / Closed / Realized |

---

## Inputs

| Input | Source |
|-------|--------|
| A04 — Project Charter | SKL-02-01 |
| A05 — Context Register (EEF/OPA, risk history) | SKL-01-02 |
| A07 — Stakeholder Register (stakeholder risks) | SKL-02-02 |
| A08 — Scope Document (scope risks) | SKL-03-03 |
| A15 — Schedule Model (schedule risks) | SKL-03-06 |
| A16 — Financial Record (cost risks) | SKL-03-14 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Risk Register | A14 (PMP) · SKL-04-08 · SKL-05-06 |
| Contingency reserve inputs | A16 §3 |
| Risk triggers | SKL-05-06 (monitoring) |
| Risk closure records | A27 (Closure Record) |

---

## Quality Criteria

- Risk appetite and probability/impact scales defined in §1 before identification begins
- All top risks have named response owners
- Response strategies documented before execution begins
- Monitoring frequency defined in §1
- Residual and secondary risks assessed for all responses
- Risk register reviewed at every status cycle during execution

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A14 — Integrated PM Plan | Risk management plan is a subsidiary plan |
| A16 — Financial Record | Contingency reserves tied to A19 |
| A12 — Change Log | Risk realizations may trigger change requests |
| A17 — Performance Report | Risk status reported each period |
| A21 — Lessons Learned | Risk lessons captured here |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.7.2.1–2.7.2.6 | Plan Risk through Monitor Risks |
| PMBOK8 Guide Figures 2-48 to 2-53 | Risk management process flows |
| Risk-PPP §3–5 | Risk identification, analysis, and response techniques |

---

*Owner: Project Manager / Risk Owner per entry · Version Control: Living document, version on major re-analysis · Change Control: Response plan T2 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch D*
