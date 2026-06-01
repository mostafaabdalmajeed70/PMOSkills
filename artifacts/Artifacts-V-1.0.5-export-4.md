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
