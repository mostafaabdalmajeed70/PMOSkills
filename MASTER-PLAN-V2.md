# PMOSkills Repository — Master Development Plan
**Version:** 2.2.0
**Date:** 2026-05-30
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

> **v2.2.0 update note:** Phase A fully complete — all 47 skills (Packs 01–07) upgraded to v1.1.0 with YAML front matter, Tests table (T01–T09), and Change Log in a single QA sweep. Pack 06 (3 skills) and Pack 07 (4 skills) fixed in session 2026-05-30. Phase B1 now in progress — artifact directory structure confirmed, 24 missing definitions identified and build order locked.

---

## 1. Current State Assessment (as of 2026-05-30 18:00 EEST)

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
| `MASTER-PLAN-V2.md` | ✅ v2.2.0 | This document — updated 2026-05-30 |
| `LICENSE` | ✅ Present | |
| `.gitignore` | ✅ Present | |

### 1.2 Skills Layer — All 47 Complete and QA'd ✅

> All 47 skills confirmed present and upgraded to v1.1.0 on 2026-05-30.
> Every file now contains: YAML front matter · Tests table (T01–T09) · Change Log.

| Pack | Folder | Skills | Count | Version | Status |
|---|---|---|---|---|---|
| Pack 01 — Org Setup | `skills/01-organizational-setup/` | SKL-01-01, 01-02, 01-03 | 3/3 | v1.1.0 | ✅ Complete + QA'd |
| Pack 02 — Initiating | `skills/02-initiating/` | SKL-02-01, 02-02 | 2/2 | v1.1.0 | ✅ Complete + QA'd |
| Pack 03 — Planning | `skills/03-planning/` | SKL-03-01 through 03-17 | 17/17 | v1.1.0 | ✅ Complete + QA'd |
| Pack 04 — Executing | `skills/04-executing/` | SKL-04-01 through 04-09 | 9/9 | v1.1.0 | ✅ Complete + QA'd |
| Pack 05 — M&C | `skills/05-monitoring-controlling/` | SKL-05-01 through 05-09 | 9/9 | v1.1.0 | ✅ Complete + QA'd |
| Pack 06 — Closing | `skills/06-closing/` | SKL-06-01, 06-02, 06-03 | 3/3 | v1.1.0 | ✅ Complete + QA'd |
| Pack 07 — Adaptive & Hybrid | `skills/07-adaptive-hybrid/` | SKL-07-01 through 07-04 | 4/4 | v1.1.0 | ✅ Complete + QA'd |
| Pack PMO | `skills/08-pmo/` *(proposed)* | None | 0/6 | — | ❌ Not started |
| Pack AI | `skills/09-ai/` *(proposed)* | None | 0/4 | — | ❌ Not started |
| **TOTAL (core packs 01–07)** | | **All 47 confirmed** | **47/47** | **v1.1.0** | ✅ **Skills layer complete + QA'd** |

**QA standard applied to all 47 skills (Phase A):**
- [x] YAML front matter — `skill_id`, `name`, `pack`, `version`, `status`, `source_type`, `authority`, `pmbok8_anchor`, `performance_domains`, `focus_area`, `primary_artifact`, `artifacts_updated`, `upstream_prerequisites`, `downstream_skills`, `file_path`, `tests`
- [x] Tests table — T01–T09 with Pass Condition and Fail Condition per test
- [x] Change Log — version history at bottom of every file
- [x] Version bumped from 1.0.0 → 1.1.0

### 1.3 Artifact Definitions Layer

| Subfolder | Files Present | Target | Status |
|---|---|---|---|
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A19, A26, A28 — 8 files | 8 definitions | ✅ Present |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18 — 3 files | 3 definitions | ✅ Present |
| `artifacts/closing/` | A21, A27 — 2 files | 2 definitions | ✅ Present |
| `artifacts/stakeholders/` | A02, A07 — 2 files | 2 definitions | ✅ Present |
| `artifacts/resources/` | A03 — 1 file | 1 definition | ✅ Present |
| `artifacts/procurement/` | A31 — 1 file | 1 definition | ✅ Present |
| `artifacts/initiating/` | ❌ 0 files | A01, A04 | ❌ Not yet written |
| `artifacts/governance/` | ❌ 0 files | A05, A36, A39 | ❌ Not yet written |
| `artifacts/quality/` | ❌ 0 files | A09, A13 | ❌ Not yet written |
| `artifacts/communications/` | ❌ 0 files | A10, A29 | ❌ Not yet written |
| `artifacts/extended-resources/` | ❌ 0 files | A20, A22, A25 | ❌ Not yet written |
| `artifacts/extended-procurement/` | ❌ 0 files | A11, A23, A24, A32 | ❌ Not yet written |
| `artifacts/extended-closing/` | ❌ 0 files | A30, A41 | ❌ Not yet written |
| `artifacts/pmo/` | ❌ 0 files | A33–A36, A40 | ❌ Not yet written |
| `artifacts/ai/` | ❌ 0 files | A37–A38 | ❌ Not yet written |
| **Templates layer** | None | 17+ template files | ❌ 0 done |
| **Examples layer** | None | 10+ example files | ❌ 0 done |
| **Missing artifact definitions** | 0 of 24 written | A01, A04, A05, A09–A11, A13, A20, A22–A25, A29–A30, A32–A41 | 🟡 In Progress — B1 active |

### 1.4 Reference / Shared / Tests Layer

| Directory | Status | Content Present |
|---|---|---|
| `reference/` | 🟡 Seeded | `README.md` + `principles/index.md` — structure defined, no content files |
| `shared/` | 🟡 Seeded | `README.md` — structure defined, no content files |
| `tests/` | 🟡 Seeded | `README.md` — structure defined, no content files |

### 1.5 Community / Governance Layer

| Area | Status |
|---|---|
| GitHub Community Standards | ✅ All 5 standards present — Code of Conduct, Contributing, Security, Issue Templates (×3), PR Template |
| Branch protection | ⚠️ Not yet verified — confirm `main` protection rules are enabled |
| CHANGELOG.md | ❌ Not yet created |
| GitHub Discussions | 🔵 Optional |
| GitHub Pages / Wiki | 🔵 Optional — future documentation site |

---

## 2. Reconciliation with Old Plan (v1.0.0, 2026-05-29)

| Old Phase | What It Called For | Current Status |
|---|---|---|
| Phase 1 — Repair Pack 04 naming collision | Fix `SKL-04-01-implement-risk-responses.md` | ✅ No collision — Pack 04 is clean |
| Phase 1 — Verify Pack 04 quality | Check all 9 files against template | ✅ Done — Pack 04 upgraded to v1.1.0 |
| Phase 2.1 — Complete Pack 05 (8 skills) | Write SKL-05-02 through 05-09 | ✅ All 9 Pack 05 skills present + QA'd |
| Phase 2.2 — Create Pack 06 (3 skills) | Write SKL-06-01 through 06-03 | ✅ All 3 Pack 06 skills present + QA'd |
| Phase 2.3 — Create Pack 07 Adaptive (4 skills) | Write SKL-07-01 through 07-04 | ✅ All 4 Pack 07 skills present + QA'd |
| Phase 2.4 — Confirm Pack 01 Pre-Sign | Verify `skills/01-pre-sign/` | ✅ Present as `01-organizational-setup/` — 3 skills confirmed |
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definitions, templates, examples | 🟡 17 definitions done · 24 missing · B1 in progress |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ✅ Phase A complete |

**New items added in v2.0.0 not in old plan:**
- Community standards layer ✅ Done
- Book authoring track (Phase I)
- MCP server design and build track (Phase G)
- AI agent design track (Phase H)
- GitHub Actions / CI validation (Phase K)
- GLOSSARY.md / PMI Lexicon file
- Artifact templates and examples (explicit plan)
- CHANGELOG.md
- Branch protection verification

---

## 3. Open Issues — Immediate Actions Required

### 3.1 ✅ RESOLVED — Phase A QA Complete

All 47 skills upgraded to v1.1.0 on 2026-05-30. QA standard applied across all packs:
- Pack 04 (9 skills) — v1.1.0 ✅
- Pack 05 (9 skills) — v1.1.0 ✅
- Pack 06 (3 skills) — v1.1.0 ✅
- Pack 07 (4 skills) — v1.1.0 ✅

Commit refs:
- Pack 06 + 07 QA: `b785ee6` (2026-05-30)

### 3.2 🟡 IN PROGRESS — Phase B1: Missing Artifact Definitions

24 artifact definitions to be built. Build order (by priority):

| Priority | Artifact | Name | Folder | Status |
|---|---|---|---|---|
| 🔴 1 | A04 | Project Charter | `artifacts/initiating/` | ❌ Not built |
| 🔴 2 | A01 | Business Case | `artifacts/initiating/` | ❌ Not built |
| 🔴 3 | A05 | Context Register (EEF/OPA) | `artifacts/governance/` | ❌ Not built |
| 🟠 4 | A09 | Quality Management Plan | `artifacts/quality/` | ❌ Not built |
| 🟠 5 | A10 | Communications Management Plan | `artifacts/communications/` | ❌ Not built |
| 🟠 6 | A11 | Procurement Management Plan | `artifacts/extended-procurement/` | ❌ Not built |
| 🟠 7 | A13 | Requirements Traceability Matrix | `artifacts/quality/` | ❌ Not built |
| 🟠 8 | A20 | Team Charter | `artifacts/extended-resources/` | ❌ Not built |
| 🟠 9 | A39 | Change Management Plan | `artifacts/governance/` | ❌ Not built |
| 🟡 10 | A25 | Resource Management Plan / RACI | `artifacts/extended-resources/` | ❌ Not built |
| 🟡 11 | A22 | Resource Acquisition Record | `artifacts/extended-resources/` | ❌ Not built |
| 🟡 12 | A29 | Meeting Records | `artifacts/communications/` | ❌ Not built |
| 🟡 13 | A30 | Project Closure Report | `artifacts/extended-closing/` | ❌ Not built |
| 🟡 14 | A41 | Benefits Realization Report | `artifacts/extended-closing/` | ❌ Not built |
| 🟡 15 | A23 | Vendor Bid Documents | `artifacts/extended-procurement/` | ❌ Not built |
| 🟡 16 | A24 | Source Selection Criteria | `artifacts/extended-procurement/` | ❌ Not built |
| 🟡 17 | A32 | Procurement SOW | `artifacts/extended-procurement/` | ❌ Not built |
| 🔵 18 | A33 | PMO Charter | `artifacts/pmo/` | ❌ Not built |
| 🔵 19 | A34 | Portfolio Register | `artifacts/pmo/` | ❌ Not built |
| 🔵 20 | A35 | Program Benefits Plan | `artifacts/pmo/` | ❌ Not built |
| 🔵 21 | A36 | Governance Framework Record | `artifacts/pmo/` | ❌ Not built |
| 🔵 22 | A37 | AI Project Readiness Assessment | `artifacts/ai/` | ❌ Not built |
| 🔵 23 | A38 | AI Risk Register | `artifacts/ai/` | ❌ Not built |
| 🔵 24 | A40 | OPM Maturity Assessment | `artifacts/pmo/` | ❌ Not built |

### 3.3 ⚠️ Branch Protection

Verify `main` branch protection rules:
- Require pull request before merging
- Require at least 1 review
- Disallow force pushes
- Disallow branch deletion

### 3.4 ❌ CHANGELOG.md Missing

Create `CHANGELOG.md` at root following Keep a Changelog format before next content release.

### 3.5 ⚠️ SKILL-REGISTRY.md Sync

Verify `SKILL-REGISTRY.md` accurately reflects all 47 skills at v1.1.0 with correct YAML fields, artifact references, and status fields.

---

## 4. Master Build Roadmap — Phases and Tracks

### Phase A — Stabilize and QA
**Priority:** ✅ COMPLETE · **Completed:** 2026-05-30

| Task | Action | Output | Status |
|---|---|---|---|
| A1 | Quality review Pack 04 skills (9 files) — verify all required sections present | All 9 upgraded to v1.1.0 | ✅ Done |
| A2 | Quality review Pack 05 skills (9 files) — verify all required sections present | All 9 upgraded to v1.1.0 | ✅ Done |
| A3 | Quality review Pack 06 skills (3 files) — verify all required sections | All 3 upgraded to v1.1.0 | ✅ Done |
| A4 | Quality review Pack 07 skills (4 files) — verify all required sections | All 4 upgraded to v1.1.0 | ✅ Done |
| A5 | Sync `SKILL-REGISTRY.md` — confirm all 47 skills listed with correct paths and statuses | Registry review | ⚠️ Pending |
| A6 | Enable GitHub branch protection on `main` | Governance enforced | ⚠️ Pending |
| A7 | Create `CHANGELOG.md` at root | Version tracking active | ❌ Not done |
| A8 | Update `README.md` — confirm skill count = 47, version reflects actual state | README accurate | ⚠️ Pending |

**QA standard applied (all 47 skills):** YAML front matter · Tests T01–T09 · Change Log · version → v1.1.0

---

### Phase B — Complete Artifact Definitions Layer
**Priority:** 🔴 High · **Status:** 🟡 B1 In Progress

#### B1 — Missing Artifact Definitions (~24 files)
**Status:** 🟡 In Progress — 0/24 built so far

These artifacts have no definition file yet and are required by existing skills.
See Section 3.2 for full build order and folder assignments.

**Artifact definition file standard:**
```yaml
---
artifact_id: A##
name: [Artifact Name]
version: 1.0.0
status: Active
category: [category]
pmbok8_anchor: [PMBOK8 section reference]
authority: PMI-derived
required_by_skills:
  - SKL-XX-XX
created_by_skills:
  - SKL-XX-XX
---
```

Sections required in every definition file:
1. Purpose
2. Scope (In Scope / Out of Scope table)
3. Trigger Conditions
4. Required Sections / Fields
5. PMBOK 8 Authority
6. Used By (skills that consume)
7. Created By (skills that produce)
8. Linked Artifacts
9. Validation Criteria
10. Change Log

**Build order:** A04 → A01 → A05 → A09 → A10 → A11 → A13 → A20 → A39 → A25 → A22 → A29 → A30 → A41 → A23 → A24 → A32 → A33 → A34 → A35 → A36 → A37 → A38 → A40

#### B2 — Artifact Templates (all confirmed definitions → template files)

For every artifact with a definition file, create `*-template.md`:
- File naming: `A##-[name]-template.md`
- Location: same subdirectory as definition file
- Content: fillable Markdown with `[FIELD: description]` placeholder syntax
- Sections must match definition structure exactly

**Priority order:** A04 → A07 → A06 → A14 → A15 → A16 → A17 → A19 → A08 → A12 → A21 → A27 → A28 → A31 → A02 → A03 → A18 → remaining

#### B3 — Artifact Examples (top 10 most-referenced)

Create `*-example.md` with realistic, anonymized project scenario for:
A04 (Charter), A06 (PM Plan), A08 (Scope), A14 (WBS), A15 (Schedule), A16 (Budget), A17 (Performance Report), A19 (Risk Register), A21 (Lessons Learned), A27 (Closure Record)

---

### Phase C — Build Reference Layer
**Priority:** 🟠 Medium-High · **Estimated effort:** High

#### C1 — Principles Files (12 files)
Path: `reference/principles/`

One file per principle (P01–P12) containing:
- Full principle statement (PMBOK8 Standard §3)
- Behavioral indicators · Anti-patterns
- Skill cross-references · Domain applicability · Supporting PMI references

**Priority:** P04 (Value), P07 (Tailoring), P10 (Risk), P01 (Stewardship) first.

#### C2 — Performance Domain Files (8 files)
Path: `reference/performance-domains/`

| File | Domain | PMBOK8 Section |
|---|---|---|
| PD01-stakeholders.md | Stakeholder Performance Domain | §2.5 |
| PD02-team.md | Team Performance Domain | §2.6 |
| PD03-development-approach.md | Development Approach & Life Cycle | §2.2 |
| PD04-planning.md | Planning Performance Domain | §2.3 |
| PD05-project-work.md | Project Work Performance Domain | §2.4 |
| PD06-delivery.md | Delivery Performance Domain | §2.7 |
| PD07-measurement.md | Measurement Performance Domain | §2.8 |
| PD08-uncertainty.md | Uncertainty Performance Domain | §2.9 |

#### C3 — Focus Area Files (5 files)
Path: `reference/focus-areas/`

FA01–FA05 — each maps: skills in focus area · artifacts triggered · principle anchors · entry/exit criteria.

#### C4 — Process Records (40 files)
Path: `reference/processes/`

One file per PMBOK 8 process: name, process group, knowledge area, purpose, inputs, tools & techniques, outputs, PMBOK8 figure reference, skill cross-reference.

**Build in batches:** Initiating (2) → Planning (24) → Executing (10) → M&C (12) → Closing (2)

#### C5 — Registries
- `reference/inputs-outputs/inputs-outputs-registry.md` — all 40 processes × I/O
- `reference/tools-techniques/tools-techniques-registry.md` — all T&T indexed

#### C6 — Appendices
- `reference/appendices/X2-pmo.md` — prerequisite for Pack PMO
- `reference/appendices/X3-ai.md` — prerequisite for Pack AI
- `reference/appendices/X4-procurement.md`
- `reference/appendices/X5-evolution.md`

#### C7 — Lexicon / Glossary
Path: `reference/GLOSSARY.md`

Maps every PMBOK 8 term in this repository to its PMI Lexicon definition:
- Term · Definition (source: PMI Lexicon of Project Management Terms) · First used in (Skill or Artifact ID) · Related terms

---

### Phase D — Build Shared Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium

#### D1 — Routing Logic
- `shared/routing/threshold-router.md` — T1–T4 decision routing with decision trees
- `shared/routing/escalation-paths.md` — escalation path definitions per decision type

#### D2 — Validators
- `shared/validators/artifact-completeness-checker.md`
- `shared/validators/waste-test.md`
- `shared/validators/baseline-integrity-check.md`

#### D3 — Pack Readiness Checklists
- One file per pack: `shared/checklists/pack-readiness/pack-0X-readiness.md`
- Pre-gate: `shared/checklists/domain-checklists/closure-readiness.md`

#### D4 — Reusable Field Components
- `shared/components/field-blocks/id-formats.md`
- `shared/components/field-blocks/status-fields.md`
- `shared/components/section-patterns/quality-criteria-section.md`

---

### Phase E — Build Tests Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium-High

#### E1 — Skill Test Files
Target: 9 test cases per skill × 47 skills = **423 test case files**

Schema per `tests/README.md`:
```
Test ID: T-PP-NN-##
Skill: SKL-PP-NN
Preconditions:
Inputs:
Expected Outputs:
Pass Criteria:
Failure Cases:
Notes:
```

**Build order:** Pack 01 (3) → Pack 02 (2) → Pack 03 (17) → Pack 04 (9) → Pack 05 (9) → Pack 06 (3) → Pack 07 (4)

#### E2 — Integration Test Files (7 files)

| File | Flow |
|---|---|
| IT-01-setup-to-initiating.md | Pack 01 → Pack 02 |
| IT-02-initiating-to-planning.md | Pack 02 → Pack 03 |
| IT-03-planning-to-executing.md | Pack 03 → Pack 04 |
| IT-04-executing-to-mc.md | Pack 04 → Pack 05 |
| IT-05-mc-to-closing.md | Pack 05 → Pack 06 |
| IT-06-hybrid-overlay.md | Pack 07 overlay on Pack 03–05 |
| IT-07-full-lifecycle.md | End-to-end flow test |

---

### Phase F — Extended Packs (PMO + AI)
**Priority:** 🔵 Lower · **Estimated effort:** Medium

**Prerequisite:** `reference/appendices/X2-pmo.md` and `X3-ai.md` must exist first.

#### F1 — Pack PMO (`skills/08-pmo/`)

| Skill ID | Skill Name | Authority Source |
|---|---|---|
| SKL-PMO-01 | Define PMO Charter and Mandate | PMO Practice Guide §3 |
| SKL-PMO-02 | Configure PMO Service Model | PMO Practice Guide §4 |
| SKL-PMO-03 | Establish Portfolio Intake and Governance | Standard for Portfolio Management §5 |
| SKL-PMO-04 | Define PM Methodology and Templates | OPM Standard §4 |
| SKL-PMO-05 | Manage PMO Maturity Assessment | OPM Standard §5 |
| SKL-PMO-06 | Run PMO Portfolio Review | Governance Practice Guide §5 |

#### F2 — Pack AI (`skills/09-ai/`)

| Skill ID | Skill Name | Authority Source |
|---|---|---|
| SKL-AI-01 | Assess AI Readiness for Project Work | Leading AI Transformation §3 |
| SKL-AI-02 | Govern AI Use in Project Delivery | Guide to Leading AI Projects §4 |
| SKL-AI-03 | Evaluate AI Tools for PMO | Guide to Leading AI Projects §5 |
| SKL-AI-04 | Manage AI-Enhanced Procurement | PMBOK8 §2.8 + AI guide |

---

### Phase G — MCP Server Design and Build
**Priority:** 🟡 Medium · **Estimated effort:** High

Create `mcp/` directory:

```
mcp/
├── README.md
├── architecture.md
├── tool-schemas/
│   ├── index.md
│   ├── get-skill.md
│   ├── get-artifact.md
│   ├── get-process.md
│   ├── list-skills-by-pack.md
│   ├── validate-artifact.md
│   └── route-decision.md
├── resource-schemas/
│   ├── index.md
│   ├── skill-resource.md
│   ├── artifact-resource.md
│   └── reference-resource.md
├── prompt-contracts/
│   ├── index.md
│   ├── execute-skill.md
│   ├── generate-artifact.md
│   └── plan-phase.md
└── endpoints.md
```

Each tool schema must include: name, description, input schema, output schema, example request/response, error cases, auth requirements.

**Implementation notes:** Python preferred · stdio (local) + HTTP/SSE (remote) · API key auth · structured JSON logging · read-only resource access.

---

### Phase H — AI Agent Design
**Priority:** 🔵 Medium-Low · **Estimated effort:** High

Create `agents/` directory:

```
agents/
├── README.md
├── PM-AGENT-01-project-planner.md
├── PM-AGENT-02-risk-manager.md
├── PM-AGENT-03-change-controller.md
├── PM-AGENT-04-stakeholder-manager.md
├── PM-AGENT-05-pmo-advisor.md
└── shared/
    ├── agent-schema-template.md
    └── safety-rules.md
```

Each agent definition must include: role definition · operating instructions · tool policy · memory policy · workflow · safety rules · escalation logic · evaluation criteria · sample prompts (3–5) · skill cross-references.

---

### Phase I — Book Authoring Track
**Priority:** 🔵 Medium-Low · **Estimated effort:** Very High

Create `book/` directory:

```
book/
├── README.md
├── OUTLINE.md
├── STYLE-GUIDE.md
├── chapters/
│   ├── 00-introduction.md
│   ├── 01-pmbok8-overview.md
│   ├── 02-principles.md
│   ├── 03-performance-domains.md
│   ├── 04-lifecycle-and-tailoring.md
│   ├── 05-initiating.md
│   ├── 06-planning.md
│   ├── 07-executing.md
│   ├── 08-monitoring-controlling.md
│   ├── 09-closing.md
│   ├── 10-adaptive-hybrid.md
│   ├── 11-pmo.md
│   ├── 12-ai-in-projects.md
│   └── 13-artifacts-reference.md
└── editorial/
    ├── review-notes.md
    └── revision-log.md
```

**Authoring rules:**
- Every statement must cite a PMBOK 8 section or companion reference
- No paraphrasing of PMI copyrighted content — synthesize and interpret
- Use `artifacts/*/example.md` files as chapter figures
- Every chapter must include a practical case study section
- Terminology must match `reference/GLOSSARY.md` at all times

---

### Phase K — Quality, CI/CD, and Release Track
**Priority:** 🟡 Ongoing · **Estimated effort:** Medium

#### K1 — Quality Standard for All Skills

Every skill file must pass:
- [ ] YAML front matter valid and complete, `skill_id` matches filename prefix
- [ ] `pmbok8_anchor` cites a real PMBOK 8 section or figure
- [ ] `primary_artifact` matches canonical A-code from Artifacts-V-1.0.5
- [ ] All upstream/downstream skill IDs exist in SKILL-REGISTRY.md
- [ ] Steps are numbered and action-oriented
- [ ] Tests table has minimum 7 entries with Pass/Fail conditions
- [ ] No unresolved `[TBD]` or `[placeholder]` text
- [ ] `source_type` is one of: `PMI-derived`, `synthesis`, `organization-defined`

#### K2 — CHANGELOG.md

Create at root following [Keep a Changelog](https://keepachangelog.com) format. Minimum entries:

```
## [Unreleased]

## [1.4.0] — 2026-05-30
### Added
- Phase A QA: All 47 skills upgraded to v1.1.0 (YAML front matter, Tests T01–T09, Change Log)
- MASTER-PLAN-V2.md v2.2.0: Progress tracking updated

## [1.3.0] — 2026-05-30
### Added
- Community standards: CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, issue templates, PR template
- MASTER-PLAN-V2.md roadmap document
- Artifact definitions: A02, A03, A06, A07, A08, A12, A14–A19, A21, A26–A28, A31
- Reference layer seeds: reference/, shared/, tests/ README files
- Principles index: reference/principles/index.md
```

#### K3 — GitHub Actions CI

Create `.github/workflows/`:
- `validate-skill-frontmatter.yml` — checks YAML front matter in all skill files
- `check-broken-links.yml` — validates internal cross-references
- `lint-markdown.yml` — enforces markdown formatting
- `registry-sync-check.yml` — verifies SKILL-REGISTRY.md matches actual skill files

#### K4 — Versioning Policy

| Increment | Trigger |
|---|---|
| Patch (x.x.N) | Bug fix, typo, reference correction |
| Minor (x.N.0) | New skill(s), new artifact definition(s), new reference file(s) |
| Major (N.0.0) | New pack, structural reorganization, breaking schema change |

**Current version:** 1.4.0 (post Phase A)
**Next milestone:** 1.5.0 — Artifact definitions complete (Phase B1 done)
**Target release:** 2.0.0 — All core layers complete (skills + artifacts + reference)

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | QA all 47 skills → v1.1.0 (YAML + Tests + Change Log) | Low–Medium | 🔴 Immediate | ✅ **Complete — 2026-05-30** |
| B1 | Missing artifact definitions: A01, A04, A05, A09–A11, A13, A20, A22–A25, A29–A32, A39, A41 | High | 🔴 High | 🟡 **In Progress — 0/24 built** |
| B2 | Artifact templates (all confirmed definitions → templates) | Very High | 🟠 High | ❌ Not done |
| B3 | Artifact examples (top 10) | Medium | 🟡 Medium | ❌ Not done |
| C1–C3 | Reference: 12 principles + 8 domains + 5 focus areas | High | 🟠 Medium-High | 🟡 Index only |
| C4–C5 | Reference: 40 process records + I/O + T&T registries | Very High | 🟡 Medium | ❌ Not done |
| C6 | Reference: appendices X2–X5 | Medium | 🟡 Medium | ❌ Not done |
| C7 | Reference: GLOSSARY.md | Medium | 🟡 Medium | ❌ Not done |
| D1–D4 | Shared: routing, validators, checklists, components | Medium | 🟡 Medium | 🟡 Seeded |
| E1–E2 | Tests: 423 skill tests + 7 integration tests | Very High | 🟡 Medium | 🟡 Seeded |
| F1 | Pack PMO (6 skills) | Medium | 🔵 Lower | ❌ Not started |
| F2 | Pack AI (4 skills) | Medium | 🔵 Lower | ❌ Not started |
| G | MCP Server: architecture + tool schemas + prompt contracts | High | 🟡 Medium | ❌ Not done |
| H | AI Agent definitions (5 agents) | High | 🔵 Medium-Low | ❌ Not done |
| I | Book authoring track (14 chapters + editorial) | Very High | 🔵 Medium-Low | ❌ Not done |
| K | QA + CI/CD + CHANGELOG + registry + README (ongoing) | Ongoing | 🟡 Ongoing | 🟡 Partial |

**Skills layer (Packs 01–07): ✅ 47/47 complete and QA'd at v1.1.0.**

---

## 6. Recommended Session Order

1. **Current session:** Phase B1 — Build missing artifact definitions (A04, A01, A05 first batch)
2. **Session +1:** Phase B1 continued — A09–A13, A20, A39, A41 (second batch)
3. **Session +2:** Phase B1 continued — A22–A25, A29–A32 (third batch)
4. **Session +3:** Phase B1 continued — A33–A40 (PMO + AI batch)
5. **Session +4:** Phase B2 — Artifact templates (priority 17 first)
6. **Session +5:** Phase C1–C3 — Principles files (12) + Domain files (8)
7. **Session +6:** Phase C4–C5 — Process records (batch 10 at a time)
8. **Session +7:** Phase C6–C7 — Appendices + GLOSSARY
9. **Session +8:** Phase G — MCP server design documents
10. **Sessions beyond:** Phase D + E, Phase F, Phase H, Phase I (book)

---

## 7. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan — 7 phases · focused on skills + artifacts + reference layers |
| 2.0.0 | 2026-05-30 | Full rebuild: added MCP server (Phase G), AI agents (Phase H), book authoring (Phase I), CI/CD (Phase K), community standards, CHANGELOG, GLOSSARY, branch protection, extended packs F1/F2, artifact templates + examples |
| 2.1.0 | 2026-05-30 | Correction: Skills inventory updated after direct repo verification. All 47 core skills confirmed present. Phase A revised to QA-only. Scorecard and session order revised. |
| 2.2.0 | 2026-05-30 | **Progress update:** Phase A fully complete — all 47 skills upgraded to v1.1.0 (YAML front matter, Tests T01–T09, Change Log). Commit `b785ee6`. Phase B1 marked In Progress. Artifact folder structure confirmed. 24 missing definitions listed with build order and folder assignments. Section 3.2 expanded with per-artifact status tracking. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-30 18:00 EEST · Version 2.2.0*
