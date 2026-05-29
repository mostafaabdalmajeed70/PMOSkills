# SKL-03-07 — Plan Stakeholder Engagement
**Skill ID:** SKL-03-07  
**Skill Name:** Plan Stakeholder Engagement  
**Version:** 1.0.0-draft  
**Lifecycle Pack:** 03-Planning  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-07-plan-stakeholder-engagement.md`

---

## Purpose

Develop actionable strategies to engage each identified stakeholder — or stakeholder group — based on their needs, expectations, interests, requirements, and potential impact on the project. This skill transforms the raw stakeholder data in A07 (Stakeholder Register and Engagement Strategy) into a concrete, sequenced engagement plan that closes the gap between where each stakeholder currently is and where they need to be for the project to succeed.

The primary output is an **updated A07**, with the Engagement Strategy section populated with specific actions, owners, timing, and success signals — embedded within the Stakeholder Register and Engagement Strategy as a single maintained record per the v1.0.3 artifact model.

This skill is first executed during **planning**, after SKL-02-02 produces the initial A07. It is then **re-executed** whenever the stakeholder landscape changes materially, a major phase gate occurs, or engagement monitoring reveals that strategies are not achieving their intended effect.

---

## Scope

**In scope:**
- Analyzing engagement gaps from A07 and converting them into engagement strategies
- Assigning engagement actions with owners, timing, and success signals
- Applying the Stakeholder Engagement Assessment Matrix to visualize and prioritize gaps
- Embedding engagement strategy content into A07 (the single merged record)
- Linking high-risk engagement gaps to A19 (Risk Management Record)
- Triggering downstream communications planning (SKL-03-08)

**Out of scope:**
- Initial stakeholder identification → SKL-02-02 (must precede this skill)
- Execution of engagement actions → executing-pack skills (Manage Stakeholder Engagement)
- Communications channel and cadence design → SKL-03-08 (Plan Communications Management)
- Monitoring whether engagement strategies are working → monitoring-pack skill (Monitor Stakeholder Engagement)

---

## Authority and Governance

| Field | Value |
|-------|-------|
| **Primary PMI Source** | PMBOK8 |
| **Exact Section** | Guide §2.5.2.2 Plan Stakeholder Engagement · Guide Figure 2-34 · Guide §2.5.1 Key Concepts |
| **Purpose of Citation** | Establish engagement planning as a process that produces actionable strategies driven by stakeholder needs, expectations, and impact assessment |
| **Source Type** | PMI-derived |
| **Governance Layer** | Project Governance |
| **Artifact Produced** | A07 — Stakeholder Register and Engagement Strategy (Engagement Strategy section updated) |
| **Owner** | Project Manager |
| **Approval Authority** | Sponsor (initial baseline); ongoing updates managed by PM within thresholds |
| **Threshold Band** | T2 — strategies for high-power or governance-level stakeholders require sponsor awareness |
| **Escalate When** | A strategy for a governance body, regulatory authority, or executive sponsor requires resources, commitments, or behavioral changes beyond PM authority |

---

## Performance Domains and Principles

**Performance Domains:** Stakeholders · Governance  
**Focus Areas:** Planning · Executing · Monitoring and Controlling

| Principle | Application in This Skill |
|-----------|--------------------------|
| P5 Engage Stakeholders | Engagement planning is the direct expression of this principle — it converts identification into deliberate action |
| P2 Focus on Value | Engagement gaps that threaten value delivery must be treated as risks, not administrative items |
| P1 Adopt a Holistic View | Strategies must account for interdependencies between stakeholders — moving one may affect others |
| P7 Embrace Adaptability | Plans are updated iteratively; a strategy that was adequate at planning may be insufficient at deployment |
| P8 Build Quality Into Processes | Engagement strategies must be explicit and measurable — vague intentions ("keep informed") are not strategies |

---

## PMBOK 8 Process: Plan Stakeholder Engagement

### Inputs (per PMBOK8 Guide Figure 2-34)

| Input | Artifact / Source | Mandatory? | Notes |
|-------|------------------|-----------|-------|
| Project charter | A04 | Yes | Confirms sponsor, named PM, scope boundary — shapes engagement context |
| Resource management plan | A26 — Resource Capacity and Acquisition Record | Conditional | Identifies who is available to execute engagement actions and at what capacity |
| Communications management plan | A28 — Communications and Reporting Record | Conditional | Existing comms plan informs engagement planning; on re-runs, both must be aligned |
| Risk management plan | A19 — Risk Management Record | Recommended | Engagement risks identified in SKL-02-02 feed directly into this process |
| Assumption log | A05 — Context Register | Recommended | Assumptions about stakeholder behavior, willingness, and context shape strategy design |
| Change log | A12 — Change and Exception Decision Log | Conditional | On re-runs; approved changes that affect scope, schedule, or authority reshape engagement needs |
| Issue log | A18 — Issue, Impediment, and Action Log | Conditional | Open issues often indicate engagement failures requiring strategic recalibration |
| Project schedule | A15 — Schedule Model and Baseline Record | Recommended | Engagement actions must be timed to project milestones, phase gates, and decision points |
| Risk register | A19 — Risk Management Record | Recommended | Stakeholder-driven risks inform the urgency and priority of specific engagement strategies |
| Stakeholder register | A07 | Yes | **Primary input** — engagement gaps, influence/impact levels, and current engagement levels from SKL-02-02 |
| Agreements | Pre-existing contracts/MOUs | Conditional | Contractual stakeholders (clients, suppliers) have engagement obligations defined by agreement |
| Enterprise environmental factors (EEFs) | A05 — Context Register | Yes | Organizational culture, political awareness, communication norms, decision-making style |
| Organizational process assets (OPAs) | A05 — Context Register | Yes | Templates, lessons from prior projects, engagement playbooks, communication standards |

### Tools and Techniques (per PMBOK8 Guide Figure 2-34)

| Tool / Technique | When to Use | Key Output |
|-----------------|------------|-----------|
| Expert judgment | Always — PM and senior team members apply knowledge of stakeholder personalities, political dynamics, and organizational culture | Judgment-informed strategy choices |
| Data gathering — Benchmarking | When comparing engagement approaches to industry best practice or prior project lessons | Calibrated strategy options |
| Data analysis — Assumption and constraint analysis | When identifying which assumptions about stakeholder behavior are most fragile | Refined strategy grounded in validated assumptions |
| Data analysis — Root cause analysis | When an engagement gap is not explained by the obvious reason | Root-cause-informed corrective strategy |
| Decision-making — Prioritization / ranking | When multiple engagement gaps compete for limited PM attention and capacity | Prioritized engagement action list |
| Data representation — Mind mapping | When stakeholder interdependencies are complex and need visual unpacking before strategy design | Stakeholder influence network |
| **Data representation — Stakeholder Engagement Assessment Matrix** | Always — the core analytical tool of this skill | Completed matrix showing C (Current) and D (Desired) for each stakeholder |
| Meetings | Sponsor alignment; team review of engagement strategies; specific stakeholder sessions | Validated strategy commitments |

#### Stakeholder Engagement Assessment Matrix — Core Technique

The Stakeholder Engagement Assessment Matrix is the central tool of this skill. It maps each stakeholder against the five engagement levels, marking their **Current (C)** position and **Desired (D)** target.

| Stakeholder / Group | Unaware | Resistant | Neutral | Supportive | Leading |
|--------------------|---------|-----------|---------|------------|---------|
| Example: Sponsor | | | | | C · D |
| Example: End Users | | C | | D | |
| Example: Compliance Officer | C | | | D | |
| Example: IT Director | | | C | D | |

> The gap between C and D is the engagement gap. Every non-zero gap requires an explicit strategy with an owner and timing. A gap where C = D requires only a maintenance strategy.

**Reading the matrix:**
- C = D in any column → maintain current engagement; no escalation needed
- C is left of D → escalate engagement (inform → consult → involve → collaborate → empower)
- C is right of D → de-escalate or redirect (e.g., an over-involved stakeholder creating noise)

### Outputs (per PMBOK8 Guide Figure 2-34)

| Output | Artifact ID | Description |
|--------|------------|-------------|
| **Stakeholder engagement plan** | A07 (updated) | Primary output — Engagement Strategy section of A07 is now fully populated with strategies, actions, owners, timing, and success signals |
| **Project management plan updates** | — | The stakeholder engagement plan embedded in A07 is now the referenced subsidiary input to A14 (Integrated PM Plan) |

---

## Instructions

Execute this skill in the following sequence. The PM leads the process, ideally with sponsor review of strategies for high-power stakeholders.

### Step 1 — Confirm Prerequisites

Before starting, verify:

- [ ] A07 exists with at minimum the Identification fields populated (output of SKL-02-02)
- [ ] All mandatory A07 fields are populated: identity, interest, influence/impact, current engagement level, target engagement level
- [ ] Engagement gaps have been computed (current vs. target)
- [ ] Risk flags from SKL-02-02 are visible in A19

If A07 is not yet populated, **return to SKL-02-02** before proceeding.

### Step 2 — Build the Stakeholder Engagement Assessment Matrix

For every stakeholder or group in A07, place a **C** (Current) and **D** (Desired) marker on the five-level scale:  
`Unaware → Resistant → Neutral → Supportive → Leading`

This matrix produces the definitive gap view. It does **not** need to be a separate document — embed the matrix state in A07. The purpose of this step is to make every gap visible and comparable before strategy work begins.

**Gap classification:**

| Gap Type | Description | Priority Signal |
|----------|-------------|----------------|
| Critical Gap | C is Unaware or Resistant; D is Supportive or Leading | Immediate — highest PM attention |
| Significant Gap | C is Neutral; D is Supportive or Leading | High — plan early, measure regularly |
| Maintenance Gap | C = D | Routine — monitor only, no active strategy needed |
| De-escalation Need | C is right of D (e.g., over-involved, creating noise) | Manage carefully — requires diplomatic reduction of engagement level |

### Step 3 — Select an Engagement Approach for Each Gap

For each non-zero gap, select one or more engagement approaches from the spectrum below. The choice must reflect the stakeholder's power level, interest, organizational position, and cultural context.

#### Engagement Approach Spectrum

| Approach | Description | Best Used When |
|----------|-------------|---------------|
| **Inform** | One-way communication: provide information, updates, reports | Stakeholder needs awareness but limited interaction is appropriate (Unaware → Neutral) |
| **Consult** | Seek input and feedback on decisions, but PM retains authority | Stakeholder has domain knowledge or legitimate interest that should shape outputs (Neutral → Supportive) |
| **Involve** | Work directly with stakeholder on decisions; two-way process | Stakeholder's buy-in is required for scope, quality, or success criteria decisions (Neutral → Supportive) |
| **Collaborate** | Partner with stakeholder; shared decision authority for certain areas | High-power stakeholder whose active participation is essential for delivery (Supportive → Leading) |
| **Empower** | Delegate authority to the stakeholder for defined domains | Stakeholder takes ownership of certain decisions or deliverables (Supportive → Leading) |

> For resistant stakeholders, the approach may also include **listen and address concerns**, **one-on-one facilitation**, or **escalation to sponsor** before a standard engagement approach is applied.

### Step 4 — Define Actions, Owners, Timing, and Success Signals

For each engagement strategy, populate the following fields in A07:

| Field | Guidance |
|-------|---------|
| **Engagement action** | Specific, observable activity: a meeting, a demo, a workshop, a review, a briefing, a direct conversation |
| **Action owner** | Named person responsible — PM, sponsor, team lead, or another stakeholder as appropriate |
| **Timing / trigger** | When the action will happen: a date, a milestone, a phase gate, a sprint event, or a condition trigger |
| **Success signal** | How the team will know the strategy is working: a behavior change, a decision made, a document signed, a feedback score |
| **Escalation condition** | When the action alone is insufficient and escalation to sponsor or governance body is needed |

> **Critical constraint:** Do not write vague strategies. "Keep informed" without a specific action, owner, and timing is not a strategy — it is an intention. Every gap must have at least one specific, actionable item.

### Step 5 — Apply Root Cause Analysis for Resistant Stakeholders

For any stakeholder classified as **Resistant**, do not default immediately to a persuasion approach. First, apply root cause analysis:

**Ask:**
1. What is the stakeholder's specific objection or concern?
2. Is the resistance based on incomplete information, past experience, loss of authority, cultural mismatch, or a genuine unresolved issue?
3. Is the resistance legitimate — i.e., does the stakeholder have a valid concern that should modify the project approach?

**Then choose:**
- If the resistance is information-based → **Inform / Consult** approach
- If it is authority or role-based → escalate to sponsor to clarify roles and authority (A35)
- If the concern is legitimate → raise a change request or risk flag (A12 / A19) and address the root cause
- If it is strategic opposition → involve the sponsor directly; document in A19 as an engagement risk

### Step 6 — Validate Strategies Against Schedule and Resources

Check that:

- [ ] All engagement actions with named owners have time and capacity within the project schedule (A15)
- [ ] No engagement strategy requires more PM time than is budgeted in the resource plan (A26)
- [ ] Engagement actions for critical stakeholders are timed before — not after — their associated decision points or phase gates
- [ ] Any engagement action requiring sponsor time has been coordinated with the sponsor

### Step 7 — Check Against Risk Register

Cross-reference every engagement gap classified as Critical or Significant with A19:

- [ ] If a gap was already flagged as a risk in SKL-02-02 → confirm the engagement strategy is now the risk response for that entry
- [ ] If a gap was not previously flagged → assess whether it meets the risk threshold; if yes, add to A19 with the engagement strategy as the risk response

This ensures engagement planning and risk planning are fully integrated, not parallel processes.

### Step 8 — Present to Sponsor for Alignment

Before finalizing A07 with engagement strategies:

- Present the Stakeholder Engagement Assessment Matrix to the sponsor
- Highlight all Critical Gaps and the proposed strategies
- Confirm that the sponsor agrees with the approach for high-power stakeholders
- Confirm whether any strategies require sponsor participation as the action owner

Record the outcome of this review. For routine re-runs, this step may be lightweight (email summary); for significant re-runs, it requires a formal review session.

### Step 9 — Trigger Downstream Skills

Once A07 engagement strategies are finalized:

| Skill | What It Does |
|-------|-------------|
| SKL-03-08 | Plan Communications Management — translates engagement strategies into channel, format, cadence, and reporting design for A28 |
| SKL-Execute-04 | Manage Stakeholder Engagement — executes the strategies defined here; SKL-03-07 must precede execution |
| SKL-Monitor-04 | Monitor Stakeholder Engagement — measures whether strategies are achieving the desired C → D movement |

---

## Core Fields — A07 Engagement Strategy Section

The following fields extend the Identification fields from SKL-02-02 and must be completed by this skill:

| Field | Mandatory? | Guidance |
|-------|-----------|---------|
| **Engagement approach** | Yes | From the spectrum: Inform / Consult / Involve / Collaborate / Empower (or combination) |
| **Specific engagement actions** | Yes | At least one named, observable action per non-zero gap |
| **Action owner** | Yes | Named individual — not "the PM" generically; a real name or role |
| **Timing / trigger** | Yes | Date, milestone, phase gate, sprint event, or behavioral trigger |
| **Success signal** | Yes | Observable indicator that the strategy is working |
| **Escalation condition** | Recommended | When the action alone is insufficient; what triggers sponsor or governance escalation |
| **SEAM position (C / D)** | Yes | Current and Desired positions on the five-level scale |
| **Strategy last reviewed date** | Yes | Tracks currency; required for audit and re-run control |

---

## Tailoring Guidance

| Context | Tailoring Decision |
|---------|-------------------|
| Small, low-risk internal project | One-page engagement strategy embedded in A07; SEAM as a simple row in the register; no separate engagement plan document |
| Agile / adaptive project | Engagement planning is iterative; strategies are reviewed and updated each sprint or iteration; product owner is primary engagement interface for user stories and demos |
| Large transformation / high-change project | Full SEAM with detailed strategy per stakeholder group; sponsor review is mandatory; A29 (Change Readiness and Adoption Record) should be co-produced with this skill |
| External contract project | Contractual engagement obligations (client reviews, acceptance stages, supplier governance) are treated as mandatory fixed-point engagement events; strategy must align with contract terms |
| Multi-phase predictive project | Re-run at each phase gate; strategies for operational stakeholders must be planned before deployment phase begins |
| Resistant high-power stakeholder | Do not treat as routine; root cause analysis (Step 5) is mandatory; sponsor involvement is required; document as engagement risk in A19 |
| High-complexity regulatory project | Strategies for regulatory bodies are not optional; engagement timing is often compliance-driven; record in A35 (Governance and Decision Authority Record) |

**Do not tailor away:**
- Engagement strategy for the sponsor (governance anchor — always required)
- SEAM completion (the diagnostic core of this skill — non-negotiable)
- Root cause analysis for resistant stakeholders (P5 — required for genuine engagement)
- Success signals for all critical-gap strategies (P8 — measurability is mandatory)

---

## Failure Cases

| Failure | Indicator | Corrective Action |
|---------|-----------|-----------------|
| A07 identification section not populated | Engagement Strategy section started without current/target levels defined | Return to SKL-02-02; do not proceed |
| Strategies written as intentions, not actions | Entries like "keep informed" or "communicate regularly" with no named action, owner, or date | Rewrite each strategy entry; enforce the four mandatory fields |
| Resistant stakeholder strategy is "inform more" | Root cause not analyzed; persuasion approach assumed | Apply Step 5 root cause analysis; escalate to sponsor if needed |
| Engagement actions not timed to decision points | Actions scheduled after the milestone they are intended to influence | Reschedule actions to occur before the relevant decision point or phase gate |
| No sponsor review for critical gaps | High-power Resistant stakeholder strategy finalized without sponsor input | Return to Step 8; sponsor alignment is mandatory for critical gaps |
| Engagement plan not linked to risk register | Critical engagement gaps not referenced in A19 | Cross-reference A19 per Step 7; add risk entries for all critical gaps |
| A28 not updated after A07 finalized | Communications plan not reflecting new engagement strategies | Trigger SKL-03-08 immediately after this skill completes |
| Separate engagement plan document maintained outside A07 | Duplicate content: separate engagement plan and A07 register | Merge into A07; retire the standalone document (waste rule) |

---

## Outputs Produced by This Skill

| Output | Location | Notes |
|--------|---------- |-------|
| A07 — Stakeholder Register and Engagement Strategy (updated) | `artifacts/templates/A07-stakeholder-register.md` | Engagement Strategy section fully populated |
| A19 updates | Risk Management Record | Engagement gaps confirmed or added as risk entries |
| A14 reference update | Integrated PM Plan (subsidiary plan index) | A07 engagement strategy section is now the referenced stakeholder engagement plan subsidiary |
| Downstream trigger list | Internal record | SKL-03-08 triggered; executing and monitoring skills queued |

---

## Re-Run Schedule

| Trigger | Re-Run Type |
|---------|------------|
| Phase gate (predictive) | Full re-run; strategies must reflect the new phase's stakeholder dynamics |
| Sprint / iteration start (adaptive) | Lightweight re-run; confirm no strategy is stale; update based on retrospective signals |
| Engagement monitoring reveals strategy not working | Targeted re-run for that stakeholder; root cause analysis required |
| New stakeholder identified (SKL-02-02 re-run output) | Targeted strategy development for the newly identified party |
| Major change approved (A12) affecting scope, authority, or team | Full re-run for stakeholders directly affected by the change |
| Resistant stakeholder escalates to governance body | Immediate — involve sponsor; update strategy in A07 and risk entry in A19 |
| Project enters deployment or transition phase | Full re-run; end-user and operational stakeholder strategies become primary |

---

## Integration Points

| Connected Artifact or Skill | Relationship |
|----------------------------|-------------|
| A07 Stakeholder Register and Engagement Strategy | Both input and primary output — updated in place, not replaced |
| A04 Project Charter | Input — context for sponsor and key stakeholder engagement approach |
| A05 Context Register | Input — EEFs (culture, political awareness) and OPAs (lessons, templates) shape strategy design |
| A12 Change and Exception Decision Log | Input on re-runs; output when strategy changes trigger formal change requests |
| A14 Integrated PM Plan | Downstream — A07 engagement strategy section is the subsidiary stakeholder engagement plan |
| A15 Schedule Model and Baseline Record | Input — engagement actions must be timed to schedule milestones and decision points |
| A18 Issue, Impediment, and Action Log | Input on re-runs — open issues surface failed engagement strategies |
| A19 Risk Management Record | Bidirectional — risk flags from SKL-02-02 feed in; engagement strategy outputs feed back as risk responses |
| A26 Resource Capacity and Acquisition Record | Input — confirms PM and sponsor capacity to execute engagement actions |
| A28 Communications and Reporting Record | Downstream — engagement strategies from A07 are the primary input to communications planning |
| A29 Change Readiness and Adoption Record | Downstream (large transformation projects) — engagement strategies inform readiness planning |
| A35 Governance and Decision Authority Record | Input and downstream — regulatory or governance-body engagement must align with the authority model |
| SKL-02-02 | Upstream prerequisite — A07 identification section must be complete |
| SKL-03-08 | Downstream — Plan Communications Management consumes A07 engagement strategies |
| SKL-Execute-04 | Downstream — Manage Stakeholder Engagement executes the strategies defined here |
| SKL-Monitor-04 | Downstream — Monitor Stakeholder Engagement measures C → D movement against plans defined here |

---

## Tests

### Test T-1: Minimum Valid Engagement Strategy
**Given:** A07 with all identification fields populated and engagement gaps defined  
**When:** SKL-03-07 is executed  
**Then:** Every non-zero engagement gap must have at minimum: one specific action, one named owner, one timing reference, and one success signal — all embedded in A07

### Test T-2: SEAM Completeness Check
**Given:** A07 with stakeholder list from SKL-02-02  
**When:** Step 2 (SEAM build) is executed  
**Then:** Every stakeholder must have both a C and D position on the five-level scale; any stakeholder missing either position must block completion of the step

### Test T-3: Vague Strategy Rejection
**Given:** A strategy entry reads: "Keep IT Director informed throughout the project"  
**When:** Strategy validation is applied in Step 4  
**Then:** Skill must fail the entry and require replacement with a specific action, owner, date/trigger, and success signal

### Test T-4: Resistant Stakeholder Root Cause
**Given:** End Users group is classified as Resistant; PM proposes "send weekly status updates" as the strategy  
**When:** Step 5 root cause check is applied  
**Then:** Skill must require root cause analysis before approving the strategy; if root cause is not authority- or information-based, a more targeted approach (workshop, facilitated session, sponsor involvement) must be proposed

### Test T-5: Timing Alignment with Schedule
**Given:** Phase 2 kickoff is at Week 8; a critical stakeholder engagement strategy action is scheduled for Week 9  
**When:** Step 6 schedule validation is run  
**Then:** Skill must flag the timing conflict; action must be rescheduled to Week 7 or earlier to precede the kickoff decision point

### Test T-6: Risk Register Integration
**Given:** Two stakeholders flagged as engagement risks in A19 by SKL-02-02  
**When:** Step 7 risk cross-reference is applied  
**Then:** Both risk entries must reference the corresponding engagement strategy as the risk response; if engagement strategy is not yet assigned, skill must block completion until responses are linked

### Test T-7: Adaptive Project Re-Run
**Given:** An adaptive project completing Sprint 4; one stakeholder has moved from Neutral to Resistant during the sprint  
**When:** SKL-03-07 is re-run  
**Then:** SEAM must reflect the updated Current position; a new or revised strategy must be developed; root cause analysis (Step 5) must be applied; risk flag must be assessed for addition to A19

### Test T-8: Separate Engagement Plan Waste Check
**Given:** A standalone "Stakeholder Engagement Plan.docx" exists alongside A07  
**When:** Waste test is applied  
**Then:** Skill must flag the duplicate; recommend merging engagement strategy content into A07 and retiring the separate document

---

## Examples

### Example A — Predictive IT Migration (Phase 1 Planning)

SEAM after Step 2:

| Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |
|------------|---------|-----------|---------|------------|---------|
| VP Operations (Sponsor) | | | | | C · D |
| IT Director | | | | C · D | |
| Finance Team Lead | | | C | D | |
| End Users — Ops Staff | | C | | D | |
| Compliance Officer | C | | | D | |

**End Users — Ops Staff (Resistant → Supportive):**
- **Root cause:** Past system migration caused 3-week disruption; they fear recurrence
- **Approach:** Involve — co-design the migration testing protocol with a user representative
- **Action:** Run 2-hour user involvement workshop in Week 3 before final migration plan is approved
- **Owner:** PM + IT Director
- **Success signal:** User representative signs off on migration test plan; no escalation to union rep
- **Escalation condition:** If opposition continues after workshop, escalate to VP Operations to formally address the concern

**Compliance Officer (Unaware → Supportive):**
- **Approach:** Inform, then Consult
- **Action 1:** Send data privacy briefing deck by Week 2; schedule 30-minute review call
- **Action 2:** Include Compliance Officer in data migration review meeting at Week 5
- **Owner:** PM
- **Success signal:** Compliance Officer confirms no data privacy objection by Week 6
- **Escalation condition:** If compliance concern is substantive, raise a risk entry in A19 and involve legal counsel

---

### Example B — Adaptive Digital Product (Sprint 5 Re-Run)

SEAM update at Sprint 5:

| Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |
|------------|---------|-----------|---------|------------|---------|
| Product Owner | | | | | C · D |
| Marketing Lead | | | | C → D (no change) | |
| Legal Counsel | | C ← (was Neutral) | | D | |

**Legal Counsel (shifted from Neutral to Resistant at Sprint 5):**
- **Root cause analysis:** New regulatory guidance released; Legal Counsel concerned about compliance gap in current sprint scope
- **Approach:** Consult → Involve
- **Action:** Facilitated review session with Legal Counsel and Product Owner in Sprint 5 Review meeting
- **Owner:** Product Owner (primary) + PM (facilitates)
- **Success signal:** Legal Counsel provides written confirmation of acceptable path forward or raises a formal change request
- **Risk flag:** Added to A19 — Regulatory compliance risk; engagement strategy is the primary response; response owner: Product Owner

---

## Companion References

| Alias | Source | Relevant Section |
|-------|--------|-----------------|
| PMBOK8 | PMBOK Guide 8th Edition | §2.5.2.2 Plan Stakeholder Engagement · Figure 2-34 · §2.5.1 Key Concepts · §2.5.3 Tailoring |
| PMBOK8 | The Standard for Project Management | §3.7 P5 Engage Stakeholders · §3.3 P2 Focus on Value · §3.1 P1 Holistic View · §3.9 P7 Adaptability |
| Process-Groups | Process Groups Practice Guide | Planning Process Group · Plan Stakeholder Engagement |
| PMI-BA | Business Analysis Practice Guide | Stakeholder engagement strategies and facilitation |
| Forms-Book | PMI Practice Standard Forms | Stakeholder engagement assessment matrix reference |

---

*Source Type: PMI-derived*  
*Governance Layer: Project Governance*  
*Authority: PMBOK8 §2.5.2.2 · Figure 2-34 · Standard §3.7 P5*  
*Linked Artifact: A07 — Stakeholder Register and Engagement Strategy (Engagement Strategy section)*  
*Related Skills: SKL-02-02 · SKL-03-08 · SKL-Execute-04 · SKL-Monitor-04*  
*Re-run: Yes — periodic; triggered by phase gates, monitoring signals, and change events*
