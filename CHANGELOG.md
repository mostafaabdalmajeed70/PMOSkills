# Changelog

All notable changes to this repository are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Authority: PMBOK 8 Primary · PMI Companion References Secondary.

---

## [2.10.0] — 2026-05-31

### Added — Phase C2: Reference Performance Domains Layer (COMPLETE)
- `reference/performance-domains/00-index.md` — Full performance domains index: 8 domains, interdependency matrix, interaction diagram, artifact coverage, skill connections. SHA: b2cdd222.
- `reference/performance-domains/PD01-stakeholders.md` — Stakeholder Performance Domain (PMBOK8 §4.1). SHA: 229de93c.
- `reference/performance-domains/PD02-team.md` — Team Performance Domain (PMBOK8 §4.2). SHA: e67e0b17.
- `reference/performance-domains/PD03-development-approach.md` — Development Approach and Life Cycle Performance Domain (PMBOK8 §4.3). SHA: c6e28640.
- `reference/performance-domains/PD04-planning.md` — Planning Performance Domain (PMBOK8 §4.4). SHA: 1cbc7013.
- `reference/performance-domains/PD05-project-work.md` — Project Work Performance Domain (PMBOK8 §4.5). SHA: d26bf832.
- `reference/performance-domains/PD06-delivery.md` — Delivery Performance Domain (PMBOK8 §4.6). SHA: 8cf1706d.
- `reference/performance-domains/PD07-measurement.md` — Measurement Performance Domain (PMBOK8 §4.7). SHA: c0f874d3.
- `reference/performance-domains/PD08-uncertainty.md` — Uncertainty Performance Domain (PMBOK8 §4.8). SHA: 102bfb0e.

### Added — Phase C3: Reference Focus Areas Layer (COMPLETE)
- `reference/focus-areas/FA01-initiating.md` — Initiating Focus Area (Process Groups Practice Guide §4). SHA: bef503db.
- `reference/focus-areas/FA02-planning.md` — Planning Focus Area (Process Groups Practice Guide §5). SHA: 316daf73.
- `reference/focus-areas/FA03-executing.md` — Executing Focus Area (Process Groups Practice Guide §6). SHA: be012353.
- `reference/focus-areas/FA04-monitoring-controlling.md` — Monitoring & Controlling Focus Area (Process Groups Practice Guide §7). SHA: c8f193da.
- `reference/focus-areas/FA05-closing.md` — Closing Focus Area (Process Groups Practice Guide §8). SHA: 02f47fd3.

Each performance domain file includes: YAML front matter, PMI-grounded definition, desired outcomes, key activities, interdependency tables, artifact connections, skill connections, and 5 practitioner questions.
Each focus area file includes: YAML front matter, purpose, key processes list, inputs/outputs summary, artifact connections, skill connections, and practitioner questions.

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.10.0 — Phase C2 and C3 marked COMPLETE; Phase C4 (40 process records) opened.

---

---

## [2.9.0] — 2026-05-31

### Added — Phase C1: Reference Principles Layer (COMPLETE)
- `reference/principles/00-index.md` — Full principles index: 12 principles, §3.N references, interdependency map, artifact coverage summary (18 artifacts), usage guidance for practitioners/AI agents/auditors. SHA: 693364ac.
- `reference/principles/P01-stewardship.md` — Be a Diligent, Respectful, and Caring Steward (PMBOK8 §3.1). SHA: 2ce6cfee.
- `reference/principles/P02-team.md` — Create a Collaborative Project Team Environment (PMBOK8 §3.2). SHA: 7bd44d69.
- `reference/principles/P03-stakeholders.md` — Effectively Engage with Stakeholders (PMBOK8 §3.3). SHA: c9fe6f0d.
- `reference/principles/P04-value.md` — Focus on Value (PMBOK8 §3.4). SHA: 05699468.
- `reference/principles/P05-systems-thinking.md` — Recognize, Evaluate, and Respond to System Interactions (PMBOK8 §3.5). SHA: 69372c50.
- `reference/principles/P06-leadership.md` — Demonstrate Leadership Behaviors (PMBOK8 §3.6). SHA: e41019fe.
- `reference/principles/P07-tailoring.md` — Tailor Based on Context (PMBOK8 §3.7). SHA: 072cef9c.
- `reference/principles/P08-quality.md` — Build Quality into Processes and Deliverables (PMBOK8 §3.8). SHA: c30df61e.
- `reference/principles/P09-complexity.md` — Navigate Complexity (PMBOK8 §3.9). SHA: f90ea7ab.
- `reference/principles/P10-risk.md` — Optimize Risk Responses (PMBOK8 §3.10). SHA: 873e5a22.
- `reference/principles/P11-adaptability.md` — Embrace Adaptability and Resiliency (PMBOK8 §3.11). SHA: 2e5e678b.
- `reference/principles/P12-change.md` — Enable Change to Achieve the Envisioned Future State (PMBOK8 §3.12). SHA: d69ebaae.

Each principle file includes: YAML front matter, PMI-grounded definition, 4–6 key characteristics, relationship to other principles table (3–4 rows), artifact connections (3–4 rows), skill connections (2–3 rows), and 5 practitioner questions.

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.9.0 — Phase C1 marked COMPLETE, Phase C2 + C3 opened.

### Confirmed Closed
- **Phase C1 — Reference Principles** — all 13 files (P01–P12 + 00-index.md) committed. 2026-05-31.

## [2.8.0] — 2026-05-31

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.8.0 — merged Plan v3.0.0 (uploaded 2026-05-31). Added: Phase 3 (47 full skill content files with standard YAML structure), Phase D (shared components + validators, 11 files), Phase E (test suite, 53 files), quality standards §2 (source traceability, artifact, skill, reference, docs, commit conventions), dependency map, completion metrics (~183 files remaining), updated session order. Phase C1 (12 principles) opened in this session.

### Added — Phase C1 In Progress
- `reference/principles/` — 13 files launched (P01–P12 + 00-index.md). Grounded in PMBOK8 Standard §3.1–§3.12. (SHAs recorded when committed.)

## [2.7.0] — 2026-05-31

### Added — Phase B2 Final Templates (Batches A–D, 14 templates)

**Batch A:**
- `artifacts/extended-procurement/A11-procurement-management-plan-template.md` — 12 sections: Make-or-Buy Decisions, Procurement Items Register, Contract Type Rationale, Supplier Selection Criteria, Roles and Responsibilities, Procurement Schedule, Contract Administration Approach, Organizational Constraints, Procurement Risk Summary. SHA: 38a7583d.
- `artifacts/quality/A13-requirements-traceability-matrix-template.md` — 8 sections: RTM Control Information, Requirements Traceability Register (11-column), Requirements Status Summary, Traceability Rules, Open Traceability Issues. SHA: 2054e3a4.
- `artifacts/portfolio/A22-portfolio-interdependency-record-template.md` — 8 sections: Dependency Register, Dependency Type Reference (static legend), Shared Capacity Conflicts, Escalation Log, Portfolio Coordination Actions. SHA: d32f1ba6.
- `artifacts/pmo/A23-pmo-improvement-backlog-template.md` — 7 sections: Backlog Register (9-column), Category Reference (static legend), Backlog Summary, Governance Notes (static). SHA: cca91922.

**Batch B:**
- `artifacts/stakeholders-communications/A29-change-readiness-and-adoption-record-template.md` — 9 sections: Change Description, Stakeholder Readiness Assessment (ADKAR dimensions), Adoption Action Plan, Deployment Gate Readiness, Stakeholder Feedback Register, Adoption Metrics. SHA: 943759ee.
- `artifacts/knowledge/A30-knowledge-and-lessons-management-record-template.md` — 8 sections: Lessons Register (11-column), Category Summary, OPA Contribution Queue, PMO Improvement Inputs, Capture Rules (static). SHA: 4f0c2f42.
- `artifacts/procurement/A32-supplier-evaluation-and-award-decision-record-template.md` — 11 sections: Procurement Reference, Evaluation Criteria and Weighting, Supplier Evaluation Scores, Evaluation Narrative, Award Recommendation, Award Decision, Sole-Source Justification, Debrief Notes. SHA: 603a2dc9.
- `artifacts/extended-procurement/A33-supplier-change-claim-compliance-record-template.md` — 9 sections: Event Register, Change Order Log, Claims and Disputes Log, Compliance Findings Log, Acceptance Findings Log, Contract Closeout Checklist (static items). SHA: 03c770bf.

**Batch C:**
- `artifacts/governance/A34-information-retention-records-control-record-template.md` — 8 sections: Retention Schedule (9-column), Active Records Inventory, Archival Actions Log, Compliance Obligations, Access Control Rules (static). SHA: 5ea220b4.
- `artifacts/governance/A35-governance-decision-authority-record-template.md` — 9 sections: Governance Bodies, Decision Categories and Ownership, Authority Threshold Matrix (T1–T4 static legend), Delegated Authority Register, Governance Calendar, Escalation Log. SHA: c7ec841b.
- `artifacts/pmo/A36-pmo-value-maturity-improvement-record-template.md` — 9 sections: Service Performance Themes, Stakeholder Feedback Themes, Maturity Assessment (Initial–Optimizing scale), Improvement Actions, Service Model Decisions, Governance Notes (static). SHA: 934971d4.
- `artifacts/governance/A37-ai-data-privacy-control-record-template.md` — 9 sections: Applicability Gate, Use Case and Exposure Register (data classification + risk level), Control Requirements, Compliance Evidence Log, Exception and Escalation Register, AI Control Rules (static). SHA: e5af8b31.
- `artifacts/governance/A39-change-management-plan-template.md` — 12 sections: Change Impact Assessment, Stakeholder Readiness Assessment (ADKAR), Change Adoption Strategy, Resistance Management, Change Champions Model, Training and Capability-Building Plan, Change Communications Approach, Adoption Metrics, Transition and Sustainment Plan. SHA: 53fe24af.

**Batch D:**
- `artifacts/initiating/A01-business-case-template.md` — 11 sections: Business Need and Strategic Alignment, Options Analysis (3-row table including Do Nothing), Recommended Option, Expected Benefits and Success Criteria, Financial Summary (cost + benefit tables + NPV/ROI/Payback/IRR), Major Risks and Assumptions, Recommendation, Approvals. SHA: 1eafd4fa.

### Added — Phase B3 Artifact Examples (10 examples, Batches E–F)

All examples use the "Meridian CRM Modernization" scenario — Nexus Solutions Ltd. (fictional, anonymized), PM: Jordan Patel, Sponsor: Alex Rivera, Budget: €2,400,000, Duration: 18 months Jan 2026 – Jun 2027.

**Batch E:**
- `artifacts/initiating/A04-project-charter-example.md` — Fully completed charter: 4 SMART objectives, 5 deliverables, 6 milestones, stakeholder table, 3 risks, authority delegation. SHA: 4e2c6db3.
- `artifacts/planning-and-baselines/A06-tailoring-decision-record-example.md` — 8 tailoring decisions: hybrid delivery, lightweight change process, sprint retrospectives as lessons capture, GDPR-triggered A37 activation, etc. SHA: 7d02f536.
- `artifacts/planning-and-baselines/A08-scope-requirements-backlog-example.md` — In/out scope, 12 requirements (functional, non-functional, compliance), WBS summary, assumptions and constraints. SHA: 32588336.
- `artifacts/planning-and-baselines/A14-integrated-project-management-plan-example.md` — Subsidiary plans index (9 plans), baselines (3 approved), integrated change control summary (T1–T3), plan maintenance cadence. SHA: 08215302.

**Batch F:**
- `artifacts/planning-and-baselines/A15-schedule-baseline-example.md` — 9 milestones, 4-phase WBS summary, critical path narrative, float/buffer strategy, schedule assumptions and constraints, change history (v1.0 unchanged). SHA: 8577161f.
- `artifacts/planning-and-baselines/A16-financial-baseline-example.md` — Full €2.4M breakdown by 8 cost categories and 4 phases, 18-month PV S-curve, full EVM table at Phase 2 close (CPI 0.97, EAC €2,397k), contingency drawdown log. SHA: b1cc07f7.
- `artifacts/monitoring-and-decisions/A17-performance-reporting-record-example.md` — Monthly report Sep 2026: RAG status across 8 dimensions, complete EVM table, sprint velocity table, 3 active issues, 2 sponsor decisions required. SHA: 9d772a2b.
- `artifacts/monitoring-and-decisions/A19-risk-management-record-example.md` — 8 risks (R-001 through R-008): data migration quality, user adoption, GDPR gap, vendor performance, contractor availability, ERP integration (realized), budget overrun (realized), sponsor change (watch). SHA: 3cc08272.
- `artifacts/monitoring-and-decisions/A21-lessons-learned-record-example.md` — 8 lessons with root cause analysis, recommendations, OPA submission queue (2 approved: OPA-TEC-2026-004, OPA-GOV-2026-011), 6 action items. SHA: 53836dce.
- `artifacts/closing/A27-project-closure-record-example.md` — Draft closure plan (projected Jun 2027): 14-deliverable register, financial closure (€2,420k vs €2,400k BAC, within contingency), 6 benefits for handover, team release plan, archive instructions. SHA: 19860c10.

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.7.0 — Phase B2 marked COMPLETE (38/38), Phase B3 marked COMPLETE (10/10), scorecard and session order updated.

### Confirmed Closed
- **Phase B2 — Artifact Templates** — all 38 templates committed and verified. 2026-05-31.
- **Phase B3 — Artifact Examples** — all 10 examples committed and verified. 2026-05-31.


## [2.6.0] — 2026-05-31

### Added — Phase 1 Documentation Layer (COMPLETE)
- `docs/how-to-use-artifacts.md` — artifact vs template vs instance, [FIELD: ...] convention, 7-step lifecycle, folder map, worked example A04. SHA: 9987331c.
- `docs/changelog-guide.md` — CHANGELOG format, semantic versioning triggers, 5-step write process, commit type table. SHA: 36b5aa8f.
- `docs/faq.md` — 27 Q&A pairs across 6 groups (Repository, Skills, Artifacts, T1–T4, AI Agents, Contributing). SHA: 08b30c5c.
- `docs/how-to-use-authority-routing.md` — T1–T4 model, 4 bands with 3 examples each, ASCII routing flowchart, 6-step application, 8 common scenarios, failure modes. SHA: d7ad07a5.
- `docs/how-to-contribute.md` — contribution types, authority rule, 8-step workflow, naming conventions, quality checklist. SHA: 3d5b20bd.
- `docs/glossary.md` — 108 PMI/PMBOK8 terms, alphabetically ordered, all 4 required fields (Definition, Source, Related artifact, Related skill), includes PMOSkills synthesis terms. SHA: 9199a797.

### Added — Phase B2 Artifact Templates (Batch 3, continued)
- `artifacts/stakeholders/A02-benefits-value-measurement-record-template.md` — 7 sections including Benefits Register (B-001–B-005), Value Measurement Plan, Benefits Realization Tracking, Post-Project Handoff. SHA: c6564959.
- `artifacts/resources/A03-repository-tool-configuration-record-template.md` — 7 sections including Repository Structure, Version Control Configuration, Access Control Matrix (5 roles), Tool Integration Register, Environment Readiness Checklist (8 static items). SHA: d0808588.
- `artifacts/communications/A10-communications-management-plan-template.md` — 9 sections including Communication Item Register (8 rows), Escalation Communications, Sensitive Information Handling. SHA: 7c4744c3.
- `artifacts/monitoring-and-decisions/A18-issue-impediment-action-log-template.md` — 6 sections including 12-column active register (I-001–I-005), Escalation Register, static Operating Rules. SHA: 097212ea.
- `artifacts/monitoring-and-decisions/A20-quantitative-risk-reserve-decision-record-template.md` — 9 sections including Risk Driver Inputs, P50–P90 confidence tables, Sensitivity Analysis, Decision Tree (conditional), Reserve Recommendation and Approval. SHA: c5ce085e.
- `artifacts/closure/A24-closure-and-benefits-transition-record-template.md` — 10 sections including Deliverable Acceptance, Benefits Transition (with A02 linkage), Residual Risks, Resource Release, Financial Close, Closure Authorization. SHA: 879a191b.
- `artifacts/resources/A25-team-operating-and-responsibility-record-template.md` — 8 sections including RACI Matrix (8 deliverables × 5 roles), Authority Levels (8 static types), Team Operating Norms (9 static areas), Escalation Path. SHA: d32576c4.
- `artifacts/resources/A26-resource-capacity-acquisition-record-template.md` — 8 sections including Staffing Requirements, Shared Resource Conflict Register, Physical Resources, Acquisition Plan, Resource Release Schedule. SHA: fe478a8d.

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.6.0 — Phase 1 marked COMPLETE, B2 template inventory updated to 24 templates, session order updated.

### Confirmed Closed
- **Phase 1 — Documentation Layer** — all 9 `docs/` files committed and verified. 2026-05-31.


## [2.5.0] — 2026-05-31

### Added
- `docs/getting-started.md` — orientation guide for PMO practitioners, AI agents, and book authors. Includes repo overview, directory map, three-audience quickstart paths, skill-finding decision tree, key files index. Phase 1 doc layer.
- `docs/how-to-use-skills.md` — complete guide to reading and executing a skill file. Covers skill file anatomy (all 13 YAML fields + named sections), 10-step execution sequence, pre-condition failure handling, T1–T4 routing pointer, worked example SKL-02-01. Phase 1 doc layer.
- `docs/ai-agent-guide.md` — operating guide for AI agents and agent developers. Covers 7-step loading order, routing logic, programmatic skill execution, artifact output rules, T1–T4 escalation, failure handling, context budget management, output format rules, 3 sample prompts. Phase 1 doc layer.
- `artifacts/governance/A05-context-register-template.md` — template for A05 Context Register. Sections: Project Reference, EEFs, OPAs, Assumptions Register, Constraints Register, Lessons Learned Pointers, Review Log. 20 `[FIELD: ...]` placeholders. Phase B2 Batch 3.
- `artifacts/quality/A09-quality-management-plan-template.md` — template for A09 Quality Management Plan. Sections: Project Reference, Quality Standards and Objectives, Roles and Responsibilities, QA Activities, QC Activities, Quality Metrics, Acceptance Criteria Process, Non-Conformance Process, Continuous Improvement, Review Log. 52 `[FIELD: ...]` placeholders. Phase B2 Batch 3.

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.5.0 — Phase 1 docs status table added, B2 template inventory corrected to 16 templates, session order updated, documentation layer section added.


## [2.3.0] — 2026-05-30

### Changed
- `MASTER-PLAN-V2.md` bumped to v2.3.0 — Phase B1 marked complete, artifact list aligned to v1.0.5 vocabulary, folder assignments corrected, A38/A40/A41 consolidation notes added.

### Fixed
- Deleted duplicate `artifacts/resources/A26-Resource-Capacity-and-Acquisition-Record.md` (title-case variant, 7,069 bytes). Canonical file is `A26-resource-capacity-acquisition-record.md` per Batch-4 / v1.0.5 standard.

### Added
- `CHANGELOG.md` (this file) — satisfies Phase K2 plan requirement.
- Consolidation notes for A38, A40, A41 clarifying their absorption into A37, A36, and A24/A02 respectively.

### Confirmed Closed
- **Phase B1** — all 24 artifact definitions built and confirmed present. Folder structure expanded from plan baseline to include: `artifacts/portfolio/`, `artifacts/closure/`, `artifacts/knowledge/`, `artifacts/stakeholders-communications/`, `artifacts/team-resources/`.

---

## [2.2.0] — 2026-05-30

### Changed
- `MASTER-PLAN-V2.md` updated to v2.2.0.
- Phase A declared complete after Pack 06 (3 skills) and Pack 07 (4 skills) upgraded to v1.1.0.
- Phase B1 declared in-progress: artifact directory structure confirmed, 24 missing definitions identified, build order locked.

### Fixed
- Pack 06 and Pack 07 YAML front matter, Tests table, and Change Log applied in QA sweep.

---

## [2.1.0] — 2026-05-30

### Changed
- `MASTER-PLAN-V2.md` created at v2.1.0, superseding `NEXT-STEPS-PLAN.md` v1.0.0.
- Reconciliation table added mapping old Phase 1–4 tasks to current phase structure.

### Confirmed Closed
- Phase A QA sweep — Packs 01–05 upgraded to v1.1.0 with YAML front matter, Tests table (T01–T09), and Change Log.

---

## [1.1.0] — 2026-05-29 / 2026-05-30

### Added
- All 47 skills upgraded from v1.0.0 to v1.1.0:
  - YAML front matter added (skill_id, name, pack, version, status, source_type, authority, pmbok8_anchor, performance_domains, focus_area, primary_artifact, artifacts_updated, upstream_prerequisites, downstream_skills, file_path, tests).
  - Tests table T01–T09 with Pass Condition and Fail Condition per test.
  - Change Log section at bottom of every skill file.
- `AUTHORITY-ROUTING.md` — T1–T4 routing complete (14,543 bytes).
- `LIFECYCLE-MAP.md` — all 7 packs mapped (12,559 bytes).
- `PRINCIPLES-CROSSWALK.md` — 12 principles × domains (8,110 bytes).
- `pmi_reference_list.md` — 23 PMI references catalogued (6,819 bytes).
- `source-authority.md` — authority hierarchy documented (8,344 bytes).
- `.github/ISSUE_TEMPLATE/` — 3 templates: bug, content, improvement.
- `.github/pull_request_template.md` — full PMBOK-quality PR checklist.
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`.

### Changed
- `SKILL-REGISTRY.md` updated to 54,932 bytes covering Packs 01–07.
- `README.md` updated to v1.3.0 (Patch C).

---

## [1.0.0] — 2026-05-28 / 2026-05-29

### Added
- Repository scaffolding: `README.md`, `LICENSE`, `.gitignore`.
- Skills layer initial build — 47 skills across Packs 01–07 at v1.0.0:
  - Pack 01 — Organizational Setup (3 skills: SKL-01-01, 01-02, 01-03)
  - Pack 02 — Initiating (2 skills: SKL-02-01, 02-02)
  - Pack 03 — Planning (17 skills: SKL-03-01 through 03-17)
  - Pack 04 — Executing (9 skills: SKL-04-01 through 04-09)
  - Pack 05 — Monitoring & Controlling (9 skills: SKL-05-01 through 05-09)
  - Pack 06 — Closing (3 skills: SKL-06-01, 06-02, 06-03)
  - Pack 07 — Adaptive & Hybrid (4 skills: SKL-07-01 through 07-04)
- Artifact layer initial build — 17 artifact definitions across:
  - `artifacts/planning-and-baselines/` — A06, A08, A14, A15, A16, A19, A26, A28
  - `artifacts/monitoring-and-decisions/` — A12, A17, A18
  - `artifacts/closing/` — A21, A27
  - `artifacts/stakeholders/` — A02, A07
  - `artifacts/resources/` — A03
  - `artifacts/procurement/` — A31
- `reference/`, `shared/`, `tests/` directory structure seeded with README stubs.
- `NEXT-STEPS-PLAN.md` v1.0.0 (initial roadmap, later superseded by MASTER-PLAN-V2.md).

---

## [0.1.0] — 2026-05-28

### Added
- Repository created: [fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills).
- Initial commit with README.md, LICENSE, and .gitignore.
- Authority model established: PMBOK 8 primary, 23 PMI companion references secondary.
- Artifacts-V-1.0.5 vocabulary adopted as the canonical artifact naming and schema standard.
