# SKL-03-10 — Identify Risks

**Skill ID:** SKL-03-10  
**Pack:** 03 — Planning  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-10-identify-risks.md`  
**Authority:** PMBOK8 Guide §2.7.2.2 · Figure 2-49 · §2.7.1 Key Concepts · A19 Risk Management Record (Artifacts-V-1.0.5)  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Identify Risks recognizes both **threats** (negative risks) and **opportunities** (positive risks) affecting the project, converts them from vague concerns into formally structured risk statements, and enters them as the initial population of the A19 Risk Register section. Risk identification is **iterative** — it does not end after this skill runs once. Every risk review triggered by the A19 plan cadence is a re-run of this skill against new project information.

This skill also absorbs and formalizes the engagement risk flags inserted into A19 by SKL-02-02 and SKL-03-07. Those entries exist as preliminary flags; this skill elevates them to full risk statements with all required fields populated.

Without this skill, A19 has a Risk Management Plan but no risk entries. SKL-03-11 (Perform Risk Analysis) cannot run against an empty register.

---

## 2. Scope

This skill covers:
- Applying structured identification techniques to surface threats and opportunities across all A19 RBS categories
- Writing every risk in the mandatory cause–event–consequence (C–E–C) structure
- Classifying every risk against the A19 RBS taxonomy
- Assigning a named risk owner to every entry
- Distinguishing genuine risks from issues, concerns, constraints, and non-risks — and correctly routing non-risks
- Promoting preliminary engagement risk flags from SKL-02-02 and SKL-03-07 to full A19 risk entries
- Populating all mandatory A19 Risk Register fields for each identified risk
- Re-running identification at each plan-defined cadence or trigger event

This skill does **not** cover:
- Scoring probability and impact (SKL-03-11)
- Developing response strategies (SKL-03-12)
- Implementing responses (SKL-04-Implement Risk Responses)
- Resolving issues (A18 — Issue, Impediment, and Action Log)
- Sizing reserves (SKL-03-11 / SKL-03-12 in coordination with A16)

---

## 3. PMBOK8 Anchor

| Field | Value |
|-------|-------|
| **Process** | Identify Risks |
| **Guide Section** | §2.7.2.2 |
| **Figure** | Figure 2-49 — Identify Risks Inputs, Tools and Techniques, and Outputs |
| **Performance Domain** | Risk · Governance |
| **Focus Area** | Planning (initial run); iterative throughout Executing and Monitoring and Controlling |
| **Domain Key Concepts** | Risk vs. issue · Threats vs. opportunities · Risk classification (Figure 2-46: Known-Known, Known-Unknown, Unknown-Known, Unknown-Unknown) · Cause–event–consequence · Overall risk vs. individual risk (PMBOK8 Guide §2.7.1) |
| **Domain Check Results** | PMBOK8 Guide Table 2-11 |
| **Secondary Authority** | Risk-PPP (PMI Practice Standard for Project Risk Management) |

**PMI Definition (paraphrased — not reproduced):** Identify Risks includes recognizing both negative and positive risks. The process focuses on distinguishing genuine risks from non-risks such as concerns and issues. Risk identification should be iterative, allowing for continuous identification as more information becomes available (PMBOK8 Guide §2.7.2.2).

---

## 4. Critical Distinction: Risk vs. Non-Risk

Before writing any A19 entry, classify each candidate using the routing table below. Entering non-risks into the risk register creates noise that degrades the quality of analysis in SKL-03-11 and obscures genuine exposures.

| Candidate Type | Definition | Correct Destination |
|---------------|------------|-------------------|
| **Risk (Threat)** | Uncertain future event that, if it occurs, would negatively impact one or more project objectives | A19 Risk Register — full entry required |
| **Risk (Opportunity)** | Uncertain future event that, if it occurs, would positively impact one or more project objectives | A19 Risk Register — full entry required |
| **Issue** | Condition or situation that has **already occurred** and requires action or management attention | A18 — Issue, Impediment, and Action Log |
| **Constraint** | Fixed boundary on scope, time, cost, or quality that is known and cannot be changed | A05 Context Register or A08 Scope Record |
| **Assumption** | Held-to-be-true statement that is not yet verified — may generate a risk if proven false | Document as an assumption in A05; convert to a risk if the assumption failing would impact objectives |
| **Concern** | General worry or preference of a stakeholder — not a specific uncertain event | A07 Stakeholder Register; track for escalation if it becomes a risk |

**Key rule:** An issue that has already started is not a risk. Route it to A18 immediately. A risk that has materialized and is now an active problem is also an issue — close the risk entry, open an A18 entry.

---

## 5. Risk Statement Format: Cause–Event–Consequence (C–E–C)

Every A19 risk entry must be written in C–E–C structure. Vague risk statements ("risk of delay," "stakeholder issues") are rejected at Test T-3.

### C–E–C Template:
> **"Because of [CAUSE], there is a risk that [EVENT], which could result in [CONSEQUENCE]."**

| Component | Definition | Example |
|-----------|------------|---------|
| **Cause** | The existing condition, fact, or trigger that creates the possibility of the risk | "Because the integration between System A and System B relies on a third-party API with no SLA" |
| **Event** | The specific uncertain event that may or may not occur | "there is a risk that the API becomes unavailable or changes without notice" |
| **Consequence** | The impact on project objectives if the event occurs | "which could result in a delay of 3–6 weeks and a rework cost of approximately $20,000" |

**Full example:**  
*"Because of the third-party API dependency with no SLA, there is a risk that the API becomes unavailable or changes without notice, which could result in a schedule delay of 3–6 weeks and rework costs of approximately $20,000."*

**Opportunity example:**  
*"Because the project team has early access to the vendor's beta SDK, there is an opportunity that early adoption delivers performance improvements beyond the baseline specification, which could result in a 15% reduction in processing time and enhanced stakeholder satisfaction."*

---

## 6. Risk Classification (PMBOK8 Figure 2-46)

Every risk must be classified against two axes when entered into A19:

### 6.1 Knowledge Classification

| Class | Definition | Implication for Identification |
|-------|------------|-------------------------------|
| **Known-Known** | Facts and fixed requirements — not a risk | Do not enter in the register; document in A05 or A08 |
| **Known-Unknown** | Identified uncertainty with assessable probability and impact | Standard A19 risk entry; full C–E–C + analysis in SKL-03-11 |
| **Unknown-Known** | Knowledge exists in the community but not with this team | Addressed through expert engagement; may convert to Known-Unknown once expertise is consulted |
| **Unknown-Unknown** | Truly emergent; cannot be identified at this time | Addressed through management reserves and project resilience practices — not a register entry |

**Practical rule:** A19 risk entries are Known-Unknown risks. The register cannot capture Unknown-Unknowns by definition. Management reserves (documented in A19/A16) are the governance mechanism for Unknown-Unknowns.

### 6.2 RBS Category Classification

Classify every A19 entry against the RBS taxonomy established in SKL-03-09. The category field in A19 must be populated before the entry is considered complete. An entry with an empty category field cannot proceed to SKL-03-11 analysis.

---

## 7. Inputs

### 7.1 Required Inputs

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A19 — Risk Management Plan section** | SKL-03-09 (approved) | Methodology, RBS taxonomy, P×I scale, cadence — the governing framework for all identification work |
| **A04 — Project Charter** | SKL-02-01 | High-level objectives, scope boundary, budget constraints — used to calibrate consequences in C–E–C statements |
| **A05 — Context Register** | SKL-02-01 | EEFs, OPAs, assumptions, constraints — primary source for cause identification; organizational lessons learned surface historical risk patterns |
| **A07 — Stakeholder Register and Engagement Strategy** | SKL-02-02 / SKL-03-07 | Engagement risk flags to be promoted; stakeholder tolerances that shape consequence severity |

### 7.2 Supporting Inputs (use if available)

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A08 — Scope and Requirements Decision Record** | SKL-03-02 through SKL-03-04 (if built) | Scope assumptions and constraints that may generate risks when violated; in-scope/out-of-scope boundaries |
| **A15 — Schedule Model** | SKL-03-06b (if built) | Schedule-related assumptions and dependencies that surface scheduling risks |
| **A16 — Financial Management Record** | SKL-03-13 (if built) | Cost estimate assumptions that may generate financial risks |
| **Lessons learned register (OPA)** | A05 | Historical risk patterns from similar past projects — feeds checklists and brainstorming |
| **A18 — Issue, Impediment, and Action Log** | Ongoing | Confirms which conditions have already materialized as issues so they are not duplicated in A19 |

---

## 8. Tools and Techniques

*Per PMBOK8 Figure 2-49.*

### 8.1 Expert Judgment
Consult domain experts, technical leads, experienced PMs, and subject matter specialists to surface risks outside the PM's direct knowledge domain. Expert judgment is the primary tool for identifying Unknown-Known risks — risks the community knows about but the project team does not yet.

**Structured approach:** Conduct 1:1 interviews with key experts (see Section 8.2). Do not rely solely on group workshops — experts often hold back in group settings due to social dynamics.

### 8.2 Data Gathering — Interviews
Structured individual interviews with key stakeholders, technical leads, and domain experts. Each interview should:
- Use the RBS taxonomy as a prompt guide (review each category with the interviewee)
- Ask for both threats **and** opportunities — interviewees default to threats without explicit prompting
- Probe assumptions: "What would have to be true for this to succeed? What if that turns out not to be true?"
- Probe constraints: "Is there anything about the way this project is set up that could create problems?"
- Record candidate risks using the C–E–C template during the interview

### 8.3 Data Gathering — Brainstorming
Facilitated group session designed to generate a broad pool of risk candidates quickly. Rules:
- Use the RBS taxonomy categories as the brainstorming structure — work through each category systematically
- Diverge first (generate without evaluation); converge second (filter against the risk/non-risk routing table)
- Capture all candidates; classify and filter after the session
- Ensure opportunities are explicitly solicited — use the framing: "What conditions could work in our favor?"

**Adaptive-approach note:** In agile/adaptive delivery, risk identification at sprint planning is effectively a focused brainstorming session constrained to the upcoming iteration's scope. The same C–E–C structure applies.

### 8.4 Data Gathering — Checklists
Use OPA-sourced checklists (from A05) or the RBS taxonomy categories as a structured prompt list to ensure coverage. Checklists are a memory aid, not a substitute for expert judgment or brainstorming. A risk not on the checklist is still a risk.

**Caution:** Do not treat a completed checklist as evidence that identification is complete. Checklists capture Known-Unknowns from past experience; they cannot surface novel risks specific to this project.

### 8.5 Data Analysis — Root Cause Analysis
For each identified risk, trace backward to identify the **cause** (the first C in C–E–C). Multiple risks may share the same root cause. Identifying shared causes enables more efficient responses in SKL-03-12 — one response may address multiple risks simultaneously.

**Application:** Group identified risks by root cause. Risks sharing a root cause are often related risks; their combined exposure may be higher than each risk considered independently.

### 8.6 Data Analysis — Assumption and Constraint Analysis
Review all assumptions documented in A05 and A08. For each assumption:
- Ask: "What happens to the project if this assumption turns out to be false?"
- If the answer is a negative impact on objectives → write a C–E–C risk entry for it
- If the answer is a positive impact → write a C–E–C opportunity entry

Review all constraints documented in A05 and A08. For each constraint:
- Ask: "What risks does this constraint create?" (e.g., a fixed end-date constraint creates scheduling risk from any delay)

### 8.7 Data Analysis — SWOT Analysis
Use a Strengths–Weaknesses–Opportunities–Threats analysis to ensure the identification session captures both internal and external risk sources and both positive (opportunities) and negative (threats) dimensions.

| Quadrant | Risk Identification Use |
|----------|------------------------|
| **Strengths** | Prompt identification of opportunities that internal capabilities could exploit |
| **Weaknesses** | Prompt identification of threats arising from internal limitations |
| **Opportunities** | Prompt identification of external positive risk events the project could benefit from |
| **Threats** | Prompt identification of external negative risk events that could harm the project |

### 8.8 Data Analysis — Document Analysis
Review relevant project documents for embedded risk signals:
- A04 (Charter): high-level risks mentioned but not yet structured
- A05 (Context Register): EEF constraints, regulatory requirements, technology environment
- A07 (Stakeholder Register): engagement risk flags from SKL-02-02 and SKL-03-07
- A08 (Scope Record): scope assumptions, acceptance criteria that may be hard to meet
- Prior project post-mortems (OPA via A05)

### 8.9 Interpersonal and Team Skills — Facilitation
The PM or risk lead facilitates identification sessions in a way that:
- Creates psychological safety for surfacing uncomfortable risks (especially risks involving organizational, leadership, or stakeholder dynamics)
- Ensures quieter team members contribute (use nominal group technique if dominant voices suppress others)
- Keeps the session focused on the C–E–C format and RBS taxonomy

### 8.10 Prompt Lists
Use the RBS taxonomy categories from A19 as a structured prompt list. For complex projects, PMBOK8 references PESTLE (Political, Economic, Social, Technological, Legal, Environmental) as an external environment prompt list.

Standard prompt list categories to review in every identification session:
- Technical risks (complexity, integration, technology maturity)
- Schedule risks (estimation accuracy, dependencies, external timing)
- Financial risks (cost estimate confidence, funding, currency)
- Stakeholder and organizational risks (engagement, resistance, governance delays)
- External risks (market, regulatory, environmental, competitive)
- Resource risks (availability, competency, supplier)

### 8.11 Artificial Intelligence
PMBOK8 Appendix X3 and §2.7.3 explicitly reference AI/generative AI as an emerging tool for risk identification. AI tools may be used to:
- Analyze similar project records for common risk patterns
- Generate candidate risk statements from scope and stakeholder documentation
- Surface Unknown-Known risks from a broader knowledge base

**Constraint:** All AI-generated risk candidates must be reviewed by a qualified human expert before being entered in A19. AI output is a prompt, not an approved risk entry.

---

## 9. Step-by-Step Instructions

### Step 1 — Confirm Prerequisites (Gate)

Before this skill begins, verify:
- [ ] SKL-03-09 complete: A19 Risk Management Plan section is approved and baselined
- [ ] A04 is baselined
- [ ] A05 is populated
- [ ] A07 (both Identification and Engagement Strategy sections) is complete
- [ ] The RBS taxonomy in A19 is finalized
- [ ] The P×I matrix in A19 is finalized and sponsor-confirmed

**If any prerequisite is missing:** Do not proceed. Identification without an approved risk plan produces entries that cannot be classified, scored, or governed consistently.

### Step 2 — Retrieve Prior Risk Flags

Pull all preliminary risk flags already in A19 from prior skills:
- Engagement risk flags from SKL-02-02 (Identify Stakeholders)
- Engagement risk confirmations from SKL-03-07 (Plan Stakeholder Engagement)

These exist as informal flags. This step converts each flag into a full C–E–C risk statement and populates all required A19 fields. Do not delete the original flag notation — update it in place, marking it as promoted.

### Step 3 — Review Source Documents for Embedded Risk Signals

Conduct document analysis (Section 8.8) across:
- A04, A05, A07, A08 (if available)
- OPA lessons learned (via A05)
- Any prior risk registers from similar projects (OPAs)

Record all candidate risks found. Do not filter yet — capture all signals first.

### Step 4 — Plan and Conduct Identification Sessions

Schedule and run identification activities based on the project context:

| Context | Recommended Approach |
|---------|---------------------|
| Small project, collocated team | Single facilitated brainstorm + 2–3 expert interviews |
| Medium project, distributed team | RBS-structured brainstorm workshop + interviews with technical leads and sponsor |
| Large / complex project | Multiple domain-specific workshops + individual expert interviews + SWOT analysis + document analysis |
| Adaptive project (sprint planning) | Per-iteration risk identification within retrospective/planning session using RBS categories |

Apply assumption and constraint analysis (Section 8.6), SWOT analysis (Section 8.7), and prompt lists (Section 8.10) across all sessions. Explicitly solicit **opportunities** in every session.

### Step 5 — Filter: Risk vs. Non-Risk

Apply the routing table from Section 4 to every candidate captured in Steps 2–4:
- Genuine threats → proceed to Step 6
- Genuine opportunities → proceed to Step 6
- Issues (already occurring) → route to A18; do not add to A19 register
- Constraints → document in A05 / A08; do not add to A19 register
- Assumptions → document in A05; convert to a risk entry only if their failure would impact objectives
- Concerns → note in A07; monitor for escalation to risk status

### Step 6 — Write C–E–C Risk Statements

For every genuine risk passing Step 5, write the full C–E–C statement (Section 5). Reject vague statements. Ensure:
- The Cause is a specific, existing condition (not generic "uncertainty")
- The Event is a discrete uncertain occurrence (not a description of the impact)
- The Consequence references a specific project objective (scope, schedule, cost, quality, stakeholder satisfaction, or value)

### Step 7 — Classify Against RBS Taxonomy

Assign each risk entry to one (or at most two, if it genuinely spans categories) RBS categories from the A19 taxonomy. If a risk cannot be classified, the RBS taxonomy is incomplete — flag for a taxonomy update via change request before proceeding.

### Step 8 — Assign Risk Owners

Assign a named, individual risk owner to every entry. Rules:
- Risk owners must be named individuals, not roles, teams, or groups
- The risk owner is responsible for monitoring the risk and implementing the approved response (once SKL-03-12 is complete)
- The PM may be the risk owner for strategic or governance risks; functional leads own domain-specific risks
- No A19 entry may be saved as complete without a named risk owner (Test T-4 enforces this)

### Step 9 — Populate All A19 Risk Register Fields

For each risk entry, populate all required fields before considering the entry complete:

| A19 Risk Register Field | Source / Rule |
|------------------------|--------------|
| Risk ID | Sequential, formatted per repository convention (e.g., R-001, R-002) |
| Risk title (short) | ≤ 10 words; used in dashboards and status reports |
| Risk type | Threat / Opportunity |
| C–E–C risk statement | Full statement from Step 6 |
| RBS category | From Step 7 |
| Risk knowledge class | Known-Unknown (confirm; if Unknown-Unknown, do not log — use management reserve) |
| Risk owner | Named individual from Step 8 |
| Trigger/early warning indicator | Observable signal that the risk is escalating or materializing |
| Probability | Blank at this stage — populated in SKL-03-11 |
| Impact | Blank at this stage — populated in SKL-03-11 |
| Risk score | Blank at this stage — calculated in SKL-03-11 |
| Response strategy | Blank at this stage — developed in SKL-03-12 |
| Response owner | Blank at this stage — assigned in SKL-03-12 |
| Status | "Identified — Awaiting Analysis" |
| Date identified | Today's date |
| Source | Technique used to identify (e.g., "Brainstorm," "Expert Interview — [Name]," "Promoted from SKL-03-07") |

### Step 10 — Review for Completeness and Internal Consistency

Before closing the identification run:
- [ ] Every entry from Step 2 (prior flags) has been promoted and fully populated
- [ ] Every entry has a C–E–C statement, RBS category, knowledge class, and risk owner
- [ ] No issues have been entered as risks (cross-check with A18)
- [ ] No constraints have been entered as risks (cross-check with A05/A08)
- [ ] Both threats **and** opportunities are represented (a register with zero opportunities is a red flag — Test T-6 checks this)
- [ ] All six RBS prompt categories have been reviewed; any category with zero entries has a documented rationale

### Step 11 — Update A19 Risk Register Section

Record the finalized risk entries in the A19 Risk Register section. Update the A19 header to reflect:
- Total number of risks identified (threats + opportunities)
- Date of this identification run
- Identification techniques used
- Any RBS categories with zero entries and the rationale

### Step 12 — Trigger Downstream

SKL-03-11 (Perform Risk Analysis) may now begin. Hand off: "A19 Risk Register section is populated with [N] risk entries; all entries have C–E–C statements, RBS categories, knowledge classes, owners, and trigger indicators; probability and impact fields are blank and ready for analysis."

---

## 10. Outputs

| Output | Artifact | Section Populated |
|--------|---------|-------------------|
| **Populated Risk Register** | A19 — Risk Management Record | Risk Register section — all identified threats and opportunities |
| **Promoted engagement risks** | A19 — Risk Management Record | Prior SKL-02-02 and SKL-03-07 flags converted to full entries |
| **A07 updates** | A07 — Stakeholder Register | Any new stakeholder risks discovered during identification that affect engagement strategies |

### What A19 Risk Register Section Contains After This Skill

Every risk entry has:
- Risk ID, title, type (threat/opportunity)
- Full C–E–C risk statement
- RBS category
- Knowledge classification (Known-Unknown confirmed)
- Named risk owner
- Trigger / early warning indicator
- Source technique
- Status: "Identified — Awaiting Analysis"
- Probability, impact, score, response: all blank (to be populated by SKL-03-11 and SKL-03-12)

---

## 11. Tailoring Guidance

| Dimension | Guidance |
|-----------|---------|
| **Development approach — Predictive** | Full initial identification session at planning; re-run at each phase gate and any trigger event per A19 cadence |
| **Development approach — Adaptive** | Lightweight risk identification at every sprint/iteration planning session using the same C–E–C format; risk-adjusted backlog items may carry risk IDs |
| **Development approach — Hybrid** | Predictive-style initial register for fixed components; adaptive per-iteration identification for evolving components; maintain one unified A19 register |
| **Small/low-complexity projects** | Single combined brainstorm + document review session; 10–20 entries is typical; one identification run per phase |
| **Large/high-complexity projects** | Domain-specific workshops per RBS category; separate expert interview program; 40–100+ entries expected; dedicated risk identification lead |
| **Regulated environment** | Regulatory risk category must be systematically covered; compliance risks have mandatory classification; document identification methodology for audit evidence |
| **Limited team availability** | Prioritize expert interviews over workshops; use AI-assisted document analysis as a supplementary tool; validate output with at least one human expert review |
| **Iterative re-runs** | Each re-run adds new entries, updates trigger status on existing entries, closes materialized risks (route to A18), and closes resolved risks |

---

## 12. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Running SKL-03-10 before A19 plan section is approved | Identified risks cannot be classified against the RBS or scored against the P×I matrix — the register is ungoverned data | Test T-1 enforces the prerequisite gate |
| Writing vague risk statements ("risk of delay," "stakeholder problems") | SKL-03-11 cannot score risks without knowing the specific event and its consequence; responses in SKL-03-12 will be generic and ineffective | Test T-3 enforces C–E–C format |
| Entering issues as risks | A19 becomes a mixed log; genuine risks are obscured; issues receive no timely action in A18 | Test T-2 enforces risk vs. issue distinction |
| Risks without owners | No accountability for monitoring; risks fall through during execution | Test T-4 enforces named ownership |
| Zero opportunities identified | Register is threat-only; team loses visibility on positive risk; opportunity exploitation is not possible in SKL-03-12 | Test T-6 checks for at least one opportunity |
| Prior engagement risk flags not promoted | SKL-02-02 and SKL-03-07 work is discarded; the stakeholder-engagement risk chain is broken | Test T-5 checks all prior flags are promoted |
| Identification treated as a one-time event | Emerging risks accumulate undetected; the register becomes stale and unreliable | Test T-7 checks iterative re-run mechanism |
| Separate risk log created alongside A19 | Dual maintenance, conflicting versions, waste rule §3.2 violation | Test T-8 enforces single-artifact rule |

---

## 13. Tests

### T-1 — Prerequisite Gate

**Assertion:** SKL-03-10 cannot run unless A19 Risk Management Plan section is approved, the RBS taxonomy is finalized, and the P×I matrix is sponsor-confirmed.

**Pass condition:** All prerequisites confirmed complete before any identification activity begins.

**Fail condition:** Identification begins without an approved plan; no RBS taxonomy is available to classify entries.

**Test type:** Pre-execution gate (block, do not proceed)

---

### T-2 — No Issues in the Risk Register

**Assertion:** A19 Risk Register section contains no entries describing conditions that have already occurred or are currently occurring.

**Pass condition:** All A19 entries describe uncertain future events. Any conditions already occurring have been routed to A18.

**Fail condition:** A19 contains entries such as "the testing environment is currently unavailable" (a current issue) rather than "there is a risk that the testing environment becomes unavailable" (an uncertain future event).

**Test type:** Content quality check

---

### T-3 — C–E–C Format Enforced

**Assertion:** Every A19 Risk Register entry has a complete C–E–C risk statement — an identifiable cause, a specific uncertain event, and a consequence referencing a project objective.

**Pass condition:** All entries have all three components. A reviewer reading the entry can identify the cause, the event, and the consequence without ambiguity.

**Fail condition:** Any entry contains only a consequence label ("risk of schedule delay"), only a vague event ("stakeholder issues"), or a cause-free statement ("scope risk exists").

**Test type:** Content format check — applied per entry

---

### T-4 — Named Risk Owner on Every Entry

**Assertion:** Every A19 Risk Register entry has a named individual assigned as risk owner.

**Pass condition:** Every entry has a first-name/last-name (or full role ID if a named individual cannot yet be assigned) in the owner field.

**Fail condition:** Any entry has "PM," "Team," "TBD," or blank in the owner field.

**Test type:** Field completeness check — applied per entry

---

### T-5 — Prior Engagement Flags Promoted

**Assertion:** All engagement risk flags entered into A19 by SKL-02-02 and SKL-03-07 have been converted to full C–E–C risk entries with all required fields populated.

**Pass condition:** A cross-check between the prior flag entries and the current register shows each flag has a corresponding full entry. The flag entry is marked as "Promoted — see Risk ID R-xxx."

**Fail condition:** Any prior flag remains in the register as an unpromoted stub with incomplete fields.

**Test type:** Cross-artifact consistency check

---

### T-6 — At Least One Opportunity Identified

**Assertion:** A19 Risk Register section contains at least one opportunity (positive risk) entry.

**Pass condition:** One or more entries have Risk Type = "Opportunity" with a complete C–E–C statement.

**Fail condition:** Zero opportunity entries exist. This is not automatically a failure — if a documented rationale explains why no opportunities were identified (e.g., highly constrained external-facing regulatory project), it passes with that rationale recorded. A register with zero opportunities and no rationale fails.

**Test type:** Coverage check

---

### T-7 — Iterative Re-run Mechanism Confirmed

**Assertion:** The A19 Risk Management Plan section (from SKL-03-09) specifies the cadence or trigger events for re-running identification, and the first identification run records its date and methodology to enable comparison in future runs.

**Pass condition:** A19 plan section contains a cadence statement; this identification run is recorded with date and techniques used.

**Fail condition:** No re-run cadence exists in the plan; or this run leaves no record of when and how it was conducted.

**Test type:** Process continuity check

---

### T-8 — No Separate Risk Log

**Assertion:** No standalone "Risk Log.xlsx," "Risk Register.docx," or equivalent file exists as a separate artifact. All risk entries live in A19.

**Pass condition:** Post-skill review finds no separate risk log. All identification output is in the A19 Risk Register section.

**Fail condition:** A separate risk file exists alongside A19, creating dual maintenance burden. Waste rule §3.2 is violated.

**Test type:** Artifact waste check

---

### T-9 — All RBS Categories Reviewed

**Assertion:** All RBS taxonomy categories defined in A19 have been explicitly reviewed during the identification session, and any category with zero entries has a documented rationale.

**Pass condition:** The A19 identification run record lists all RBS categories reviewed; categories with zero entries carry a rationale note (e.g., "Procurement/Supplier — not applicable; project has no external suppliers").

**Fail condition:** Categories were not systematically reviewed; zero-entry categories have no rationale; identification was ad hoc rather than taxonomy-guided.

**Test type:** Methodology completeness check

---

## 14. Dependency Chain

```
UPSTREAM (must complete before SKL-03-10)
─────────────────────────────────────────
SKL-03-09 → A19 Risk Management Plan section (approved)    [mandatory gate]
SKL-02-02 → A19 engagement risk flags                      [must be promoted]
SKL-03-07 → A19 engagement risk confirmations              [must be promoted]
SKL-02-01 → A04 Project Charter                            [mandatory]
SKL-02-01 → A05 Context Register                           [mandatory]
A08, A15, A16                                               [supporting if available]

DOWNSTREAM (cannot start until SKL-03-10 produces populated A19 register)
──────────────────────────────────────────────────────────────────────────
SKL-03-11 — Perform Risk Analysis (reads all A19 entries; applies P×I matrix)
  └──▶ SKL-03-12 — Plan Risk Responses
           └──▶ SKL-04-Implement Risk Responses
                └──▶ SKL-05-Monitor Risks (re-runs identification at each cadence)

ITERATIVE RE-RUN TRIGGERS (re-run SKL-03-10 during Executing / Monitoring):
SKL-05-Monitor Risks → trigger → re-run SKL-03-10 → new entries → re-run SKL-03-11 → re-run SKL-03-12
```

---

## 15. Re-run Triggers

This skill re-runs throughout the project lifecycle. Each re-run is governed by the cadence and triggers defined in A19 (from SKL-03-09). Standard re-run triggers include:

- **Phase gate:** Full re-run at every phase boundary; prior entries reviewed for status
- **Iteration/sprint planning:** Lightweight re-run scoped to upcoming iteration work
- **New stakeholder identified:** Review A07 changes for new engagement risk flags to promote
- **Major scope change approved:** Scope-driven risks may emerge from the change
- **Major schedule or cost change:** New constraint-based risks may emerge
- **External event:** Market change, regulatory announcement, supplier disruption
- **Risk materialization:** When a risk becomes an issue (route to A18), re-review neighboring risks in the same RBS category — they may be escalating
- **Risk monitoring signal:** Trigger indicator observed for a known risk — re-examine related entries

---

## 16. Examples

### Example A — Small Predictive Project (Office Relocation)

**Context:** 3-month office relocation. Low complexity. Single identification session.

**Techniques used:** Brainstorming (team), document review (A04, A05), assumption analysis.

**Sample entries:**

| Risk ID | Type | C–E–C Statement (abbreviated) | RBS Category | Owner |
|---------|------|-------------------------------|-------------|-------|
| R-001 | Threat | Because the building permit depends on local authority approval with no committed timeline, there is a risk that permit approval is delayed, which could result in a 4–8 week schedule delay and associated staff disruption costs | External/Regulatory | PM |
| R-002 | Threat | Because furniture suppliers are operating at high capacity, there is a risk that delivery lead times extend beyond the project schedule, which could result in staff working without adequate equipment for 2–3 weeks | Schedule | Logistics Lead |
| R-003 | Opportunity | Because the new building includes more efficient floor space, there is an opportunity that teams can co-locate who were previously separated, which could result in reduced coordination overhead and faster decision-making post-move | Stakeholders | PM |

---

### Example B — Adaptive Software Project (Scrum)

**Context:** 6-month product development. Per-sprint identification at sprint planning.

**Sprint 1 identification session (15 minutes, embedded in sprint planning):**

| Risk ID | Type | C–E–C Statement (abbreviated) | RBS Category | Owner |
|---------|------|-------------------------------|-------------|-------|
| R-001 | Threat | Because the authentication library chosen has not been used in production by the team, there is a risk that integration issues emerge in Sprint 2, which could result in 1–2 sprint velocity loss | Technical/Integration | Tech Lead |
| R-002 | Threat | Because stakeholder sign-off on the UI specification has not yet occurred, there is a risk that rework is required after design review, which could result in scope change affecting Sprint 3–4 delivery | Stakeholders | Product Owner |
| R-003 | Opportunity | Because the lead developer has recent experience with the target API, there is an opportunity to complete API integration faster than estimated, which could recover 3 story points for Sprint 2 | Technical | Tech Lead |

---

### Example C — Large Infrastructure Project

**Context:** 24-month infrastructure delivery. High complexity. Multiple workshops + expert interviews.

**Workshop structure:**
- Day 1: Technical and Schedule workshops (RBS categories: Technical, Schedule)
- Day 2: Financial and Resource workshops (RBS categories: Financial, Resources)
- Day 3: Stakeholder and External workshops (RBS categories: Stakeholders/Organizational, External)
- Post-workshop: Expert interviews (3 domain specialists; 1 regulatory compliance expert)
- Document analysis: A05 (OPA lessons from 3 prior similar projects), A07, A08

**Output:** 67 identified risks (52 threats, 15 opportunities) across 6 RBS categories. 9 entries promoted from prior SKL-02-02 and SKL-03-07 engagement flags.

---

## 17. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project Governance |
| **Threshold Band** | T2 — PM manages identification process; sponsor awareness required for high-complexity or high-sensitivity identification results (e.g., when initial register reveals risks that may breach appetite thresholds) |
| **Iterative nature** | This skill runs continuously — it is not closed after planning. Every re-run is governed by the same tests. |

---

## 18. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.2.2; Figure 2-49; §2.7.1 Key Concepts; Figure 2-46; Table 2-11 | Process basis, inputs/tools/outputs, risk vs. issue distinction, risk classification framework, check results |
| Artifacts-V-1.0.5 | Artifacts-V-1.0.5 | A19 Risk Management Record | Artifact schema, field definitions, governance layer, waste test |
| PMI Practice Standard for Project Risk Management | Risk-PPP | Risk identification methodology, C–E–C structure | Secondary authority for identification techniques and risk statement guidance |
| PMBOK Guide, Eighth Edition | PMBOK8 | Appendix X3 AI | AI-assisted risk identification guidance |
| PMI Lexicon of Project Management Terms | Lexicon | v5.0, January 2026 | Definitions: risk, issue, threat, opportunity, overall risk |

---

*Authority: PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules §3.2 Consolidation Rule*  
*Owner: Project Manager or designated risk lead*  
*Iterative: Re-runs at every cadence trigger defined in A19 plan section*  
*Next Skill: SKL-03-11 — Perform Risk Analysis*
