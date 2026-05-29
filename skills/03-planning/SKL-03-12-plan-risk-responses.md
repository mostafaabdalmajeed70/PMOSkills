# SKL-03-12 — Plan Risk Responses

**Skill ID:** SKL-03-12  
**Pack:** 03 — Planning  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-12-plan-risk-responses.md`  
**Authority:** PMBOK8 Guide §2.7.2.4 · Figure 2-51 · §2.7.1 Key Concepts · §5 (Strategies for Threats, Strategies for Opportunities, Contingent Response Strategies, Strategies for Overall Project Risk) · A19 Risk Management Record · A20 Quantitative Risk and Reserve Decision Record · A16 Financial Management and Cost Baseline Record (Artifacts-V-1.0.5)  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Plan Risk Responses develops suitable and effective options, selects strategies, and agrees on actions to address individual risks and the overall project risk exposure recorded in the A19 Risk Register. This skill transforms the priority-ranked, scored A19 register — produced by SKL-03-11 — into an actionable response plan: every High and Very High entry gets a named strategy, a response owner, a trigger condition, and an action set that can be directly implemented in SKL-04 (Implement Risk Responses).

PMBOK8 §2.7.2.4 states the key benefit is that this process "identifies suitable ways to address overall project risk and individual project risks" and also "allocates resources or includes reserves" in project documents as needed [file:22]. Without this skill, identified and scored risks remain unaddressed — the register is a diagnosis without a treatment plan.

---

## 2. Scope

This skill covers:
- Selecting and documenting a response strategy for every A19 entry with status "Analysis Complete — Response Required" or "Analysis Complete — Watch and Plan"
- Designing the specific response actions, owners, trigger conditions, and estimated costs for each strategy
- Selecting strategies for overall project risk (distinct from individual risk strategies)
- Applying contingent response strategies where appropriate
- Designing consolidated responses for risk clusters that share a root cause
- Designing exploitation and enhancement strategies for opportunities with the same rigor as threat responses
- Estimating the secondary and residual risk effects of proposed responses
- Feeding reserve sizing inputs to A16 (contingency reserve) and coordinating with A20 where quantitative reserve data exists
- Updating A19 with completed response plans, response owners, trigger and fallback fields
- Identifying any response actions that require schedule, scope, or resource changes and triggering the appropriate change process (A12)

This skill does **not** cover:
- Performing risk analysis (SKL-03-11)
- Actually executing the response actions (SKL-04 — Implement Risk Responses)
- Ongoing monitoring of risk status (SKL-05 — Monitor Risks)
- Formally approving contingency reserve amounts in A16 (done by the sponsor / finance authority per A20)
- Identifying new risks (SKL-03-10)

---

## 3. PMBOK8 Anchor

| Field | Value |
|-------|-------|
| **Process** | Plan Risk Responses |
| **Guide Section** | §2.7.2.4 |
| **Figure** | Figure 2-51 — Plan Risk Responses Inputs, Tools and Techniques, and Outputs |
| **Strategy References** | PMBOK8 §5 — Strategies for Threats; Strategies for Opportunities; Contingent Response Strategies; Strategies for Overall Project Risk |
| **Performance Domain** | Risk · Finance · Governance · Schedule · Resources |
| **Focus Area** | Planning (initial run); re-run iteratively throughout Executing and Monitoring and Controlling |
| **Domain Key Concepts** | Risk response · Risk appetite · Risk threshold · Residual risk · Secondary risk · Contingent response · Active vs. passive acceptance · Contingency reserve · Management reserve (PMBOK8 Guide §2.7.1) |
| **Domain Check Results** | PMBOK8 Table 2-11 |
| **Secondary Authority** | Risk-PPP (PMI Practice Standard for Project Risk Management) |

**PMI Definition (paraphrased):** Plan Risk Responses is the process of developing options, selecting strategies, and agreeing on actions to address overall project risk exposure as well as to treat individual project risks. This process is performed throughout the project [file:22].

---

## 4. Strategy Taxonomy

PMBOK8 §5 defines distinct response strategies for threats, opportunities, and overall project risk [file:22]. This skill applies all three groups.

### 4.1 Strategies for Threats (Individual Risks — Negative)

| Strategy | Core Intent | When to Use | Key Characteristics |
|----------|-------------|-------------|---------------------|
| **Escalate** | Move ownership outside the project | Threat exceeds the PM's authority or the project's scope of control | PM notifies the appropriate level; threat is recorded in A19 for reference but is no longer actively managed by the project team |
| **Avoid** | Eliminate the threat entirely | High probability AND high negative impact; removal is feasible | Reduces probability to zero; may require scope, schedule, or resource changes; most aggressive threat strategy |
| **Transfer** | Shift ownership to a third party | Financial threats that another party can bear more effectively | Insurance, performance bonds, warranties, guarantees, fixed-price contracts; risk premium is usually paid to the transferring party |
| **Mitigate** | Reduce probability and/or impact | Threat cannot or should not be avoided; cost of mitigation is justified | Prototyping, redundancy, additional testing, selecting a more stable supplier; early action is more effective than post-event repair |
| **Accept** | Acknowledge the threat; no proactive action | Low-priority threats; mitigation cost exceeds expected harm | Active: establish a contingency reserve; Passive: periodic review only |

### 4.2 Strategies for Opportunities (Individual Risks — Positive)

| Strategy | Core Intent | When to Use | Key Characteristics |
|----------|-------------|-------------|---------------------|
| **Escalate** | Move ownership outside the project | Opportunity exceeds the PM's authority or the project's capacity to capture it | PM notifies the appropriate level; opportunity recorded in A19 for reference but not actively managed |
| **Exploit** | Ensure the opportunity definitely occurs | High-priority opportunity where certainty of realization is desired | Raises probability to 100%; assign the best resources; use new technology; most aggressive opportunity strategy |
| **Share** | Partner with a third party to capture the benefit | Opportunity is larger than the project can capture alone | Joint ventures, partnerships, special-purpose companies; risk premium paid to the sharing partner |
| **Enhance** | Increase probability and/or impact of the opportunity | High-priority opportunity where exploitation is not feasible | Focus on enabling causes; add resources to an activity to finish early; increase scale of benefit if possible |
| **Accept** | Acknowledge the opportunity; no proactive action | Low-priority opportunities; cost of response exceeds expected benefit | Active: establish a contingency reserve to capitalize if the opportunity occurs; Passive: periodic review only |

### 4.3 Strategies for Overall Project Risk

These strategies apply to the aggregate risk exposure assessed in SKL-03-11 — not to individual register entries [file:22].

| Strategy | Applies To | Description |
|----------|-----------|-------------|
| **Avoid** | Negative overall risk (High/Very High) | Take focused action to bring overall risk below threshold — may include removing high-risk scope elements; if threshold cannot be restored, project cancellation may result |
| **Exploit** | Positive overall risk | Take focused action to capture the positive aggregate — may include adding high-value scope elements, or revising risk thresholds with stakeholder agreement |
| **Transfer / Share** | Either polarity | Involve a third party to manage aggregate exposure — transfer (negative) or share (positive); may involve joint venture or special-purpose entity |
| **Mitigate / Enhance** | Negative (mitigate) or positive (enhance) | Replan project elements — change scope, priority, resource allocation, or delivery sequence to shift overall risk band toward the acceptable range |
| **Accept** | Either polarity | Continue with the project as defined, even if overall risk is outside thresholds; active acceptance = establish overall contingency reserve; passive acceptance = periodic review |

### 4.4 Contingent Response Strategies

Contingent responses are **pre-agreed actions triggered by a defined event** — they are not executed immediately but are activated when a specific trigger condition is met [file:22]. They are recorded in A19 and are ready for immediate implementation in SKL-04 when the trigger fires.

**Key fields for a contingent response:**
- Trigger condition: the specific observable event or threshold that activates the response (not just "if the risk occurs")
- Contingent action: the exact actions to be taken when the trigger fires
- Response owner: the person responsible for executing the action when triggered
- Response budget: the pre-authorized cost or time allocation for the contingent action (drawn from contingency reserve)

---

## 5. Inputs

### 5.1 Required Inputs

| Input | Source | What the Skill Uses |
|-------|--------|---------------------|
| **A19 — Risk Register (fully scored)** | SKL-03-11 (complete) | All risk entries with probability, impact, band, urgency, cascade flags, critical tags, overall risk band, and analysis status |
| **A19 — Risk Management Plan section** | SKL-03-09 (approved) | Risk appetite statement, threshold definitions, escalation authority, response format expectations |
| **A04 — Project Charter** | SKL-02-01 | Objective baselines; sponsor authority and escalation contacts |
| **A16 — Financial Management and Cost Baseline Record** | SKL-03-13 | Current contingency reserve and management reserve status; budget envelope for response cost estimation |

### 5.2 Supporting Inputs

| Input | Source | What the Skill Uses |
|-------|--------|---------------------|
| **A20 — Quantitative Risk and Reserve Decision Record** | SKL-03-11 Track 2 (if produced) | Reserve sizing recommendations (EMV / Monte Carlo P80–P50 gap) feeding A16 |
| **A15 — Schedule Model and Baseline Record** | SKL-03-06b | Activity durations and critical path — for scheduling response actions and assessing schedule reserve needs |
| **A26 — Resource Capacity and Acquisition Record** | SKL-03-14 | Resource availability for response actions that require additional staff, equipment, or contractors |
| **A07 — Stakeholder Register and Engagement Strategy** | SKL-02-02 | Stakeholder risk tolerances; escalation contacts for Escalate strategy |
| **A08 — Scope and Requirements Decision Record** | SKL-03-02/03 | Scope constraints that limit or enable Avoid and Exploit strategies |

---

## 6. Tools and Techniques

*Per PMBOK8 Figure 2-51.*

### 6.1 Expert Judgment
Applied throughout this skill to select the most effective strategy for each risk entry, calibrate response cost estimates, validate trigger conditions, and assess secondary risks. Subject matter experts, legal counsel (for Transfer strategies), and insurance specialists (for transfer via insurance) are relevant sources.

### 6.2 Data Gathering — Interviews
Structured interviews with risk owners, domain leads, and functional managers to:
- Validate proposed strategies and confirm feasibility
- Elicit specific action proposals for response design
- Confirm who the appropriate response owner should be for each entry
- Estimate the cost of proposed response actions
- Identify secondary risks the proposed response might introduce

### 6.3 Interpersonal and Team Skills — Facilitation
The PM facilitates the response planning session to ensure:
- Threats and opportunities receive symmetric attention (opportunities are not treated as optional)
- Response strategies are chosen explicitly — not defaulted to Accept without deliberate review
- Response owners accept ownership (not just assignment)
- Cascade risk clusters are discussed as a group before individual responses are designed

### 6.4 Strategies for Threats
Applied per Section 4.1 above. Selection is based on risk band, priority, urgency, feasibility, and cost-effectiveness of the proposed strategy [file:22].

### 6.5 Strategies for Opportunities
Applied per Section 4.2 above [file:22]. Symmetric treatment with threat strategies — equivalent facilitation effort is required.

### 6.6 Contingent Response Strategies
Applied per Section 4.4 above [file:22]. Most often paired with the **Accept** strategy for medium-priority threats and opportunities, but can also supplement Mitigate or Enhance strategies.

### 6.7 Strategies for Overall Project Risk
Applied per Section 4.3 above [file:22]. Assessed after individual responses are designed — because individual responses may collectively shift the overall project risk band. The overall strategy is documented in the A19 header, not in an individual risk entry.

### 6.8 Data Analysis — Alternative Analysis
When multiple response strategy options exist for a risk, evaluate them comparatively:
- Strategy A vs. Strategy B: which provides better risk reduction for the cost?
- What is the residual risk after each strategy?
- Which strategy best fits the project's risk appetite and budget envelope?
- What secondary risks does each option introduce?

### 6.9 Data Analysis — Cost-Benefit Analysis
Compares the cost of a proposed response to its expected benefit in risk reduction [file:22]:

\[ 	ext{Response Benefit} = 	ext{Risk Score (pre-response)} - 	ext{Residual Risk Score (post-response)} \]

A response is cost-effective when:
\[ 	ext{Cost of Response} \leq 	ext{EMV Reduction Achieved} \]

where \( 	ext{EMV Reduction} = (P_{pre} 	imes I_{pre}) - (P_{post} 	imes I_{post}) \) expressed in monetary or ordinal terms.

**Practical rule:** Do not spend more on preventing a risk than the risk's EMV. A $50,000 mitigation investment against a threat with EMV = $20,000 violates this rule unless secondary risk, reputation, or regulatory factors justify it.

### 6.10 Decision-Making — Multicriteria Decision Analysis
Used when selecting among multiple response options across several evaluative dimensions simultaneously [file:22]. Criteria may include: risk reduction effectiveness, cost, schedule impact, feasibility, residual risk level, secondary risk exposure, and strategic alignment. A weighted scoring matrix rates each option against each criterion.

---

## 7. Response Design Parameters

For every A19 entry that receives a response (any entry with status "Analysis Complete — Response Required"), the following fields must be populated:

| Field | Description |
|-------|-------------|
| **Response strategy** | Chosen strategy label (e.g., Mitigate, Exploit, Accept-Active) |
| **Response justification** | Why this strategy was chosen over alternatives; cost-benefit basis if applicable |
| **Specific response actions** | List of concrete, implementable actions — each action must be assignable and verifiable |
| **Response owner** | Named individual who is accountable for executing and monitoring the response (not a team or role) |
| **Trigger condition** | Observable event or threshold that activates the response (for contingent responses) or monitoring check frequency (for ongoing responses) |
| **Estimated response cost** | Labor, materials, contractor fees, or schedule buffer associated with response actions |
| **Reserve type** | Which reserve the response cost is drawn from: contingency (known risk) or management (unknown risk); or no reserve (cost absorbed in existing budget) |
| **Residual risk** | The expected probability and impact remaining after the response is implemented — expressed as a residual risk score |
| **Secondary risks** | New risks the response itself may introduce; each must be added as a new A19 entry and scheduled for SKL-03-11 analysis |
| **Fallback plan** | What will be done if the primary response fails to achieve the expected risk reduction (optional but recommended for Very High risks) |
| **Post-response status target** | The expected band after response implementation (e.g., "Mitigated from Very High to Medium") |

---

## 8. Residual Risk and Secondary Risk

### 8.1 Residual Risk
Every risk response is designed to change the probability, impact, or both — but almost never reduces a risk to zero. The **residual risk** is the remaining exposure after the response is fully implemented. It must be:
- Assessed and scored (new probability × new impact)
- Assigned to a band
- Verified to fall within the project's acceptable risk threshold (per A19 risk appetite statement)
- Documented in A19

**Governance rule:** If the post-response residual risk is still Very High or High, the response is insufficient — either an additional strategy must be layered, the strategy must be upgraded (e.g., Mitigate → Avoid), or the residual is escalated to the sponsor as a residual exposure requiring acceptance at the governance level.

### 8.2 Secondary Risk
A secondary risk is a new risk that arises **as a direct result of implementing a risk response**. Examples:
- Transferring a vendor risk via a fixed-price contract introduces the secondary risk that the vendor files a claim
- Mitigating a schedule risk by fast-tracking critical path activities introduces the secondary risk of rework from parallel execution
- Exploiting an opportunity to use a new technology introduces the secondary risk of team skill gaps

**Process rule:** Every identified secondary risk must be added as a new entry in A19 and scheduled for SKL-03-11 analysis in the next analysis run. Secondary risks are not automatically low priority — assess them explicitly.

---

## 9. Opportunity Response Principle

PMBOK8's framework treats opportunities as positive risks that deserve the same analytical and response rigor as threats [file:22]. A common failure mode is to spend 90% of the response planning session on threats and treat opportunity responses as optional. This skill enforces symmetric treatment:

- Every opportunity with band High or Very High must have a named strategy (Exploit or Enhance) with a documented rationale for why Exploit was or was not selected
- Every opportunity response must have a named owner — exploitation does not happen without an accountable person
- Accepted opportunities (passive) must include a note on why exploitation or enhancement was not cost-effective or feasible
- Opportunity contingency reserves (active acceptance) — where money or time is set aside to capture an opportunity if it materializes — are recorded separately from threat contingency reserves in A19 and A16

---

## 10. Reserve Integration

Risk responses interact directly with A16 (Financial Management Record) in two ways:

### 10.1 Contingency Reserve (Known Risks)
Contingency reserve is authorized for identified risks — it is held in A16 and may be drawn upon when a risk trigger fires. This skill provides the **reserve demand** inputs:
- For each Accept-Active response: the time or cost value of the contingency reserve needed
- For each contingent response: the pre-authorized budget needed for the contingent action
- Summed across all entries: the total contingency reserve demand

**Priority of evidence:**
1. If A20 exists (Track 2 from SKL-03-11): use the A20 reserve recommendation (EMV or Monte Carlo P80–P50 gap) as the primary evidence
2. If A20 does not exist: sum the Accept-Active reserve amounts and contingent response costs from A19 entries as the contingency reserve demand estimate

**Reserve governance rule:** The PM does not self-approve contingency reserve amounts. Reserve sizing is submitted to the sponsor and/or finance authority for approval via A20 (if Track 2) or via an A16 update with documented justification.

### 10.2 Management Reserve (Unknown Risks)
Management reserve covers unknown unknowns — risks not yet identified. It is not managed at the individual risk level and is not drawn from the contingency reserve. The PM and sponsor agree on the management reserve level as a percentage of the cost baseline or a fixed value. This skill may recommend adjusting the management reserve level if the overall project risk band has changed, but the approval authority for management reserve remains with the sponsor or governance body.

---

## 11. Response Design for Risk Clusters

When SKL-03-11 identified clusters of risks sharing a common root cause or cascade chain, this skill designs **consolidated responses** for the cluster — not N independent responses for N individual entries:

1. **Root cause cluster:** Design one response that addresses the shared root cause. If the root cause is eliminated or mitigated, all entries in the cluster benefit simultaneously.
2. **Cascade chain:** Design the response for the first risk in the chain first. If the first risk is avoided or mitigated, the cascade-dependent risks may be rendered inactive.
3. **Single owner for the cluster:** Assign one response owner for the cluster response. Individual response owners remain for entries that require independent actions.

**Efficiency test:** If N risks share a root cause and N responses are designed independently without acknowledging the cluster, the response plan has failed the consolidation check. Record the cluster consolidation in A19.

---

## 12. Step-by-Step Instructions

### Step 1 — Confirm Prerequisites (Gate)

Before response planning begins, verify:
- [ ] SKL-03-11 complete: all A19 entries have status "Analysis Complete — Response Required", "Analysis Complete — Watch and Plan", or "Analysis Complete — Accept / Monitor"
- [ ] Overall project risk band is recorded in A19 header
- [ ] A19 Risk Management Plan section contains the approved risk appetite statement and escalation authority contacts
- [ ] A16 is available (for reserve demand context) — even if not yet baselined
- [ ] If Track 2 was run: A20 is available with reserve recommendation

**If any Very High entries are present and no sponsor escalation has been recorded in A12:** Stop. Return to SKL-03-11 Step 7 escalation requirement. Do not proceed until the escalation is logged.

### Step 2 — Retrieve Analysis Inputs

Pull:
- All A19 entries with analysis status (full list, sorted by priority band descending: Very High → High → Medium → Low → Watch-only)
- A19 header: overall project risk band, cascade clusters, root cause groups, cascade chains, sensitivity-critical tags
- A19 Risk Management Plan section: risk appetite, thresholds, approved response format
- A04 charter: sponsor contacts, budget boundary
- A16: current contingency reserve status; budget envelope
- A20 (if available): reserve recommendation

### Step 3 — Assess Overall Project Risk Strategy

Before designing individual responses, assess the overall project risk band and select an overall strategy:

| Overall Band | Required Action |
|-------------|-----------------|
| **Very High** | Mandatory escalation (from SKL-03-11) + select Avoid or Mitigate/Enhance strategy at the project level; bring the overall band to an acceptable level before proceeding |
| **High** | Select Mitigate/Enhance or Transfer/Share; document overall project risk strategy in A19 header; continue with individual responses |
| **Moderate** | Active management; individual response design will likely bring the band down; document acceptance of current overall level |
| **Low / Very Low** | Accept with passive or active reserve; monitor at standard cadence |

Document the overall project risk strategy in the A19 header with the rationale.

### Step 4 — Review Risk Clusters and Cascade Chains

Review the cluster and cascade analysis from SKL-03-11:
- List all root cause groups and cascade chains
- Determine which clusters justify a consolidated response (per Section 11)
- Assign a cluster response owner for each consolidated group
- Mark cluster-response entries in A19 so that individual responses for those entries reference the cluster strategy

### Step 5 — Design Individual Responses (Very High Entries First)

For each A19 entry in priority order (Very High → High → Medium → Low):

1. **Review** the risk statement (C–E–C), probability, impact, urgency, and cascade flags
2. **Evaluate strategy options** using the Section 4 taxonomy — consider all relevant strategies before selecting
3. **Run cost-benefit analysis** (Section 6.9) for competing strategy options; select the most cost-effective option that brings residual risk within threshold
4. **Apply multicriteria decision analysis** (Section 6.10) when multiple options score comparably
5. **Design the specific response actions** — concrete, implementable, each with an owner and a due date or trigger
6. **Identify the response owner** — confirm acceptance of ownership (not just assignment)
7. **Set the trigger condition** — for contingent responses: the specific observable event; for ongoing responses: the monitoring frequency
8. **Estimate the response cost** and identify the reserve type
9. **Assess residual risk** — assign post-response P × I scores and band
10. **Identify secondary risks** — note each one for immediate entry into A19 and scheduling for SKL-03-11

**Priority rules for strategy selection:**

- **Very High threats:** Consider Avoid or Transfer before defaulting to Mitigate; Accept is not appropriate without explicit governance approval
- **Very High opportunities:** Consider Exploit before Enhance; Accept is not appropriate without a documented rationale for non-exploitation
- **High threats:** Mitigate is standard; Transfer if the financial structure supports it
- **High opportunities:** Enhance or Exploit depending on feasibility
- **Medium threats:** Accept-Active (contingency) or Mitigate with a contingent fallback
- **Medium opportunities:** Enhance or Accept-Active (contingency reserve to capture)
- **Low / Watch-only:** Accept-Passive; periodic review; no action plan required

**Escalation handling:** For any entry requiring Escalate:
- Identify the correct escalation recipient (portfolio, program, or relevant organizational authority)
- Confirm the recipient accepts ownership — an escalation without acceptance is not a completed response
- Record the acceptance in A19 and log the escalation in A12
- Remove the entry from active response tracking (still visible in A19 for reference)

### Step 6 — Design Responses for Watch-Only and Accept Entries

For entries with band Low or Watch-only:
- **Accept-Passive:** Confirm the decision; set the monitoring frequency in the A19 trigger field; no action required unless the risk escalates
- **Accept-Active (if applicable):** Estimate the contingency reserve amount if the risk occurs; record in A19 reserve field

### Step 7 — Review Opportunity Responses (Symmetry Check)

After all threat responses are designed, specifically audit the opportunity entries:
- [ ] Every High and Very High opportunity has a named strategy — not a default Accept
- [ ] Every Exploit or Enhance response has a named owner and specific actions
- [ ] Every escalated opportunity has a confirmed escalation recipient
- [ ] Opportunity contingency reserves (Accept-Active) are separately noted from threat reserves

### Step 8 — Assess Residual Overall Project Risk

After all individual responses are designed, reassess the overall project risk:
- Do the collective responses — if implemented — bring the overall project risk band to an acceptable level?
- If Yes: record the post-response expected overall risk band in A19 header
- If No: additional overall project risk strategies (per Section 4.3) are required, or the remaining residual overall risk must be formally accepted by the sponsor with an A12 entry

### Step 9 — Consolidate Reserve Demand

Compile the reserve demand from all response entries:
1. Sum all contingency reserve amounts from Accept-Active entries and contingent response budgets
2. Combine with A20 reserve recommendation (if available)
3. Produce a total contingency reserve demand figure (time and cost, separately)
4. Note whether management reserve is recommended for adjustment (based on overall risk band change since SKL-03-09)
5. Submit the reserve demand to the finance authority via an A16 update request or A20 update (if Track 2 is in effect)

### Step 10 — Identify Schedule and Resource Impacts

For every response that requires:
- **New activities in A15 (Schedule Model):** Note the activity, estimated duration, and predecessor/successor relationships; flag for SKL update
- **New resources in A26:** Note the skill, quantity, and timing needed
- **Scope changes in A08:** Note the scope adjustment and flag for change control via A12
- **Contract actions (Transfer strategy):** Coordinate with the Procurement function; flag for A31 (Procurement and Supplier Management Record)

These cross-domain impacts are change requests — each must be logged in A12 and processed through the appropriate change control path.

### Step 11 — Update A19 with Complete Response Plans

For every entry, populate all response plan fields per Section 7:
- Response strategy, justification, specific actions, owner, trigger condition
- Estimated response cost and reserve type
- Residual risk score and band
- Secondary risks (as new entries for the next SKL-03-11 run)
- Fallback plan (for Very High entries)
- Post-response status: "Response Planned — Awaiting Implementation"

Update A19 header with:
- Overall project risk strategy selected
- Post-response expected overall risk band
- Date of this response planning run
- Number of entries per response strategy type
- Total contingency reserve demand (cost and schedule)
- Pending cross-domain impacts identified

### Step 12 — Trigger Downstream

Hand off to SKL-04 (Implement Risk Responses): "A19 Risk Register has complete response plans for all analysis-complete entries. [N] entries are Response Planned — Awaiting Implementation. Post-response overall risk band is expected to reach [Band] upon implementation. Reserve demand of [Cost] / [Duration] is pending A16/A20 approval. Cross-domain change requests are logged in A12."

---

## 13. Outputs

Per PMBOK8 Figure 2-51 [file:22]:

| Output | Artifact | Content |
|--------|---------|---------|
| **Project management plan updates** | A14, A15, A16, A19 | Schedule changes from Avoid/Mitigate responses; reserve updates in A16; updated risk approach documentation |
| **Project document updates — Risk Register** | A19 | All response fields populated per Section 7; overall risk strategy in header; post-response residual risk scores; secondary risks added as new entries |
| **Project document updates — Risk Report** | A19 header / A17 | Summary risk report: strategy distribution, reserve demand, key response owners, post-response overall risk band |
| **Project document updates — Assumption Log** | A05 | New assumptions identified during response design (e.g., "This response assumes vendor A is available at the required capacity") |
| **Project document updates — Cost Forecasts** | A16 | Updated contingency reserve demand; any response costs that must be added to cost estimates |
| **Project document updates — Project Schedule** | A15 | Response actions that become scheduled activities |
| **Project document updates — Project Team Assignments** | A26 | Response owners formally noted as responsible parties |
| **Change requests** | A12 | Any response requiring scope, schedule, cost, or resource changes outside current thresholds |

---

## 14. Tailoring Guidance

| Dimension | Guidance |
|-----------|---------|
| **Small / low-complexity project** | Simple response for each entry: strategy label, one action, one owner, one trigger; no contingent response tables needed; verbal acceptance by owners in a team meeting |
| **Medium project** | Full response design for High and Very High entries; simplified Accept-Active or Accept-Passive for Medium and Low; cascade cluster check mandatory if any clusters were identified in SKL-03-11 |
| **Large / high-complexity project** | Full response design for all non-Watch-only entries; contingent response tables for Very High entries; multicriteria decision analysis for competing options; formal fallback plans; reserve demand coordinated with A20 and sponsor |
| **Adaptive / sprint-based project** | Response planning embedded in sprint planning; strategies and owners noted in the A19 entry; contingent responses trigger during sprint execution without requiring a new formal response-planning cycle; reserve treated as team capacity buffer in the backlog |
| **Fixed-price contract** | Transfer strategy (via fixed-price mechanism) has already been applied at the contractual level for many risks — document this explicitly in A19 so responses are not double-designed; focus the remaining register entries on residual and secondary risks from the contracting arrangement |
| **Re-run (mid-project)** | Re-plan responses only for entries whose band has changed since the last run, entries with newly fired triggers that did not resolve as expected, and newly added entries from the latest SKL-03-11 run; do not re-design stable, functioning response plans |

---

## 15. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Responses designed before analysis is complete | Priority ranking is unavailable; resources are misallocated to low-priority risks | Test T-1 gate enforces SKL-03-11 completion prerequisite |
| Default Accept for all High entries without deliberate choice | High risks remain unaddressed; the register is a risk list with no defense | Test T-2 checks that High and Very High entries have non-Accept strategies (or documented escalated acceptance) |
| Opportunities left without a response strategy | Exploitation potential is lost; the opportunity register becomes decorative | Test T-3 checks opportunity strategy completeness |
| Response owner assigned without acceptance | The response will not be executed — ownership without accountability is nominal | Test T-4 requires documented owner acceptance |
| Residual risk not assessed | No evidence that the response will bring risk within threshold; governance is blind to remaining exposure | Test T-5 enforces residual risk scoring on all responded entries |
| Secondary risks not entered into A19 | New risks introduced by responses are invisible; they cannot be analyzed in SKL-03-11 | Test T-6 checks that identified secondary risks appear as new A19 entries |
| Response cost exceeds contingency reserve envelope without approval | Budget breach; illegal draw on reserves without authority | Test T-7 checks that total response cost demand is submitted for A16/A20 approval |
| Cross-domain impacts not flagged as change requests | Schedule, scope, or resource impacts proceed without governance approval | Test T-8 checks that A12 entries exist for all responses with cross-domain impacts |
| Separate response spreadsheet created outside A19 | Dual maintenance; A19 goes stale; waste rule §3.2 violated | Test T-9 enforces single-artifact rule |

---

## 16. Tests

### T-1 — Prerequisite Gate (SKL-03-11 Complete)

**Assertion:** SKL-03-12 cannot begin until all A19 entries have analysis status (no "Awaiting Analysis" entries remain) and the overall project risk band is recorded in the A19 header.

**Pass condition:** Zero blank probability/impact/band fields in A19; overall risk band is present in A19 header; no Very High entries without A12 escalation log.

**Fail condition:** Any entry still shows "Awaiting Analysis"; or overall risk band field is blank; or a Very High entry exists with no A12 escalation.

**Test type:** Pre-execution gate (block)

---

### T-2 — No Undeclared Default-Accept for High and Very High Entries

**Assertion:** Every A19 entry with band Very High or High has a documented response strategy that is not Accept-Passive unless accompanied by explicit sponsor approval logged in A12.

**Pass condition:** All Very High and High entries have a strategy of: Escalate (with accepted escalation), Avoid, Transfer, Mitigate, Accept-Active with reserve, or Exploit/Share/Enhance/Exploit — none left as Accept-Passive without a governance authorization.

**Fail condition:** Any Very High or High entry has "Accept-Passive" or blank strategy with no A12 escalation approving the acceptance at that band level.

**Test type:** Strategy adequacy check

---

### T-3 — Opportunity Response Completeness

**Assertion:** All A19 entries with Risk Type = "Opportunity" and band High or Very High have a named response strategy (Escalate, Exploit, Share, Enhance, or Accept-Active), a named response owner, and specific response actions.

**Pass condition:** All High/Very High opportunities have non-blank strategy, owner, and actions fields. No High/Very High opportunity is Accept-Passive without a documented rationale for non-exploitation.

**Fail condition:** Any High or Very High opportunity has blank strategy, blank owner, or blank actions — indicating the opportunity response was skipped.

**Test type:** Coverage check for opportunity parity

---

### T-4 — Response Owner Acceptance Documented

**Assertion:** Every A19 entry with a planned response has a named response owner who has confirmed acceptance of the ownership role (not merely been assigned it).

**Pass condition:** A19 ownership-acceptance field (or a note in the response justification field) confirms the owner was informed and accepted the role during the response planning session.

**Fail condition:** Any High or Very High entry has a response owner listed with no acceptance notation — the owner may not know they are responsible.

**Test type:** Accountability confirmation check

---

### T-5 — Residual Risk Scored for All Responded Entries

**Assertion:** Every A19 entry with status "Response Planned — Awaiting Implementation" has residual probability, impact, and residual risk score fields populated.

**Pass condition:** All responded entries have non-blank residual scores. Residual band is at or below the project's acceptable risk threshold (per A19 Risk Management Plan section) — or a governance acceptance is recorded in A12 for residuals that remain above threshold.

**Fail condition:** Any responded entry has blank residual risk fields; or any residual band remains Very High or High without a corresponding A12 acceptance entry.

**Test type:** Completeness and governance compliance check

---

### T-6 — Secondary Risks Entered into A19

**Assertion:** Every secondary risk identified during response design has been added as a new A19 entry with status "Identified — Awaiting Analysis" and is scheduled for analysis in the next SKL-03-11 run.

**Pass condition:** All secondary risks mentioned in the response design notes exist as standalone A19 entries with C–E–C statements and RBS categories assigned.

**Fail condition:** A secondary risk is described in the response notes of an existing entry but does not appear as its own A19 entry — it cannot be analyzed, prioritized, or responded to if it only exists in a note field.

**Test type:** Completeness check — applied per secondary risk identified

---

### T-7 — Reserve Demand Submitted for Approval

**Assertion:** The total contingency reserve demand (cost and schedule) calculated from all Accept-Active and contingent response entries has been submitted to the finance authority for A16 or A20 approval. The PM has not self-approved reserve levels.

**Pass condition:** A16 update request or A20 update exists with the reserve demand figure; approval status is noted (Pending / Approved / Revised); the submission is traceable to A12 if the reserve adjustment requires a change request.

**Fail condition:** Total reserve demand was calculated but not submitted; or the PM recorded a reserve amount in A16 without documented authority.

**Test type:** Governance compliance check

---

### T-8 — Cross-Domain Impacts Logged as Change Requests

**Assertion:** Any response action that requires a change to A15 (schedule), A08 (scope), A16 (budget beyond reserve envelope), or A26 (resource allocation) has a corresponding entry in A12 (Change and Exception Decision Log) pending the appropriate approval.

**Pass condition:** A12 contains change request entries for each cross-domain impact identified in Step 10. Each entry has an impact summary, a decision authority, and an outcome (Pending / Approved / Rejected).

**Fail condition:** A15, A08, or A26 is modified to accommodate a risk response with no A12 entry — the change bypassed governance.

**Test type:** Change governance compliance check

---

### T-9 — No Separate Response Spreadsheet

**Assertion:** No standalone risk response plan spreadsheet, risk treatment register, or response tracker exists as a separate artifact outside A19.

**Pass condition:** Post-skill review finds no separate response document. All response fields are in A19. A working-session scratchpad may exist temporarily but must not be maintained as a living document alongside A19.

**Fail condition:** A "Risk Response Plan.xlsx" or equivalent exists alongside A19 with response fields that duplicate the A19 register. Waste rule §3.2 is violated.

**Test type:** Artifact waste check

---

## 17. Dependency Chain

```
UPSTREAM (must complete before SKL-03-12)
──────────────────────────────────────────
SKL-03-11 → A19 scored, ranked, banded    [mandatory gate — Test T-1]
A12 → Very High escalation logged          [mandatory — SKL-03-11 escalation rule]
A04, A16, A07                              [supporting context inputs]
A20 (Track 2)                              [if available — reserve demand input]

DOWNSTREAM (reads outputs of SKL-03-12)
───────────────────────────────────────
SKL-04 — Implement Risk Responses
  ├── Reads: A19 response actions, owners, trigger conditions
  ├── Reads: A19 contingent response budgets (sourced from approved A16 reserve)
  ├── Reads: A12 change requests (approved response-related changes)
  └── Reads: A26 resource assignments for response execution

A16 Financial Management Record update
  └── Reserve demand approval: sponsor / finance authority

A15 Schedule Model update
  └── New activities for response actions (where Avoid or Mitigate required schedule changes)

A12 Change and Exception Decision Log
  └── Cross-domain change requests from Steps 9–10

A05 Context Register update
  └── New response assumptions recorded

ITERATIVE RE-RUN TRIGGERS:
New secondary risks added in A19 → schedule SKL-03-11 + SKL-03-12 for those entries
Risk band changes mid-project → re-run SKL-03-12 for affected entries
Response effectiveness review (Monitor Risks) flags failing response → re-design in SKL-03-12
Phase gate → review all current response plans for continued adequacy
```

---

## 18. Examples

### Example A — Small Predictive Project (Office Relocation, 3 months)

**Context:** 3-entry A19 register from SKL-03-11 Example A.

| Risk ID | Band | Type | Strategy Selected | Owner | Trigger / Monitoring | Residual Band |
|---------|------|------|------------------|-------|---------------------|---------------|
| R-001 | High | Threat | Mitigate — negotiate early delivery commitment with building contractor; include penalty clause | Logistics Lead | If confirmed delivery date slips by >1 week, activate fallback (temporary space) | Medium |
| R-002 | Low | Threat | Accept-Passive | PM | Monthly review | Low |
| R-003 | Medium+ | Opportunity | Enhance — brief the facilities team on cost-saving reconfiguration options before final layout is locked | PM | Facilities design sign-off date | Low+ |

**Overall project risk strategy:** Accept-Active — contingency reserve of 1 week buffer in schedule and $5,000 in budget.  
**Reserve demand:** $5,000 contingency (PM has delegated authority within charter budget boundary — no A20 required).

---

### Example B — Adaptive Software Project (Scrum, Sprint 1)

**Context:** 3-entry A19 from SKL-03-11 Example B.

| Risk ID | Band | Type | Strategy Selected | Owner | Trigger / Monitoring | Residual Band |
|---------|------|------|------------------|-------|---------------------|---------------|
| R-001 | High | Threat — immediate | Avoid — clarify the ambiguous API specification with the integration team before Sprint 2 begins; do not proceed with dependent development until confirmation received | Lead Developer | Confirmation received / not received by Day 3 of Sprint 1 | Low |
| R-002 | Medium | Threat | Accept-Active — add 2-hour test buffer to Sprint 2 backlog | QA Lead | If test session overrun >20% observed in Sprint 1 | Low |
| R-003 | Low+ | Opportunity | Accept-Passive — note the reuse potential in Sprint retrospective | PM | Sprint retrospective | Low+ |

**Overall project risk strategy:** Accept-Moderate — Sprint velocity buffer maintained as implicit contingency.  
**Secondary risk:** Delaying integration work past Day 3 introduces secondary risk R-004 (blocked Sprint 2 dependent stories) — added to A19 for SKL-03-11 analysis at Sprint 2 planning.

---

### Example C — Large Infrastructure Project ($12M, 24 months)

**Context:** 67-entry A19 from SKL-03-11 Example C; Track 2 A20 available with $525K contingency recommendation.

**Top 5 responses for Very High and top-tornado entries:**

| Risk ID | Band | Type | Strategy | Owner | Response Actions Summary | Residual Band | Secondary Risk |
|---------|------|------|---------|-------|--------------------------|---------------|----------------|
| R-5.2 | Very High | Threat | Mitigate + contingent fallback | Systems Integrator Lead | (1) Add FAT testing phase before installation; (2) if FAT fails, contingent action = use OEM remote commissioning team | High → Medium | R-5.2a: FAT schedule delay (new entry) |
| R-4.6 | Very High | Threat | Transfer (insurance bond) + Mitigate | Procurement Lead | (1) Require piling contractor to post performance bond; (2) add 2-week schedule float after piling phase | Medium | R-4.6a: Bond claim administration burden (new entry) |
| R-3.1 | Very High | Opportunity | Exploit | PM + Sponsor | (1) Secure early material delivery commitment; (2) pre-position team for mobilization 3 weeks ahead of baseline | High → Medium+ (exploit: realized gain) | None |
| R-7.2 | High | Opportunity | Enhance | QA Lead | (1) Pre-position additional hydrotest inspector; (2) develop accelerated hydrotest protocol | Low+ | None |
| R-2.4 | High | Threat | Avoid | Engineering Lead | Revise design specification to remove dependency on single-source component; substitute approved alternate | Low | R-2.4a: Design revision schedule impact (A12 change request) |

**Overall project risk strategy:** Mitigate/Enhance — implementation of the top 5 responses is expected to reduce the overall band from High to Moderate. Remaining residual exposure accepted by sponsor (A12 entry logged).

**Reserve demand submitted to finance authority:**
- Contingency reserve: $525,000 (per A20 Monte Carlo P80–P50 recommendation)
- Management reserve: 3% of cost baseline ($360,000) — sponsor approval pending

---

## 19. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project Governance |
| **Threshold Band** | T2 — PM manages response design; sponsor review required for Very High residuals and for reserve approval; all cross-domain change requests follow the A12 authority matrix |
| **Iterative nature** | Re-runs triggered by: new secondary risks, band changes mid-project, failing response effectiveness reviews in Monitor Risks, and phase gates |

---

## 20. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.2.4; Figure 2-51; §2.7.1 Key Concepts; §5 Strategies for Threats, Opportunities, Overall Project Risk, Contingent Response Strategies | Process basis, I/T/O, strategy taxonomy, response design principles |
| Artifacts-V-1.0.5 | Artifacts-V-1.0.5 | A19 Risk Management Record; A20 Quantitative Risk and Reserve Decision Record; A16 Financial Management Record; A12 Change and Exception Decision Log | Artifact schema, field definitions, governance layer, waste tests |
| PMI Practice Standard for Project Risk Management | Risk-PPP | Response strategy depth, residual and secondary risk principles | Secondary authority for response design methodology |
| PMI Lexicon of Project Management Terms | Lexicon | v5.0, January 2026 | Definitions: risk response, residual risk, secondary risk, contingency reserve, management reserve, active/passive acceptance |

---

*Authority: PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules §3.1 Waste Rule · §3.2 Consolidation Rule*  
*Owner: Project Manager or designated risk lead*  
*Iterative: Re-runs triggered by new secondary risks, band changes, failing responses, and phase gates*  
*Predecessor: SKL-03-11 — Perform Risk Analysis*  
*Next Skill: SKL-04-Implement Risk Responses*
