---
skill_id: SKL-05-09
skill_name: Monitor Communications
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A28 — Communications and Reporting Record"
artifacts_updated:
  - "A17 — Integrated Performance Reporting Record (communications section)"
  - "A18 — Issue, Impediment and Action Log (communications failures)"
pmbok8_anchor: "Guide §2.5.2.6 Monitor Communications · Process Groups Practice Guide §5.11"
performance_domains:
  - Stakeholders
  - Governance
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-04-07 — Manage Communications must be active (A28 delivery log being maintained)"
downstream_skills:
  - "SKL-06-01 — Close Project or Phase (final communications closure)"
file_path: "skills/05-monitoring-controlling/SKL-05-09-monitor-communications.md"
tests: 7
---

# SKL-05-09 — Monitor Communications

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A28 — Communications and Reporting Record
**PMBOK8 Anchor:** Guide §2.5.2.6 · Process Groups Practice Guide §5.11

---

## Purpose

Monitor Communications evaluates whether project communications are meeting stakeholder needs and project objectives. It audits the A28 delivery log for completeness and timeliness, assesses whether the communications plan is still appropriate, identifies communications failures, and determines whether the plan needs to be revised. This is the surveillance complement to SKL-04-07 (Manage Communications), which delivers; this skill evaluates.

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Communications plan | A28 | Plan section | Current |
| Delivery log | A28 | Delivery log | Current period |
| Stakeholder engagement levels | A07 | SEAM current (C) | Current |
| Issue log | A18 | Communications issues | Current |
| Performance report | A17 | Communications section | Current |

---

## Steps

### Step 1 — Audit Delivery Log Completeness
For each communication item planned in A28 for the current period:
- Does a delivery log entry exist?
- Was it delivered on time?
- Was it delivered to all planned recipients?
- Was the correct method and format used?

For each gap (missing entry, late delivery, wrong recipient, wrong format):
- Document in A28 delivery log as a gap entry
- Log in A18 if the gap poses a risk to stakeholder engagement or decision-making

### Step 2 — Assess Stakeholder Feedback and Responsiveness
Review A28 for interactive communication outcomes and A07 for SEAM level changes:
- Are stakeholders responding to communications?
- Are decisions being made on time after communications are sent?
- Are any stakeholder SEAM levels declining despite planned communications?

If communications are not producing the intended effect on stakeholder engagement:
- Flag for strategy review in Step 3
- Log in A18 if engagement risk is identified

### Step 3 — Evaluate Communications Plan Adequacy
Assess whether the current A28 plan is still fit for purpose:

| Assessment dimension | Question | Action if inadequate |
|---|---|---|
| Frequency | Are communications too frequent or too infrequent for stakeholder needs? | Revise A28 delivery schedule |
| Channel | Are the communication channels appropriate for the audience? | Update A28 with revised channels |
| Format | Are formats clear and appropriate for the information type? | Update A28 templates section |
| Coverage | Are any active stakeholders not covered in the plan? | Add to A28; coordinate with A07 update |
| Access level | Has any stakeholder access classification changed? | Update A28 sensitivity section |

Document assessment outcome in A28 plan review section. If changes are needed, re-trigger SKL-03-08 (Plan Communications Management) for the affected sections.

### Step 4 — Log Communications Failures and Gaps
For each confirmed communications failure (missed delivery, access breach, wrong format, unacknowledged decision):
- Create or update A18 issue entry with classification = Communications
- Assign owner (typically the sender responsible per A28)
- Set resolution due date
- Assess whether the failure requires A28 plan update

### Step 5 — Update A17 Communications Section
Record monitoring findings in A17:
- Planned vs. actual communications delivered this period
- Count of on-time, late, and missed deliveries
- Communications gaps and their status
- Plan revision decisions taken
- Issues logged

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Delivery audit findings | A28 | Delivery log gap entries |
| Plan adequacy assessment | A28 | Plan review section |
| Communications issues | A18 | Issue log |
| Communications performance data | A17 | Communications section |

---

## Operating Rules

1. Delivery log audit is mandatory at every reporting period — even when no failures are suspected.
2. A communications plan that fails to produce the intended stakeholder engagement effect for two consecutive periods must be revised.
3. Communications failures that affect stakeholder decision-making must be logged in A18 within 48 hours of identification.
4. Plan revisions triggered by monitoring must re-trigger SKL-03-08 for the affected plan sections — informal updates are not acceptable.
5. Monitoring findings must be reported in A17 at every period.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Delivery audit not performed | A28 has no audit entries; delivery log shows no review | Perform immediate audit; retroactive gap identification; establish audit cadence |
| Plan inadequacy not recognized | Multiple missed deliveries or stakeholder complaints with no plan revision | Conduct plan adequacy assessment; re-trigger SKL-03-08 for affected sections |
| Communications failure not in A18 | Decision-affecting missed communication with no A18 entry | Log in A18 immediately; assess impact on affected decision or stakeholder; take corrective action |
| Stakeholder coverage gap | Active high-interest stakeholder with no A28 plan entry | Add to A28; back-fill missed communications; coordinate with A07 |
| Audit findings not in A17 | A17 issued without communications monitoring data | Add communications section to A17 template; supplement current period immediately |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Delivery audit each period | A28 audit entries present at every reporting period | Period passes with no A28 audit |
| T-2 | Gaps documented | Every delivery gap has an A28 gap entry | Planned communication not delivered without A28 gap entry |
| T-3 | Communications issues in A18 | Decision-affecting failures logged in A18 within 48 hours | Communication failure affecting decision-making with no A18 entry |
| T-4 | Plan adequacy assessed | A28 plan review section updated at least once per phase | No plan adequacy assessment for an entire project phase |
| T-5 | Plan revision triggers SKL-03-08 | Material plan changes re-trigger SKL-03-08 | Plan changed informally without SKL-03-08 re-run |
| T-6 | Stakeholder coverage complete | All active high-interest stakeholders have A28 plan entries | High-interest stakeholder not covered by any A28 plan entry |
| T-7 | A17 communications section current | A17 contains communications performance data at every period | A17 issued without communications section |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.5.2.6 · Process Groups Practice Guide §5.11*
*Source type: PMI-derived*
