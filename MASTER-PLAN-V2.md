# PMOSkills Repository — Master Development Plan
**Version:** 2.1.0
**Date:** 2026-05-30
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

> **v2.1.0 correction note:** Skills layer inventory corrected after direct repo verification. All 47 core skills across Packs 01–07 are confirmed present. Phases B1–B3 (previously marked ❌ Not done) are now marked ✅ Complete. Phase A repairs updated accordingly. Execution scorecard and session order revised.

---

## 1. Current State Assessment (as of 2026-05-30)

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
| `MASTER-PLAN-V2.md` | ✅ Present | This document |
| `LICENSE` | ✅ Present | |
| `.gitignore` | ✅ Present | |

### 1.2 Skills Layer — Verified from Repository (2026-05-30)

> All file counts verified by direct directory inspection. No assumptions.

| Pack | Folder | Skills Confirmed | Count | Status |
|---|---|---|---|---|
| Pack 01 — Org Setup | `skills/01-organizational-setup/` | SKL-01-01, 01-02, 01-03 | 3/3 | ✅ Complete |
| Pack 02 — Initiating | `skills/02-initiating/` | SKL-02-01, 02-02 | 2/2 | ✅ Complete |
| Pack 03 — Planning | `skills/03-planning/` | SKL-03-01 through 03-17 | 17/17 | ✅ Complete |
| Pack 04 — Executing | `skills/04-executing/` | SKL-04-01 through 04-09 | 9/9 | ✅ Complete |
| Pack 05 — Monitoring & Controlling | `skills/05-monitoring-controlling/` | SKL-05-01 through 05-09 | 9/9 | ✅ Complete |
| Pack 06 — Closing | `skills/06-closing/` | SKL-06-01, 06-02, 06-03 | 3/3 | ✅ Complete |
| Pack 07 — Adaptive & Hybrid | `skills/07-adaptive-hybrid/` | SKL-07-01 through 07-04 | 4/4 | ✅ Complete |
| Pack PMO | `skills/08-pmo/` *(proposed)* | None | 0/6 | ❌ Not started |
| Pack AI | `skills/09-ai/` *(proposed)* | None | 0/4 | ❌ Not started |
| **TOTAL (core packs 01–07)** | | **All 47 confirmed** | **47/47** | ✅ **Skills layer complete** |

**Pack 05 file list (confirmed):**

| File | Size |
|---|---|
| `SKL-05-01-monitor-and-control-project-work.md` | 15,725 bytes |
| `SKL-05-02-perform-integrated-change-control.md` | 16,892 bytes |
| `SKL-05-03-control-scope.md` | 15,612 bytes |
| `SKL-05-04-control-schedule.md` | 19,741 bytes |
| `SKL-05-05-control-costs.md` | 19,072 bytes |
| `SKL-05-06-monitor-risks.md` | 18,102 bytes |
| `SKL-05-07-monitor-stakeholder-engagement.md` | 19,547 bytes |
| `SKL-05-08-control-resources.md` | 17,383 bytes |
| `SKL-05-09-monitor-communications.md` | 18,715 bytes |

### 1.3 Artifact Definitions Layer

| Subfolder | Files Present | Target | Status |
|---|---|---|---|
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A19, A26, A28 — 8 files | 8 definitions | ✅ Complete (definitions) |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18 — 3 files | 3 definitions | ✅ Complete (definitions) |
| `artifacts/closing/` | A21, A27 — 2 files | 2 definitions | ✅ Complete (definitions) |
| `artifacts/stakeholders/` | A02, A07 — 2 files | 2 definitions | ✅ Complete (definitions) |
| `artifacts/resources/` | A03 — 1 file | 1 definition | ✅ Complete (definitions) |
| `artifacts/procurement/` | A31 — 1 file | 1 definition | ✅ Complete (definitions) |
| **Templates layer** | None | 17+ template files | ❌ 0 done |
| **Examples layer** | None | 10+ example files | ❌ 0 done |
| **Missing artifact definitions** | A01, A04, A05, A09–A11, A13, A20, A22–A25, A29–A30, A32–A41 | ~24 definitions | ❌ Not yet written |

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
| Phase 1 — Verify Pack 04 quality | Check all 9 files against template | ⚠️ Quality review still recommended (file sizes 7–14 KB vs Pack 03 max 49 KB) |
| Phase 2.1 — Complete Pack 05 (8 skills) | Write SKL-05-02 through 05-09 | ✅ All 9 Pack 05 skills present |
| Phase 2.2 — Create Pack 06 (3 skills) | Write SKL-06-01 through 06-03 | ✅ All 3 Pack 06 skills present |
| Phase 2.3 — Create Pack 07 Adaptive (4 skills) | Write SKL-07-01 through 07-04 | ✅ All 4 Pack 07 skills present |
| Phase 2.4 — Confirm Pack 01 Pre-Sign | Verify `skills/01-pre-sign/` | ✅ Present as `01-organizational-setup/` — 3 skills confirmed |
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definitions, templates, examples | 🟡 17 definitions done · templates and examples not started |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ❌ Not started |

**New items added in v2.0.0 not in old plan:**
- Community standards layer ✅ Done
- Book authoring track (Phase J)
- MCP server design and build track (Phase H)
- AI agent design track (Phase I)
- GitHub Actions / CI validation (Phase K)
- GLOSSARY.md / PMI Lexicon file
- Artifact templates and examples (explicit plan)
- CHANGELOG.md
- Branch protection verification

---

## 3. Open Issues — Immediate Actions Required

### 3.1 ⚠️ Pack 04 Quality Review (Recommended)

No naming collision exists. However, Pack 04 files are significantly smaller than Pack 03 files. A quality review is recommended to confirm each file contains the full required template sections.

| Skill | Size | Benchmark (Pack 03 avg) | Action |
|---|---|---|---|
| SKL-04-01 | 10,681 bytes | ~20,000 bytes | Review completeness |
| SKL-04-02 | 13,858 bytes | ~20,000 bytes | Acceptable — verify sections |
| SKL-04-03 | 7,411 bytes | ~20,000 bytes | ⚠️ Likely needs expansion |
| SKL-04-04 | 8,019 bytes | ~20,000 bytes | ⚠️ Review |
| SKL-04-05 | 7,582 bytes | ~20,000 bytes | ⚠️ Review |
| SKL-04-06 | 7,547 bytes | ~20,000 bytes | ⚠️ Review |
| SKL-04-07 | 7,401 bytes | ~20,000 bytes | ⚠️ Review |
| SKL-04-08 | 7,685 bytes | ~20,000 bytes | ⚠️ Review |
| SKL-04-09 | 9,251 bytes | ~20,000 bytes | ⚠️ Review |

### 3.2 ⚠️ Pack 05–07 Quality Review (Recommended)

Pack 05 files are 15–20 KB each — reasonable depth. Pack 06 files are 8–10 KB — may need expansion. Pack 07 files are 9–11 KB — review recommended.

### 3.3 ⚠️ Branch Protection

Verify `main` branch protection rules:
- Require pull request before merging
- Require at least 1 review
- Disallow force pushes
- Disallow branch deletion

### 3.4 ❌ CHANGELOG.md Missing

Create `CHANGELOG.md` at root following Keep a Changelog format before next content release.

### 3.5 ⚠️ SKILL-REGISTRY.md Sync

Verify `SKILL-REGISTRY.md` accurately reflects all 47 skills with correct file paths, artifact references, and status fields for Packs 05–07 (newly confirmed complete).

---

## 4. Master Build Roadmap — Phases and Tracks

### Phase A — Stabilize and QA
**Priority:** 🔴 Immediate · **Estimated effort:** Low–Medium

| Task | Action | Output |
|---|---|---|
| A1 | Quality review Pack 04 skills (9 files) — verify all required sections present | Confirmed quality or expansion list |
| A2 | Quality review Pack 05 skills (9 files) — verify all required sections present | Confirmed quality or expansion list |
| A3 | Quality review Pack 06 skills (3 files) — verify all required sections | Confirmed quality or expansion list |
| A4 | Quality review Pack 07 skills (4 files) — verify all required sections | Confirmed quality or expansion list |
| A5 | Sync `SKILL-REGISTRY.md` — confirm all 47 skills listed with correct paths and statuses | Registry accurate |
| A6 | Enable GitHub branch protection on `main` | Governance enforced |
| A7 | Create `CHANGELOG.md` at root | Version tracking active |
| A8 | Update `README.md` — confirm skill count = 47, version reflects actual state | README accurate |

---

### Phase B — Complete Artifact Definitions Layer
**Priority:** 🔴 High · **Estimated effort:** Very High

#### B1 — Missing Artifact Definitions (~24 files)

These artifacts have no definition file yet and are required by existing skills:

| Artifact | Name | Required by Skills | Priority |
|---|---|---|---|
| A01 | Business Case | SKL-02-01 | 🔴 High |
| A04 | Project Charter | SKL-02-01 | 🔴 High |
| A05 | Context Register (EEF/OPA) | SKL-06-03 | 🔴 High |
| A09 | Quality Management Plan | SKL-03-09 | 🟠 Medium-High |
| A10 | Communications Management Plan | SKL-03-08 | 🟠 Medium-High |
| A11 | Procurement Management Plan | SKL-04-09 | 🟠 Medium-High |
| A13 | Requirements Traceability Matrix | SKL-03-03 | 🟠 Medium-High |
| A20 | Team Charter | SKL-04-04 | 🟠 Medium-High |
| A22 | Resource Acquisition Record | SKL-04-03 | 🟡 Medium |
| A23 | Vendor Bid Documents | SKL-04-09 | 🟡 Medium |
| A24 | Source Selection Criteria | SKL-04-09 | 🟡 Medium |
| A25 | Resource Management Plan / RACI | SKL-04-03, 04-04 | 🟡 Medium |
| A29 | Meeting Records | SKL-04-07 | 🟡 Medium |
| A30 | Project Closure Report | SKL-06-01 | 🟡 Medium |
| A32 | Procurement SOW | SKL-04-09 | 🟡 Medium |
| A33 | PMO Charter | Pack PMO | 🔵 Lower |
| A34 | Portfolio Register | Pack PMO | 🔵 Lower |
| A35 | Program Benefits Plan | Pack PMO | 🔵 Lower |
| A36 | Governance Framework Record | Pack PMO | 🔵 Lower |
| A37 | AI Project Readiness Assessment | Pack AI | 🔵 Lower |
| A38 | AI Risk Register | Pack AI | 🔵 Lower |
| A39 | Change Management Plan | SKL-05-02 | 🟡 Medium |
| A40 | OPM Maturity Assessment | Pack PMO | 🔵 Lower |
| A41 | Benefits Realization Report | SKL-06-01 | 🟡 Medium |

**Build order:** A04 → A01 → A05 → A09 → A10 → A11 → A13 → A20 → A39 → A25 → A22 → A29 → A30 → A41 → A23 → A24 → A32 → A33–A41

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

## [1.3.0] — 2026-05-30
### Added
- Community standards: CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, issue templates, PR template
- MASTER-PLAN-V2.md roadmap document
- Artifact definitions: A02, A03, A06, A07, A08, A12, A14–A19, A21, A26–A28, A31
- Reference layer seeds: reference/, shared/, tests/ README files
- Principles index: reference/principles/index.md

## [1.2.0] — (date)
### Added
- Pack 05 skills: SKL-05-01 through 05-09
- Pack 06 skills: SKL-06-01 through 06-03
- Pack 07 skills: SKL-07-01 through 07-04
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

**Current version:** 1.3.0
**Next milestone:** 1.4.0 — Artifact definitions complete (Phase B1 done)
**Target release:** 2.0.0 — All core layers complete (skills + artifacts + reference)

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | Stabilize: QA review Packs 04–07 · SKILL-REGISTRY sync · branch protection · CHANGELOG | Low–Medium | 🔴 Immediate | ❌ Not done |
| B1 | Missing artifact definitions (A01, A04, A05, A09–A11, A13, A20, A22–A25, A29–A32, A39, A41) | High | 🔴 High | ❌ Not done |
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

**Skills layer (Packs 01–07): ✅ 47/47 complete — no longer a gap.**

---

## 6. Recommended Session Order

1. **Session next:** Phase A — QA review Packs 04–07 + SKILL-REGISTRY sync + CHANGELOG.md
2. **Session +1:** Phase B1 — Missing artifact definitions (A01, A04, A05 first)
3. **Session +2:** Phase B1 continued — A09–A13, A20, A39, A41
4. **Session +3:** Phase B2 — Artifact templates (priority 17 first)
5. **Session +4:** Phase C1–C3 — Principles files (12) + Domain files (8)
6. **Session +5:** Phase C4–C5 — Process records (batch 10 at a time)
7. **Session +6:** Phase C6–C7 — Appendices + GLOSSARY
8. **Session +7:** Phase G — MCP server design documents
9. **Session +8:** Phase D + E — Shared validators + test cases
10. **Sessions beyond:** Phase F (extended packs), Phase H (agents), Phase I (book)

---

## 7. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan — 7 phases · focused on skills + artifacts + reference layers |
| 2.0.0 | 2026-05-30 | Full rebuild: added MCP server (Phase G), AI agents (Phase H), book authoring (Phase I), CI/CD (Phase K), community standards, CHANGELOG, GLOSSARY, branch protection, extended packs F1/F2, artifact templates + examples |
| 2.1.0 | 2026-05-30 | **Correction:** Skills inventory updated after direct repo verification. All 47 core skills (Packs 01–07) confirmed present. Phases B1–B3 (skills completion) removed from roadmap — marked complete. Phase A revised to QA-only (no repairs needed). Scorecard and session order revised accordingly. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-30 · Version 2.1.0*
