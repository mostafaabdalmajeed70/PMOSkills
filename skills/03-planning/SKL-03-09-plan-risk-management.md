# SKL-03-09 — Plan Risk Management

**Skill ID:** SKL-03-09  
**Pack:** 03 — Planning  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-09-plan-risk-management.md`  
**Authority:** PMBOK8 Guide §2.7.2.1 · Figure 2-48 · A19 Risk Management Record (Artifacts-V-1.0.5)  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Plan Risk Management defines **how** risk management activities will be conducted throughout the project — setting the methodology, roles, risk appetite alignment, probability/impact scales, category structure, cadence, and reserve approach before any risks are identified. It produces the Risk Management Plan section of **A19 — Risk Management Record**.

Without this skill, all downstream risk skills (SKL-03-10 Identify Risks, SKL-03-11 Perform Risk Analysis, SKL-03-12 Plan Risk Responses) lack the shared framework they depend on. Attempting to identify or analyze risks before the plan is complete produces inconsistent, incomparable, and ungoverned risk data.

---

## 2. Scope

This skill covers:
- Determining the risk management methodology appropriate to the project context
- Establishing probability and impact scales (qualitative assessment matrix)
- Defining the risk breakdown structure (RBS) or category taxonomy
- Documenting risk appetite and threshold alignment with organizational policy
- Assigning roles and responsibilities for risk management
- Setting risk review cadence and trigger events
- Determining the approach to reserves (contingency/management) — not yet sizing them
- Recording all decisions in the Risk Management Plan section of A19
- Updating A14 (Integrated PM Plan) with a subsidiary reference to A19

This skill does **not** cover:
- Identifying specific risks (SKL-03-10)
- Assessing probability and impact of specific risks (SKL-03-11)
- Sizing or approving specific reserve amounts (SKL-03-11 and SKL-03-12 in coordination with A16)
- Developing risk responses (SKL-03-12)

---

## 3. PMBOK8 Anchor

| Field | Value |
|-------|-------|
| **Process** | Plan Risk Management |
| **Guide Section** | §2.7.2.1 |
| **Figure** | Figure 2-48 — Plan Risk Management Inputs, Tools and Techniques, and Outputs |
| **Performance Domain** | Risk · Governance |
| **Focus Area** | Planning |
| **Domain Key Concepts** | Risk appetite · Risk threshold · Risk exposure · Risk classification · Project resilience (PMBOK8 Guide §2.7.1) |
| **Domain Check Results** | PMBOK8 Guide Table 2-11 |
| **Secondary Authority** | Risk-PPP (PMI Practice Standard for Project Risk Management) |

**PMI Definition (paraphrased — not reproduced):** Plan Risk Management is the process of defining how to conduct risk management activities for a project. The process should begin when a project is conceived and be completed early in the project. Risk management activities and tools are a key element of this process (PMBOK8 Guide §2.7.2.1).

---

## 4. Inputs

### 4.1 Required Inputs

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A04 — Project Charter** | SKL-02-01 | Project objectives, high-level risks, budget boundary, authority constraints — sets context for risk appetite calibration |
| **A05 — Context Register** | SKL-02-01 / SKL-02-02 | EEFs and OPAs that govern or constrain risk methodology; existing risk templates or classification systems |
| **A07 — Stakeholder Register and Engagement Strategy** | SKL-02-02 / SKL-03-07 | Stakeholder risk tolerances and appetite signals; engagement risks already flagged that must be incorporated into the plan |
| **A14 — Integrated PM Plan (in-progress components)** | SKL-03-01 (being assembled) | Development approach decision; financial management plan components if available — informs reserve approach choice |

### 4.2 Supporting Inputs (use if available)

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A06 — Tailoring Decision Record** | Planning | Development approach choice (predictive/adaptive/hybrid) affects how risk reviews are structured |
| **Organizational risk policy or risk management templates** | OPAs (via A05) | Starting basis for the P×I matrix, RBS taxonomy, and reserve approach — avoids reinventing from zero |
| **Prior project lessons learned** | OPAs (via A05) | Known risk patterns, failed methodologies, and effective review cadences from similar past work |

---

## 5. Tools and Techniques

*Per PMBOK8 Figure 2-48.*

### 5.1 Expert Judgment
Consult subject matter experts (risk specialists, experienced PMs, domain experts, sponsor, governance body) to calibrate:
- Appropriateness of proposed methodology for this project type and context
- Risk appetite thresholds relative to organizational norms
- Probability and impact scale granularity (3-point, 5-point, or custom)
- Whether quantitative analysis (A20) will be needed

### 5.2 Data Gathering — Interviews
Conduct structured or semi-structured interviews with:
- **Sponsor** — to surface strategic risk appetite and tolerance boundaries that must bound the plan
- **Key stakeholders** — to surface their individual risk tolerances and domain concerns
- **Team leads or architects** — to identify technical or delivery constraints that shape the risk framework

Interview purpose: calibrate, not enumerate risks. The interview output feeds the plan design, not the risk register.

### 5.3 Data Analysis — Stakeholder Analysis
Review A07 engagement data to identify:
- Stakeholders with low risk tolerance who will escalate threshold breaches quickly
- Stakeholders with high risk appetite who may underreport or underweight risks
- Stakeholders whose engagement risks (already in A19 from prior skills) imply a specific risk category must be defined

Use this to align the risk plan's threshold and escalation rules with the actual stakeholder landscape.

### 5.4 Meetings
Conduct a risk planning meeting with:
- Project manager
- Sponsor (or delegate for appetite confirmation)
- Key team members
- Risk specialist (if available)

**Agenda:**
1. Confirm project risk context and strategic sensitivity
2. Agree on methodology (qualitative-only vs. qualitative + quantitative)
3. Define and agree the P×I matrix scales
4. Agree the RBS/risk category structure
5. Confirm risk appetite and threshold values
6. Set review cadence and trigger events
7. Confirm roles and responsibilities
8. Confirm reserve approach in principle

**Output of meeting:** Draft A19 Risk Management Plan section for PM review and approval sign-off.

---

## 6. Core Technique: P×I Matrix Design

The **Probability × Impact (P×I) Matrix** is the foundation of qualitative risk analysis. Designing it correctly here — before SKL-03-11 runs — is the most consequential decision in this skill. If the matrix is poorly designed, risk prioritization in SKL-03-11 will be unreliable.

### 6.1 Scale Selection

| Scale Option | When to Use | Caution |
|-------------|-------------|---------|
| **3-point** (Low/Med/High) | Simple, short-duration, low-complexity projects | Loses distinction between moderate risks; reduces analytical precision |
| **5-point** (Very Low → Very High) | Recommended default for most projects | Sufficient granularity without over-engineering |
| **Numeric (0.1–0.9 probability; 0.05–0.8 impact)** | When EMV calculations will be needed (quantitative path) | Requires broader team calibration |

**Default recommendation:** 5-point scale unless context analysis (A05, A06) establishes a rationale for deviation. Document the choice and rationale in A19.

### 6.2 Impact Dimensions

Define impact for at least these four dimensions (align with project performance domains):

| Dimension | Low | Medium-Low | Medium | Medium-High | High |
|-----------|-----|-----------|--------|------------|------|
| **Schedule** | < 5% delay | 5–10% | 10–20% | 20–30% | > 30% delay |
| **Cost** | < 5% overrun | 5–10% | 10–20% | 20–30% | > 30% overrun |
| **Scope/Quality** | Minor quality defect | Noticeable but acceptable | Degraded outcome | Material loss of value | Project objective unmet |
| **Stakeholders** | Minimal concern | Moderate dissatisfaction | Formal complaint or escalation | Sponsor intervention | Relationship breakdown |

Document the chosen impact thresholds in A19. These become the calibration reference for all risk assessors in SKL-03-11.

### 6.3 Risk Appetite and Threshold Integration

Translate organizational and project-specific risk appetite into threshold rules directly in the plan:

| Risk Score Range | Threshold Classification | Default Response Logic |
|----------------|-------------------------|----------------------|
| Very High (e.g., 4×4 and above) | Escalate immediately — sponsor or governance body | Active response required; SKL-03-12 cannot leave without a response strategy |
| High (3×4, 4×3) | PM must address; report to sponsor | Active response planned in SKL-03-12 |
| Medium | PM manages; include in A19 monitoring watch list | Passive watch or contingent response |
| Low / Very Low | Accept; log only | No active response required unless pattern emerges |

These thresholds are applied in SKL-03-11 (risk scoring) and SKL-03-12 (response planning).

### 6.4 Risk Breakdown Structure (RBS) Taxonomy

Establish the risk category structure. Minimum recommended categories for most projects:

```
Project Risk Categories (RBS)
├── Technical
│   ├── Technology maturity and readiness
│   ├── Integration and dependencies
│   └── Requirements stability
├── Schedule
│   ├── Estimation accuracy
│   ├── Critical path exposure
│   └── External dependency timing
├── Financial
│   ├── Cost estimate confidence
│   ├── Funding certainty
│   └── Currency or rate exposure (if applicable)
├── Stakeholders and Organizational
│   ├── Engagement and resistance (feeds from A07)
│   ├── Organizational change readiness
│   └── Governance and decision delay
├── External
│   ├── Market and competitive
│   ├── Regulatory and compliance
│   └── Environmental and physical
└── Resources
    ├── Availability and capacity
    ├── Competency and skill
    └── Supplier and procurement
```

Tailor the RBS to the project context. For small simple projects, collapse to three to four categories. For complex or regulated projects, expand as needed. Document the chosen taxonomy in A19.

---

## 7. Step-by-Step Instructions

### Step 1 — Confirm Prerequisites (Gate)

Before this skill begins, verify:

- [ ] A04 (Project Charter) is baselined
- [ ] A05 (Context Register) is populated with relevant EEFs and OPAs
- [ ] A07 (Stakeholder Register) Identification section is complete (SKL-02-02 done)
- [ ] A07 Engagement Strategy section is complete (SKL-03-07 done)
- [ ] Development approach is known (from A06 or A13 if built)

**If any prerequisite is incomplete:** Do not proceed. Document the blocker as an impediment in A18. Risk planning without a charter produces a plan unanchored to project scope, budget, or authority. Risk planning without stakeholder data produces a plan blind to the dominant source of engagement-related risk.

### Step 2 — Retrieve Context and Appetite Signals

Pull from A04, A05, and A07:

- What is the project's risk classification (from A05/A06 complexity assessment)?
- Are there organizational risk policies, methodology templates, or prescribed scales in the OPAs?
- What engagement risk flags are already in A19 (from SKL-02-02 and SKL-03-07)?
- What stakeholder risk tolerance signals appear in A07?
- What is the development approach? (Adaptive projects need iterative risk cadence; predictive projects need phased cadence.)

Record context signals in A19 Risk Management Plan section as the basis for all decisions below.

### Step 3 — Select and Justify Risk Methodology

Decide:
- **Qualitative-only** or **Qualitative + Quantitative** path
- Whether A20 (Quantitative Risk and Reserve Decision Record) will be created (only if analysis value justifies the effort — apply the waste test)
- Whether an external risk specialist will be engaged
- What risk management tools or software will be used (if any)

Document the methodology choice and its rationale in A19. This is a committed governance decision — changing it later requires a change request.

**Adaptive project note:** In adaptive delivery, risk is reviewed at each iteration/sprint. The plan must specify the iteration-based risk review mechanism explicitly so it is not left to ad hoc team behavior.

### Step 4 — Design and Record the P×I Matrix

Using the technique in Section 6:
- Select the probability and impact scales
- Define impact dimensions and calibration thresholds
- Set the risk scoring grid (P × I = score)
- Define the threshold bands and their response logic
- Confirm the matrix is aligned to the organization's risk appetite (sponsor confirmation required for T-band)

Record the full matrix in A19 Risk Management Plan section.

### Step 5 — Establish and Record the RBS Taxonomy

Using the framework in Section 6.4:
- Select or adapt the standard RBS categories for this project
- Confirm engagement risk categories are included (they surface in SKL-02-02 and SKL-03-07)
- Remove categories that are not applicable (waste rule §3.2 — do not maintain procurement risk categories for a project with no procurement)
- Document the rationale for any additions or removals

Record the finalized RBS in A19 Risk Management Plan section.

### Step 6 — Define Roles, Responsibilities, and Cadence

Specify in A19:
- **Risk Owner model:** Every risk entry in A19 must have a named risk owner — this is a non-negotiable rule enforced in SKL-03-10 and SKL-03-12
- **Risk manager (if different from PM):** Name the person responsible for maintaining A19 and running risk reviews
- **Risk review cadence:** Regular schedule (e.g., weekly, biweekly, or per iteration); include trigger-based reviews for major events
- **Escalation rules:** Which risk score thresholds trigger sponsor or governance body involvement (aligned to the T-bands from Step 4)
- **Reserve approach in principle:** Document whether contingency reserves will be managed in A19/A20 and management reserves in A14/A16. Do not size reserves here — that is SKL-03-11 and SKL-03-12's work.

### Step 7 — Update A19 Risk Management Plan Section

Write the Risk Management Plan section of A19 with these fields populated:

| A19 Risk Management Plan Field | Source |
|-------------------------------|--------|
| Methodology and approach | Step 3 |
| P×I matrix and scale definitions | Step 4 |
| Risk category taxonomy (RBS) | Step 5 |
| Risk appetite and threshold bands | Steps 4 and 5 |
| Roles and responsibilities | Step 6 |
| Review cadence and trigger events | Step 6 |
| Reserve approach in principle | Step 6 |
| Quantitative analysis decision | Step 3 |
| Cross-references to A04, A05, A07 | Throughout |

### Step 8 — Reference A19 in A14

Add A19 (Risk Management Record) as a subsidiary plan reference in A14 (Integrated Project Management Plan). The reference should specify:
- A19 as the single risk governance record for this project
- The threshold at which changes to the A19 Risk Management Plan section require a formal change request through A12

### Step 9 — Obtain Approval

Submit the A19 Risk Management Plan section for review and approval:
- **PM:** reviews for internal consistency and completeness
- **Sponsor:** confirms that the risk appetite and threshold definitions match organizational policy and project strategic sensitivity
- **Governance body or PMO:** if organizational policy requires it (consult A06 for project-specific rules)

Approval is a **mandatory gate** before SKL-03-10 (Identify Risks) begins.

---

## 8. Outputs

| Output | Artifact | Section Populated |
|--------|---------|-------------------|
| **Risk Management Plan** | A19 — Risk Management Record | Risk Management Plan section (Steps 3–6) |
| **A14 subsidiary reference** | A14 — Integrated Project Management Plan | A19 added to subsidiary plan index |

### What A19 Risk Management Plan Section Contains After This Skill

- Risk management methodology and approach
- Development-approach-aligned review cadence
- P×I matrix with probability scale, impact scale (by dimension), and scoring grid
- Risk threshold bands with corresponding response logic
- Risk breakdown structure (RBS) taxonomy
- Risk appetite statement aligned to organizational policy
- Roles and responsibilities (risk manager, risk owner model, escalation authority)
- Reserve approach in principle (contingency/management — not yet sized)
- Cross-reference to prior risk flags from SKL-02-02 and SKL-03-07

### What A19 Does NOT Yet Contain After This Skill

- Individual risk entries (created in SKL-03-10)
- Probability and impact scores for specific risks (SKL-03-11)
- Risk response strategies (SKL-03-12)
- Sized reserve amounts (SKL-03-11 / SKL-03-12 in coordination with A16)

---

## 9. Tailoring Guidance

| Dimension | Guidance |
|-----------|---------|
| **Development approach** | Adaptive projects: specify iteration-based risk cadence and risk-adjusted backlog mechanism explicitly in the plan; do not use phase-gate language for adaptive delivery. Predictive: standard phase-cadence risk reviews. Hybrid: define both cadences and their interfaces. |
| **Project size and complexity** | Small/low-complexity: 3-category RBS, 3-point scale, qualitative-only. Large/high-complexity: full 5-point scale, multi-dimension impact, quantitative path decision documented. |
| **Regulated environment** | Regulatory risk categories must appear in the RBS. Reserve approach may be constrained by external policy — document in A19. |
| **Organizational OPA availability** | If organizational risk templates and P×I matrices already exist in OPAs (A05), adopt them and note the source. Modify only where project context requires it. Do not reinvent without rationale. |
| **No-quantitative path** | Explicitly document in A19 that quantitative analysis has been assessed and not required, with the rationale. This prevents SKL-03-11 from inadvertently triggering A20 work without a governance decision. |
| **Scaling for programs or large projects** | Plan may need to define risk integration with a program risk register. Document the escalation interface if one exists. |

---

## 10. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Running SKL-03-10 before A19 Risk Management Plan section is approved | Risk identification produces unclassifiable, incomparable, and ungoverned entries with no consistent P×I calibration | Test T-1 enforces the prerequisite gate |
| P×I matrix designed without sponsor appetite confirmation | Threshold bands do not reflect the organization's actual tolerance — risk escalations are misjudged | Test T-4 checks appetite documentation |
| RBS omits engagement risk categories | Stakeholder and organizational risks identified in A07 (SKL-03-07) cannot be properly classified or tracked | Test T-5 checks RBS coverage |
| Reserve approach left undefined | SKL-03-11 (Perform Risk Analysis) cannot produce a valid reserve recommendation without knowing the reserve model | Test T-6 checks reserve approach documentation |
| Plan changed after SKL-03-10 begins without a change request | Re-identification and re-scoring of all prior risks is required, creating rework and inconsistency | Test T-7 checks change control trigger |
| Separate risk management plan document created in addition to A19 | Creates dual maintenance burden, conflicting versions, and violates waste rule §3.2 | Test T-8 checks artifact consolidation |
| No cadence defined for adaptive projects | Risk reviews happen ad hoc or not at all across iterations | Test T-3 checks cadence specification |

---

## 11. Tests

### T-1 — Prerequisite Gate

**Assertion:** SKL-03-09 cannot run unless A04, A05, A07 (Identification and Engagement Strategy sections), and a known development approach are all in place.

**Pass condition:** All four prerequisites verified as complete before any plan design work begins.

**Fail condition:** Any prerequisite is missing or incomplete.

**Test type:** Pre-execution gate (block, do not proceed)

---

### T-2 — Methodology Decision Documented

**Assertion:** A19 Risk Management Plan section explicitly states whether the project will use qualitative-only or qualitative + quantitative risk analysis, with rationale.

**Pass condition:** A19 contains a clear methodology statement with a documented rationale; if quantitative analysis is excluded, the rationale explains why A20 is not warranted.

**Fail condition:** Methodology is undocumented; "TBD" appears in the methodology field; no rationale is provided.

**Test type:** Content completeness check

---

### T-3 — Cadence Is Approach-Appropriate

**Assertion:** The risk review cadence documented in A19 is explicitly calibrated to the project's development approach.

**Pass condition:** Predictive projects specify phase or time-based review schedule; adaptive projects specify iteration-based review mechanism; hybrid projects specify both and their interface.

**Fail condition:** Cadence is a generic "monthly risk review" with no reference to delivery approach; adaptive projects have phase-gate language; no trigger-based reviews are specified.

**Test type:** Content quality check

---

### T-4 — Risk Appetite and Thresholds Documented and Sponsor-Confirmed

**Assertion:** A19 contains documented risk appetite and threshold bands, and the sponsor has confirmed that these reflect organizational policy and project strategic sensitivity.

**Pass condition:** A19 threshold bands are present, each band has a response logic statement, and the record shows sponsor confirmation (meeting minutes, email, or sign-off notation).

**Fail condition:** Threshold bands are missing; sponsor confirmation is absent; thresholds are copied from a template without any project-specific calibration.

**Test type:** Content completeness + approval evidence check

---

### T-5 — RBS Covers Engagement Risk Categories

**Assertion:** The RBS taxonomy in A19 includes at least one stakeholder or organizational risk category that explicitly covers the engagement risk flags already entered in A19 by SKL-02-02 and SKL-03-07.

**Pass condition:** At least one RBS category maps to stakeholder, organizational change, or engagement-type risks; the engagement risk flags from prior skills are classifiable within the taxonomy.

**Fail condition:** RBS contains only technical, schedule, and financial categories with no stakeholder or organizational dimension; existing A19 engagement risk entries cannot be classified against the new taxonomy.

**Test type:** Cross-artifact consistency check

---

### T-6 — Reserve Approach Defined in Principle

**Assertion:** A19 documents whether contingency reserves and management reserves will be used, and describes the governance model for each (who holds them, who authorizes release), even though actual sizing is deferred to SKL-03-11 and SKL-03-12.

**Pass condition:** A19 contains a reserve approach statement covering both contingency and management reserve governance. Actual amounts may be blank (to be sized later) but governance model is stated.

**Fail condition:** Reserve section is entirely blank; no distinction between contingency and management reserves; reserve governance responsibility is unassigned.

**Test type:** Content completeness check

---

### T-7 — A14 Subsidiary Reference Added

**Assertion:** A14 (Integrated Project Management Plan) is updated to reference A19 as the risk management subsidiary plan.

**Pass condition:** A14 subsidiary plan index includes A19 with its approved status and cross-reference.

**Fail condition:** A14 has no reference to A19; A19 exists as an isolated artifact with no integration into the project plan structure.

**Test type:** Artifact linkage check

---

### T-8 — No Separate Risk Management Plan Document

**Assertion:** No document titled "Risk Management Plan.docx" or equivalent is created as a standalone artifact. All risk management plan content lives in the A19 Risk Management Plan section.

**Pass condition:** Post-skill review finds no separate risk management plan document; all plan content is in A19.

**Fail condition:** A standalone "Risk Management Plan" document exists alongside A19, creating dual maintenance burden. Waste rule §3.2 is violated.

**Test type:** Artifact waste check

---

## 12. Dependency Chain

```
UPSTREAM (must complete before SKL-03-09)
──────────────────────────────────────────
SKL-02-01 → A04 (Project Charter)                [mandatory]
SKL-02-01 → A05 (Context Register)               [mandatory]
SKL-02-02 → A07 Identification section           [mandatory]
SKL-02-02 → A19 engagement risk flags            [informing]
SKL-03-07 → A07 Engagement Strategy section      [mandatory]
SKL-03-07 → A19 engagement risk confirmations    [informing]

DOWNSTREAM (cannot start until SKL-03-09 completes and A19 plan section is approved)
───────────────────────────────────────────────────────────────────────────────────
SKL-03-10 — Identify Risks  (reads A19 plan section as primary input)
SKL-03-11 — Perform Risk Analysis (applies the P×I matrix from A19)
SKL-03-12 — Plan Risk Responses (uses thresholds and RBS from A19)
SKL-03-01 — Integrate and Align Project Plans (references A19 in A14)
```

---

## 13. Re-run Triggers

Re-run this skill (or update A19 Risk Management Plan section via change request) when:

- Development approach changes materially (e.g., shift from predictive to hybrid) — cadence must be redesigned
- Organizational risk appetite policy changes — threshold bands must be recalibrated
- Project is re-authorized or enters a new phase with a materially different risk profile
- A post-mortem or monitoring finding reveals the P×I matrix is not producing useful prioritization — matrix may need recalibration
- A new risk category emerges that the RBS does not cover — taxonomy update required
- New stakeholders are identified whose risk tolerance significantly differs from the current threshold design

All re-runs that change the P×I matrix, thresholds, or RBS after SKL-03-10 has produced risk entries **require** re-scoring of existing risks in A19. This is a change-controlled update.

---

## 14. Approval Authority

| Action | Authority |
|--------|-----------|
| A19 Risk Management Plan section — initial baseline | Sponsor confirmation of appetite and thresholds; PM sign-off on methodology completeness |
| Routine A19 plan updates (cadence, RBS adjustments) | PM within delegated thresholds |
| Changes to threshold bands or reserve approach after baseline | Change request through A12; sponsor re-confirmation required |
| Quantitative analysis path activation (A20) | PM recommendation; sponsor or finance authority approval if reserve sizing is material |

---

## 15. Examples

### Example A — Small Predictive Project (Simple)

A three-month office relocation project. A05 shows standard organizational risk templates are available in OPAs. Context is low complexity.

**Tailoring decisions logged in A19:**
- Methodology: Qualitative-only; A20 not warranted
- Scale: 3-point (Low/Medium/High)
- RBS: 4 categories (Technical/Logistics, Schedule, Stakeholders, External)
- Cadence: Biweekly risk review in standing PM meeting
- Reserve approach: 10% contingency reserve managed by PM within approved budget threshold

### Example B — Agile Software Development Project (Adaptive)

A six-month product development project using Scrum. High technical uncertainty, evolving stakeholder landscape.

**Tailoring decisions logged in A19:**
- Methodology: Qualitative + indicator-based quantitative (story-point-based risk exposure tracking)
- Scale: 5-point
- RBS: 6 categories (Technical Debt/Architecture, Integration, Schedule/Velocity, Stakeholders, External, Data/Privacy)
- Cadence: Risk review at every sprint retrospective + ad hoc trigger-based reviews for spikes
- Reserve approach: Sprint-level contingency buffer (capacity reserve, not cost reserve); management reserve held by sponsor

### Example C — High-Complexity Infrastructure Programme

A 24-month infrastructure project with regulatory exposure and multiple suppliers.

**Tailoring decisions logged in A19:**
- Methodology: Qualitative + Quantitative (Monte Carlo simulation for schedule/cost reserves via A20)
- Scale: Numeric probability (0.1–0.9) × 5-point impact by dimension
- RBS: 8 categories including Regulatory/Compliance, Procurement/Supplier, Environmental
- Cadence: Monthly risk committee review + phase-gate reviews; trigger-based for regulatory events
- Reserve approach: Formal contingency reserve (per SKL-03-11/A20 analysis) + management reserve held by sponsor/governing body; separate from budget in A16

---

## 16. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project Governance |
| **Threshold Band** | T2 — Sponsor confirmation required for risk appetite and threshold band definitions; PM manages routine plan maintenance |
| **Approval gate before downstream skills** | Mandatory — SKL-03-10 is blocked until this gate passes |

---

## 17. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.2.1; Figure 2-48; §2.7.1 Key Concepts; Table 2-11 | Process basis, inputs/tools/outputs, key concepts, check results |
| Artifacts-V-1.0.5 | Artifacts-V-1.0.5 | A19 Risk Management Record | Artifact schema, governance layer, fields, waste test |
| PMI Practice Standard for Project Risk Management | Risk-PPP | Risk planning methodology | Secondary authority for methodology and reserve approach guidance |
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.1 Risk Domain Key Concepts | Risk appetite, risk threshold, risk exposure, project resilience definitions |

---

*Authority: PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules §3.2 Consolidation Rule*  
*Owner: Project Manager or designated risk lead*  
*Approval Gate: Sponsor confirmation before SKL-03-10 begins*  
*Next Skill: SKL-03-10 — Identify Risks*
