# SKL-04-01 — Implement Risk Responses

**Skill ID:** SKL-04-01  
**Canonical Title:** Implement Risk Responses  
**Pack:** 04 — Executing  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/04-executing/SKL-04-01-implement-risk-responses.md`  
**Authority:** PMBOK8 Guide §2.7.2.5 · Figure 2-52 · PMBOK8 Guide §2.7.1 Key Concepts · Risk Management in Portfolios, Programs, and Projects A Practice Guide §4.7 and §7.2.5 · A19 Risk Management Record · A12 Change and Exception Decision Log · A18 Issue, Impediment, and Action Log · A16 Financial Management and Cost Baseline Record  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Implement Risk Responses executes the agreed risk response plans recorded in A19 so that planned actions actually occur when required, trigger conditions are monitored, reserves are used correctly, and the project's threat exposure is reduced while opportunities are captured. It is the execution bridge between SKL-03-12 (Plan Risk Responses) and SKL-05 (Monitor Risks).

PMBOK8 §2.7.2.5 defines this process as implementing sufficient risk response plans, with the key benefit that agreed responses are executed as planned to address overall project risk exposure, minimize threats, and maximize opportunities. PMI's Risk Management Practice Guide adds the critical operating detail: risk owners monitor action effectiveness and trigger conditions, risk response owners carry out agreed actions, and implementation must occur within the normal project execution framework.

---

## 2. Scope

This skill covers:
- Executing approved unconditional response actions from A19
- Monitoring and acting on trigger conditions for contingent responses
- Mobilizing response owners, risk owners, and required stakeholders
- Drawing approved contingency reserve and recording its use
- Converting realized risks into issues in A18 when the event has occurred
- Updating A19 with implementation status, actual actions taken, and immediate outcome notes
- Raising A12 entries when implementation causes or requires integrated changes outside preapproved bounds
- Recording implementation lessons learned and handoff signals to SKL-05 (Monitor Risks)

This skill does **not** cover:
- Selecting response strategies or designing them from scratch (SKL-03-12)
- Re-scoring risks or assessing residual effectiveness over time (SKL-05)
- Identifying new risks except secondary risks discovered during execution, which are captured for SKL-03-11
- Approving new reserves or major baseline changes without governance authority

---

## 3. PMBOK8 Anchor

| Field | Value |
|-------|-------|
| **Process** | Implement Risk Responses |
| **Guide Section** | §2.7.2.5 |
| **Figure** | Figure 2-52 — Implement Risk Responses Inputs, Tools and Techniques, and Outputs |
| **Performance Domain** | Risk · Governance · Finance · Schedule · Resources |
| **Focus Area** | Executing |
| **Domain Key Concepts** | Risk response, issue, contingency reserve, management reserve, resilience, trigger conditions, risk owner, response owner |
| **Primary Output Pattern** | Change requests + project document updates |
| **Secondary Authority** | Risk-PPP §4.7, §7.2.5 |

**PMI definition (paraphrased):** Implement Risk Responses is the process of executing risk plans to address project risks, minimize threats, and maximize opportunities. It ensures agreed-upon responses are carried out as planned.

---

## 4. Operating Model

This skill uses a four-state execution model:

| State | Meaning | Typical Evidence |
|------|---------|------------------|
| **Ready** | Response is fully planned in A19 and can be executed | Owner named, trigger defined, reserve source defined if needed |
| **Activated** | Trigger fired or unconditional response start authorized | A19 status updated; A18 action opened if work is needed immediately |
| **Executed** | Planned response actions were performed | Action completion evidence, communication sent, reserve use recorded if applicable |
| **Handed to Monitoring** | Response implementation is complete and effectiveness must now be observed | A19 updated with actual implementation date, issue links, secondary-risk links, and monitoring note |

This model prevents a common failure mode described in PMI guidance: teams identify and plan responses, document them, and then do nothing. A response is not complete because it was planned; it is complete only when the planned action has actually been performed and logged.

---

## 5. Roles

### 5.1 Risk Owner
The risk owner remains accountable for the assigned risk, watches trigger conditions, keeps awareness of changes in the risk profile, and decides whether the implemented response appears to have addressed the risk or whether additional actions must be planned. The risk owner is not automatically the same person as the response owner.

### 5.2 Risk Response Owner
The risk response owner carries out the agreed response actions, keeps the risk owner informed about status, and escalates blockers immediately. PMI's practice guidance explicitly separates risk ownership from response execution responsibility when useful.

### 5.3 Project Manager
The PM ensures response execution happens within the normal execution framework, coordinates cross-domain impacts, confirms approved reserves and authorities are used correctly, and raises A12 decisions when implementation exceeds existing approval boundaries.

### 5.4 Sponsor / Governing Authority
The sponsor or designated authority approves reserve use or changes when thresholds require it, accepts escalated residual exposures, and decides on major corrective direction when response implementation materially affects scope, schedule, cost, or viability.

---

## 6. Inputs

| Input | Source | Use in This Skill |
|------|--------|-------------------|
| **A19 — Risk Management Record** | SKL-03-12 | Primary source of planned responses, triggers, owners, fallback plans, residual expectations, and reserve requirements |
| **A14 — Integrated Project Management Plan** | Planning baseline | Confirms execution context, approved thresholds, and linked management components |
| **A16 — Financial Management and Cost Baseline Record** | Finance planning | Confirms approved contingency reserve and cost handling rules |
| **A18 — Issue, Impediment, and Action Log** | Execution log | Receives realized-risk issues and action tracking items |
| **A12 — Change and Exception Decision Log** | Governance | Records implementation-related exceptions, approvals, or threshold breaches |
| **Lessons learned register / A05 notes** | Prior knowledge | Helps avoid repeating ineffective responses |
| **Risk report / A19 header summary** | Monitoring context | Highlights top priorities, urgent items, and overall exposure |

Supporting inputs when applicable:
- A15 for response activities that are schedule-driven or insert new work
- A26 for response resource assignments
- Procurement records when Transfer or Share responses depend on seller action

---

## 7. Tools and Techniques

Per PMBOK8 Figure 2-52, the principal tools and techniques are **expert judgment**, **interpersonal and team skills**, **influencing**, and **project management information systems**.

### 7.1 Expert Judgment
Used to decide whether the trigger really fired, whether fallback conditions are met, whether reserve draw is within the approved bounds, and whether the implemented action matches the intent of the response plan.

### 7.2 Interpersonal and Team Skills
Used to secure stakeholder commitment, reinforce owner accountability, coordinate across functions, and remove friction when a response needs fast execution. This is especially important for contingent responses where delays reduce effectiveness.

### 7.3 Influencing
Used when the response depends on people outside the core project team, such as suppliers, compliance functions, customers, or shared-resource managers. Response execution often fails because ownership is nominal and influence was never applied.

### 7.4 Project Management Information System
Used to monitor trigger indicators, action due dates, reserve usage, response status, dependencies, and cross-links among A19, A18, A12, A15, and A16.

---

## 8. Core Execution Rules

### Rule 1 — Only execute approved responses
No response action starts unless it is already planned and authorized in A19 or separately approved through A12. Emergency action may be taken to protect people, assets, or compliance position, but it must be logged immediately afterward.

### Rule 2 — Trigger-based responses require observable triggers
A contingent response activates only when the documented trigger condition is met. Vague triggers such as "if things look bad" are invalid and should be corrected in SKL-03-12.

### Rule 3 — Realized risks become issues
Once the uncertain event has occurred, the item is no longer only a risk. It must also be logged in A18 as an issue, impediment, or action set requiring active management.

### Rule 4 — Reserve use follows authority
Contingency reserve may be used for identified risks under approved rules. Management reserve is not drawn by default and requires the appropriate authority.

### Rule 5 — Implementation may or may not need change control
PMI's practice guidance is explicit that some approved response actions are already part of the project management plan and do not require a new formal change request just to execute them. However, new responses, baseline impacts beyond preapproval, or organization-specific policy requirements do require A12 processing.

### Rule 6 — Secondary risks are captured immediately
If execution of a response creates a new threat or opportunity, that secondary risk is added to A19 with status `Identified — Awaiting Analysis` and queued for SKL-03-11.

---

## 9. Response Activation Logic

| Response Type | Activation Pattern | Typical Immediate Action |
|--------------|-------------------|--------------------------|
| **Unconditional preventive response** | Start as scheduled in the plan | Execute planned mitigation or enhancement task |
| **Contingent threat response** | Trigger threshold reached | Execute fallback or contingency action; open issue if event occurred |
| **Contingent opportunity response** | Opportunity signal appears strong enough | Execute capture action; allocate reserved capacity if approved |
| **Escalated response** | Outside project authority | Notify receiving authority; confirm acceptance; update A12 and A19 |
| **Transfer / Share response** | Contract, insurance, partner, or seller mechanism activated | Invoke contractual path, warranty, claim, bond, or shared-benefit mechanism |

---

## 10. Step-by-Step Instructions

### Step 1 — Confirm Readiness
Verify before execution:
- [ ] A19 entry status is `Response Planned — Awaiting Implementation`
- [ ] Response owner is named
- [ ] Trigger condition exists for contingent responses
- [ ] Reserve source and approval status are clear if funds or schedule buffer are needed
- [ ] Required linked change approvals are already in A12 where applicable

If any of these are missing, do not improvise. Return the item to SKL-03-12 for response-plan correction.

### Step 2 — Determine Activation Basis
Classify the response as one of the following:
1. **Scheduled / unconditional**, meaning the work should start because the plan says so.
2. **Triggered**, meaning the documented condition fired.
3. **Escalated**, meaning execution is by another authority level.
4. **Emergency protective action**, meaning immediate action is necessary and retrospective logging is required.

Record the activation basis in A19 implementation notes.

### Step 3 — Brief Owners and Stakeholders
Confirm the response owner, risk owner, PM, and any affected functional leads understand:
- The specific action to perform
- Timing and urgency
- Allowed reserve use
- Success signal or completion evidence
- Fallback path if the first action does not work

This briefing is mandatory for time-sensitive responses and for any response involving external parties.

### Step 4 — Execute the Planned Action
Carry out the planned action exactly as agreed, unless a higher authority has approved a deviation. Typical execution patterns include:
- Add redundancy or extra testing for mitigation
- Switch supplier or invoke warranty/bond for transfer-related action
- Stop or redesign work for avoidance
- Commit premium resources or fast-path enabling work for exploitation
- Activate partner engagement for sharing or transfer/share strategies
- Mobilize reserved time or funds for active acceptance and contingency execution

Update A18 with executable tasks if multiple action steps must be tracked operationally.

### Step 5 — Handle Realization and Issue Conversion
If the risk event has actually occurred:
- Open or update an A18 issue entry immediately
- Link the issue to the originating A19 risk ID
- Record the date of occurrence, current impact, and immediate containment action
- Continue the response as issue management work, not only as risk work

A19 remains the source of the original risk history; A18 becomes the live operational control record.

### Step 6 — Use Reserve Correctly
When the response draws on approved reserve:
- Confirm the reserve type: contingency or management
- Record the amount/time used and the authorization basis
- Update A16 or submit the needed finance update
- Note whether the draw was partial or full

Reserve use must never be hidden inside ordinary spending lines. It must be visible and traceable.

### Step 7 — Check for Cross-Domain Impacts
During execution, determine whether the response changes:
- Scope boundary
- Scheduled activities or milestones
- Cost baseline beyond approved reserve handling
- Resource assignments or availability
- Procurement obligations or seller commitments

If yes, create or update the corresponding A12 entry unless the action was already preapproved as part of the existing plan and within the documented authority threshold.

### Step 8 — Capture Secondary Risks and Opportunity Side Effects
Identify whether the executed response created:
- A new threat
- A new opportunity
- A changed dependency or stakeholder exposure
- A new operational interface risk

Add each as a fresh A19 entry with cross-reference to the parent response.

### Step 9 — Record Implementation Status in A19
Update the original A19 entry with:
- Activation date
- Action(s) actually executed
- Response owner completion status
- Trigger observed (if any)
- Reserve used
- Linked A18 issue ID if realized
- Linked A12 decision ID if change/exceptions were involved
- Immediate implementation outcome note
- Status: `Response Implemented — Pending Effectiveness Review`

### Step 10 — Hand Off to Monitoring
Pass the item to SKL-05 with a focused monitoring note:
- What was implemented
- What should now be observed
- What success or failure signal to watch
- When to review effectiveness
- Whether fallback remains available

Implementation is complete only when this monitoring handoff is explicit.

---

## 11. Execution Patterns by Strategy

| Planned Strategy | What Implementation Looks Like |
|------------------|--------------------------------|
| **Avoid** | Work is changed, stopped, redesigned, resequenced, or removed so the threat path no longer exists |
| **Mitigate** | Preventive or impact-reduction actions are carried out before or during the risk window |
| **Transfer** | Contractual, insurance, bond, warranty, or outsourced responsibility mechanism is activated |
| **Accept-Active** | Contingency plan or reserved budget/time is mobilized when required |
| **Accept-Passive** | No proactive action beyond watching the agreed indicator and being ready to escalate if the profile changes |
| **Exploit** | Specific steps are taken to make the opportunity happen, often with priority resources |
| **Enhance** | Probability or benefit is improved by enabling actions or selective investment |
| **Share** | A partner is engaged to co-capture the benefit under the agreed arrangement |
| **Escalate** | Ownership is formally transferred upward or outward and acceptance is confirmed |

---

## 12. Change-Control Decision Logic

Use this decision test during execution:

| Condition | A12 Needed? | Reason |
|----------|-------------|--------|
| Response action already approved in A19, within authority, within reserve bounds | **Usually no** | Execution of an already approved response is part of the current plan |
| Triggered contingency action already preapproved, within documented limits | **Usually no** | Same rationale as above |
| Response requires new scope, new budget beyond approved reserve, or altered milestone commitment | **Yes** | Integrated impact exceeds execution authority |
| New response invented during execution | **Yes** | It was not previously planned or agreed |
| Organizational policy requires all baseline-affecting changes to be logged | **Yes** | Local governance rule overrides simplified handling |

This logic follows PMI's distinction that some response execution is built into the project management plan, while new or materially different responses move through formal change control.

---

## 13. Outputs

Per PMBOK8 Figure 2-52, the main outputs are **change requests** and **project document updates**.

| Output | Artifact | Content |
|-------|----------|---------|
| **Change requests** | A12 | New approvals, exceptions, reserve escalations, or integrated impacts requiring decision |
| **Issue log updates** | A18 | Realized risks, active containment tasks, impediments, and action owners |
| **Risk register updates** | A19 | Implementation status, actual actions taken, trigger results, reserve usage, secondary-risk links, monitoring handoff |
| **Risk report updates** | A19 header / A17 | Updated top-exposure narrative where implementation materially shifts exposure |
| **Project team assignment updates** | A26 or A19 linked fields | Response-owner execution assignments as actually mobilized |
| **Lessons learned updates** | Lessons learned register / A05 | What worked, what failed, what was late, and what should be standardized |

---

## 14. Tailoring Guidance

| Context | Tailoring Guidance |
|--------|--------------------|
| **Small project** | Combine A19 and A18 updates in one short execution review; use lightweight evidence; avoid overformalizing reserve tracking if no reserve was drawn |
| **Large / regulated project** | Require explicit trigger evidence, formal execution confirmation, reserve authorization trace, and linked A12 records for any baseline effect |
| **Adaptive project** | Execute many responses inside iteration work; still log trigger-based actions and realized issues; use sprint-level cadence for response execution review |
| **Supplier-heavy project** | Put stronger emphasis on transfer/share activation mechanics, contract notices, warranty conditions, and procurement linkage |
| **High-urgency environment** | Pre-brief response owners, define emergency authority boundaries, and keep fallback mechanisms ready for rapid activation |

---

## 15. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Response was planned but never started | Exposure remains unchanged despite apparent planning maturity | Test T-2 execution evidence required |
| Trigger fired but no one noticed | Contingent response starts late and loses value | Test T-3 trigger monitoring confirmation |
| Realized risk stayed only in A19 and was not opened in A18 | Active work is unmanaged as an issue | Test T-4 issue-conversion rule |
| Reserve was used without traceable authorization | Financial control breach and false baseline visibility | Test T-5 reserve traceability |
| New response invented during execution without approval | Uncontrolled change and unclear accountability | Test T-6 A12 rule |
| Secondary risk noted informally but not added to A19 | New exposure is invisible to analysis and planning cycles | Test T-7 secondary-risk capture |
| Response owner and risk owner assumed the other person was acting | No one actually executes the plan | Test T-1 role confirmation |
| Implementation completed but no monitoring handoff occurred | Effectiveness is never checked | Test T-8 handoff rule |

---

## 16. Tests

### T-1 — Owner Readiness Confirmed
**Assertion:** Every response executed under this skill has a named risk owner and a named response owner, or a documented statement that one person holds both roles.

**Pass condition:** A19 shows role clarity before execution starts.

**Fail condition:** Execution begins with unclear ownership.

---

### T-2 — Execution Evidence Exists
**Assertion:** Any A19 entry moved to implementation has evidence that the planned action was actually performed.

**Pass condition:** A19 implementation note or linked A18 actions show dates, actor, and action taken.

**Fail condition:** Status changed to implemented with no execution evidence.

---

### T-3 — Trigger-Based Actions Cite the Trigger
**Assertion:** Every contingent response implemented under this skill records the exact trigger condition observed.

**Pass condition:** A19 includes the trigger and activation date.

**Fail condition:** Contingent response was executed with no recorded trigger or the trigger text is vague.

---

### T-4 — Realized Risks Become Issues
**Assertion:** If the uncertain event occurred, an A18 issue entry exists and is linked to the originating A19 risk.

**Pass condition:** A18 contains a linked issue record.

**Fail condition:** The event occurred but only the risk register was updated.

---

### T-5 — Reserve Usage Is Traceable
**Assertion:** Any use of contingency or management reserve during response execution is logged with amount, date, and authority.

**Pass condition:** A16 or linked finance note shows traceable reserve use.

**Fail condition:** Reserve was consumed without visible traceability.

---

### T-6 — New or Expanded Responses Follow Governance
**Assertion:** If implementation required a materially new response or exceeded approved bounds, A12 records the decision request and authority path.

**Pass condition:** Linked A12 entry exists.

**Fail condition:** Team improvised outside approved limits with no governance trace.

---

### T-7 — Secondary Risks Enter A19
**Assertion:** New threats or opportunities created by executing a response are entered as new A19 items.

**Pass condition:** Each secondary risk has its own A19 ID and reference back to the source response.

**Fail condition:** Secondary risks appear only in narrative notes.

---

### T-8 — Monitoring Handoff Exists
**Assertion:** Every implemented response ends with a clear monitoring note specifying what effectiveness signal to observe next.

**Pass condition:** A19 status is `Response Implemented — Pending Effectiveness Review` with monitoring note.

**Fail condition:** Response is marked complete with no follow-up observation requirement.

---

## 17. Dependency Chain

```text
UPSTREAM
SKL-03-11 — Perform Risk Analysis
SKL-03-12 — Plan Risk Responses
A19 — Response planned and approved
A16 — Reserve authority available if needed
A12 — Preapprovals or exceptions where applicable

CURRENT SKILL
SKL-04-01 — Implement Risk Responses

DOWNSTREAM
SKL-05 — Monitor Risks
A18 — Live issue/action control for realized events
A12 — New decisions triggered by implementation impacts
A19 — Updated implementation status and secondary-risk links
```

---

## 18. Example

### Example A — Triggered Threat Response
A19 contains risk `R-014 Supplier test failure may delay deployment`, with a contingent mitigation trigger: `Factory acceptance test defect rate > 8%`. The observed defect rate reaches 11%, so the response owner activates the fallback plan to deploy an OEM specialist team, logs the triggered action in A19, opens an A18 issue for the failed test batch, and records approved contingency spend in A16.

### Example B — Opportunity Exploit Response
A19 contains opportunity `O-006 Early permit approval could enable a 2-week acceleration`. The response owner confirms approval has been obtained, mobilizes the preplanned early-start crew, updates A19 with activation and action dates, and hands the item to SKL-05 to verify whether milestone acceleration was actually achieved.

---

## 19. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project Governance |
| **Primary Authority** | PM within approved thresholds |
| **Escalate When** | Reserve use exceeds delegated authority, a new response is required, baseline impacts exceed limits, or residual exposure threatens project viability |
| **Execution Nature** | Ongoing throughout execution; event-driven and cadence-supported |

---

## 20. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.2.5; Figure 2-52; §2.7.1 | Process definition, I/T/O, key concepts |
| Risk Management in Portfolios, Programs, and Projects: A Practice Guide | Risk-PPP | §4.7; §4.8.1-.2; §7.2.5 | Role clarity, trigger monitoring, reserve use, execution mechanics, issue conversion context |
| Process Groups: A Practice Guide | Process-Groups | 6.8 Implement Risk Responses; 7.2 Perform Integrated Change Control | Execution-process linkage and change-control interaction |
| Artifacts-V-1.0.5 | Artifacts-V-1.0.5 | A12, A16, A18, A19 | Repository artifact grounding |

---

*Authority: PMBOK8 · Risk-PPP · Process-Groups · Artifacts-V-1.0.5*  
*Owner: Project Manager or designated risk lead during execution*  
*Predecessor: SKL-03-12 — Plan Risk Responses*  
*Next Skill: SKL-05 — Monitor Risks*
