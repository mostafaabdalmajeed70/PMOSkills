# SKILL-REGISTRY.md
**Repository:** PMO Skill Repository  
**Version:** 1.0.0-draft  
**Authority:** PMBOK8 Primary  
**Purpose:** Master index of all skills. Filter by Lifecycle Pack, Performance Domain, Principle, Process, or Artifact to locate the right skill file.

---

## Skill Record Schema

Every skill row contains:

| Field | Description |
|-------|-------------|
| `Skill ID` | Unique identifier, format: `SKL-[PACK]-[SEQ]` |
| `Skill Name` | Plain-language name of the skill |
| `Lifecycle Pack` | 00-Core · 01-Pre-sign · 02-Initiating · 03-Planning · 04-Executing · 05-M&C · 06-Closing · 07-PMO · 08-AI-Procurement |
| `Performance Domain Tags` | Governance · Scope · Schedule · Finance · Stakeholders · Resources · Risk |
| `Principle Tags` | One or more of the 6 PMBOK 8 principles |
| `Related PMBOK Process(es)` | Exact PMBOK 8 process name(s) |
| `Source Artifact(s)` | A01–A41 artifact IDs from Artifacts-V-1.1.md |
| `Required Inputs` | Minimum inputs for skill execution |
| `Generated Outputs` | Artifacts, decisions, or records produced |
| `Authority Route` | T1 / T2 / T3 / T4 + Approval authority |
| `Companion References` | Secondary PMI sources used |
| `File Path` | Relative path in this repository |
| `Test Status` | Draft · Untested · Tested · Validated |

---

## 6 PMBOK 8 Principles (Reference)

| Code | Principle |
|------|-----------|
| P1 | Adopt a Holistic View |
| P2 | Focus on Value |
| P3 | Embed Quality Into Processes and Deliverables |
| P4 | Be an Accountable Leader |
| P5 | Integrate Sustainability Within All Project Areas |
| P6 | Build an Empowered Culture |

---

## PACK 00 — Core Skills (Shared Components)

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-00-01 | Waste Test Validator | Governance | P1 P2 | All | Any | Draft artifact | Pass/fail waste assessment | T1 — PM | skills/00-core/SKL-00-01-waste-test.md |
| SKL-00-02 | Authority Routing Checker | Governance | P4 | All | Any | Decision description, threshold level | Correct approval authority + escalation path | T1 → T4 | skills/00-core/SKL-00-02-authority-routing.md |
| SKL-00-03 | Source Labeling Validator | Governance | P1 P4 | All | Any | Artifact draft | Labeled PMI-derived / synthesis / org-defined | T1 — PM | skills/00-core/SKL-00-03-source-labeling.md |
| SKL-00-04 | Tailoring Decision Trigger | Governance | P1 P2 | Integrate and Align Project Plans | A06 | Project context, complexity factors | Tailoring profile update or waiver record | T2 — Sponsor/PMO | skills/00-core/SKL-00-04-tailoring-trigger.md |
| SKL-00-05 | Artifact Quality Checklist | Governance | P3 P4 | All | Any | Draft artifact | Quality check result, remediation notes | T1 — PM | skills/00-core/SKL-00-05-quality-checklist.md |

---

## PACK 01 — Pre-sign Skills (Before Formal Authorization)

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-01-01 | Intake and Prioritization Decision | Governance Finance Resources Risk | P1 P2 P4 | Initiate Project or Phase | A04 (Portfolio) | Demand description, strategic priorities, capacity view | Approve/defer/reject/sequence decision record | T3 — Portfolio Board | skills/01-pre-sign/SKL-01-01-intake-prioritization.md |
| SKL-01-02 | Business Case Creation | Governance Finance Stakeholders | P2 P4 | Initiate Project or Phase | A01 | Problem/opportunity statement, strategic objectives, preliminary financial data | Business case with recommendation | T3 — Sponsor/Portfolio | skills/01-pre-sign/SKL-01-02-business-case.md |
| SKL-01-03 | Business Case Revalidation | Governance Finance | P2 P4 | Monitor and Control Project Performance | A01 A02 | Existing business case, updated assumptions, performance data | Revalidated or updated business case decision | T3 — Sponsor | skills/01-pre-sign/SKL-01-03-business-case-revalidation.md |
| SKL-01-04 | Benefits and Value Baseline | Governance Finance Stakeholders | P2 P5 | Initiate Project or Phase · Close Project or Phase | A02 | Business case, success measures, benefit owners | Benefits record with measures, owners, review cadence | T3 — Sponsor/Business Owner | skills/01-pre-sign/SKL-01-04-benefits-baseline.md |
| SKL-01-05 | Feasibility and Options Analysis | Governance Scope Risk Finance | P1 P2 | Initiate Project or Phase | A03 | Need statement, constraints, technical inputs, financial data | Feasibility record with recommended option | T3 — Sponsor | skills/01-pre-sign/SKL-01-05-feasibility.md |
| SKL-01-06 | PMO Service Scoping | Governance | P4 | None (PMO governance artifact) | A11 | Project context, PMO service catalog | PMO service engagement record | T2 — PMO Leader | skills/01-pre-sign/SKL-01-06-pmo-service-scoping.md |
| SKL-01-07 | Portfolio Interdependency Review | Governance Resources Schedule Risk | P1 P2 | Integrate and Align Project Plans | A22 | Portfolio priorities, schedule data, dependency info | Dependency record, escalation needs, sequencing decisions | T4 — Portfolio Board | skills/01-pre-sign/SKL-01-07-portfolio-interdependency.md |

---

## PACK 02 — Initiating Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-02-01 | Project Charter Creation | Governance Stakeholders | P2 P4 | Initiate Project or Phase | A03 | Business case, recommended option, statement of work | Signed project charter with PM authority | T3 — Sponsor | skills/02-initiating/SKL-02-01-project-charter.md |
| SKL-02-02 | Stakeholder Identification | Stakeholders Governance | P1 P4 P6 | Identify Stakeholders | A07 | Charter, org charts, context factors | Initial stakeholder register with engagement strategy | T2 — PM/Sponsor | skills/02-initiating/SKL-02-02-stakeholder-id.md |
| SKL-02-03 | Context Register Creation | Governance Risk Resources | P1 P4 | Initiate Project or Phase | A05 | Policies, standards, lessons learned, compliance constraints, market conditions | Context register with EEFs, OPAs, assumptions | T1 — PM | skills/02-initiating/SKL-02-03-context-register.md |
| SKL-02-04 | Governance and Authority Setup | Governance | P4 P6 | Initiate Project or Phase · Integrate and Align Project Plans | A35 | Charter, tailoring constraints, PMO input | Governance record: forums, thresholds, escalation routes | T3 — Sponsor/PM | skills/02-initiating/SKL-02-04-governance-setup.md |
| SKL-02-05 | Initial Tailoring Decision | Governance | P1 P2 P4 | Integrate and Align Project Plans | A06 | Charter, context register, complexity factors | Tailoring profile: retained/removed controls, approval thresholds | T2 — PM/Sponsor | skills/02-initiating/SKL-02-05-initial-tailoring.md |
| SKL-02-06 | Phase Gate Authorization Record | Governance Finance | P2 P4 | Initiate Project or Phase | A03 A35 | Phase completion evidence, next phase plan | Gate decision record: proceed/pause/stop | T3 — Sponsor/Governing Body | skills/02-initiating/SKL-02-06-phase-gate.md |

---

## PACK 03 — Planning Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-03-01 | Integrated Project Management Plan | Governance Scope Schedule Finance Stakeholders Resources Risk | P1 P2 P4 | Integrate and Align Project Plans | A14 | All planning records approved | Integrated plan, baseline references, governance calendar | T3 — Sponsor/Governing Body | skills/03-planning/SKL-03-01-integrated-plan.md |
| SKL-03-02 | Lifecycle and Approach Decision | Governance Schedule Resources Risk | P1 P2 P4 | Integrate and Align Project Plans | A13 | Charter, context, tailoring record, stakeholder needs | Lifecycle pattern: predictive/adaptive/hybrid with rationale | T2–T3 — Sponsor | skills/03-planning/SKL-03-02-lifecycle-decision.md |
| SKL-03-03 | Scope Management Planning | Scope Stakeholders Risk | P2 P3 | Plan Scope Management | A08 | Charter, stakeholder record, product vision | Scope management approach, WBS or backlog structure | T2 — PM/Sponsor | skills/03-planning/SKL-03-03-scope-plan.md |
| SKL-03-04 | Requirements Elicitation and Analysis | Scope Stakeholders Risk | P2 P3 P6 | Elicit and Analyze Requirements | A08 | Charter, stakeholder record, product vision, workshops | Prioritized requirements, assumptions, acceptance criteria | T2 — PM/Product Owner | skills/03-planning/SKL-03-04-requirements.md |
| SKL-03-05 | Scope Definition and Structure | Scope Governance | P2 P3 | Define Scope · Develop Scope Structure | A08 | Requirements record, charter | Scope statement, WBS or value breakdown structure | T2 — PM/Sponsor | skills/03-planning/SKL-03-05-scope-definition.md |
| SKL-03-06 | Schedule Model and Baseline | Schedule Resources Risk Governance | P2 P3 P4 | Plan Schedule Management · Develop Schedule | A15 | Scope decisions, resource info, risk data | Schedule baseline, milestones, critical path or flow view | T2 — PM/Change Authority | skills/03-planning/SKL-03-06-schedule-baseline.md |
| SKL-03-07 | Financial Management and Budget | Finance Governance Risk | P2 P3 P4 | Plan Financial Management · Estimate Costs · Develop Budget | A16 | Scope, schedule, resource estimates, risk data, business case | Cost baseline, funding plan, reserve logic | T3 — Sponsor/Finance Authority | skills/03-planning/SKL-03-07-financial-baseline.md |
| SKL-03-08 | Stakeholder Engagement Planning | Stakeholders Governance | P2 P4 P6 | Plan Stakeholder Engagement | A07 | Charter, initial stakeholder register | Engagement strategies, communication needs, escalation flags | T2 — PM/Sponsor | skills/03-planning/SKL-03-08-stakeholder-plan.md |
| SKL-03-09 | Communications Management Planning | Stakeholders Governance | P4 P6 | Plan Communications Management | A28 | Stakeholder record, integrated plan | Audience map, communication cadence, channel rules | T2 — PM | skills/03-planning/SKL-03-09-comms-plan.md |
| SKL-03-10 | Resource Management Planning | Resources Schedule Finance Governance | P4 P6 | Plan Resource Management · Estimate Resources | A26 | Scope, schedule, financial record | Staffing plan, acquisition path, resource conflict visibility | T2 — PM/Functional Manager | skills/03-planning/SKL-03-10-resource-plan.md |
| SKL-03-11 | Risk Management Planning | Risk Governance Finance Scope Schedule | P1 P2 P3 | Plan Risk Management | A19 | Charter, context, scope, estimates, stakeholder insights | Risk management approach, risk thresholds, process cadence | T2 — PM/Sponsor | skills/03-planning/SKL-03-11-risk-plan.md |
| SKL-03-12 | Risk Identification | Risk All Domains | P1 P2 P3 | Identify Risks | A19 | Risk management record, scope, schedule, financial data | Initial risk register with threats and opportunities | T1 — PM/Risk Owner | skills/03-planning/SKL-03-12-risk-identification.md |
| SKL-03-13 | Team Operating Agreement | Resources Governance Stakeholders | P4 P6 | Plan Resource Management · Lead the Team | A09 A25 | Charter, tailoring record, team structure | Team operating model, cadence, roles, decision rules | T1 — PM/Delivery Lead | skills/03-planning/SKL-03-13-team-agreement.md |
| SKL-03-14 | Procurement Strategy and Sourcing Plan | Governance Finance Risk Resources Schedule | P1 P2 P4 | Plan Sourcing Strategy | A31 | Resource record, financial record, scope decisions, procurement rules | Sourcing approach, contract type options, supplier engagement rules | T3 — Procurement/Sponsor | skills/03-planning/SKL-03-14-procurement-plan.md |
| SKL-03-15 | Change Readiness and Adoption Planning | Stakeholders Resources Governance Risk | P2 P4 P6 | Plan Stakeholder Engagement | A29 | Stakeholder record, scope decisions, rollout plans | Readiness profile, adoption actions, training needs | T2 — PM/Change Lead | skills/03-planning/SKL-03-15-change-readiness.md |

---

## PACK 04 — Executing Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-04-01 | Manage Project Execution | Governance All Domains | P2 P3 P4 P6 | Manage Project Execution | A14 A17 A18 | Integrated plan, team agreement, current status | Work performance data, action log updates, issue escalations | T1 — PM | skills/04-executing/SKL-04-01-manage-execution.md |
| SKL-04-02 | Quality Assurance Management | Scope Governance | P3 | Manage Quality Assurance | A38 | Quality management plan, process data, deliverable samples | Quality assurance findings, process improvement actions | T2 — PM/Quality Authority | skills/04-executing/SKL-04-02-quality-assurance.md |
| SKL-04-03 | Project Knowledge Management | Governance Resources | P1 P3 P6 | Manage Project Knowledge | A30 | Issue log, change log, retrospectives | Lessons captured, reusable practices, repository updates | T1 — PM/Knowledge Owner | skills/04-executing/SKL-04-03-knowledge-management.md |
| SKL-04-04 | Stakeholder Engagement Execution | Stakeholders Governance | P2 P4 P6 | Manage Stakeholder Engagement | A07 A29 | Stakeholder register, engagement strategy | Engagement actions, feedback captured, escalation flags | T1–T2 — PM | skills/04-executing/SKL-04-04-stakeholder-engagement.md |
| SKL-04-05 | Communications Execution | Stakeholders Governance | P4 P6 | Manage Communications | A28 | Communications plan, reporting cadence | Information distributed, feedback received, issues flagged | T1 — PM/Comms Lead | skills/04-executing/SKL-04-05-comms-execution.md |
| SKL-04-06 | Resource Acquisition and Team Setup | Resources Schedule Finance Governance | P4 P6 | Acquire Resources | A26 A25 | Resource plan, sourcing decisions, financial record | Acquired team/resources, team operating record activated | T2 — PM/Procurement | skills/04-executing/SKL-04-06-resource-acquisition.md |
| SKL-04-07 | Team Leadership and Development | Resources Stakeholders | P4 P6 | Lead the Team | A25 A27 | Team agreement, team health record | Performance coaching, development actions, escalation decisions | T1 — PM/Delivery Lead | skills/04-executing/SKL-04-07-team-leadership.md |
| SKL-04-08 | Risk Response Implementation | Risk Governance | P1 P2 P3 | Implement Risk Responses | A19 | Risk register, response plans, project conditions | Executed responses, updated risk register, change requests | T2 — PM/Risk Owner | skills/04-executing/SKL-04-08-risk-response.md |
| SKL-04-09 | Supplier Delivery Management | Governance Finance Risk Resources Schedule | P2 P3 P4 | Manage Project Execution | A31 A33 | Supplier management record, contract, delivery schedule | Supplier performance data, compliance checks, issue flags | T2 — PM/Procurement | skills/04-executing/SKL-04-09-supplier-delivery.md |
| SKL-04-10 | Issue and Action Tracking | Governance All Domains | P4 P6 | Manage Project Execution | A18 | Team signals, quality findings, stakeholder concerns | Assigned actions, escalation decisions, closure evidence | T1 — PM/Delivery Lead | skills/04-executing/SKL-04-10-issue-tracking.md |

---

## PACK 05 — Monitoring and Controlling Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-05-01 | Integrated Performance Reporting | Governance Schedule Finance Stakeholders Resources Risk | P2 P3 P4 | Monitor and Control Project Performance | A17 | Schedule data, financial data, risk data, issue data | Status narrative, forecast, escalations, corrective action requests | T1–T2 — PM/Sponsor | skills/05-monitoring-controlling/SKL-05-01-performance-report.md |
| SKL-05-02 | Change Assessment and Decision | Governance Scope Schedule Finance Risk | P1 P2 P4 | Assess and Implement Changes | A12 A21 | Change requests, impact analysis, variance data | Approved/rejected/deferred change decision with rationale | T2–T3 — Change Authority/Sponsor | skills/05-monitoring-controlling/SKL-05-02-change-assessment.md |
| SKL-05-03 | Scope Monitoring and Validation | Scope Governance | P2 P3 | Monitor and Control Scope · Validate Scope | A08 | Scope baseline, deliverables, acceptance evidence | Validated scope, approved changes, acceptance record | T2 — PM/Customer/Product Owner | skills/05-monitoring-controlling/SKL-05-03-scope-monitoring.md |
| SKL-05-04 | Schedule Monitoring and Forecasting | Schedule Risk Finance Governance | P2 P3 P4 | Monitor and Control Schedule | A15 A17 | Schedule baseline, work performance data | Updated schedule forecast, variance analysis, recovery options | T2 — PM/Change Authority | skills/05-monitoring-controlling/SKL-05-04-schedule-monitoring.md |
| SKL-05-05 | Financial Monitoring and Control | Finance Governance Risk | P2 P3 P4 | Monitor and Control Finances | A16 A17 | Cost baseline, expenditure data, financial forecasts | Cost variance, EVM metrics, forecast updates, funding alerts | T2–T3 — PM/Finance/Sponsor | skills/05-monitoring-controlling/SKL-05-05-financial-monitoring.md |
| SKL-05-06 | Risk Monitoring | Risk Governance All Domains | P1 P2 P3 | Monitor Risks | A19 A12 | Risk register, work performance data, issue log | Updated risk register, new risk flags, response effectiveness data | T1–T2 — PM/Risk Owner | skills/05-monitoring-controlling/SKL-05-06-risk-monitoring.md |
| SKL-05-07 | Stakeholder Engagement Monitoring | Stakeholders Governance | P4 P6 | Monitor Stakeholder Engagement | A07 A28 | Stakeholder register, engagement data, feedback | Updated engagement status, strategy adjustments, escalations | T1–T2 — PM | skills/05-monitoring-controlling/SKL-05-07-stakeholder-monitoring.md |
| SKL-05-08 | Resource Monitoring | Resources Schedule Finance Governance | P2 P4 | Monitor and Control Resourcing | A26 A17 | Resource plan, utilization data, capacity signals | Resource variance, conflict flags, reallocation decisions | T2 — PM/Functional Manager | skills/05-monitoring-controlling/SKL-05-08-resource-monitoring.md |
| SKL-05-09 | Quality Control Monitoring | Scope Governance | P3 | Manage Quality Assurance | A38 A17 | Quality metrics, deliverable data, process performance | Quality control findings, defect tracking, improvement actions | T2 — PM/Quality Authority | skills/05-monitoring-controlling/SKL-05-09-quality-control.md |
| SKL-05-10 | Quantitative Risk and Reserve Review | Risk Finance Governance | P1 P2 P3 | Perform Risk Analysis | A20 | Risk register, cost/schedule baselines, probability data | Reserve adequacy assessment, quantitative exposure update | T3 — Sponsor/Finance/Governing Body | skills/05-monitoring-controlling/SKL-05-10-quantitative-risk.md |
| SKL-05-11 | Trade-Off Decision Record | Governance All Domains | P1 P2 P4 | Assess and Implement Changes · Monitor and Control Project Performance | A21 | Performance report, risk data, change proposals | Documented trade-off decision with rationale and follow-up | T2–T3 — Sponsor/Change Authority | skills/05-monitoring-controlling/SKL-05-11-tradeoff-decision.md |
| SKL-05-12 | Supplier Change and Compliance Check | Governance Finance Risk Scope Schedule | P2 P3 P4 | Assess and Implement Changes | A33 | Supplier record, change events, compliance findings | Supplier decision log, approved adjustments, compliance evidence | T2–T3 — Procurement/Legal/Sponsor | skills/05-monitoring-controlling/SKL-05-12-supplier-compliance.md |

---

## PACK 06 — Closing Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-06-01 | Closure Readiness Assessment | Governance All Domains | P2 P3 P4 | Close Project or Phase | A24 | Integrated plan, acceptance evidence, issue log, risk register | Closure readiness checklist: criteria met/outstanding | T2 — PM/Sponsor | skills/06-closing/SKL-06-01-closure-readiness.md |
| SKL-06-02 | Deliverable Acceptance and Handover | Scope Governance Stakeholders | P2 P3 | Close Project or Phase | A24 | Deliverables, acceptance criteria, customer sign-off | Formal acceptance record, handover documentation | T3 — Sponsor/Customer/Business Owner | skills/06-closing/SKL-06-02-acceptance-handover.md |
| SKL-06-03 | Benefits Transition Record | Governance Finance Stakeholders | P2 P5 | Close Project or Phase | A02 A24 | Benefits record, operational transition plan, value measures | Benefits handover plan, ownership transfer, follow-up schedule | T3 — Sponsor/Business Owner | skills/06-closing/SKL-06-03-benefits-transition.md |
| SKL-06-04 | Financial Closure | Finance Governance | P2 P4 | Close Project or Phase | A16 A24 | Cost actuals, baseline, vendor invoices, reserve balance | Financial closure report: final cost, reserve disposition, accounts closed | T3 — Finance Authority/Sponsor | skills/06-closing/SKL-06-04-financial-closure.md |
| SKL-06-05 | Lessons Learned Capture and Closure | Governance Resources | P1 P3 P6 | Manage Project Knowledge · Close Project or Phase | A30 A24 | Issue log, change log, retrospectives, closure record | Final lessons record, reusable practice recommendations, PMO escalation | T1 — PM/Knowledge Owner/PMO | skills/06-closing/SKL-06-05-lessons-learned.md |
| SKL-06-06 | Resource Release and Team Closure | Resources Governance | P4 P6 | Close Project or Phase | A24 A26 | Resource records, team agreements, closure readiness | Resource release plan, team recognition record, role transitions | T2 — PM/Functional Manager | skills/06-closing/SKL-06-06-resource-release.md |
| SKL-06-07 | Procurement Closure | Governance Finance Risk | P2 P4 | Close Project or Phase | A31 A33 A24 | Supplier records, contract, acceptance evidence, open claims | Supplier closeout: final acceptance, claims resolved, contracts archived | T3 — Procurement/Legal/Sponsor | skills/06-closing/SKL-06-07-procurement-closure.md |
| SKL-06-08 | Records Retention and Archival | Governance | P3 P4 | Close Project or Phase | A34 A24 | All project documents, retention policy, compliance requirements | Archived record set, retention schedule, access rules | T2–T3 — Records Owner/Compliance | skills/06-closing/SKL-06-08-records-retention.md |
| SKL-06-09 | Final Project Report | Governance All Domains | P2 P3 P4 | Close Project or Phase | A24 A17 A02 | Performance data, acceptance evidence, benefits record, lessons | Final project report: performance summary, value delivered, recommendations | T3 — Sponsor/Governing Body | skills/06-closing/SKL-06-09-final-report.md |
| SKL-06-10 | Phase Gate or Project Closure Authorization | Governance Finance Stakeholders | P2 P4 | Close Project or Phase | A24 A35 | Closure readiness assessment, final report, benefits transition | Formal closure authorization record | T3 — Sponsor/Governing Body | skills/06-closing/SKL-06-10-closure-authorization.md |

---

## PACK 07 — PMO Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-07-01 | PMO Configuration and Authority Definition | Governance | P4 P6 | None (PMO governance) | A11 A39 | Organization structure, PMO charter, PMO type selection | PMO configuration record: type, authority, services, boundaries | T4 — PMO Governance Forum/Executive | skills/07-pmo/SKL-07-01-pmo-configuration.md |
| SKL-07-02 | PMO Service Catalog Management | Governance | P2 P4 | None (PMO governance) | A11 | PMO configuration, project demand, capability data | Updated PMO service catalog with offerings and SLAs | T3 — PMO Leader | skills/07-pmo/SKL-07-02-service-catalog.md |
| SKL-07-03 | PMO Service Engagement | Governance | P4 | None (PMO governance) | A11 | Project request, service catalog, capability needs | PMO service engagement record: scope, cadence, contact | T2 — PMO Leader/Service Owner | skills/07-pmo/SKL-07-03-service-engagement.md |
| SKL-07-04 | PMO Value and Maturity Assessment | Governance | P2 P4 | None (PMO governance) | A36 | PMO performance data, project outcomes, maturity model | Maturity assessment, value metrics, improvement roadmap | T3–T4 — PMO Governance/Executive | skills/07-pmo/SKL-07-04-maturity-assessment.md |
| SKL-07-05 | PMO Improvement Backlog Management | Governance | P2 P3 P6 | None (PMO governance) | A23 | Retrospectives, feedback, audit findings, service metrics | Prioritized improvement backlog, approved changes | T2 — PMO Leader | skills/07-pmo/SKL-07-05-improvement-backlog.md |
| SKL-07-06 | PMO Template and Method Governance | Governance | P3 P4 | None (PMO governance) | A23 A11 | Repository feedback, PMI updates, project team input | Approved template updates, deprecated templates, change log | T2 — PMO Leader | skills/07-pmo/SKL-07-06-template-governance.md |
| SKL-07-07 | PMO Portfolio Reporting | Governance Finance Resources Risk | P2 P4 | Monitor and Control Project Performance | A17 A22 | Multi-project performance data, portfolio priorities | Portfolio performance report, interdependency flags, escalations | T3 — Portfolio Board/PMO | skills/07-pmo/SKL-07-07-portfolio-reporting.md |

---

## PACK 08 — AI and Procurement Skills

| Skill ID | Skill Name | Domain Tags | Principle Tags | PMBOK Process | Artifact(s) | Required Inputs | Generated Outputs | Authority Route | File |
|----------|-----------|-------------|----------------|---------------|-------------|-----------------|-------------------|-----------------|------|
| SKL-08-01 | AI Use Case Assessment | Governance Risk | P1 P3 P4 P5 | Manage Project Execution | A37 | Project context, proposed AI tools, data inventory | AI use case record: approved uses, oversight rules, bias controls | T3 — Security/Privacy/Compliance/Sponsor | skills/08-ai-procurement/SKL-08-01-ai-use-case.md |
| SKL-08-02 | AI Decision Support and Oversight | Governance Risk | P3 P4 P5 | Monitor and Control Project Performance | A37 | AI system outputs, human oversight log, decision audit | Human-in-the-loop decision record, AI audit trail | T2–T3 — PM/Compliance Authority | skills/08-ai-procurement/SKL-08-02-ai-oversight.md |
| SKL-08-03 | Data and Privacy Control Record | Governance Risk | P3 P4 P5 | All | A37 | Data inventory, classification, regulatory constraints | Data control record: classification, access rules, retention policy | T3 — Security/Privacy Authority | skills/08-ai-procurement/SKL-08-03-data-privacy.md |
| SKL-08-04 | Make-or-Buy Analysis | Governance Finance Risk | P2 P4 | Plan Sourcing Strategy | A31 | Scope decisions, resource data, market options, financial model | Make-or-buy recommendation with rationale | T3 — Sponsor/Procurement | skills/08-ai-procurement/SKL-08-04-make-or-buy.md |
| SKL-08-05 | Procurement Bid and Source Selection | Governance Finance Risk Resources | P2 P3 P4 | Plan Sourcing Strategy | A31 A32 | Procurement strategy, evaluation criteria, supplier responses | Bid documents, shortlist, evaluation record, award recommendation | T3 — Procurement Board/Sponsor | skills/08-ai-procurement/SKL-08-05-source-selection.md |
| SKL-08-06 | Contract Administration | Governance Finance Risk Scope Schedule | P2 P3 P4 | Manage Project Execution · Monitor and Control | A31 A33 | Signed contract, delivery schedule, acceptance criteria | Contract administration log, performance record, compliance checks | T2 — Procurement Lead/PM | skills/08-ai-procurement/SKL-08-06-contract-admin.md |
| SKL-08-07 | Claims and Dispute Management | Governance Finance Risk | P2 P4 | Assess and Implement Changes | A33 | Claim submission, contract terms, dispute record | Claim resolution record, legal referral if needed, closure evidence | T3 — Procurement/Legal/Sponsor | skills/08-ai-procurement/SKL-08-07-claims-disputes.md |

---

## Summary Counts

| Pack | Skills Count |
|------|-------------|
| 00 Core | 5 |
| 01 Pre-sign | 7 |
| 02 Initiating | 6 |
| 03 Planning | 15 |
| 04 Executing | 10 |
| 05 Monitoring & Controlling | 12 |
| 06 Closing | 10 |
| 07 PMO | 7 |
| 08 AI & Procurement | 7 |
| **Total** | **79 skills** |

---

*Authority: PMBOK8 Primary · All 40 processes covered · All 7 performance domains covered · All 6 principles embedded*  
*Cross-referenced to Artifacts-V-1.1.md (A01–A41) and Artifacts-Authorities-V-1.1.md*
