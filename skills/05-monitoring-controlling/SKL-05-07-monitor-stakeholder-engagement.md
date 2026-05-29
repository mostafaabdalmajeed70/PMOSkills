---
skill_id: SKL-05-07
skill_name: Monitor Stakeholder Engagement
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A07 — Stakeholder Register and Engagement Strategy"
artifacts_updated:
  - "A17 — Integrated Performance Reporting Record (stakeholder section)"
  - "A18 — Issue, Impediment and Action Log (engagement gaps)"
pmbok8_anchor: "Guide §2.5.2.5 Monitor Stakeholder Engagement · Process Groups Practice Guide §5.10"
performance_domains:
  - Stakeholders
  - Governance
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-04-06 — Manage Stakeholder Engagement must be active (A07 current levels being recorded)"
downstream_skills:
  - "SKL-06-01 — Close Project or Phase (final stakeholder closure)"
file_path: "skills/05-monitoring-controlling/SKL-05-07-monitor-stakeholder-engagement.md"
tests: 7
---

# SKL-05-07 — Monitor Stakeholder Engagement

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A07 — Stakeholder Register and Engagement Strategy
**PMBOK8 Anchor:** Guide §2.5.2.5 · Process Groups Practice Guide §5.10

---

## Purpose

Monitor Stakeholder Engagement evaluates the effectiveness of stakeholder engagement activities by comparing current (C) and desired (D) SEAM levels across all stakeholders, identifies persistent engagement gaps, assesses stakeholder risk, and determines whether engagement strategies need to be revised. This skill is the surveillance complement to SKL-04-06 (Manage Stakeholder Engagement), which executes; this skill evaluates.

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Stakeholder register | A07 | All stakeholders | Current |
| SEAM current (C) and desired (D) levels | A07 | SEAM column | Updated by SKL-04-06 |
| Engagement event log | A28 | Delivery log | Current |
| Issue log | A18 | Engagement issues | Current |
| Performance report | A17 | Stakeholder section | Current |

---

## Steps

### Step 1 — Review SEAM Trend Data
For each stakeholder in A07, compare current (C) vs. desired (D) engagement level:
- Calculate the gap: D − C (positive = under-engaged; negative = over-engaged relative to desired)
- Assess trend: is C moving toward D, static, or moving away from D?
- Classify each stakeholder:

| Classification | Condition | Priority |
|---|---|---|
| On target | C = D | Low — maintain |
| Improving | C moving toward D | Medium — sustain |
| Static gap | C unchanged for ≥2 periods, C ≠ D | High — strategy review needed |
| Deteriorating | C moving away from D | High — immediate action |
| High-power resistant | C = Resistant, Power = High | Critical — sponsor escalation |

### Step 2 — Assess Engagement Strategy Effectiveness
For each stakeholder in the Static gap or Deteriorating category:
- Review A07 engagement strategy for that stakeholder
- Review A28 engagement event log — are planned activities being executed?
- Assess whether the strategy itself is incorrect (wrong method, wrong channel, wrong frequency)
- Determine required action: intensify, change method, re-trigger SKL-03-07, or escalate

### Step 3 — Identify New or Changed Stakeholders
Review the project environment for:
- New stakeholders who have not yet been added to A07
- Existing stakeholders whose role, interest, or power has changed
- Stakeholders who should be exited from active engagement (project phase no longer relevant to them)

Update A07 register for any changes found. New high-power or high-interest stakeholders must trigger SKL-03-07 strategy development.

### Step 4 — Log Engagement Gaps and Risks
For every stakeholder with a Static gap or Deteriorating trend:
- Log in A18 if the gap poses a risk to project outcomes, milestone acceptance, or sponsor support
- Link the A18 issue to the A07 stakeholder record
- Assess whether the engagement gap should be added to A19 as a stakeholder-related project risk

### Step 5 — Update A17 Stakeholder Section
Record monitoring findings in A17:
- Number of stakeholders by SEAM classification
- Count of stakeholders On Target, Improving, Static gap, Deteriorating
- High-priority engagement actions taken this period
- Escalations raised
- Changes to stakeholder register

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Updated SEAM trend data | A07 | SEAM trend column |
| Strategy revision decisions | A07 | Engagement strategy section |
| Engagement gap issues | A18 | Issue log |
| Stakeholder risk entries | A19 | Risk register (if applicable) |
| Stakeholder performance section | A17 | Stakeholder section |

---

## Operating Rules

1. A07 SEAM trend must be assessed at every reporting period — not only when problems are visible.
2. Stakeholders with a Static gap for two or more consecutive periods must have a revised engagement strategy in A07.
3. New high-power or high-interest stakeholders must be added to A07 within the same reporting period they are identified.
4. High-power Resistant stakeholders must be escalated per A06 — retention of this category beyond two periods without action is a governance failure.
5. Engagement monitoring findings must be reported in A17 at every period.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| SEAM trend not assessed | A07 has no trend history; C levels static across all stakeholders | Immediate SEAM trend review; retroactive categorization; confirm A28 activities are being executed |
| Static gap not actioned | A07 shows two or more periods of Static gap with no strategy change | Immediate engagement strategy revision for affected stakeholders; re-trigger SKL-03-07 |
| New stakeholder not added | Stakeholder identified informally but not in A07 | Add to A07 immediately; assess power and interest; create engagement strategy if High power/interest |
| Engagement gap not in A18 | Deteriorating stakeholder with no A18 entry | Log in A18; assess project risk; add to A19 if risk to project outcomes |
| A17 stakeholder section omitted | A17 issued without stakeholder monitoring data | Supplement A17 with stakeholder section before next issuance; confirm reporting template includes stakeholder data |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | SEAM trend assessed each period | A07 has trend classification for all stakeholders at every reporting period | Period passes with no SEAM trend assessment |
| T-2 | Static gap actioned | Every stakeholder with Static gap ≥2 periods has a revised A07 strategy | Static gap stakeholder with unchanged strategy after two periods |
| T-3 | Deteriorating escalated | Deteriorating stakeholder has A18 issue and corrective action | Deteriorating stakeholder with no A18 entry |
| T-4 | New stakeholders captured | A07 updated within same period as new stakeholder identification | New stakeholder active in project environment not in A07 |
| T-5 | High-power resistant escalated | High-power Resistant stakeholder escalated per A06 within two cycles | High-power Resistant retained three or more cycles without escalation |
| T-6 | Stakeholder risk in A19 | Significant engagement gaps with project risk impact logged in A19 | Engagement gap posing project risk with no A19 entry |
| T-7 | A17 stakeholder section current | A17 contains stakeholder monitoring data at every period | A17 issued without stakeholder section |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.5.2.5 · Process Groups Practice Guide §5.10*
*Source type: PMI-derived*
