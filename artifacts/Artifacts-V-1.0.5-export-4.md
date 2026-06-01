# Artifacts-V-1.0.3

## Integrated Project Management Repository Blueprint — v1.0.3

### Status
- Version: 1.0.3
- Supersedes: `Artifacts-V-1.0.2.md`
- Purpose: Normalize repository terminology to PMBOK® Guide Eighth Edition vocabulary, separate governance layers, reduce artifact waste, and establish a traceable reference model.
- Repository stance: PMBOK 8 vocabulary is the default language of this repository. Any retained local construct is explicitly labeled as `organization-defined` or `synthesis`.

---

## 1. Authority model

### 1.1 Source precedence
1. **Primary authority:** `[PMBOK8]`.
2. **Secondary authority:** PMI companion standards and practice guides listed in `pmi_reference_list.md`.
3. **Tertiary authority:** organization-defined operating methods, templates, automation choices, and reporting practices.

### 1.2 Vocabulary baseline
This repository uses PMBOK 8 vocabulary as the canonical model:
- **Six principles**.
- **Five focus areas**: Initiating, Planning, Executing, Monitoring and Controlling, Closing.
- **Seven performance domains**: Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk.
- **Forty nonprescriptive processes**.

### 1.3 Labeling rules
Use the following source-type labels on every artifact:
- `PMI-derived`: directly based on a PMI concept, process, or artifact pattern.
- `organization-defined`: created for local operating convenience and not PMI-native terminology.
- `synthesis`: combines multiple PMI sources and/or adds light local adaptation.

### 1.4 Canonical aliases
Use the aliases defined in `pmi_reference_list.md` as the repository registry, including `[PMBOK8]`, `[PMO-Guide]`, `[GPPP]`, `[OPM-Standard]`, `[Process-Groups]`, `[PMI-BA]`, `[BAP-2E]`, `[Requirements]`, `[Complexity]`, `[Risk-PPP]`, and `[Forms-Book]`.

### 1.5 Reference correction note
For repository use, treat the PMI Lexicon entry as **Version 5.0, January 2026** and retain alias `[Lexicon]`.

---

## 2. Governance layer model

This repository separates governance into distinct layers. Artifact ownership, approval authority, escalation, and reporting shall not be blended across these layers unless a specific cross-layer dependency is documented.

### 2.1 Organizational governance
- Concern: enterprise direction, strategic constraints, risk appetite, policy, compliance boundaries.
- Typical authorities: executive leadership, governing body, designated policy owners.
- Typical PMI anchors: `[OPM-Standard]`, `[GPPP]`.

### 2.2 OPM governance
- Concern: strategic alignment and integration across portfolios, programs, and projects.
- Typical authorities: OPM governing body, portfolio governance forums, enterprise decision groups.
- Typical PMI anchors: `[GPPP]`, `[OPM-Standard]`.

### 2.3 PMO governance
- Concern: PMO services, PMO autonomy, decision rights, service quality, support model, and continuous improvement.
- Typical authorities: PMO sponsor, PMO leader, PMO steering mechanism as defined by the organization.
- Typical PMI anchors: `[PMO-Guide]`.

### 2.4 Portfolio, program, and project governance
- Concern: prioritization, authorization, performance oversight, change authority, and value delivery at the relevant delivery layer.
- Typical authorities: portfolio board, program board, sponsor, project steering group, designated change authority.
- Typical PMI anchors: `[GPPP]`, `[PMBOK8]`.

### 2.5 Delivery team ways of working
- Concern: day-to-day execution choices, delivery cadence, collaboration rules, local working agreements.
- Typical authorities: project manager, product owner, delivery lead, team, within approved thresholds.
- Typical PMI anchors: `[PMBOK8]`, `[APG]`, `[Process-Groups]`.

---

## 3. Repository operating rules

### 3.1 Waste rule
Any artifact that requires more than 30 minutes of manual upkeep per cycle without driving an active decision, control action, or compliance need is a candidate for elimination, consolidation, or automation.

### 3.2 Consolidation rule
If two or more artifacts answer the same decision question, they shall be merged unless a regulatory, contractual, or audit reason requires separation.

### 3.3 Approval rule
Approval authority shall be assigned according to risk, impact, regulatory need, and governance layer. Do not route all approvals to the PMO or upward by default.

### 3.4 Tailoring rule
Tailoring is expected. Tailoring decisions shall be documented once in a single reusable decision record rather than repeated across multiple logs.

### 3.5 Reference rule
Every artifact shall include:
- Primary PMI source.
- Exact section.
- Purpose of citation.
- Source type.

---

## 4. Deprecated local terminology

The following legacy labels from v1.0.2 may be retained only as internal shorthand and shall not be presented as PMI-native terminology:
- `Supportive-Enabler Matrix` → `organization-defined PMO operating model`.
- `Governance Tiering, Tailoring & Waiver Model` → `organization-defined tailoring control method`.
- `Project DNA Scan` → `organization-defined complexity and tailoring assessment`.
- `Right-Sized Governance Tailoring Log` → replaced by **Tailoring Decision Record**.
- `Strategic Value Tracking Baseline Plan` and `Strategic Objective Verification Sheet` → merged into **Benefits and Value Measurement Record**.

---

## 5. Standard artifact record schema

Use this schema for every artifact definition:

```md
### [Artifact ID] Artifact name
- Artifact type:
- Source type: PMI-derived | organization-defined | synthesis
- Governance layer:
- Purpose:
- When used:
- Primary PMI source:
- Exact section:
- Purpose of citation:
- Performance domain(s):
- Focus area(s):
- Related process(es):
- Inputs:
- Outputs:
- Core fields:
- Owner:
- Approval authority:
- Tailoring guidance:
- Waste test:
- Notes:
```

---

## 6. Lean artifact catalog

| ID | Artifact | Layer | Source type | Status in v1.0.3 |
|---|---|---|---|---|
| A01 | Business Case | Portfolio/Project Governance | PMI-derived | Retained |
| A02 | Benefits and Value Measurement Record | Portfolio/Project Governance | synthesis | Retained, merged |
| A03 | Feasibility and Viable Options Record | Project Governance | synthesis | Retained, simplified |
| A04 | Project Charter | Project Governance | PMI-derived | Retained |
| A05 | Context Register | Project Governance | synthesis | New merged artifact |
| A06 | Tailoring Decision Record | Project Governance | synthesis | New merged artifact |
| A07 | Stakeholder Register and Engagement Strategy | Project Governance | synthesis | Retained, merged |
| A08 | Scope and Requirements Decision Record | Project Governance | synthesis | New merged artifact |
| A09 | Delivery Approach and Team Operating Agreement | Delivery Ways of Working | synthesis | Retained, simplified |
| A10 | Intake and Prioritization Decision Record | Portfolio Governance | synthesis | Retained, simplified |
| A11 | PMO Service Engagement Record | PMO Governance | organization-defined | Retained, simplified |
| A12 | Change and Exception Decision Log | Project Governance | synthesis | New merged artifact |

---

## 7. Core artifact definitions

### A01 Business Case
- Artifact type: decision and authorization record
- Source type: PMI-derived
- Governance layer: Portfolio/Project Governance
- Purpose: justify investment, expected value, and decision to proceed.
- When used: before formal authorization and whenever major revalidation is required.
- Primary PMI source: `[PMBOK8]`
- Exact section: `The Standard for Project Management, §2.1`; `Guide, Governance Performance Domain, §2.1.1`; `Guide, §4.5.1 Initiate Project or Phase`
- Purpose of citation: establish value rationale, authorization context, and alignment with project initiation.
- Performance domain(s): Governance, Finance, Stakeholders
- Focus area(s): Initiating
- Related process(es): Initiate Project or Phase
- Inputs: strategic objectives, problem/opportunity statement, preliminary options, economic analysis, regulatory constraints
- Outputs: authorization recommendation, expected benefits, constraints, success criteria baseline
- Core fields:
  - business need
  - strategic alignment
  - options considered
  - expected benefits
  - major risks and assumptions
  - affordability summary
  - recommendation
- Owner: sponsor or delegated business owner
- Approval authority: portfolio authority or sponsor consistent with organizational thresholds
- Tailoring guidance: use lightweight format for low-risk initiatives; expand only when uncertainty, spend, or regulation requires it
- Waste test: fail if repeated value statements are restated in multiple downstream templates without adding a new decision
- Notes: supersedes the oversized v1.0.2 "Comprehensive Business Case Framework" format

### A02 Benefits and Value Measurement Record
- Artifact type: value tracking and realization record
- Source type: synthesis
- Governance layer: Portfolio/Project Governance
- Purpose: capture expected benefits, ownership, measures, checkpoints, and value review triggers in one place.
- When used: initiated with the business case and maintained through closure and benefits follow-up as needed.
- Primary PMI source: `[PMBOK8]`
- Exact section: `The Standard for Project Management, §2.1`; `Guide, Governance Performance Domain, §2.1.1`
- Purpose of citation: ground benefits thinking in value delivery and governance.
- Performance domain(s): Governance, Stakeholders, Finance
- Focus area(s): Initiating, Monitoring and Controlling, Closing
- Related process(es): Initiate Project or Phase; Monitor and Control Project Performance; Close Project or Phase
- Inputs: business case, success measures, benefit owners, organizational KPIs
- Outputs: agreed value measures, review dates, benefit ownership, continuation/termination triggers
- Core fields:
  - benefit statement
  - measure and baseline
  - target and due date
  - benefit owner
  - review cadence
  - variance thresholds
  - decision trigger
- Owner: sponsor with project manager support
- Approval authority: sponsor or designated governing body
- Tailoring guidance: merge with the business case for very small efforts; separate only if post-project benefit tracking is material
- Waste test: fail if it duplicates a standalone strategy tracker, value baseline log, and objective verification sheet
- Notes: replaces v1.0.2 Items #2, #3, and #17

### A03 Feasibility and Viable Options Record
- Artifact type: analysis record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: document the viable solution options and the basis for recommendation.
- When used: before charter approval where uncertainty, technical complexity, sourcing complexity, or regulation warrants analysis.
- Primary PMI source: `[PMI-BA]`
- Exact section: `Determine Viable Options and Provide Recommendation`; `[PMBOK8] Guide, §4.5.1`
- Purpose of citation: support option evaluation and initiation inputs.
- Performance domain(s): Governance, Scope, Risk, Finance
- Focus area(s): Initiating
- Related process(es): Initiate Project or Phase
- Inputs: need statement, constraints, technical insights, financial data, sourcing inputs
- Outputs: recommended option, rejected options rationale, key assumptions, feasibility conclusions
- Core fields:
  - options compared
  - feasibility criteria
  - assumptions and constraints
  - recommendation
  - unresolved risks
- Owner: business analyst, architect, or project lead as assigned
- Approval authority: sponsor or designated initiating authority
- Tailoring guidance: optional for routine low-risk work with one obvious solution path
- Waste test: fail if it becomes a long workbook when one recommendation note would answer the decision question
- Notes: replaces the heavyweight v1.0.2 feasibility workbook format

### A04 Project Charter
- Artifact type: formal authorization artifact
- Source type: PMI-derived
- Governance layer: Project Governance
- Purpose: formally authorize the project and clarify sponsor, project manager, scope boundary, and authority.
- When used: once the initiative is approved to proceed into formal project work.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §4.5.1 Initiate Project or Phase`
- Purpose of citation: establish the charter as the formal authorization record.
- Performance domain(s): Governance, Stakeholders
- Focus area(s): Initiating
- Related process(es): Initiate Project or Phase; Identify Stakeholders
- Inputs: business case, recommended option, statement of work or equivalent
- Outputs: project authorization, named project manager, high-level success criteria, constraints
- Core fields:
  - project purpose
  - high-level scope
  - high-level milestone intent
  - budget boundary
  - named sponsor
  - named project manager and authority
  - initial success criteria
- Owner: sponsor
- Approval authority: sponsor or equivalent project authorizer
- Tailoring guidance: keep concise; do not use the charter as a substitute for full planning documentation
- Waste test: fail if the charter repeats the complete business case and full plan set
- Notes: retain as core mandatory artifact

### A05 Context Register
- Artifact type: situational reference record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: consolidate context factors that shape planning and delivery.
- When used: during initiation and refined during planning.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §1.1.2 Enterprise Environmental Factors`; `Guide, §1.1.3 Organizational Process Assets`
- Purpose of citation: capture external and internal contextual factors affecting project work.
- Performance domain(s): Governance, Risk, Resources
- Focus area(s): Initiating, Planning
- Related process(es): Initiate Project or Phase; Integrate and Align Project Plans
- Inputs: policies, standards, lessons learned, compliance constraints, market conditions, technical environment
- Outputs: usable context summary for planning decisions
- Core fields:
  - EEFs
  - OPAs
  - assumptions
  - constraints
  - policy references
  - lessons learned pointers
- Owner: project manager
- Approval authority: none required unless a compliance interpretation needs formal sign-off
- Tailoring guidance: this merged record replaces separate EEF, OPA, and early assumption mini-logs
- Waste test: fail if separate logs are maintained with the same fields and no distinct governance reason
- Notes: replaces v1.0.2 Items #6, #7, and most early use of #11

### A06 Tailoring Decision Record
- Artifact type: governance and tailoring record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture complexity factors, tailoring decisions, approval thresholds, and any approved exceptions in one place.
- When used: at project setup and whenever material tailoring changes occur.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §3 Tailoring`; `Guide, Table 2-1`; `Guide, Governance Performance Domain, §2.1`
- Purpose of citation: ground tailoring and governance selection in PMBOK 8.
- Performance domain(s): Governance
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Integrate and Align Project Plans; Assess and Implement Changes
- Inputs: charter, context register, complexity factors, delivery approach proposal
- Outputs: approved tailoring profile, escalation thresholds, retained controls, waived controls with rationale
- Core fields:
  - project characteristics
  - selected approach
  - retained artifacts
  - removed or merged artifacts
  - rationale
  - approval thresholds
  - exception references
- Owner: project manager
- Approval authority: project sponsor, steering group, or PMO only where organizational policy assigns that authority
- Tailoring guidance: use one record, not separate DNA scan, tailoring log, and waiver form unless regulation demands separation
- Waste test: fail if complexity scoring is performed without changing any management choice
- Notes: replaces v1.0.2 Items #9, #16, and #226 as the default baseline artifact

### A07 Stakeholder Register and Engagement Strategy
- Artifact type: stakeholder record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: identify stakeholders and define engagement approach in a single maintained record.
- When used: initiated during chartering and updated throughout the project.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Stakeholders Performance Domain, §2.5`; `Table 2-1: Identify Stakeholders, Plan Stakeholder Engagement, Manage Stakeholder Engagement, Monitor Stakeholder Engagement`
- Purpose of citation: establish stakeholder identification and engagement as continuing project work.
- Performance domain(s): Stakeholders, Governance
- Focus area(s): Initiating, Planning, Executing, Monitoring and Controlling
- Related process(es): Identify Stakeholders; Plan Stakeholder Engagement; Manage Stakeholder Engagement; Monitor Stakeholder Engagement
- Inputs: charter, org charts, sponsor input, context factors
- Outputs: stakeholder map, engagement strategy, communication needs, escalation flags
- Core fields:
  - stakeholder identity
  - role and interest
  - influence and impact
  - current and target engagement
  - engagement approach
  - communication needs
- Owner: project manager
- Approval authority: sponsor for initial strategic alignment; ongoing updates usually do not require formal approval
- Tailoring guidance: merge salience analysis and engagement planning into this record unless a complex transformation requires a separate workshop artifact
- Waste test: fail if separate salience canvas and kickoff planning sheets do not create unique decisions
- Notes: replaces v1.0.2 Items #10, #12, and #13 as a default merged artifact

### A08 Scope and Requirements Decision Record
- Artifact type: scope and requirements record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: define high-level scope boundaries, key requirements decisions, and major assumptions and constraints.
- When used: during planning and whenever material scope decisions are made.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Plan Scope Management, Elicit and Analyze Requirements, Define Scope, Develop Scope Structure, Monitor and Control Scope, Validate Scope`; `[Requirements]` planning and control guidance
- Purpose of citation: anchor scope and requirements decisions in current PMI process structure and supporting practice guidance.
- Performance domain(s): Scope, Stakeholders, Risk
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Plan Scope Management; Elicit and Analyze Requirements; Define Scope; Develop Scope Structure; Monitor and Control Scope; Validate Scope
- Inputs: charter, stakeholder record, context register, product vision, constraints
- Outputs: scope boundary, prioritized requirements, assumptions and constraints, acceptance logic
- Core fields:
  - in-scope and out-of-scope
  - prioritized needs
  - assumptions and constraints
  - acceptance criteria summary
  - unresolved scope issues
- Owner: project manager and business analysis lead as assigned
- Approval authority: sponsor, product owner, customer representative, or governance body according to context
- Tailoring guidance: lightweight narrative is enough for simple work; avoid multiple overlapping canvases unless they serve a distinct workshop purpose
- Waste test: fail if separate boundary log, mission canvas, and requirements sheet all contain the same decisions
- Notes: replaces v1.0.2 Items #11 and #15 as the default baseline artifact

### A09 Delivery Approach and Team Operating Agreement
- Artifact type: team operating artifact
- Source type: synthesis
- Governance layer: Delivery Ways of Working
- Purpose: define delivery approach, cadence, team norms, interfaces, and decision rules for execution.
- When used: at planning startup and updated when the team operating model materially changes.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Preface: five Focus Areas and 40 nonprescriptive processes`; `Appendix X2`; `[APG]`
- Purpose of citation: support choice of ways of working without turning local delivery design into fake PMI terminology.
- Performance domain(s): Governance, Resources, Schedule, Stakeholders
- Focus area(s): Planning, Executing
- Related process(es): Manage Project Execution; Manage Project Knowledge; Lead the Team
- Inputs: charter, tailoring decision record, team structure, sourcing decisions
- Outputs: team operating model, cadence, roles, meeting strategy, escalation route
- Core fields:
  - lifecycle approach
  - cadence and ceremonies
  - role responsibilities
  - team decision rules
  - dependency interfaces
  - communication norms
- Owner: project manager or delivery lead
- Approval authority: project manager within thresholds; sponsor or governance body if approach changes affect risk, contract, or funding
- Tailoring guidance: this is explicitly organization-defined in format, even when grounded in PMI guidance
- Waste test: fail if it duplicates a separate kickoff blueprint and execution strategy sheet without changing how the team works
- Notes: replaces most of v1.0.2 Items #19 and portions of #12

### A10 Intake and Prioritization Decision Record
- Artifact type: portfolio governance artifact
- Source type: synthesis
- Governance layer: Portfolio Governance
- Purpose: document intake, prioritization, deferral, and sequencing decisions for proposed work.
- When used: before project authorization and at reprioritization points.
- Primary PMI source: `[GPPP]`
- Exact section: `Governance at the Portfolio Level`; `[PMBOK8] Governance Performance Domain`
- Purpose of citation: separate portfolio decision-making from project delivery management.
- Performance domain(s): Governance, Finance, Resources, Risk
- Focus area(s): Initiating, Monitoring and Controlling
- Related process(es): Initiate Project or Phase; Monitor and Control Project Performance
- Inputs: business case, capacity picture, interdependencies, strategic priorities
- Outputs: approve, defer, reject, sequence, or rescope decision
- Core fields:
  - demand description
  - strategic alignment
  - capacity implications
  - risk implications
  - prioritization result
  - decision rationale
- Owner: portfolio function or PMO portfolio service
- Approval authority: portfolio governance body
- Tailoring guidance: do not embed this record inside the project artifact set once the authorization decision is complete
- Waste test: fail if the same prioritization evidence is repeated inside project-level governance artifacts
- Notes: replaces the oversized v1.0.2 intake scorecard pattern

### A11 PMO Service Engagement Record
- Artifact type: PMO governance artifact
- Source type: organization-defined
- Governance layer: PMO Governance
- Purpose: define what services the PMO will provide to a delivery effort and under what service expectations.
- When used: when the PMO offers coaching, assurance, reporting, tooling, standards support, or capability services.
- Primary PMI source: `[PMO-Guide]`
- Exact section: `PMO governance and PMO structural components`
- Purpose of citation: distinguish PMO service governance from project governance.
- Performance domain(s): Governance
- Focus area(s): Initiating, Planning
- Related process(es): none mandated; this is a PMO service-management artifact
- Inputs: project context, PMO service catalog, capability needs
- Outputs: agreed PMO support package, service expectations, review points
- Core fields:
  - service requested
  - service owner
  - cadence
  - expected outputs
  - customer contact
  - review and exit criteria
- Owner: PMO service owner
- Approval authority: PMO leader or delegated PMO authority; customer acknowledgment as needed
- Tailoring guidance: keep outside the mandatory project control baseline unless PMO support is actually engaged
- Waste test: fail if maintained for projects receiving no active PMO service
- Notes: replaces the heavyweight PMO service blueprint pattern as a simple engagement artifact

### A12 Change and Exception Decision Log
- Artifact type: integrated decision log
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture material changes, exceptions, risk escalations, and approved decisions in one auditable log.
- When used: throughout execution and monitoring.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Assess and Implement Changes; Monitor and Control Project Performance`; `[Lexicon] change request, change control board, risk escalation`
- Purpose of citation: align change and escalation handling with PMBOK 8 and PMI terminology.
- Performance domain(s): Governance, Risk, Scope, Schedule, Finance, Resources, Stakeholders
- Focus area(s): Monitoring and Controlling
- Related process(es): Monitor and Control Project Performance; Assess and Implement Changes; Monitor Risks
- Inputs: change requests, exceptions, escalation triggers, variance analysis
- Outputs: decision history, approvals, conditions, action owners
- Core fields:
  - issue or change summary
  - impact summary
  - decision required
  - decision authority
  - outcome
  - action owner
  - due date
- Owner: project manager or project controls lead
- Approval authority: role-based per threshold and governance layer
- Tailoring guidance: use one integrated log unless formal regulation requires separate risk, change, and exception registers
- Waste test: fail if separate logs create reconciliation work without distinct control value
- Notes: default vehicle for lean governance evidence during execution

---

## 8. Approval authority matrix

| Decision type | Default authority | Escalate when |
|---|---|---|
| Approve business case | Portfolio authority or sponsor | Funding, policy, or strategic threshold exceeded |
| Authorize project charter | Sponsor or designated project governing body | Enterprise-level commitment or regulatory exposure |
| Approve tailoring within thresholds | Project manager and sponsor | Control removal affects compliance, auditability, or risk appetite |
| Approve PMO service package | PMO service owner or PMO leader | Service cost or autonomy issue exceeds PMO threshold |
| Approve scope or requirement baseline changes | Product owner, sponsor, or delegated change authority | Material value, cost, schedule, or compliance impact |
| Approve portfolio reprioritization | Portfolio governance body | Strategic or capacity conflict crosses enterprise threshold |
| Approve risk or compliance exception | Designated accountable authority | Outside project authority or policy tolerance |

---

## 9. Migration map from v1.0.2

| v1.0.2 artifact(s) | v1.0.3 action |
|---|---|
| #1 Comprehensive Business Case Framework | Keep as A01 with lighter structure |
| #2 Benefits Realization Plan Template + #3 Strategic Value Tracking Baseline Plan + #17 Strategic Objective Verification Sheet | Merge into A02 |
| #4 Feasibility Study Workbook & Technical Viability Matrix | Simplify into A03 |
| #5 Project Charter Executive Form | Keep as A04 |
| #6 EEF log + #7 OPA ledger + early parts of #11 assumptions/constraints | Merge into A05 |
| #9 Project DNA Scan + #16 Tailoring Log + #226 Formal Governance Tailoring Waiver Form | Merge into A06 |
| #10 Stakeholder register + #12 Kickoff blueprint + #13 Salience canvas | Merge into A07 and A09 as needed |
| #11 Boundary assumption log + #15 Scope bounding canvas | Merge into A08 |
| #14 Intake scorecard | Simplify into A10 |
| #19 Execution strategy spectrum sheet | Fold into A09 |
| #229 PMO service catalog blueprint | Simplify into A11 |
| Multiple downstream change, waiver, and exception records | Consolidate into A12 unless regulation requires separation |

---

## 10. Reference style examples

Use references in the artifact body like this:
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §4.5.1 Initiate Project or Phase`
- Purpose of citation: `Defines the process basis for project charter creation.`
- Source type: `PMI-derived`

For synthesis artifacts:
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §3 Tailoring`; `[Complexity]`; `[PMO-Guide]`
- Purpose of citation: `Combines PMBOK 8 tailoring guidance with PMI complexity and PMO support considerations.`
- Source type: `synthesis`

For organization-defined artifacts:
- Primary PMI source: `[PMO-Guide]`
- Exact section: `PMO governance and service model sections`
- Purpose of citation: `Supports the existence of a PMO service engagement mechanism, while the actual format remains organization-defined.`
- Source type: `organization-defined`

---

## 11. Editorial rules for future additions

1. Do not invent PMI process names.
2. Do not use PMBOK 7 or older knowledge-area phrasing as the default structure unless explicitly cited for comparison.
3. Keep governance layer, owner, and approval authority separate.
4. Prefer one decision record over multiple adjacent logs.
5. Mark local operating methods as `organization-defined`.
6. Use the canonical alias registry from `pmi_reference_list.md`.
7. Update the Lexicon citation to Version 5.0, January 2026 whenever the repository cites `[Lexicon]`.

---

## 12. Next-step backlog

- Apply this schema across the remaining clusters.
- Replace all legacy references of the form `PMBOK 8th — Guide` and `PMBOK 8th — Standard` with `[PMBOK8]` plus exact section text.
- Retag every artifact with governance layer and source type.
- Remove duplicated check-result and acceptance-authority text where it is boilerplate rather than decision-specific.
- Review every artifact above the 30-minute upkeep threshold for merge or elimination.



---

## 13. Extended artifact catalog

This section continues the v1.0.3 normalization across planning, lifecycle selection, schedule, finance, risk, and execution/monitoring artifacts derived from the remaining v1.0.2 clusters.

| ID | Artifact | Layer | Source type | Status in v1.0.4 |
|---|---|---|---|---|
| A13 | Development Approach and Lifecycle Decision Record | Project Governance | synthesis | New merged artifact |
| A14 | Integrated Project Management Plan | Project Governance | PMI-derived | New normalized artifact |
| A15 | Schedule Model and Baseline Record | Project Governance | synthesis | New merged artifact |
| A16 | Financial Management and Cost Baseline Record | Project Governance | synthesis | New merged artifact |
| A17 | Integrated Performance Reporting Record | Project Governance | synthesis | New merged artifact |
| A18 | Issue, Impediment, and Action Log | Delivery/Project Governance | synthesis | New merged artifact |
| A19 | Risk Management Record | Project Governance | synthesis | New normalized artifact |
| A20 | Quantitative Risk and Reserve Decision Record | Project Governance | synthesis | New merged artifact |
| A21 | Trade-Off Decision Record | Project Governance | synthesis | New normalized artifact |
| A22 | Portfolio Interdependency Record | Portfolio Governance | synthesis | New normalized artifact |
| A23 | PMO Improvement Backlog | PMO Governance | organization-defined | New normalized artifact |
| A24 | Closure and Benefits Transition Record | Project Governance | synthesis | New normalized artifact |

---

## 14. Extended artifact definitions

### A13 Development Approach and Lifecycle Decision Record
- Artifact type: lifecycle and tailoring decision record
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: select and justify the delivery approach and lifecycle pattern, including predictive, adaptive, iterative, incremental, hybrid, or other organization-approved variants.
- When used: during early planning and when a material shift in delivery approach is proposed.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §2.3 Development Approach and Life Cycle`; `Guide, §3 Tailoring`; `[APG]`
- Purpose of citation: ground lifecycle choice in PMBOK 8 and related agile/adaptive guidance.
- Performance domain(s): Governance, Schedule, Resources, Risk
- Focus area(s): Planning
- Related process(es): Integrate and Align Project Plans
- Inputs: charter, context register, tailoring decision record, stakeholder needs, requirement volatility, compliance needs
- Outputs: chosen lifecycle, rationale, planning cadence, review cadence, control implications
- Core fields:
  - approach options considered
  - chosen lifecycle pattern
  - rationale
  - fit criteria
  - delivery cadence
  - review and escalation thresholds
- Owner: project manager with team and sponsor input
- Approval authority: sponsor or delegated project governing body when the choice affects commitments or controls
- Tailoring guidance: replace separate approach filter matrices and bespoke lifecycle selector templates with one decision record unless a scaled program requires a visual supplement
- Waste test: fail if multiple lifecycle canvases restate the same decision without changing execution behavior
- Notes: replaces v1.0.2 Items #26, #27, and most of #31-#36 at the project level

### A14 Integrated Project Management Plan
- Artifact type: integrated baseline and management artifact
- Source type: PMI-derived
- Governance layer: Project Governance
- Purpose: integrate approved planning content into one coherent project management plan.
- When used: after charter approval and before major execution begins; maintained under change control as needed.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Planning Focus Area §4.5.2`; `[Process-Groups]`
- Purpose of citation: establish the integrated planning basis and the role of the project management plan.
- Performance domain(s): Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk
- Focus area(s): Planning
- Related process(es): Integrate and Align Project Plans
- Inputs: approved planning records across all relevant domains
- Outputs: integrated management plan, baseline references, governance and control approach
- Core fields:
  - subsidiary plan index
  - baseline references
  - planning assumptions
  - control thresholds
  - governance calendar
  - reporting cadence
- Owner: project manager
- Approval authority: sponsor or designated governance body consistent with project risk and organizational policy
- Tailoring guidance: scale structure to context; do not force full subsidiary plans for small low-risk work
- Waste test: fail if the plan becomes a document container for redundant content already maintained in living records
- Notes: replaces the heavyweight v1.0.2 Item #23 framework with a lean integrated plan pattern

### A15 Schedule Model and Baseline Record
- Artifact type: schedule planning and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture milestones, sequencing logic, estimates, schedule baseline, and approved schedule changes in one managed record or linked model set.
- When used: during planning and throughout monitoring and controlling.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Plan Schedule Management, Define Activities, Sequence Activities, Estimate Activity Durations, Develop Schedule, Monitor and Control Schedule`; `[Scheduling-3E]`
- Purpose of citation: align schedule development and control with PMBOK 8 processes and scheduling practice guidance.
- Performance domain(s): Schedule, Resources, Risk, Governance
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Plan Schedule Management; Define Activities; Sequence Activities; Estimate Activity Durations; Develop Schedule; Monitor and Control Schedule
- Inputs: scope and requirements decision record, lifecycle decision record, resource information, risk information
- Outputs: schedule baseline, milestone view, critical path or flow view as applicable, approved changes
- Core fields:
  - activity or backlog structure
  - dependencies
  - estimates
  - milestones
  - baseline date set
  - variance thresholds
  - approved changes
- Owner: project manager, planner, or scheduling lead
- Approval authority: project manager within thresholds; sponsor or change authority for material baseline shifts
- Tailoring guidance: use predictive schedules, flow metrics, or iteration plans as appropriate to the chosen lifecycle
- Waste test: fail if separate planning, baseline, and changelog artifacts are maintained without distinct control value
- Notes: absorbs schedule-related baseline patterns and connected update ledgers from later v1.0.2 sections

### A16 Financial Management and Cost Baseline Record
- Artifact type: financial planning and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: define financial rules, estimates, funding timing, reserves, baseline, and cost control logic in one integrated record.
- When used: during planning and ongoing financial monitoring.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Finance Performance Domain §2.4`; `Table 2-1: Plan Financial Management, Estimate Costs, Develop Budget, Monitor and Control Finances`
- Purpose of citation: ground financial planning, budgeting, and control in PMBOK 8.
- Performance domain(s): Finance, Governance, Risk
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Plan Financial Management; Estimate Costs; Develop Budget; Monitor and Control Finances
- Inputs: business case, scope decisions, schedule information, resource estimates, risk data
- Outputs: cost baseline, funding plan, reserve logic, financial thresholds, approved changes
- Core fields:
  - estimating basis
  - budget structure
  - contingency and management reserves
  - funding release assumptions
  - control thresholds
  - variance actions
  - approved baseline changes
- Owner: project manager with finance support
- Approval authority: sponsor, finance authority, or project governing body according to spending authority thresholds
- Tailoring guidance: one integrated record replaces separate cost management plan, cost baseline ledger, funding horizon log, and baseline changelog unless regulation requires separation
- Waste test: fail if financial information is duplicated across multiple ledgers with manual reconciliation effort
- Notes: replaces or consolidates v1.0.2 Items #117, #118, #122, #123, #124, and #125

### A17 Integrated Performance Reporting Record
- Artifact type: monitoring and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: provide a unified view of progress, value, variance, forecasts, and decision triggers across domains.
- When used: throughout execution and monitoring according to reporting cadence.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Monitor and Control Project Performance`; `Guide, Governance and Finance Performance Domains`
- Purpose of citation: support integrated monitoring rather than siloed status reporting.
- Performance domain(s): Governance, Schedule, Finance, Stakeholders, Resources, Risk
- Focus area(s): Monitoring and Controlling
- Related process(es): Monitor and Control Project Performance
- Inputs: schedule data, financial data, risk data, issue data, stakeholder signals
- Outputs: status narrative, forecast, decision escalations, corrective action requests
- Core fields:
  - reporting period
  - progress summary
  - variance summary
  - forecast summary
  - decisions needed
  - actions and owners
- Owner: project manager or project controls lead
- Approval authority: acknowledgement by sponsor or governance forum as required; the report itself normally informs decisions rather than requiring approval
- Tailoring guidance: use a dashboard, report, or briefing pack format based on audience needs
- Waste test: fail if separate status reports are produced for PMO, sponsor, and team from the same raw data without distinct decision value
- Notes: provides the lean successor to cross-domain status and baseline reporting artifacts in later v1.0.2 sections

### A18 Issue, Impediment, and Action Log
- Artifact type: integrated operational control log
- Source type: synthesis
- Governance layer: Delivery Ways of Working / Project Governance
- Purpose: track issues, blockers, assigned actions, and escalation routes during execution.
- When used: throughout execution and monitoring.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Monitor and Control Project Performance`; `[Process-Groups]`; `[Lexicon] issue-related terminology as applicable`
- Purpose of citation: align day-to-day control work with PMI monitoring practices while keeping the format lean.
- Performance domain(s): Governance, Risk, Resources, Stakeholders
- Focus area(s): Executing, Monitoring and Controlling
- Related process(es): Manage Project Execution; Monitor and Control Project Performance
- Inputs: team signals, quality findings, stakeholder concerns, risk events, dependencies
- Outputs: assigned actions, escalation decisions, closure evidence
- Core fields:
  - issue or blocker
  - impact
  - owner
  - due date
  - escalation path
  - resolution status
- Owner: project manager, delivery lead, or scrum master equivalent
- Approval authority: none for logging; escalation decisions follow the approval authority matrix
- Tailoring guidance: merge issue, impediment, and action tracking unless contractual or regulated controls require separate logs
- Waste test: fail if a blocker log and an issue log are reconciled manually with no distinct use
- Notes: replaces v1.0.2 Item #21 and related impediment records as the default baseline

### A19 Risk Management Record
- Artifact type: risk planning and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: define risk approach and maintain identified threats and opportunities, responses, owners, and review triggers.
- When used: during planning and throughout monitoring and controlling.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Risk Performance Domain §2.8`; `Table 2-1: Plan Risk Management, Identify Risks, Perform Risk Analysis, Plan Risk Responses, Monitor Risks`; `[Risk-PPP]`
- Purpose of citation: ground risk work in PMBOK 8 and PMI risk practice guidance.
- Performance domain(s): Risk, Governance, Finance, Schedule, Scope, Resources, Stakeholders
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Plan Risk Management; Identify Risks; Perform Risk Analysis; Plan Risk Responses; Monitor Risks
- Inputs: charter, context, scope, estimates, stakeholder insights, issue log
- Outputs: current risk record, prioritized exposures, response plans, escalation triggers
- Core fields:
  - risk statement
  - category
  - probability and impact
  - response strategy
  - owner
  - trigger
  - status
- Owner: project manager or assigned risk lead
- Approval authority: project manager within thresholds; sponsor or governing body for major risk responses or tolerance exceptions
- Tailoring guidance: combine plan and register for most projects; split only for large or highly regulated environments
- Waste test: fail if separate risk plan and risk register repeat the same governance thresholds and response logic
- Notes: normalizes v1.0.2 Item #170 and connected risk-planning artifacts into one baseline record

### A20 Quantitative Risk and Reserve Decision Record
- Artifact type: analytical decision artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture materially important quantitative analyses used to justify reserve levels, contingency releases, or major option choices.
- When used: when uncertainty, spend, or exposure is high enough to justify quantitative analysis.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Risk Performance Domain §2.8`; `Table 2-1: Perform Risk Analysis`; `[Risk-PPP]`
- Purpose of citation: support quantitative analysis and reserve decision-making.
- Performance domain(s): Risk, Finance, Governance
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Perform Risk Analysis; Develop Budget; Monitor Risks; Monitor and Control Finances
- Inputs: risk management record, estimates, reserve assumptions, options analysis
- Outputs: quantified exposure view, reserve recommendation, decision rationale
- Core fields:
  - analysis method
  - scenarios assessed
  - quantified exposure
  - reserve recommendation
  - assumptions
  - decision requested
- Owner: project manager with specialist support as needed
- Approval authority: sponsor, finance authority, or change authority depending on reserve use and exposure level
- Tailoring guidance: use only when the decision value justifies the analytical effort
- Waste test: fail if Monte Carlo, EMV, and reserve-planner worksheets are produced with no resulting decision
- Notes: consolidates v1.0.2 Items #122, #172, and #174 as a lean decision-focused artifact family

### A21 Trade-Off Decision Record
- Artifact type: integrated decision artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: document material trade-offs among scope, schedule, cost, risk, resources, and value.
- When used: when corrective action or change requires an explicit trade-off choice.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, §2.4 Finance Performance Domain`; `Guide, §2.8 Risk Performance Domain`; `Table 2-1: Assess and Implement Changes; Monitor and Control Project Performance`
- Purpose of citation: support integrated decision-making across constraints and outcomes.
- Performance domain(s): Governance, Scope, Schedule, Finance, Resources, Risk, Stakeholders
- Focus area(s): Monitoring and Controlling
- Related process(es): Assess and Implement Changes; Monitor and Control Project Performance
- Inputs: performance report, risk data, change proposals, dependency impacts
- Outputs: documented decision, rationale, constraints prioritized, follow-up actions
- Core fields:
  - decision context
  - options considered
  - trade-off summary
  - preferred option
  - authority
  - follow-up actions
- Owner: project manager
- Approval authority: sponsor, change authority, or steering group depending on threshold
- Tailoring guidance: use for high-impact integrated decisions; routine local choices belong in normal team action tracking
- Waste test: fail if separate trade-off, escalation, and exception papers are created for one decision event
- Notes: normalizes v1.0.2 Item #120 into a reusable decision record

### A22 Portfolio Interdependency Record
- Artifact type: portfolio coordination artifact
- Source type: synthesis
- Governance layer: Portfolio Governance
- Purpose: show significant cross-project or cross-program dependencies, resource conflicts, and coordination decisions.
- When used: when multiple initiatives compete for shared milestones, resources, or dependencies.
- Primary PMI source: `[GPPP]`
- Exact section: `Governance at the Portfolio Level`; `[PMO-Guide]`
- Purpose of citation: separate enterprise coordination from project-level control.
- Performance domain(s): Governance, Resources, Schedule, Finance, Risk
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Monitor and Control Project Performance; Integrate and Align Project Plans
- Inputs: portfolio priorities, schedule data, capacity data, dependency information
- Outputs: dependency visibility, escalation needs, sequencing decisions
- Core fields:
  - dependency description
  - affected initiatives
  - resource or milestone conflict
  - impact summary
  - portfolio decision
  - action owner
- Owner: portfolio management function or PMO portfolio service
- Approval authority: portfolio governance body
- Tailoring guidance: keep outside the mandatory single-project artifact set unless the project is part of a dependent network
- Waste test: fail if every project keeps its own copy of the same portfolio dependency matrix
- Notes: normalizes v1.0.2 Item #121 and related multi-project coordination artifacts

### A23 PMO Improvement Backlog
- Artifact type: PMO service improvement artifact
- Source type: organization-defined
- Governance layer: PMO Governance
- Purpose: capture PMO capability improvements, simplification opportunities, training needs, and template changes.
- When used: continuously as part of PMO improvement work.
- Primary PMI source: `[PMO-Guide]`
- Exact section: `PMO governance and continuous improvement themes`
- Purpose of citation: support PMO learning and service evolution while keeping the backlog format organization-defined.
- Performance domain(s): Governance
- Focus area(s): Monitoring and Controlling, Closing
- Related process(es): none mandated; this is a PMO governance/support artifact
- Inputs: retrospectives, project feedback, service metrics, audit findings
- Outputs: approved PMO improvements, prioritized change work, template retirements
- Core fields:
  - improvement item
  - source of feedback
  - value expected
  - priority
  - owner
  - implementation status
- Owner: PMO leader or delegated capability owner
- Approval authority: PMO leader or PMO governance forum
- Tailoring guidance: maintain only if the PMO actively governs improvements through a backlog method
- Waste test: fail if feedback is collected but never converted into actual PMO decisions or changes
- Notes: normalizes v1.0.2 Item #119

### A24 Closure and Benefits Transition Record
- Artifact type: closure and transition artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: document closure readiness, handover status, unresolved items, lessons, and the transition of benefit tracking where applicable.
- When used: during closing and immediately after closure.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Close Project or Phase`; `Guide, Closing Focus Area §4.5.5`
- Purpose of citation: anchor formal closure and transition activities in PMBOK 8.
- Performance domain(s): Governance, Stakeholders, Finance, Resources, Risk
- Focus area(s): Closing
- Related process(es): Close Project or Phase
- Inputs: integrated performance reporting record, benefits record, issue log, acceptance evidence
- Outputs: closure approval package, handover status, post-project follow-up ownership
- Core fields:
  - closure criteria status
  - deliverable acceptance status
  - remaining actions
  - lessons summary
  - transition owner
  - benefits follow-up plan
- Owner: project manager
- Approval authority: sponsor, customer, or designated closure authority according to context
- Tailoring guidance: combine closeout checklist, handover memo, and lessons summary where possible
- Waste test: fail if multiple closeout artifacts repeat the same acceptance and handover evidence
- Notes: extends the lean model into closing so benefits tracking is not lost after delivery

---

## 15. Extended migration map

| v1.0.2 artifact(s) | v1.0.4 action |
|---|---|
| #20 PMO Master Project Ingestion Portfolio Checklist + #25 Project Launch Authorization Gate | Retire as standalone artifacts; fold essential controls into A11, A14, and governance checklists |
| #21 Continuous Project Issue Log Ledger | Simplify into A18 |
| #22 Project Change Request Lifecycle Submission Form + #118 Baseline Changelog | Fold into A12 and relevant baseline records |
| #23 Project Management Plan Subsidiary Component Integrity Framework | Normalize into A14 |
| #26 Development Approach Selection Matrix + #27 Tailoring Worksheet | Merge into A13 with A06 linkage |
| #28 Triple-Bottom-Line Scorecard | Fold into A02 unless separate reporting is justified |
| #29 Continuous Adaptation Tracking Loop | Fold into A06 and A23 |
| #30 PMO Configuration Palette of Options Matrix | Keep only as PMO-internal method under A11/A23, not as PMI-native project artifact |
| #31-#36 DA lifecycle selectors | Fold into A13 or A09 as organization-defined lifecycle implementation aids |
| #37-#41 focus-area orchestration and domain maps | Retire as default mandatory project artifacts; keep only as optional repository design references |
| #117-#125 finance ledgers and plans | Merge into A16 and A17 |
| #120 trade-off ledger | Normalize into A21 |
| #121 portfolio interdependency matrix | Normalize into A22 |
| #170 risk register + #174 decision tree analysis + related quantitative worksheets | Normalize into A19 and A20 |

---

## 16. Additional editorial controls

1. Do not treat Disciplined Agile lifecycle labels as default PMI artifact names inside the core project repository.
2. Keep optional visual maps, orchestration matrices, and scaffolding models out of the mandatory baseline unless they demonstrably improve a real decision.
3. When a baseline exists, store approved changes with the baseline owner rather than in a separate enterprise-style audit ledger unless required by policy.
4. Separate PMO service administration from project delivery control.
5. Preserve closure and benefits transition as explicit end-of-project work so value tracking does not disappear at delivery.

---

## 17. Remaining clusters conversion

This version completes the conversion of the remaining v1.0.2 clusters into a lean PMBOK 8-aligned repository model. The remaining coverage areas are team and resource management, communications and stakeholder information flow, change readiness and knowledge management, procurement and supplier control, records retention, governance authority, PMO value management, and AI/data/privacy safeguards.

| ID | Artifact | Layer | Source type | Status in v1.0.5 |
|---|---|---|---|---|
| A25 | Team Operating and Responsibility Record | Delivery Ways of Working / Project Governance | synthesis | New merged artifact |
| A26 | Resource Capacity and Acquisition Record | Project Governance | synthesis | New merged artifact |
| A27 | Team Health and Development Record | Delivery Ways of Working / PMO Governance | synthesis | New merged artifact |
| A28 | Communications and Reporting Record | Project Governance | synthesis | New merged artifact |
| A29 | Change Readiness and Adoption Record | Project Governance | synthesis | New merged artifact |
| A30 | Knowledge and Lessons Management Record | Project Governance / PMO Governance | synthesis | New merged artifact |
| A31 | Procurement and Supplier Management Record | Project Governance | synthesis | New merged artifact |
| A32 | Supplier Evaluation and Award Decision Record | Project Governance / Portfolio Governance | synthesis | New merged artifact |
| A33 | Supplier Change, Claim, and Compliance Record | Project Governance | synthesis | New merged artifact |
| A34 | Information Retention and Records Control Record | Project Governance / PMO Governance | synthesis | New normalized artifact |
| A35 | Governance and Decision Authority Record | Project Governance | synthesis | New normalized artifact |
| A36 | PMO Value, Maturity, and Improvement Record | PMO Governance | organization-defined | New merged artifact |
| A37 | AI, Data, and Privacy Control Record | Project Governance / PMO Governance | synthesis | New normalized artifact |

---

## 18. Remaining artifact definitions

### A25 Team Operating and Responsibility Record
- Artifact type: team alignment and responsibility artifact
- Source type: synthesis
- Governance layer: Delivery Ways of Working / Project Governance
- Purpose: combine team working agreements, role clarity, and responsibility mapping in one lean artifact.
- When used: during planning and updated when the team structure or accountability model materially changes.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Resources Performance Domain`; `Table 2-1: Plan Resource Management, Lead the Team, Monitor and Control Resourcing`; `[APG]`
- Purpose of citation: ground team alignment, role clarity, and collaboration practices in PMI guidance without turning local formats into PMI-native terms.
- Performance domain(s): Resources, Governance, Stakeholders
- Focus area(s): Planning, Executing
- Related process(es): Plan Resource Management; Lead the Team; Monitor and Control Resourcing
- Inputs: project charter, integrated project management plan, stakeholder record, delivery approach and team operating agreement
- Outputs: team working agreement, role clarity, accountability map, conflict and escalation route
- Core fields:
  - team purpose and norms
  - core roles and responsibilities
  - decision boundaries
  - escalation route
  - working agreements
  - collaboration expectations
- Owner: project manager or delivery lead
- Approval authority: project manager for routine team setup; sponsor or governance body only when role decisions alter authority thresholds
- Tailoring guidance: use one record instead of separate team charter, RACI sheet, and responsibility escalation matrix unless regulation or contract structure requires separation
- Waste test: fail if a team charter, RACI, and team protocol sheet all contain the same role and behavior rules
- Notes: consolidates v1.0.2 Items #181 and #184, and absorbs routine responsibility content from related team setup artifacts

### A26 Resource Capacity and Acquisition Record
- Artifact type: resource planning and acquisition artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: integrate staffing, shared capacity, physical resource needs, acquisition timing, and key allocation constraints.
- When used: during planning and maintained when resource commitments or conflicts materially change.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Resources Performance Domain`; `Table 2-1: Plan Resource Management, Acquire Resources, Lead the Team, Monitor and Control Resourcing`
- Purpose of citation: support resourcing decisions, acquisition planning, and capacity control.
- Performance domain(s): Resources, Schedule, Finance, Governance
- Focus area(s): Planning, Executing, Monitoring and Controlling
- Related process(es): Plan Resource Management; Acquire Resources; Monitor and Control Resourcing
- Inputs: scope decisions, schedule model, financial record, portfolio interdependency record, stakeholder needs
- Outputs: staffing and acquisition view, shared-resource conflict visibility, resource release and escalation logic
- Core fields:
  - required roles and resources
  - timing and duration
  - acquisition path
  - shared-resource conflicts
  - allocation assumptions
  - release criteria
- Owner: project manager with functional managers or resource owners as needed
- Approval authority: role-based according to staffing authority, procurement limits, and shared-capacity thresholds
- Tailoring guidance: merge staffing plan, allocation ledger, and equipment setup notes unless different control owners require separate records
- Waste test: fail if multiple resource ledgers are reconciled manually every cycle with no distinct decision value
- Notes: consolidates v1.0.2 Items #183, #185, and #186, with optional skill detail from #182 only when needed

### A27 Team Health and Development Record
- Artifact type: team development and health artifact
- Source type: synthesis
- Governance layer: Delivery Ways of Working / PMO Governance
- Purpose: track team capability growth, health signals, coaching actions, and development needs in one practical record.
- When used: during execution and at periodic team reviews.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Resources Performance Domain`; `Appendix X2`; `[PMO-Guide]`
- Purpose of citation: support team development, capability improvement, and PMO coaching services where relevant.
- Performance domain(s): Resources, Stakeholders
- Focus area(s): Executing, Monitoring and Controlling, Closing
- Related process(es): Lead the Team; Manage Project Knowledge; Monitor and Control Resourcing
- Inputs: retrospective insights, team observations, coaching feedback, capability goals
- Outputs: improvement actions, training needs, health trends, coaching follow-up
- Core fields:
  - health observations
  - capability gaps
  - coaching actions
  - learning actions
  - trend notes
  - owner and follow-up date
- Owner: delivery lead, project manager, or PMO coach as assigned
- Approval authority: usually none for updates; PMO or HR involvement only when organizational intervention is required
- Tailoring guidance: merge health pulse, development actions, and performance support notes unless privacy rules require a separate handling method
- Waste test: fail if maturity trackers, safety surveys, and coaching logs produce no action decisions
- Notes: consolidates v1.0.2 Items #187, #188, #189, #212, #213, and #214 into one lean operating family, with PMO-internal extensions allowed

### A28 Communications and Reporting Record
- Artifact type: communications planning and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: integrate stakeholder information needs, communication routes, reporting cadence, and executive reporting logic.
- When used: during planning and maintained through execution and monitoring.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Plan Communications Management, Manage Communications, Monitor Communications`; `Guide, Stakeholders Performance Domain`
- Purpose of citation: ground communication planning and monitoring in PMBOK 8 processes and stakeholder management guidance.
- Performance domain(s): Stakeholders, Governance
- Focus area(s): Planning, Executing, Monitoring and Controlling
- Related process(es): Plan Communications Management; Manage Communications; Monitor Communications
- Inputs: stakeholder register and engagement strategy, integrated performance reporting record, context register
- Outputs: audience map, communication cadence, channel rules, reporting products, escalation paths
- Core fields:
  - stakeholder audience
  - information need
  - channel and format
  - cadence
  - sender or owner
  - feedback route
  - confidentiality or access constraints
- Owner: project manager or communications lead
- Approval authority: sponsor or governance body for high-sensitivity reporting models; routine updates usually managed by the project manager
- Tailoring guidance: use one record instead of separate communications matrix, communications plan, status deck template, and channel blueprint unless audiences or security models materially differ
- Waste test: fail if multiple communication artifacts repeat the same audience, cadence, and channel decisions
- Notes: consolidates v1.0.2 Items #190, #191, #192, and #211

### A29 Change Readiness and Adoption Record
- Artifact type: stakeholder transition and adoption artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture organizational change impacts, readiness, adoption actions, and stakeholder feedback relevant to solution uptake.
- When used: during planning, execution, deployment, and transition.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Stakeholders Performance Domain`; `[Change-Guide]`; `[PMI-BA]`
- Purpose of citation: support stakeholder adoption, readiness thinking, and implementation impact management.
- Performance domain(s): Stakeholders, Resources, Governance, Risk
- Focus area(s): Planning, Executing, Monitoring and Controlling, Closing
- Related process(es): Plan Stakeholder Engagement; Manage Stakeholder Engagement; Monitor Stakeholder Engagement; Close Project or Phase
- Inputs: stakeholder record, scope decisions, communications record, rollout plans, feedback data
- Outputs: readiness profile, adoption actions, training actions, unresolved resistance items, transition follow-up
- Core fields:
  - impacted groups
  - impact summary
  - readiness assessment
  - adoption actions
  - feedback themes
  - outstanding concerns
- Owner: project manager, change lead, or business owner as assigned
- Approval authority: sponsor or business owner when adoption decisions affect deployment timing or value realization
- Tailoring guidance: merge change impact assessment and stakeholder feedback logging unless there is a formal enterprise change office method requiring a separate artifact
- Waste test: fail if readiness sheets and feedback logs repeat the same impacted groups and action plans
- Notes: consolidates v1.0.2 Items #209 and #210

### A30 Knowledge and Lessons Management Record
- Artifact type: knowledge and lessons artifact
- Source type: synthesis
- Governance layer: Project Governance / PMO Governance
- Purpose: capture lessons, reusable knowledge, retrospective actions, and escalation of meaningful cross-project learning.
- When used: throughout execution and at closure.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Manage Project Knowledge; Close Project or Phase`; `[PMO-Guide]`
- Purpose of citation: ground project knowledge management and organizational learning in PMI guidance.
- Performance domain(s): Governance, Resources, Risk
- Focus area(s): Executing, Closing
- Related process(es): Manage Project Knowledge; Close Project or Phase
- Inputs: issue log, change log, retrospectives, closure record, PMO improvement backlog
- Outputs: lessons captured, reusable practices, action items, repository updates, escalation candidates
- Core fields:
  - lesson statement
  - context
  - impact
  - recommendation
  - reuse tag
  - owner
  - repository or escalation destination
- Owner: project manager or knowledge owner
- Approval authority: none for capture; PMO review only for enterprise template or policy changes
- Tailoring guidance: capture lessons in the same operational system used by the team where possible; avoid separate multimedia indexing records unless the repository genuinely uses them
- Waste test: fail if lessons are archived but not linked to future planning or PMO improvement decisions
- Notes: consolidates v1.0.2 Items #215, #216, #217, and #218 into one default knowledge-management family

### A31 Procurement and Supplier Management Record
- Artifact type: procurement planning and control artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: define supplier engagement approach, contract administration rules, delivery expectations, and ongoing supplier control needs.
- When used: during planning, procurement execution, and supplier monitoring.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Appendix X4 procurement-related guidance`; `Table 2-1: Procure Project Resources; Monitor and Control Project Work`; `[Forms-Book]`
- Purpose of citation: support procurement planning and administration using PMI-aligned terminology.
- Performance domain(s): Governance, Finance, Risk, Resources, Schedule
- Focus area(s): Planning, Executing, Monitoring and Controlling
- Related process(es): Procure Project Resources; Monitor and Control Project Performance
- Inputs: resource record, financial record, risk record, scope decisions, organizational procurement rules
- Outputs: supplier management approach, contract administration rules, acceptance and escalation logic
- Core fields:
  - procurement need
  - supplier scope
  - contract type or sourcing path
  - key obligations
  - acceptance rules
  - performance and escalation rules
- Owner: project manager with procurement support
- Approval authority: procurement authority, sponsor, or contract authority according to thresholds
- Tailoring guidance: use one project-level procurement control record rather than separate sourcing strategy, supplier coordination, and contract administration mini-ledgers unless different owners require them
- Waste test: fail if supplier-management fields are copied across a project plan, procurement tracker, and contract note with no added control value
- Notes: provides the default lean baseline for the procurement-heavy portions of v1.0.2 Cluster 15

### A32 Supplier Evaluation and Award Decision Record
- Artifact type: supplier selection and authorization artifact
- Source type: synthesis
- Governance layer: Project Governance / Portfolio Governance
- Purpose: document supplier qualification, evaluation, recommendation, and award decision rationale.
- When used: during supplier selection and award approval.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Appendix X4 procurement-related guidance`; `[Forms-Book]`
- Purpose of citation: anchor supplier selection and award thinking in PMI procurement support material.
- Performance domain(s): Governance, Finance, Risk, Resources
- Focus area(s): Planning, Executing
- Related process(es): Procure Project Resources
- Inputs: procurement strategy, supplier responses, evaluation criteria, risk inputs, legal and compliance inputs
- Outputs: shortlist, recommended supplier, award decision, award conditions
- Core fields:
  - evaluation criteria
  - suppliers considered
  - qualification result
  - risk and compliance findings
  - recommended supplier
  - award decision
- Owner: procurement lead or designated evaluation lead
- Approval authority: procurement board, sponsor, or contract authority according to organization design
- Tailoring guidance: combine prequalification, evaluation summary, and award recommendation into one decision record unless a formal tender regime requires distinct stages
- Waste test: fail if prequalification grids, award forms, and certification sheets restate the same selection evidence
- Notes: consolidates v1.0.2 Items #232 and #234, and absorbs essential decision content from adjacent vendor-scoring artifacts

### A33 Supplier Change, Claim, and Compliance Record
- Artifact type: supplier administration and exception artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: capture supplier-related changes, disputes, claims, compliance checks, inbound acceptance findings, and resolution decisions.
- When used: throughout supplier delivery and during closing.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Appendix X4 procurement-related guidance`; `Table 2-1: Assess and Implement Changes; Close Project or Phase`
- Purpose of citation: align supplier change and claim handling with PMI-aligned control and closure practices.
- Performance domain(s): Governance, Finance, Risk, Scope, Schedule
- Focus area(s): Monitoring and Controlling, Closing
- Related process(es): Assess and Implement Changes; Monitor and Control Project Performance; Close Project or Phase
- Inputs: supplier management record, change requests, claims, compliance checks, acceptance findings
- Outputs: supplier decisions, approved contract adjustments, claim resolutions, compliance evidence, closeout items
- Core fields:
  - supplier event or issue
  - type of event
  - impact summary
  - compliance finding
  - decision authority
  - resolution
  - follow-up action
- Owner: project manager, contract administrator, or procurement lead
- Approval authority: procurement authority, legal authority, sponsor, or quality authority depending on issue type and threshold
- Tailoring guidance: use one record for supplier-side change, claim, and compliance history unless legal or audit requirements demand separated registers
- Waste test: fail if change orders, claims logs, and supplier acceptance checklists are maintained separately with the same case identifiers and decisions
- Notes: consolidates v1.0.2 Items #237, #238, #239, #273, and #274

### A34 Information Retention and Records Control Record
- Artifact type: records management artifact
- Source type: synthesis
- Governance layer: Project Governance / PMO Governance
- Purpose: define retention, storage, access, archival, and disposal controls for project records.
- When used: during planning and maintained through closure.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Table 2-1: Plan Communications Management; Close Project or Phase`; `[OPM-Standard]`
- Purpose of citation: support controlled retention and retrieval of project information as part of organizational project management practice.
- Performance domain(s): Governance, Stakeholders
- Focus area(s): Planning, Closing
- Related process(es): Plan Communications Management; Close Project or Phase
- Inputs: communications record, compliance rules, organizational records policies, closure record
- Outputs: retention rules, archival location, access constraints, disposal triggers
- Core fields:
  - record category
  - retention rule
  - storage location
  - access level
  - archival owner
  - disposal trigger
- Owner: project manager or records owner as assigned
- Approval authority: records-management authority, PMO, or compliance owner according to policy
- Tailoring guidance: keep this as one control record unless distinct legal jurisdictions require separate schedules
- Waste test: fail if the same retention rules are copied into every artifact template
- Notes: normalizes v1.0.2 Item #208

### A35 Governance and Decision Authority Record
- Artifact type: governance framework artifact
- Source type: synthesis
- Governance layer: Project Governance
- Purpose: define governance forums, decision rights, authority thresholds, cadence, and escalation rules for the project.
- When used: at startup and when governance design materially changes.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Guide, Governance Performance Domain`; `Table 2-1: Monitor and Control Project Performance; Assess and Implement Changes`; `[PMO-Guide]`; `[GPPP]`
- Purpose of citation: establish PMI-aligned governance without blending PMO, portfolio, and project authority layers.
- Performance domain(s): Governance
- Focus area(s): Planning, Monitoring and Controlling
- Related process(es): Integrate and Align Project Plans; Monitor and Control Project Performance; Assess and Implement Changes
- Inputs: charter, tailoring decision record, organizational governance constraints, PMO service engagement record
- Outputs: governance calendar, decision-rights map, threshold rules, escalation routes
- Core fields:
  - governance bodies
  - decision categories
  - delegated authorities
  - approval thresholds
  - cadence
  - escalation triggers
- Owner: sponsor and project manager jointly, with PMO input only where PMO governance applies
- Approval authority: sponsor or designated project governing body
- Tailoring guidance: use one project governance record rather than separate governance charter, approval matrix, and governance scorecard as mandatory artifacts
- Waste test: fail if governance forums and authority thresholds are repeated in multiple planning artifacts without unique control purpose
- Notes: consolidates v1.0.2 Items #299, #301, and project-level portions of #302 while preserving separate PMO governance in A36

### A36 PMO Value, Maturity, and Improvement Record
- Artifact type: PMO governance and improvement artifact
- Source type: organization-defined
- Governance layer: PMO Governance
- Purpose: manage PMO service value, maturity evolution, customer feedback, and continuous improvement in one PMO-owned record set.
- When used: periodically according to PMO governance cadence.
- Primary PMI source: `[PMO-Guide]`
- Exact section: `PMO governance, PMO services, and PMO evolution themes`; `[PMBOK8] Appendix X2`
- Purpose of citation: support PMO service management and continuous improvement while keeping the format organization-defined.
- Performance domain(s): Governance, Stakeholders, Resources
- Focus area(s): Monitoring and Controlling, Closing
- Related process(es): none mandated for project teams; this is a PMO governance artifact
- Inputs: PMO service engagement records, PMO improvement backlog, service feedback, maturity reviews
- Outputs: PMO value view, maturity actions, service changes, simplification decisions
- Core fields:
  - service performance themes
  - stakeholder feedback themes
  - maturity observations
  - improvement actions
  - owner
  - target date
- Owner: PMO leader
- Approval authority: PMO governance forum or executive PMO sponsor
- Tailoring guidance: merge PMO value scorecard, maturity review, and improvement actions unless the PMO has a formal enterprise assessment regime requiring separate artifacts
- Waste test: fail if satisfaction scorecards and maturity reviews are produced without resulting PMO service changes
- Notes: consolidates v1.0.2 Items #229, #302, #305, and #306, while related improvement backlog control remains A23

### A37 AI, Data, and Privacy Control Record
- Artifact type: digital risk and compliance artifact
- Source type: synthesis
- Governance layer: Project Governance / PMO Governance
- Purpose: document AI-related, data-security, privacy, and prompt/data-handling controls where digital solutions or suppliers create elevated exposure.
- When used: when the project, product, or supplier environment involves AI, sensitive data, automated decision support, or regulated digital processing.
- Primary PMI source: `[PMBOK8]`
- Exact section: `Appendix X3 AI-related guidance`; `Appendix X4 procurement-related guidance`; `[AI-Essentials]`; `[AI-Projects]`
- Purpose of citation: support responsible handling of AI, data, privacy, and supplier digital-control risks.
- Performance domain(s): Governance, Risk, Stakeholders, Resources
- Focus area(s): Planning, Monitoring and Controlling, Closing
- Related process(es): Plan Risk Management; Identify Risks; Procure Project Resources; Monitor Risks; Assess and Implement Changes
- Inputs: risk record, procurement record, supplier evaluation record, organizational security policies
- Outputs: control requirements, compliance checks, decision restrictions, supplier or project exceptions
- Core fields:
  - use case or exposure area
  - data classification
  - privacy and security controls
  - AI-specific controls
  - supplier obligations
  - exception or escalation path
- Owner: project manager with security, data, or compliance support as needed
- Approval authority: designated security, privacy, compliance, or sponsor authority according to organizational policy
- Tailoring guidance: do not create this artifact unless digital, AI, or data exposure justifies it; when needed, keep one integrated record instead of separate privacy, bias, and prompt-sanitization logs unless required by regulation
- Waste test: fail if AI control checklists are maintained for projects with no AI or sensitive-data exposure
- Notes: normalizes v1.0.2 Item #235 and the earlier repository AI guardrail theme into one risk-based artifact

---

## 19. Final migration map for remaining clusters

| v1.0.2 artifact(s) | v1.0.5 action |
|---|---|
| #181 Team Charter Ground Rules Blueprint + #184 Responsibility Assignment Matrix | Merge into A25 |
| #182 Skill inventory + #183 allocation ledger + #185 resource management plan + #186 resource calibration matrix | Merge into A26, with optional capability detail feeding A27 |
| #187 Tuckman tracker + #188 workplace friction index + #189 team appraisal workbook + #212 competency framework + #213 mentorship log + #214 growth roadmap | Merge into A27 |
| #190 communications mapping matrix + #191 communications management plan + #192 omnichannel communications blueprint + #211 status briefing deck | Merge into A28 |
| #208 archival retention log | Normalize into A34 |
| #209 change impact readiness assessment + #210 stakeholder feedback log | Merge into A29 |
| #215 community of practice charter + #216 lessons learned repository + #217 retrospective video curation + #218 post-mortem framework | Merge into A30, with PMO-only extensions under A23/A36 |
| #229 PMO service catalog capability deployment blueprint | Keep PMO service delivery logic in A11 and PMO value/improvement logic in A36 |
| #232 supplier prequalification grid + #234 procurement award board certification form | Merge into A32 |
| #233 ecosystem partnering framework + #237 procurement change order ledger + #238 vendor disputes log + #239 supplier release quality checklist + #273-#274 closing duplicates | Manage through A31 and A33 |
| #235 supplier data security/privacy attestation and related AI/privacy controls | Normalize into A37 |
| #227 stage-gate sheet + #228 cross-project scope priority matrix + #243 milestone dependencies directory | Keep portfolio-level decisions in A10 and A22; do not duplicate inside project governance artifacts |
| #299 governance framework charter + #301 decision rights matrix + project-level use of #302 governance health scorecard | Merge into A35 |
| #305 PMO maturity assessment + #306 PMO value scorecard | Merge into A36 |
| Repeated closing and audit variants across later clusters | Fold into A24, A33, and A34 based on purpose |

---

## 20. Repository baseline after full conversion

After v1.0.5, the repository baseline consists of a lean, end-to-end artifact family rather than hundreds of overlapping forms. Use the following as the default catalog unless regulation, contract terms, or enterprise policy require additional separation.

| Family | Default artifacts |
|---|---|
| Strategy and authorization | A01, A02, A03, A04, A10 |
| Context and tailoring | A05, A06, A13, A35 |
| Stakeholders, scope, communications | A07, A08, A28, A29 |
| Team and resources | A09, A25, A26, A27 |
| Planning and baselines | A14, A15, A16 |
| Monitoring and decisions | A12, A17, A18, A19, A20, A21 |
| Portfolio and PMO interfaces | A11, A22, A23, A36 |
| Procurement and digital controls | A31, A32, A33, A37 |
| Knowledge, closure, and records | A24, A30, A34 |

---

## 21. Final editorial controls

1. A project shall not be required to instantiate every artifact in this catalog; tailoring decides the minimum viable set.
2. Project governance artifacts shall remain distinct from PMO governance artifacts and from portfolio governance artifacts.
3. Optional visual canvases, dashboards, and workshop aids are allowed only as supporting views of an approved baseline artifact, not as separate mandatory controls.
4. Source type must be declared on every artifact definition and template.
5. Every artifact must cite the primary PMI source, exact section, purpose of citation, and source type.
6. Artifacts above the waste threshold must be merged, automated, or retired.
7. No artifact may use custom repository vocabulary as if it were PMI-native terminology.

---

## 22. Completion note

`Artifacts-V-1.0.5.md` is the full-conversion baseline that replaces the sprawling v1.0.2 structure with a traceable, layered, and tailorable repository architecture grounded in PMBOK 8 vocabulary and supported by the PMI reference list.
