# SKL-05-01 — Monitor Risks

**Skill ID:** SKL-05-01  
**Canonical Title:** Monitor Risks  
**Alias:** SKL-05 — Monitor Risk  
**Pack:** 05 — Monitoring and Controlling  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/05-monitoring-controlling/SKL-05-01-monitor-risks.md`  
**Authority:** PMBOK8 Guide §2.7.2.6 · Figure 2-53 · PMBOK8 Guide §2.7.5 Table 2-11 · Risk Management in Portfolios, Programs, and Projects A Practice Guide §4.8, §4.8.1, §4.8.2, Figure 4-5, §7.2.6 · Process Groups: A Practice Guide §7.10  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Monitor Risks is the process of tracking identified risks, monitoring the implementation of risk response plans, identifying and analyzing new risks, planning responses for new risks, and evaluating the effectiveness of risk responses and risk management processes throughout the project. Its purpose is to maintain continuity of risk ownership, detect changes in exposure early, and keep response plans viable as the project environment changes.

In PMI terms, this process is not limited to checking whether a risk still exists. It also reassesses the status of previously identified risks, identifies emergent, secondary, and residual risks, verifies that trigger conditions are watched, reviews reserve sufficiency, analyzes trends and performance signals, and captures lessons learned for improvement.

---

## 2. Scope

This skill covers:
- Tracking the current status of previously identified risks in A19
- Monitoring trigger conditions for contingent responses
- Checking whether implemented responses are effective
- Detecting emergent, secondary, and residual risks
- Converting realized risks into active issue control through A18 when appropriate
- Reviewing whether contingency and management reserves remain sufficient
- Checking risk trends, risk profile movement, and relevant performance signals
- Raising A12 change or exception decisions when monitoring reveals the need for corrective action or replanning
- Updating A19, lessons learned records, and related planning documents
- Feeding new or changed risks back into Identify Risks, Perform Risk Analysis, and Plan Risk Responses when needed

This skill does **not** cover:
- The original selection of risk response strategies from scratch
- The physical execution of response actions already approved
- General project performance control outside the risk lens unless directly relevant to risk signals

---

## 3. PMBOK Anchor

| Field | Value |
|-------|-------|
| **Process** | Monitor Risks |
| **Guide Section** | §2.7.2.6 |
| **Figure** | Figure 2-53 — Monitor Risks Inputs, Tools and Techniques, and Outputs |
| **Performance Domain** | Risk · Governance · Finance · Schedule · Stakeholders |
| **Focus Area** | Monitoring and Controlling |
| **Primary Outcome** | Continued risk visibility, effective responses, timely escalation, and updated risk records |
| **Secondary Authority** | Risk-PPP §4.8, Figure 4-5, §7.2.6; Process Groups §7.10 |

**PMI definition (paraphrased):** Monitor Risks tracks and analyzes risks, monitors implementation of response plans, identifies new risks, plans responses for new risks, and evaluates response and process effectiveness throughout the project.

---

## 4. Operating Model

This skill uses a six-state monitoring model for each risk record:

| State | Meaning | Typical Control Action |
|------|---------|------------------------|
| **Active Watch** | Risk remains relevant and is being monitored | Review status, triggers, trends, and exposure |
| **Triggered** | Defined condition has been observed | Confirm response activation or escalation path |
| **Response Under Review** | A response has been implemented and its effectiveness is being observed | Measure whether exposure is decreasing |
| **Residual Exposure** | Planned response executed but some exposure remains | Keep active, adjust score, or plan additional action |
| **Realized / Issue Active** | The uncertain event has occurred or is occurring | Maintain A18 issue control linked to A19 |
| **Closed / No Longer Relevant** | Risk no longer applies or exposure is acceptable and inactive | Record closure basis and lessons learned |

This model keeps monitoring distinct from implementation. A response can be implemented under SKL-04, yet the risk still needs observation here until the team confirms either effectiveness, residual exposure, or closure.

---

## 5. Core Monitoring Questions

Every monitoring cycle should answer the following:
1. Does the risk still exist in a meaningful way?
2. Has its probability, impact, timing, or manageability changed?
3. Have any trigger conditions been reached or invalidated?
4. Were planned responses actually implemented?
5. Are implemented responses effective and efficient?
6. Did execution create any secondary risks?
7. What residual exposure remains after the response?
8. Has a new emergent risk appeared?
9. Are contingency and management reserves still adequate?
10. Does the project need replanning, escalation, or formal change control?

---

## 6. Roles

### 6.1 Risk Owner
The risk owner remains accountable for tracking the specific risk, monitoring its trigger conditions, coordinating reassessment, and ensuring contingent actions occur in a timely manner when defined conditions are met.

### 6.2 Project Manager
The project manager integrates risk monitoring into regular project control, ensures updates propagate to the relevant logs and plans, and raises A12 decisions when monitoring reveals threshold breaches, ineffective responses, or material baseline implications.

### 6.3 Risk Response Owner
When a response is in effect or was recently implemented, the response owner provides status and outcome evidence so the risk owner can judge effectiveness and residual exposure.

### 6.4 Team and Functional Leads
Team members and functional leads provide signal data, technical observations, schedule and cost indicators, stakeholder feedback, and lessons learned that may reveal changed or newly emerging risks.

### 6.5 Sponsor or Governance Authority
The sponsor or designated authority receives escalations when residual exposure exceeds tolerance, reserves are insufficient, new responses exceed delegated authority, or overall project risk threatens objectives or viability.

---

## 7. Inputs

PMBOK8 Figure 2-53 identifies the main inputs as the project management plan, project documents including issue log, lessons learned register, risk register, and risk report, plus work performance data and work performance reports.

| Input | Source | Use in This Skill |
|------|--------|-------------------|
| **A19 — Risk Management Record** | Risk domain records | Primary source for current risks, triggers, owners, planned responses, residual notes, and status history |
| **A18 — Issue, Impediment, and Action Log** | Execution / control | Tracks realized risks and active issue management linked back to A19 |
| **A12 — Change and Exception Decision Log** | Governance | Receives escalations, threshold breaches, and corrective or preventive decision needs |
| **A16 — Financial Management and Cost Baseline Record** | Finance control | Supports reserve sufficiency review and approved reserve consumption tracking |
| **Risk management plan / A14-linked plan content** | Planning baseline | Provides thresholds, review cadence, definitions, reporting rules, and ownership model |
| **Lessons learned register** | Knowledge records | Supplies historical effectiveness and captures new learning |
| **Work performance data and reports** | Project control system | Reveal trends, variances, emerging signals, and effectiveness clues |
| **Assumption and issue records** | Cross-domain records | Help determine whether a risk remains valid or has evolved |

Supporting inputs when relevant:
- Schedule and milestone status
- Cost forecasts and variance reports
- Quality and defect information
- Stakeholder feedback and escalation notes
- Procurement and supplier performance information

---

## 8. Tools and Techniques

PMBOK8 Figure 2-53 names **data analysis**, **technical performance analysis**, **reserve analysis**, **audits**, and **meetings** as the principal techniques.

### 8.1 Data Analysis
Used to detect changed exposure, trend movement, emerging patterns, and response effectiveness. This includes reading performance reports for signals that indicate new risks or ineffective responses.

### 8.2 Technical Performance Analysis
Used to compare actual technical or delivery performance against thresholds, tolerances, or leading indicators that may reveal threat growth or opportunity emergence.

### 8.3 Reserve Analysis
Used to check whether contingency and management reserves remain adequate for current exposure, whether reserve usage aligns with approved risk responses, and whether additional action is needed.

### 8.4 Audits
Used to assess the effectiveness of risk management practices, identify barriers, and extract broader improvements for current and future projects.

### 8.5 Meetings
Used to maintain risk awareness, validate updated status, coordinate reassessment, confirm ownership continuity, and align actions across the project team and stakeholder groups.

---

## 9. Monitoring Rules

### Rule 1 — Monitoring is continuous
Risk monitoring is not a one-time review. It occurs at regular intervals, at phase gates, and whenever relevant events or exception conditions arise.

### Rule 2 — Triggers must remain observable
A contingent response is only useful if its trigger conditions are actively watched and remain valid. If the trigger definition no longer matches project reality, the risk record must be updated.

### Rule 3 — Realized risks must be controlled as issues
If the uncertain event has occurred, the item is no longer only a future possibility. It must be linked to active issue management in A18 while the originating risk history remains in A19.

### Rule 4 — Ineffective responses require action
If monitoring shows that a response is not reducing exposure or not being executed as planned, the team must replan, escalate, or request change through A12 as appropriate.

### Rule 5 — New risks found during monitoring enter the risk cycle
Emergent, secondary, or residual risks discovered here are added to A19 and sent into analysis and response planning as needed.

### Rule 6 — Monitoring includes the process itself
The team does not only monitor risks; it also monitors whether its risk management approach is working. Audits, integrated review, and lessons learned are part of this process.

---

## 10. What to Monitor

| Monitoring Object | Minimum Check |
|------------------|---------------|
| **Individual risk status** | Still relevant, changed, inactive, or closed |
| **Probability / impact / timing** | Any material shift since last review |
| **Trigger conditions** | Reached, approaching, invalid, or missing |
| **Response implementation status** | Not started, in progress, completed, ineffective, or effective |
| **Residual risk** | Remaining exposure after implemented response |
| **Secondary risk** | New risk created by a response action |
| **Emergent risk** | Newly detected uncertainty from changing conditions |
| **Overall risk profile** | Trend in aggregate exposure or concentration |
| **Reserves** | Adequate, tightening, or insufficient |
| **Risk process effectiveness** | Cadence working, ownership clear, updates timely, decisions traceable |
| **Lessons learned** | Improvement opportunities captured |

Process Groups §7.10 also emphasizes monitoring whether known risks are no longer about to occur, monitoring all actions implemented in response to risks, observing risk trends and profile, assessing KPIs and KRIs, and ensuring effective communication among team members, risk owners, and risk response owners.

---

## 11. Step-by-Step Instructions

### Step 1 — Establish the Monitoring Set
Pull the current A19 records and separate them into:
- Active watch risks
- Triggered risks
- Recently implemented responses awaiting effectiveness review
- Residual risks
- Closed risks pending archival verification
- Newly logged emergent risks awaiting analysis

This ensures no risk disappears because of poor list hygiene.

### Step 2 — Review Each Risk’s Current Validity
For each active risk, determine whether it:
- Still exists as stated
- Has changed in probability, impact, timing, or exposure path
- Has been overtaken by events and should be closed or rewritten
- Has become an issue because the event occurred

If the risk statement is no longer accurate, update A19 rather than carrying forward stale wording.

### Step 3 — Check Trigger Conditions
Verify for every contingent response that:
- The trigger is still relevant
- The trigger is being observed by a named owner
- Evidence exists for whether the trigger has or has not occurred
- New warning signs suggest the trigger definition should be refined

If a trigger fires, confirm whether the planned action under SKL-04 was initiated and whether escalation is needed.

### Step 4 — Assess Response Implementation Status
For every risk with a planned or implemented response, determine whether the response was:
- Not started
- In progress
- Completed as planned
- Delayed or blocked
- Ineffective
- Effective but leaving residual exposure

If monitoring reveals that a planned response was never executed, open or update A18 action items and escalate as needed.

### Step 5 — Evaluate Effectiveness and Efficiency
Judge whether the response is actually reducing exposure and whether it is doing so at an acceptable cost and pace. Use performance indicators, technical outcomes, defect data, schedule effects, cost impacts, and stakeholder signals as evidence.

A response can be technically completed yet still ineffective. In that case, the risk remains active and further planning is required.

### Step 6 — Identify Residual, Secondary, and Emergent Risks
During each review, explicitly ask:
- What exposure remains after the response?
- Did the response create a new threat or opportunity?
- Did external or internal changes create a new risk not previously listed?

Create new A19 entries for each secondary or emergent risk, and link them to the source event or response where relevant.

### Step 7 — Review Reserves and Tolerance Position
Check whether remaining contingency and management reserves are still aligned with current exposure. Reserve analysis should answer whether the project still has enough time, money, or other reserved capacity to manage known uncertainty.

If reserve sufficiency is weak or thresholds are breached, raise A12 for decision or escalation.

### Step 8 — Review Overall Risk Trend and Communication Health
Move from the individual level to the overall profile:
- Is aggregate exposure rising or falling?
- Are risks clustering around the same cause or objective?
- Are stakeholders informed at the required cadence?
- Are risk owners and response owners actively communicating?

This step prevents local monitoring from missing systemic exposure.

### Step 9 — Update Records and Decide Control Actions
Update A19 with the new status, evidence, trend notes, changed scores where applicable, residual exposure notes, and next review date. Update A18 for realized issues or action follow-up, and create A12 entries for changes, escalation, or exceptions that require decision.

Possible control decisions are:
- Keep under active watch
- Close the risk
- Reanalyze the risk
- Replan or replace the response
- Escalate the exposure
- Convert to active issue control

### Step 10 — Capture Process Learning
At the end of the review cycle, record lessons learned about triggers, response effectiveness, reserve sizing, ownership clarity, review cadence, and information quality. Periodically perform risk audits and broader integrated analysis to improve the risk process itself and update organizational knowledge.

---

## 12. Decision Logic

| Condition Observed | Control Decision |
|-------------------|------------------|
| Risk no longer relevant and no residual concern remains | Close risk in A19 with closure rationale |
| Event occurred and is actively affecting objectives | Keep A19 history, open or continue A18 issue control |
| Response implemented and exposure now acceptable | Mark as residual watch or close, depending on remaining exposure |
| Response not implemented or ineffective | Replan, escalate, or raise A12 |
| New uncertainty discovered | Add new A19 entry and route to analysis and response planning |
| Aggregate exposure exceeds tolerance | Escalate to governance and review reserves / strategy |
| Trigger definition is invalid or stale | Update A19 and possibly replan contingent response |

---

## 13. Outputs

PMBOK8 Figure 2-53 identifies the outputs as **work performance information**, **change requests**, **project management plan updates**, **project document updates**, and **organizational process asset updates**.

| Output | Artifact / Record | Content |
|-------|-------------------|---------|
| **Work performance information** | Project reporting layer | Risk trend insights, reserve position, response effectiveness observations |
| **Change requests** | A12 | Corrective action, preventive action, replanning, reserve escalation, response replacement |
| **Project management plan updates** | A14-linked components | Risk management plan or other affected plans where monitoring shows needed adjustment |
| **Project document updates** | A19, A18, lessons learned register, assumptions, issue records | Status, new risks, changed triggers, residual and secondary risks, closure notes |
| **Organizational process asset updates** | Knowledge repository | Risk audit results, lessons learned, reusable guidance |

Typical A19 field updates include:
- Monitoring date
- Reviewer or owner
- Current status
- Trigger status
- Response effectiveness note
- Residual exposure note
- Secondary risk link
- Reserve sufficiency note
- Next review date
- Escalation flag
- Closure rationale if applicable

---

## 14. Tailoring Guidance

| Context | Tailoring Guidance |
|--------|--------------------|
| **Small project** | Use short cadence reviews and a compact risk board, but still separate active risks, realized issues, and closed items |
| **Large or regulated project** | Use formal audit trails, explicit trigger evidence, reserve analysis, risk review boards, and tighter escalation thresholds |
| **Adaptive project** | Monitor risks at iteration or sprint cadence, refresh triggers more frequently, and treat backlog changes as risk signals |
| **Supplier-heavy project** | Pay special attention to contractual triggers, delivery performance, external dependencies, and transferred or shared risks |
| **High-uncertainty environment** | Increase review frequency, emphasize emergent risk detection, and keep management reserve visibility high |

PMBOK8 tailoring considerations for the Risk domain emphasize project size and complexity, constraints, risk appetite and thresholds, a holistic view across domains, strategic importance, development approach, flexible risk response adjustments, advanced analysis techniques, and resilience planning.

---

## 15. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Risk register updated rarely | Stale exposure picture and late action | Test T-1 cadence and freshness check |
| Triggers exist on paper but no one watches them | Contingent responses activate too late | Test T-2 trigger ownership and evidence |
| Team marks responses complete without checking effect | False confidence and hidden residual exposure | Test T-3 effectiveness review |
| Realized risk remains only in A19 | Active problem is unmanaged as an issue | Test T-4 issue linkage |
| New secondary risk mentioned informally but not logged | New exposure is invisible to planning | Test T-5 secondary risk capture |
| Reserve sufficiency never reviewed | Project runs out of time or money buffers unexpectedly | Test T-6 reserve review |
| Monitoring focuses only on individual risks, not profile trend | Systemic exposure goes unnoticed | Test T-7 overall risk profile review |
| No lessons learned or audits occur | Same risk-management mistakes repeat | Test T-8 process-improvement loop |

---

## 16. Tests

### T-1 — Monitoring Freshness
**Assertion:** Every active risk has been reviewed at the defined cadence or after a relevant event.

**Pass condition:** A19 shows a recent monitoring date and next review date for active items.

**Fail condition:** Active risks remain unreveiwed beyond the defined cadence.

---

### T-2 — Trigger Ownership and Evidence
**Assertion:** Every contingent response has a named owner and current evidence of trigger status.

**Pass condition:** A19 shows trigger owner, trigger state, and recent evidence.

**Fail condition:** Trigger exists without current observation evidence.

---

### T-3 — Effectiveness Review
**Assertion:** Any implemented response has an effectiveness note, not only a completion note.

**Pass condition:** A19 records whether exposure decreased, remained, or worsened after implementation.

**Fail condition:** Response marked done with no effectiveness assessment.

---

### T-4 — Risk-to-Issue Conversion
**Assertion:** When a risk event occurs, a linked A18 issue exists and is actively managed.

**Pass condition:** A19 links to A18 issue control.

**Fail condition:** Risk event occurred but no issue linkage exists.

---

### T-5 — Secondary and Emergent Risk Capture
**Assertion:** Monitoring outputs create new A19 records for secondary and emergent risks when detected.

**Pass condition:** Each newly observed risk has its own ID and source linkage.

**Fail condition:** New risks appear only in narrative notes.

---

### T-6 — Reserve Sufficiency Review
**Assertion:** Risk reviews periodically assess remaining contingency and management reserve adequacy.

**Pass condition:** Monitoring records show reserve sufficiency status and any required escalation.

**Fail condition:** No evidence of reserve analysis exists.

---

### T-7 — Overall Risk Profile Review
**Assertion:** Monitoring includes not only individual risks but also aggregate trend and concentration analysis.

**Pass condition:** Review output comments on profile movement or concentration patterns.

**Fail condition:** Only item-by-item notes exist with no overall view.

---

### T-8 — Process Improvement Loop
**Assertion:** Risk monitoring periodically produces lessons learned, audit results, or process-improvement actions.

**Pass condition:** Lessons learned or audit outputs are updated and reusable.

**Fail condition:** Monitoring produces no knowledge improvement artifacts.

---

## 17. Dependency Chain

```text
UPSTREAM
SKL-03-11 — Perform Risk Analysis
SKL-03-12 — Plan Risk Responses
SKL-04-01 — Implement Risk Responses
A19 — Current risk records
A18 — Current realized issues and action tracking
A16 — Reserve position

CURRENT SKILL
SKL-05-01 — Monitor Risks

DOWNSTREAM / LOOP-BACK
A19 — Updated status, emergent, secondary, and residual risks
A18 — Realized risk issue control
A12 — Decisions, escalations, corrective or preventive actions
SKL-03-11 — Reanalyze changed or new risks
SKL-03-12 — Replan responses where monitoring shows need
SKL-04-01 — Execute newly approved or triggered responses
Knowledge assets — Lessons learned and audit outputs
```

---

## 18. Example

### Example A — Residual Threat After Mitigation
A supplier delay risk was mitigated by adding a backup vendor. Monitoring shows the primary vendor recovered, but the backup vendor created added coordination cost and only partially reduced schedule exposure. The original risk remains open in A19 with a lower schedule score but a residual cost exposure note, and a secondary coordination risk is added as a new A19 entry.

### Example B — Triggered Opportunity Review
An opportunity to accelerate deployment depended on permit approval by a specific date. Monitoring confirms the trigger occurred, the exploit response was implemented, and milestone tracking now shows a one-week gain instead of the planned two-week gain. The opportunity remains under review until the team confirms whether the remaining benefit is fully realized or whether a follow-on action is needed.

---

## 19. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project governance with escalation to program / portfolio / enterprise when thresholds are exceeded |
| **Primary Authority** | Project manager and assigned risk owners within delegated tolerance |
| **Escalate When** | Residual or aggregate exposure exceeds threshold, reserve becomes insufficient, new response exceeds authority, or overall project risk threatens value delivery |
| **Cadence** | Continuous, plus event-driven and periodic formal review |

---

## 20. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | §2.7.2.6, Figure 2-53, Table 2-11, tailoring and interaction notes | Core process definition, I/T/O, outcomes |
| Risk Management in Portfolios, Programs, and Projects: A Practice Guide | Risk-PPP | §4.8, §4.8.1, §4.8.2, Figure 4-5, §7.2.6 | Monitoring mechanics, risk audits, reassessment, residual and emergent risk handling |
| Process Groups: A Practice Guide | Process-Groups | §7.10 Monitor Risks | Detailed monitoring and controlling checks |
| SKL-04-01 — Implement Risk Responses | Predecessor skill | Repository dependency | Handoff of implemented responses for effectiveness review |

---

*Authority: PMBOK8 · Risk-PPP · Process-Groups*  
*Owner: Project Manager or designated risk lead during monitoring and controlling*  
*Predecessor: SKL-04-01 — Implement Risk Responses*  
*Loop-back Skills: SKL-03-11, SKL-03-12, SKL-04-01*
