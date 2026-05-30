# PMOSkills Repository — Master Development Plan
**Version:** 2.3.0
**Date:** 2026-05-30
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

> **v2.3.0 update note (2026-05-30):** Phase B1 complete — all 24 missing artifact definitions confirmed built and present in the repository. Artifact table corrected to reflect actual folder layout (diverges from v2.2.0 plan due to v1.0.5 normalization). A38, A40, and A41 confirmed consolidated per Artifacts-V-1.0.5 authority model (see Section 3.2 for details). A26 duplicate deleted. CHANGELOG.md created (K2 resolved). Plan aligned to v1.0.5 vocabulary throughout. Phase B2 (artifact templates) is next.

---

## 1. Current State Assessment (as of 2026-05-30 21:00 EEST)

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
| `MASTER-PLAN-V2.md` | ✅ v2.3.0 | This document — updated 2026-05-30 |
| `CHANGELOG.md` | ✅ v2.3.0 | Created 2026-05-30 · K2 resolved |
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

### 1.3 Artifact Definitions Layer — Phase B1 Complete ✅

> **v2.3.0 note:** The actual folder layout diverges from the v2.2.0 plan table due to v1.0.5 normalization. The table below reflects the actual repository state as of 2026-05-30.
> A38 (AI Risk Register) is **consolidated into A37** per Artifacts-V-1.0.5. No separate A38 file is required or expected.
> A40 (OPM Maturity Assessment) is **consolidated into A36** per Artifacts-V-1.0.5. No separate A40 file is required or expected.
> A41 (Benefits Realization Report) is **consolidated into A24 + A02** per Artifacts-V-1.0.5. No separate A41 file is required or expected.

| Actual Folder | Files Present | Status |
|---|---|---|
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A19, A26 (canonical), A28 | ✅ 8 files |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18 | ✅ 3 files |
| `artifacts/closing/` | A21, A27 | ✅ 2 files |
| `artifacts/stakeholders/` | A02, A07 | ✅ 2 files |
| `artifacts/resources/` | A03, A25, A26 (canonical v1.0.5 Batch-4), A27 | ✅ 4 files |
| `artifacts/procurement/` | A31 | ✅ 1 file |
| `artifacts/initiating/` | A01, A04 | ✅ 2 files — B1 batch 1 |
| `artifacts/governance/` | A05 (×2 variants), A34, A35, A37, A39 | ✅ 6 files — B1 batch 1–4 |
| `artifacts/quality/` | A09, A13 | ✅ 2 files — B1 batch 2 |
| `artifacts/communications/` | A10 | ✅ 1 file — B1 batch 2 |
| `artifacts/extended-procurement/` | A11, A33 | ✅ 2 files — B1 batch 3 |
| `artifacts/extended-resources/` | A20 | ✅ 1 file — B1 batch 3 |
| `artifacts/portfolio/` | A22 | ✅ 1 file — B1 batch 3 |
| `artifacts/pmo/` | A23, A36 | ✅ 2 files — B1 batch 4 |
| `artifacts/closure/` | A24 | ✅ 1 file — B1 batch 4 |
| `artifacts/knowledge/` | A30 (inferred) | ✅ 1 file — B1 batch 4 |
| `artifacts/stakeholders-communications/` | A29 (inferred) | ✅ 1 file — B1 batch 4 |
| `artifacts/team-resources/` | Seeded | 🟡 Seeded |
| **Templates layer** | None | ❌ 0 done — Phase B2 |
| **Examples layer** | None | ❌ 0 done — Phase B3 |

**A26 duplicate resolved:** `artifacts/resources/A26-Resource-Capacity-and-Acquisition-Record.md` (title-case, 7,069 bytes older variant) deleted 2026-05-30. Canonical file: `artifacts/resources/A26-resource-capacity-acquisition-record.md`.

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
| CHANGELOG.md | ✅ Created 2026-05-30 — K2 resolved |
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
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definitions, templates, examples | ✅ Definitions: 24+17 = 41 present · A38/A40/A41 consolidated · Templates B2 pending |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ✅ Phase A complete |

**New items added in v2.0.0 not in old plan:**
- Community standards layer ✅ Done
- CHANGELOG.md ✅ Done (K2 resolved)
- Book authoring track (Phase I)
- MCP server design and build track (Phase G)
- AI agent design track (Phase H)
- GitHub Actions / CI validation (Phase K)
- GLOSSARY.md / PMI Lexicon file
- Artifact templates and examples (explicit plan)
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

### 3.2 ✅ RESOLVED — Phase B1: Artifact Definitions Complete

All 24 originally missing artifact definitions are confirmed present in the repository as of 2026-05-30.

**Vocabulary alignment note:** The v2.2.0 plan table used stale pre-normalization names for some artifacts. The table below reflects the v1.0.5-canonical names actually used in the built files. The plan vocabulary has been updated accordingly.

**Consolidation decisions (Artifacts-V-1.0.5 authority):**

| Legacy Plan Entry | v1.0.5 Consolidation Decision | Rationale |
|---|---|---|
| A38 — AI Risk Register | **Consolidated into A37** (AI, Data, and Privacy Control Record) | v1.0.5 waste rule: AI risk controls belong in one integrated record, not a separate register |
| A40 — OPM Maturity Assessment | **Consolidated into A36** (PMO Value, Maturity, and Improvement Record) | v1.0.5 consolidation rule: PMO maturity assessment is a sub-function of PMO improvement governance |
| A41 — Benefits Realization Report | **Consolidated into A24 + A02** (Closure and Benefits Transition Record + Benefits Realization Record) | v1.0.5 waste rule: closure and benefits tracking are unified in A24; post-project benefit ownership in A02 |

**Full B1 build verification table:**

| Priority | ID | Name (v1.0.5 canonical) | Actual Folder | Status |
|---|---|---|---|---|
| 🔴 1 | A04 | Project Charter | `artifacts/initiating/` | ✅ Built |
| 🔴 2 | A01 | Business Case | `artifacts/initiating/` | ✅ Built |
| 🔴 3 | A05 | Context Register | `artifacts/governance/` | ✅ Built |
| 🟠 4 | A09 | Quality Management Plan | `artifacts/quality/` | ✅ Built |
| 🟠 5 | A10 | Communications Management Plan | `artifacts/communications/` | ✅ Built |
| 🟠 6 | A11 | Procurement Management Plan | `artifacts/extended-procurement/` | ✅ Built |
| 🟠 7 | A13 | Requirements Traceability Matrix | `artifacts/quality/` | ✅ Built |
| 🟠 8 | A20 | Team Charter | `artifacts/extended-resources/` | ✅ Built |
| 🟠 9 | A39 | Change Management Plan | `artifacts/governance/` | ✅ Built |
| 🟡 10 | A25 | Team Operating and Responsibility Record | `artifacts/resources/` | ✅ Built |
| 🟡 11 | A22 | Portfolio Interdependency Record | `artifacts/portfolio/` | ✅ Built |
| 🟡 12 | A29 | Change Readiness and Adoption Record | `artifacts/stakeholders-communications/` | ✅ Built |
| 🟡 13 | A30 | Knowledge and Lessons Management Record | `artifacts/knowledge/` | ✅ Built |
| 🟡 14 | A24 | Closure and Benefits Transition Record | `artifacts/closure/` | ✅ Built (absorbs A41) |
| 🟡 15 | A23 | PMO Improvement Backlog | `artifacts/pmo/` | ✅ Built |
| 🟡 16 | A26 | Resource Capacity and Acquisition Record | `artifacts/resources/` | ✅ Built (canonical Batch-4 file) |
| 🟡 17 | A32 | Supplier Evaluation and Award Decision Record | `artifacts/procurement/` | ✅ Built |
| 🔵 18 | A33 | Supplier Change, Claim, and Compliance Record | `artifacts/extended-procurement/` | ✅ Built |
| 🔵 19 | A34 | Information Retention and Records Control Record | `artifacts/governance/` | ✅ Built |
| 🔵 20 | A35 | Governance and Decision Authority Record | `artifacts/governance/` | ✅ Built |
| 🔵 21 | A36 | PMO Value, Maturity, and Improvement Record | `artifacts/pmo/` | ✅ Built (absorbs A40) |
| 🔵 22 | A37 | AI, Data, and Privacy Control Record | `artifacts/governance/` | ✅ Built (absorbs A38) |
| 🔵 23 | A38 | AI Risk Register | — | ✅ Consolidated into A37 |
| 🔵 24 | A40 | OPM Maturity Assessment | — | ✅ Consolidated into A36 |

**A26 duplicate fix:** `artifacts/resources/A26-Resource-Capacity-and-Acquisition-Record.md` (title-case variant, 7,069 bytes) deleted. Canonical: `A26-resource-capacity-acquisition-record.md`. Commit: `99afad5`.

### 3.3 ⚠️ OPEN — Branch Protection

Verify `main` branch protection rules:
- Require pull request before merging
- Require at least 1 review
- Disallow force pushes
- Disallow branch deletion

### 3.4 ✅ RESOLVED — CHANGELOG.md Created

`CHANGELOG.md` created at root 2026-05-30. Covers v0.1.0 through v2.3.0. Commit: `848de34`. K2 resolved.

### 3.5 ⚠️ PENDING — SKILL-REGISTRY.md Sync

Verify `SKILL-REGISTRY.md` accurately reflects all 47 skills at v1.1.0 with correct YAML fields, artifact references, and status fields.

### 3.6 ⚠️ PENDING — A05 Duplicate in governance/

Two A05 files exist in `artifacts/governance/`:
- `A05-context-register-eef-opa.md` (9,133 bytes)
- `A05-context-register.md` (11,437 bytes)

Review both files. Delete the older or narrower variant and keep only one canonical A05 per v1.0.5 standard.

---

## 4. Master Build Roadmap — Phases and Tracks

### Phase A — Stabilize and QA
**Priority:** ✅ COMPLETE · **Completed:** 2026-05-30

| Task | Action | Output | Status |
|---|---|---|---|
| A1 | Quality review Pack 04 skills (9 files) | All 9 upgraded to v1.1.0 | ✅ Done |
| A2 | Quality review Pack 05 skills (9 files) | All 9 upgraded to v1.1.0 | ✅ Done |
| A3 | Quality review Pack 06 skills (3 files) | All 3 upgraded to v1.1.0 | ✅ Done |
| A4 | Quality review Pack 07 skills (4 files) | All 4 upgraded to v1.1.0 | ✅ Done |
| A5 | Sync `SKILL-REGISTRY.md` | Registry review | ⚠️ Pending |
| A6 | Enable GitHub branch protection on `main` | Governance enforced | ⚠️ Pending |
| A7 | Create `CHANGELOG.md` at root | Version tracking active | ✅ Done — 2026-05-30 |
| A8 | Update `README.md` — confirm skill count = 47 | README accurate | ⚠️ Pending |

---

### Phase B — Complete Artifact Definitions Layer
**Priority:** B1 ✅ Complete · B2/B3 next

#### B1 — Missing Artifact Definitions
**Status:** ✅ COMPLETE — all 24 artifact definitions built and verified as of 2026-05-30.
See Section 3.2 for full verification table and consolidation decisions.

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

One file per principle (P01–P12):
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
✅ **RESOLVED** — `CHANGELOG.md` created 2026-05-30. Covers v0.1.0 through v2.3.0. Commit: `848de34`.

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

**Current version:** 2.3.0 (post Phase A + B1)
**Next milestone:** 2.4.0 — Artifact templates complete (Phase B2 done)
**Target release:** 3.0.0 — All core layers complete (skills + artifacts + reference)

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | QA all 47 skills → v1.1.0 (YAML + Tests + Change Log) | Low–Medium | 🔴 Immediate | ✅ **Complete — 2026-05-30** |
| B1 | Missing artifact definitions — all 24 built | High | 🔴 High | ✅ **Complete — 2026-05-30** |
| B2 | Artifact templates (all confirmed definitions → templates) | Very High | 🟠 High | ❌ Not done — next |
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
| K | QA + CI/CD + CHANGELOG + registry + README (ongoing) | Ongoing | 🟡 Ongoing | 🟡 K2 done · K1/K3 pending |

**Skills layer (Packs 01–07): ✅ 47/47 complete and QA'd at v1.1.0.**
**Artifacts layer (B1): ✅ 41 definitions present (17 original + 24 B1 built). A38/A40/A41 consolidated.**

---

## 6. Recommended Session Order

1. **Current session:** Resolve A05 duplicate in `artifacts/governance/` (Section 3.6)
2. **Session +1:** Phase B2 — Artifact templates (A04, A07, A06, A14, A15, A16 first batch)
3. **Session +2:** Phase B2 continued — A17, A19, A08, A12, A21, A27, A28, A31
4. **Session +3:** Phase B2 continued — remaining artifact templates
5. **Session +4:** Phase B3 — Artifact examples (top 10)
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
| 2.2.0 | 2026-05-30 | Progress update: Phase A fully complete — all 47 skills upgraded to v1.1.0. Phase B1 marked In Progress. Artifact folder structure confirmed. 24 missing definitions listed with build order and folder assignments. |
| 2.3.0 | 2026-05-30 | Phase B1 confirmed complete. Artifact table corrected to actual v1.0.5 folder layout. A38/A40/A41 consolidation decisions documented. A26 duplicate deleted (`99afad5`). CHANGELOG.md created (`848de34`). A05 duplicate flagged (Section 3.6). Scorecard updated. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-30 21:00 EEST · Version 2.3.0*
