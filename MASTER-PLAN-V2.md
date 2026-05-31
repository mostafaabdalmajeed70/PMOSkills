# PMOSkills Repository — Master Development Plan
**Version:** 2.9.0
**Date:** 2026-05-31
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29) and v3.0.0 (2026-05-31)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0 · `NEXT-STEPS-PLAN.md` v3.0.0

> **v2.9.0 update note (2026-05-31):** Phase C1 COMPLETE — all 13 principle files committed (P01–P12 + 00-index). Phase C2 (8 performance domain files) and Phase C3 (5 focus area files) now in progress in parallel.

---

## 0. Purpose of This Plan

This plan defines every remaining work item required to transform the PMOSkills repository from its current state into a **production-quality, PMO-grade, AI-executable skills repository** that covers the full project lifecycle according to PMI PMBOK 8th Edition and its companion references.

The plan is structured for AI agent execution. Each phase has:
- A clear **entry condition** (what must be true before starting)
- Explicit **deliverables** with file paths
- A **quality gate** that must pass before the phase is closed
- A **commit convention** for traceability

---

## 1. Current State Assessment (as of 2026-05-31)

### 1.1 Repository Structure

| Directory / File | Status | Notes |
|---|---|---|
| `README.md` | ✅ v1.3.0 | Updated Patch C |
| `SKILL-REGISTRY.md` | ✅ 54,932 bytes | Full registry — Packs 01–07 |
| `AUTHORITY-ROUTING.md` | ✅ 14,543 bytes | T1–T4 routing complete |
| `LIFECYCLE-MAP.md` | ✅ 12,559 bytes | All 7 packs mapped |
| `PRINCIPLES-CROSSWALK.md` | ✅ 8,110 bytes | 12 principles × domains |
| `pmi_reference_list.md` | ✅ 6,819 bytes | 23 references catalogued |
| `source-authority.md` | ✅ 8,344 bytes | Authority hierarchy documented |
| `CODE_OF_CONDUCT.md` | ✅ Present | Contributor Covenant 2.1 + PMI ethics |
| `CONTRIBUTING.md` | ✅ Present | Full workflow, authority rules, commit conventions |
| `SECURITY.md` | ✅ Present | Secrets, PII, AI agent security |
| `.github/ISSUE_TEMPLATE/` | ✅ Present | 3 templates: bug, content, improvement |
| `.github/pull_request_template.md` | ✅ Present | Full PMBOK-quality PR checklist |
| `MASTER-PLAN-V2.md` | ✅ v2.8.0 | This document — updated 2026-05-31 |
| `CHANGELOG.md` | ✅ Present | Updated 2026-05-31 |
| `LICENSE` | ✅ Present | |
| `.gitignore` | ✅ Present | |

### 1.2 Skills Layer

| Status | Detail |
|---|---|
| Skills scaffolded | ✅ 47 skills at v1.1.0 (Packs 01–07), YAML front matter + Tests table + Change Log present |
| Skills full content | ❌ 0/47 full content files built — **Phase 3 target** |

### 1.3 Artifact Definitions Layer — Phase B1 Complete ✅

All 39 definitions present (A01–A39, A38/A40/A41 consolidated per v1.0.5 rules).

### 1.4 Documentation Layer — Phase 1 COMPLETE ✅

| File | Status | SHA | Committed |
|---|---|---|---|
| `docs/getting-started.md` | ✅ Done | 19cab09a | 2026-05-31 |
| `docs/how-to-use-skills.md` | ✅ Done | 1b710aa9 | 2026-05-31 |
| `docs/ai-agent-guide.md` | ✅ Done | 6097fb1c | 2026-05-31 |
| `docs/how-to-use-artifacts.md` | ✅ Done | 9987331c | 2026-05-31 |
| `docs/changelog-guide.md` | ✅ Done | 36b5aa8f | 2026-05-31 |
| `docs/faq.md` | ✅ Done | 08b30c5c | 2026-05-31 |
| `docs/how-to-use-authority-routing.md` | ✅ Done | d7ad07a5 | 2026-05-31 |
| `docs/how-to-contribute.md` | ✅ Done | 3d5b20bd | 2026-05-31 |
| `docs/glossary.md` | ✅ Done | 9199a797 | 2026-05-31 |

**Phase 1 COMPLETE — 9/9 docs files committed.**

### 1.5 Artifact Templates Layer — Phase B2 COMPLETE ✅

All 38 templates committed. Full inventory:

| Artifact | Template File | SHA |
|---|---|---|
| A01 — Business Case | `artifacts/initiating/A01-business-case-template.md` | 1eafd4fa |
| A02 — Benefits and Value Measurement Record | `artifacts/stakeholders/A02-benefits-value-measurement-record-template.md` | c6564959 |
| A03 — Repository and Tool Configuration Record | `artifacts/resources/A03-repository-tool-configuration-record-template.md` | d0808588 |
| A04 — Project Charter | `artifacts/initiating/A04-project-charter-template.md` | (prior session) |
| A05 — Context Register | `artifacts/governance/A05-context-register-template.md` | b59885b9 |
| A06 — Tailoring Decision Record | `artifacts/planning-and-baselines/A06-tailoring-decision-record-template.md` | (prior session) |
| A07 — Stakeholder Register | `artifacts/stakeholders/A07-stakeholder-register-template.md` | (prior session) |
| A08 — Scope and Requirements Backlog | `artifacts/planning-and-baselines/A08-scope-requirements-backlog-template.md` | (prior session) |
| A09 — Quality Management Plan | `artifacts/quality/A09-quality-management-plan-template.md` | 590f9fbb |
| A10 — Communications Management Plan | `artifacts/communications/A10-communications-management-plan-template.md` | 7c4744c3 |
| A11 — Procurement Management Plan | `artifacts/extended-procurement/A11-procurement-management-plan-template.md` | 38a7583d |
| A12 — Change Log | `artifacts/monitoring-and-decisions/A12-change-log-template.md` | (prior session) |
| A13 — Requirements Traceability Matrix | `artifacts/quality/A13-requirements-traceability-matrix-template.md` | 2054e3a4 |
| A14 — Integrated Project Management Plan | `artifacts/planning-and-baselines/A14-integrated-project-management-plan-template.md` | (prior session) |
| A15 — Schedule Baseline | `artifacts/planning-and-baselines/A15-schedule-baseline-template.md` | (prior session) |
| A16 — Financial Baseline | `artifacts/planning-and-baselines/A16-financial-baseline-template.md` | (prior session) |
| A17 — Integrated Performance Reporting | `artifacts/monitoring-and-decisions/A17-performance-reporting-record-template.md` | (prior session) |
| A18 — Issue Impediment and Action Log | `artifacts/monitoring-and-decisions/A18-issue-impediment-action-log-template.md` | 097212ea |
| A19 — Risk Management Record | `artifacts/monitoring-and-decisions/A19-risk-management-record-template.md` | (prior session) |
| A20 — Quantitative Risk and Reserve Decision Record | `artifacts/monitoring-and-decisions/A20-quantitative-risk-reserve-decision-record-template.md` | c5ce085e |
| A21 — Lessons Learned Record | `artifacts/monitoring-and-decisions/A21-lessons-learned-record-template.md` | (prior session) |
| A22 — Portfolio Interdependency Record | `artifacts/portfolio/A22-portfolio-interdependency-record-template.md` | d32f1ba6 |
| A23 — PMO Improvement Backlog | `artifacts/pmo/A23-pmo-improvement-backlog-template.md` | cca91922 |
| A24 — Closure and Benefits Transition Record | `artifacts/closure/A24-closure-and-benefits-transition-record-template.md` | 879a191b |
| A25 — Team Operating and Responsibility Record | `artifacts/resources/A25-team-operating-and-responsibility-record-template.md` | d32576c4 |
| A26 — Resource Capacity and Acquisition Record | `artifacts/resources/A26-resource-capacity-acquisition-record-template.md` | fe478a8d |
| A27 — Project Closure Record | `artifacts/closing/A27-project-closure-record-template.md` | (prior session) |
| A28 — Communications and Reporting Record | `artifacts/planning-and-baselines/A28-communications-reporting-record-template.md` | (prior session) |
| A29 — Change Readiness and Adoption Record | `artifacts/stakeholders-communications/A29-change-readiness-and-adoption-record-template.md` | 943759ee |
| A30 — Knowledge and Lessons Management Record | `artifacts/knowledge/A30-knowledge-and-lessons-management-record-template.md` | 4f0c2f42 |
| A31 — Procurement and Supplier Management | `artifacts/procurement/A31-procurement-supplier-management-record-template.md` | (prior session) |
| A32 — Supplier Evaluation and Award Decision Record | `artifacts/procurement/A32-supplier-evaluation-and-award-decision-record-template.md` | 603a2dc9 |
| A33 — Supplier Change, Claim, and Compliance Record | `artifacts/extended-procurement/A33-supplier-change-claim-compliance-record-template.md` | 03c770bf |
| A34 — Information Retention and Records Control Record | `artifacts/governance/A34-information-retention-records-control-record-template.md` | 5ea220b4 |
| A35 — Governance and Decision Authority Record | `artifacts/governance/A35-governance-decision-authority-record-template.md` | c7ec841b |
| A36 — PMO Value, Maturity, and Improvement Record | `artifacts/pmo/A36-pmo-value-maturity-improvement-record-template.md` | 934971d4 |
| A37 — AI, Data, and Privacy Control Record | `artifacts/governance/A37-ai-data-privacy-control-record-template.md` | e5af8b31 |
| A39 — Change Management Plan | `artifacts/governance/A39-change-management-plan-template.md` | 53fe24af |

**Phase B2 COMPLETE — 38/38 templates committed.**

### 1.6 Artifact Examples Layer — Phase B3 COMPLETE ✅

All 10 examples use the "Meridian CRM Modernization" scenario (Nexus Solutions Ltd., fictional).

| Artifact | Example File | SHA |
|---|---|---|
| A04 — Project Charter | `artifacts/initiating/A04-project-charter-example.md` | 4e2c6db3 |
| A06 — Tailoring Decision Record | `artifacts/planning-and-baselines/A06-tailoring-decision-record-example.md` | 7d02f536 |
| A08 — Scope and Requirements Backlog | `artifacts/planning-and-baselines/A08-scope-requirements-backlog-example.md` | 32588336 |
| A14 — Integrated Project Management Plan | `artifacts/planning-and-baselines/A14-integrated-project-management-plan-example.md` | 08215302 |
| A15 — Schedule Baseline | `artifacts/planning-and-baselines/A15-schedule-baseline-example.md` | 8577161f |
| A16 — Financial Baseline | `artifacts/planning-and-baselines/A16-financial-baseline-example.md` | b1cc07f7 |
| A17 — Performance Reporting Record | `artifacts/monitoring-and-decisions/A17-performance-reporting-record-example.md` | 9d772a2b |
| A19 — Risk Management Record | `artifacts/monitoring-and-decisions/A19-risk-management-record-example.md` | 3cc08272 |
| A21 — Lessons Learned Record | `artifacts/monitoring-and-decisions/A21-lessons-learned-record-example.md` | 53836dce |
| A27 — Project Closure Record | `artifacts/closing/A27-project-closure-record-example.md` | 19860c10 |

**Phase B3 COMPLETE — 10/10 examples committed.**

### 1.7 Reference Layer — Phase C In Progress 🟡

| Sub-phase | Target | Status |
|---|---|---|
| C1 — 12 Principle files | `reference/principles/P01–P12.md` + `00-index.md` | ✅ COMPLETE — 2026-05-31 |
| C2 — 8 Performance Domain files | `reference/performance-domains/PD01–PD08.md` + `00-index.md` | 🟡 In progress |
| C3 — 5 Focus Area files | `reference/focus-areas/FA01–FA05.md` | 🟡 In progress |
| C4 — 40 Process records | `reference/processes/` | ❌ Not started |
| C5 — I/O and T&T registries | `reference/` | ❌ Not started |
| C6 — Appendices X2–X5 | `reference/appendices/` | ❌ Not started |
| C7 — Reference GLOSSARY | `reference/GLOSSARY.md` | ❌ Not started |

### 1.8 Shared Layer — Phase D Seeded 🟡

| File | Status |
|---|---|
| `shared/README.md` | ✅ Seeded |
| `shared/validators/artifact-waste-test.md` | ❌ Not built |
| `shared/validators/skill-quality-check.md` | ❌ Not built |
| `shared/validators/baseline-integrity-check.md` | ❌ Not built |
| `shared/components/field-blocks.md` | ❌ Not built |
| `shared/components/section-patterns.md` | ❌ Not built |
| `shared/components/status-indicators.md` | ❌ Not built |
| `shared/routing/t1-t4-routing-logic.md` | ❌ Not built |
| `shared/routing/escalation-matrix.md` | ❌ Not built |
| `shared/checklists/phase-entry-checklist.md` | ❌ Not built |
| `shared/checklists/phase-exit-checklist.md` | ❌ Not built |
| `shared/checklists/artifact-readiness-checklist.md` | ❌ Not built |

### 1.9 Tests Layer — Phase E Seeded 🟡

| File | Status |
|---|---|
| `tests/README.md` | ✅ Seeded |
| `tests/skill-tests/` (47 files) | ❌ Not built |
| `tests/integration-tests/IT-01 through IT-06` | ❌ Not built |

---

## 2. Quality Standards (from Plan v3.0.0 §2)

### 2.1 Source Traceability Standard
- Every claim, process, artifact, or principle reference must cite a specific PMI source using the format: `*Authority: [Source] — [Section/Chapter/Page]*`
- Allowed sources in order of authority:
  1. PMBOK8 Guide (sections cited as `§X.X.X`)
  2. PMBOK8 Standard (principles cited by principle name)
  3. PMI companion references (cited by short code: WBS-3E, PSS-3E, etc.)
  4. Synthesis (explicitly labeled)
  5. Organization-defined (explicitly labeled)
- No unsourced claims about PMI standards or processes.

### 2.2 Artifact Quality Standard
- Every artifact definition must include: `artifact_id`, `artifact_name`, `version`, `status`, `authority`, purpose, inputs, outputs, quality criteria, related artifacts, waste test, migration note.
- Every artifact template must include: `[FIELD: description]` placeholders — no blank fields, usage note at top, parent definition reference in YAML front matter.

### 2.3 Skill Quality Standard (Phase 3)
Every full skill file must include:
- Skill ID, name, pack, version, status
- Purpose (one paragraph)
- Scope — includes AND excludes (explicit)
- Pre-conditions (numbered)
- Step-by-step instructions (numbered, precise, executable)
- Inputs table (source artifact, required?)
- Outputs table (target artifact, quality criterion)
- Authority and Governance (T1–T4 threshold, approver, escalation trigger)
- Constraints (regulatory, process, authority)
- Failure Cases (numbered)
- Quality Checks (numbered pass criteria)
- Test Cases (minimum 2: happy path + failure path)
- PMBOK8 anchor (specific section)

### 2.4 Reference File Standard (Phase C)
Every `reference/` file must include:
- Type declaration (Principle / Performance Domain / Focus Area)
- PMBOK8 source section (specific — no vague references)
- PMI definition (cited, not paraphrased without attribution)
- Key characteristics (bulleted, PMI-sourced)
- Relationship to other principles/domains (cross-reference table)
- Artifact connections (which artifacts this governs)
- Skill connections (which skills implement this)
- Practitioner questions (3–5 grounded in the principle/domain)

### 2.5 Documentation Quality Standard
Every `docs/` file must include: `## Purpose`, `## Audience`, `## Prerequisites`, numbered instructions (for procedural files), cross-references to related skills and artifacts, `## Related Files` table at bottom.

### 2.6 Commit Convention
```
type(scope): short description

Body: what changed and why.
Files: list of files added/modified/deleted.
Phase: which plan phase this commit belongs to.
```
Types: `feat` · `fix` · `docs` · `chore` · `refactor` · `test`
Scopes: `skills` · `artifacts` · `docs` · `reference` · `shared` · `tests` · `root`

---

## 3. Repository Target Structure

```
PMOSkills/
├── README.md
├── SKILL-REGISTRY.md
├── AUTHORITY-ROUTING.md
├── LIFECYCLE-MAP.md
├── PRINCIPLES-CROSSWALK.md
├── MASTER-PLAN-V2.md
├── CHANGELOG.md
├── source-authority.md
├── pmi_reference_list.md
│
├── docs/                              ← PHASE 1 ✅ COMPLETE
│   ├── img/pmoskills.jpg
│   ├── getting-started.md
│   ├── how-to-use-skills.md
│   ├── how-to-use-artifacts.md
│   ├── how-to-use-authority-routing.md
│   ├── how-to-contribute.md
│   ├── glossary.md
│   ├── faq.md
│   ├── ai-agent-guide.md
│   └── changelog-guide.md
│
├── artifacts/                         ← PHASES B1/B2/B3 ✅ COMPLETE
│   └── [39 definitions + 38 templates + 10 examples]
│
├── skills/                            ← PHASE 3 TARGET
│   ├── 01-organizational-setup/       (3 skills)
│   ├── 02-initiating/                 (2 skills)
│   ├── 03-planning/                   (17 skills)
│   ├── 04-executing/                  (9 skills)
│   ├── 05-monitoring-controlling/     (9 skills)
│   ├── 06-closing/                    (3 skills)
│   └── 07-adaptive-hybrid/            (4 skills)
│
├── reference/                         ← PHASE C TARGET (in progress)
│   ├── principles/
│   │   ├── 00-index.md
│   │   ├── P01-stewardship.md
│   │   ├── P02-team.md
│   │   ├── P03-stakeholders.md
│   │   ├── P04-value.md
│   │   ├── P05-systems-thinking.md
│   │   ├── P06-leadership.md
│   │   ├── P07-tailoring.md
│   │   ├── P08-quality.md
│   │   ├── P09-complexity.md
│   │   ├── P10-risk.md
│   │   ├── P11-adaptability.md
│   │   └── P12-change.md
│   ├── performance-domains/
│   │   ├── 00-index.md
│   │   ├── PD01-stakeholders.md
│   │   ├── PD02-team.md
│   │   ├── PD03-development-approach.md
│   │   ├── PD04-planning.md
│   │   ├── PD05-project-work.md
│   │   ├── PD06-delivery.md
│   │   ├── PD07-measurement.md
│   │   └── PD08-uncertainty.md
│   ├── focus-areas/
│   │   ├── FA01-initiating.md
│   │   ├── FA02-planning.md
│   │   ├── FA03-executing.md
│   │   ├── FA04-monitoring-controlling.md
│   │   └── FA05-closing.md
│   ├── processes/
│   │   └── [40 process files]
│   └── appendices/
│       ├── X2-pmo.md
│       ├── X3-ai.md
│       ├── X4-procurement.md
│       └── X5-evolution.md
│
├── shared/                            ← PHASE D TARGET
│   ├── components/
│   │   ├── field-blocks.md
│   │   ├── section-patterns.md
│   │   └── status-indicators.md
│   ├── validators/
│   │   ├── artifact-waste-test.md
│   │   ├── skill-quality-check.md
│   │   └── baseline-integrity-check.md
│   ├── routing/
│   │   ├── t1-t4-routing-logic.md
│   │   └── escalation-matrix.md
│   └── checklists/
│       ├── phase-entry-checklist.md
│       ├── phase-exit-checklist.md
│       └── artifact-readiness-checklist.md
│
└── tests/                             ← PHASE E TARGET
    ├── skill-tests/
    │   └── [47 test files — one per skill]
    └── integration-tests/
        ├── IT-01-setup-to-initiate.md
        ├── IT-02-initiate-to-plan.md
        ├── IT-03-plan-to-execute.md
        ├── IT-04-execute-to-monitor.md
        ├── IT-05-monitor-to-close.md
        └── IT-06-full-lifecycle.md
```

---

## 4. Master Build Roadmap

### Phase A — Stabilize and QA ✅ COMPLETE (2026-05-30)

### Phase 1 — Documentation Layer (`docs/`) ✅ COMPLETE (2026-05-31)

### Phase B — Artifact Templates and Examples ✅ COMPLETE (2026-05-31)
- B1: Definitions (39 total) ✅
- B2: Templates (38 total) ✅
- B3: Examples (10 total) ✅

### Phase C — Reference Layer 🟡 IN PROGRESS

**Entry condition:** Phase B complete ✅  
**Exit quality gate:** All 12 principle files, 8 performance domain files, 5 focus area files, 40 process records, and 4 appendix files complete. Each sourced to a specific PMBOK 8 section.

| Sub-phase | Deliverables | Count | Status |
|---|---|---|---|
| C1 | `reference/principles/P01–P12.md` + `00-index.md` | 13 files | 🟡 In progress |
| C2 | `reference/performance-domains/PD01–PD08.md` + `00-index.md` | 9 files | ❌ |
| C3 | `reference/focus-areas/FA01–FA05.md` | 5 files | ❌ |
| C4 | `reference/processes/` (40 process files) | 40 files | ❌ |
| C5 | I/O and T&T registries | TBD | ❌ |
| C6 | `reference/appendices/X2–X5.md` | 4 files | ❌ |
| C7 | `reference/GLOSSARY.md` | 1 file | ❌ |

**Reference file standard structure** (from Plan v3.0.0 §4):
```markdown
# [Reference Item Name]
**Type:** Principle / Performance Domain / Focus Area
**PMBOK8 Source:** [Chapter and section]
**Version:** 1.0.0

## Definition
[PMI definition — cited from PMBOK8 Lexicon or chapter]

## Key Characteristics
[Bullet list — directly from PMBOK 8 source]

## Relationship to Other Principles/Domains
[Cross-reference table]

## Artifact Connections
[Which artifacts this principle/domain governs or influences]

## Skill Connections
[Which skills implement or apply this principle/domain]

## Questions to Ask in Practice
[3–5 practitioner-level questions grounded in this principle/domain]

*Authority: PMBOK8 — [Section] · Source type: PMI-derived*
```

### Phase 3 — Build Full Skill Content (47 files) ❌ NOT STARTED

**Entry condition:** Phase C complete (reference files cited by skills)  
**Exit quality gate:** All 47 skill files pass §2.3 Skill Quality Standard. Each cross-checked against its PMBOK 8 anchor section.

**Skill build priority order:**

| Priority | Skills | Reason |
|---|---|---|
| 1 | SKL-01-01, SKL-01-02, SKL-01-03 | Foundation — organizational setup gates all else |
| 2 | SKL-02-01, SKL-02-02 | Initiating — Charter and Stakeholder identification gate all planning |
| 3 | SKL-03-01 through SKL-03-05 | Core planning (Tailoring, Scope, WBS, Requirements) |
| 4 | SKL-03-06 through SKL-03-17 | Remaining planning skills |
| 5 | SKL-04-01 through SKL-04-09 | Executing skills |
| 6 | SKL-05-01 through SKL-05-09 | Monitoring & Controlling |
| 7 | SKL-06-01 through SKL-06-03 | Closing |
| 8 | SKL-07-01 through SKL-07-04 | Adaptive & Hybrid |

**Full skill file structure** (every skill must conform):
```markdown
---
skill_id: SKL-NN-NN
skill_name: [Full skill name]
pack: [Pack number and name]
version: "1.0.0"
status: Active
pmbok8_anchor: "[Section reference]"
focus_area: [Initiating / Planning / Executing / M&C / Closing / Adaptive]
performance_domains: [List]
artifacts_produced: [List of A-IDs]
artifacts_consumed: [List of A-IDs]
authority_threshold: [T1/T2/T3/T4]
---

# SKL-NN-NN — [Skill Name]

## Purpose
## Scope
## Pre-conditions
## Instructions
## Inputs
## Outputs
## Authority and Governance
## Constraints
## Failure Cases
## Quality Checks
## Test Cases
## PMBOK8 Anchor
```

### Phase D — Shared Components and Validators ❌ NOT STARTED

**Entry condition:** Phase 3 complete  
**Exit quality gate:** All validators produce deterministic pass/fail when applied to any artifact or skill file.

| File | Description |
|---|---|
| `shared/validators/artifact-waste-test.md` | Universal 10-question waste test — Pass = needed, Fail = redundant |
| `shared/validators/skill-quality-check.md` | 15-point checklist for skill file completeness |
| `shared/validators/baseline-integrity-check.md` | Cross-artifact consistency check (A15 ↔ A14 ↔ A16) |
| `shared/components/field-blocks.md` | Reusable field patterns with copy-paste Markdown |
| `shared/components/section-patterns.md` | Common section structures |
| `shared/components/status-indicators.md` | Standard status/RAG values |
| `shared/routing/t1-t4-routing-logic.md` | Machine-readable routing rules |
| `shared/routing/escalation-matrix.md` | Full escalation decision matrix |
| `shared/checklists/phase-entry-checklist.md` | Entry criteria per lifecycle phase |
| `shared/checklists/phase-exit-checklist.md` | Exit criteria per lifecycle phase |
| `shared/checklists/artifact-readiness-checklist.md` | Artifact completeness checklist |

### Phase E — Test Suite ❌ NOT STARTED

**Entry condition:** Phase 3 and Phase D complete  
**Exit quality gate:** Every skill has at least 2 test cases. All 6 integration tests pass end-to-end.

**Test file standard structure:**
```markdown
# Test: [Skill ID] — [Skill Name]
**Skill:** SKL-NN-NN
**Test version:** 1.0.0

## Test 1 — Happy Path
**Input:** [Complete, valid input]
**Steps:** [Which skill steps are exercised]
**Expected output:** [Expected artifact output]
**Pass criterion:** [Measurable condition]

## Test 2 — Missing Input Failure
**Input:** [Input with one required element missing]
**Expected behavior:** [Skill halts at pre-condition check]
**Pass criterion:** [Failure mode detected and reported]

## Test 3 — Authority Threshold Edge Case (if applicable)
**Input:** [Decision at a T-tier boundary]
**Expected behavior:** [Escalation to correct authority]
```

Deliverables: 47 skill test files + 6 integration tests (IT-01 through IT-06 covering setup-to-close lifecycle).

### Phase F — Extended Packs (PMO + AI) ❌ NOT STARTED

F1: Pack PMO (6 skills) · F2: Pack AI (4 skills)

### Phase G — MCP Server Design ❌ NOT STARTED

Tool schemas, resource schemas, prompt contracts, endpoint descriptions, authentication notes, error cases, example requests/responses.

### Phase H — AI Agent Design ❌ NOT STARTED

Role definitions, operating instructions, tool policy, memory policy, workflow, safety rules, escalation logic, evaluation criteria, sample prompts.

### Phase I — Book Authoring Track ❌ NOT STARTED

### Phase 7 (Quality Audit) — Ongoing After Each Phase

For each file produced, the AI agent must verify:
- [ ] YAML front matter complete and valid
- [ ] All `[FIELD: ...]` placeholders present in templates (none pre-filled)
- [ ] All cross-references resolve to files that exist
- [ ] Every PMI citation includes a specific section reference (no vague "PMBOK 8" citations)
- [ ] Waste test passes (artifact is not redundant)
- [ ] Commit message follows convention (§2.6)
- [ ] File is in the correct directory per target structure (§3)
- [ ] No content copied verbatim from PMI copyrighted text

### Phase K — Quality, CI/CD, Release (ongoing)

K2 ✅ Done (CHANGELOG) · K1/K3 pending

---

## 5. Dependency Map

```
Phase 1 (docs/)           ✅ COMPLETE
Phase B (artifacts)       ✅ COMPLETE
Phase C (reference)       🟡 IN PROGRESS — no dependency on Phase 3
Phase 3 (skill content)   ← Requires Phase B complete ✅ + Phase C complete
Phase D (shared)          ← Requires Phase 3 complete
Phase E (tests)           ← Requires Phase 3 + Phase D complete
Phase 7 (quality audit)   ← Runs after EACH phase — continuous
```

**Parallelizable now:** Phase C sub-phases (C1–C3 can run in parallel).

---

## 6. Execution Scorecard

| Phase | Deliverable | Target | Status |
|---|---|---|---|
| A | QA all 47 skills → v1.1.0 | 47 skills | ✅ Complete — 2026-05-30 |
| B1 | Artifact definitions | 39 | ✅ Complete — 2026-05-30 |
| B2 | Artifact templates | 38 | ✅ Complete — 2026-05-31 |
| B3 | Artifact examples | 10 | ✅ Complete — 2026-05-31 |
| Phase 1 | docs/ documentation | 9 | ✅ Complete — 2026-05-31 |
| C1 | Reference: 12 principles | 13 files | ✅ Complete — 2026-05-31 |
| C2 | Reference: 8 performance domains | 9 files | 🟡 In progress |
| C3 | Reference: 5 focus areas | 5 files | 🟡 In progress |
| C4 | Reference: 40 processes | 40 files | ❌ |
| C5–C7 | Reference: registries, appendices, glossary | TBD | ❌ |
| Phase 3 | 47 full skill content files | 47 | ❌ |
| Phase D | Shared components + validators | 11 | ❌ |
| Phase E | Test suite | 53 | ❌ |
| Phase F | Extended packs PMO + AI | 10 skills | ❌ |
| Phase G | MCP Server design | TBD | ❌ |
| Phase H | AI Agent definitions | TBD | ❌ |
| Phase I | Book authoring | TBD | ❌ |
| **Total files remaining** | — | **~171** | — |

**Completion metrics (from Plan v3.0.0 §8, updated):**

| Metric | Current | Target |
|---|---|---|
| Artifact definition files | 39 | 39 ✅ |
| Artifact template files | 38 | 38 ✅ |
| Artifact example files | 10 | 10 ✅ |
| docs/ help files | 9 | 9 ✅ |
| Skill content files (full) | 0 | 47 |
| `reference/` files | 0 | ~72 (13P + 9PD + 5FA + 40proc + 4app + 1glossary) |
| `shared/` files | 0 | 11 |
| `tests/` files | 0 | 53 (47 skill + 6 integration) |
| **Total files remaining** | — | **~183** |

---

## 7. Recommended Session Order

1. **Current session:** Phase C1 — 12 principle files + index (13 files, `reference/principles/`)
2. **Next session:** Phase C2 — 8 performance domain files + index (9 files)
3. **Session +2:** Phase C3 — 5 focus area files; Phase C6 — 4 appendix files (run parallel)
4. **Session +3:** Phase C4 — Process records batch 1 (10 files)
5. **Session +4:** Phase C4 — Process records batch 2 (10 files)
6. **Session +5:** Phase C4 — Process records batch 3 (10 files) + batch 4 (10 files)
7. **Session +6:** Phase C5 + C7 — I/O registries + reference GLOSSARY
8. **Session +7:** Phase 3 — Skill content Pack 01 + Pack 02 (5 skills)
9. **Session +8:** Phase 3 — Skill content Pack 03 batch 1 (SKL-03-01 through 03-09)
10. **Sessions +9–12:** Phase 3 — Remaining 33 skill files
11. **Sessions +13–14:** Phase D (shared) + Phase E (tests)
12. **Sessions beyond:** Phase F, G, H, I

---

## 8. AI Agent Operating Rules (Plan v3.0.0 §10 — preserved verbatim)

1. **Never modify a canonical artifact definition file without bumping its version.**
2. **Never create a skill file that references an artifact that does not yet exist** — create the artifact first.
3. **Always check `MASTER-PLAN-V2.md` before starting a session** to avoid duplicating completed work.
4. **Always commit after each file** — not in large batches — to maintain traceability.
5. **Treat every `[FIELD: ...]` placeholder as sacred** — they must appear in templates exactly as specified, never pre-filled with sample data.
6. **Never cite PMBOK 8 without a section number.**
7. **Apply the waste test to every artifact before committing it** — if it fails, revise or consolidate.
8. **When in doubt about scope, authority, or terminology, defer to PMBOK8 as primary source.**
9. **Update MASTER-PLAN-V2.md and CHANGELOG.md at the end of every session — no exceptions.**
10. **The quality audit checklist (§4 Phase 7) applies to every file, every session.**

---

## 9. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan |
| 2.0.0 | 2026-05-30 | Full rebuild |
| 2.1.0 | 2026-05-30 | Skills inventory corrected |
| 2.2.0 | 2026-05-30 | Phase A complete |
| 2.3.0 | 2026-05-30 | Phase B1 complete |
| 2.4.0 | 2026-05-30 | Duplicates deleted · B2 progress table added |
| 2.5.0 | 2026-05-31 | Phase 1 opened · B2 Batch 3 started |
| 2.6.0 | 2026-05-31 | Phase 1 COMPLETE · B2 expanded to 24 templates |
| 2.7.0 | 2026-05-31 | Phase B2 COMPLETE (38/38) · Phase B3 COMPLETE (10/10) |
| 2.8.0 | 2026-05-31 | Merged Plan v3.0.0 — added Phase 3 (skills), Phase D (shared), Phase E (tests), quality standards §2, dependency map, completion metrics, session order; Phase C1 in progress |
| 2.9.0 | 2026-05-31 | Phase C1 COMPLETE (13 files: P01–P12 + index) · Phase C2 + C3 in progress |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-31 · Version 2.9.0*
