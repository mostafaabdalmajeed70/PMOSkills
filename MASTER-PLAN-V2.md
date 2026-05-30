# PMOSkills Repository — Master Development Plan
**Version:** 2.4.0
**Date:** 2026-05-30
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

> **v2.4.0 update note (2026-05-30):** 9 stale duplicate definition files deleted across `planning-and-baselines/`, `monitoring-and-decisions/`, and `closing/`. Each artifact now has exactly one canonical definition file. B2 first-batch templates (A04, A06, A07, A14, A15, A16) confirmed present. Section 3.6 (A05 duplicate) resolved — only `A05-context-register.md` remains in `artifacts/governance/`. Artifact table updated to reflect clean post-dedup state.

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
| `MASTER-PLAN-V2.md` | ✅ v2.4.0 | This document — updated 2026-05-30 |
| `CHANGELOG.md` | ✅ Present | Created 2026-05-30 · K2 resolved |
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

### 1.3 Artifact Definitions Layer — Phase B1 Complete ✅

> **v2.4.0 note:** 9 stale duplicate definition files deleted 2026-05-30 (see Section 3.7). Each artifact folder now contains exactly one canonical definition file per artifact ID. The table below reflects the clean, post-dedup repository state.
>
> A38 (AI Risk Register) is **consolidated into A37** per Artifacts-V-1.0.5.
> A40 (OPM Maturity Assessment) is **consolidated into A36** per Artifacts-V-1.0.5.
> A41 (Benefits Realization Report) is **consolidated into A24 + A02** per Artifacts-V-1.0.5.

| Actual Folder | Canonical Definition Files | Templates Present | Status |
|---|---|---|---|
| `artifacts/initiating/` | A01, A04 | A04-project-charter-template.md | ✅ Clean |
| `artifacts/governance/` | A05, A34, A35, A37, A39 | — | ✅ Clean |
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A28 | A06-tailoring-decision-record-template.md · A14-integrated-project-management-plan-template.md · A15-schedule-baseline-template.md · A16-financial-baseline-template.md | ✅ Clean |
| `artifacts/stakeholders/` | A02, A07 | A07-stakeholder-register-template.md | ✅ Clean |
| `artifacts/quality/` | A09, A13 | — | ✅ Clean |
| `artifacts/communications/` | A10 | — | ✅ Clean |
| `artifacts/extended-procurement/` | A11, A33 | — | ✅ Clean |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18, A19, A20, A21 | — | ✅ Clean |
| `artifacts/extended-resources/` | A20 | — | ✅ Clean |
| `artifacts/portfolio/` | A22 | — | ✅ Clean |
| `artifacts/pmo/` | A23, A36 | — | ✅ Clean |
| `artifacts/closure/` | A24 | — | ✅ Clean |
| `artifacts/resources/` | A25, A26 | — | ✅ Clean |
| `artifacts/procurement/` | A31, A32 | — | ✅ Clean |
| `artifacts/closing/` | A27 | — | ✅ Clean |
| `artifacts/knowledge/` | A30 | — | ✅ Clean |
| `artifacts/stakeholders-communications/` | A29 | — | ✅ Clean |
| `artifacts/team-resources/` | — | — | 🟡 Seeded |
| **Templates layer** | — | 6 templates present (A04, A06, A07, A14, A15, A16) | 🟡 B2 in progress |
| **Examples layer** | — | None | ❌ B3 not started |

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
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definitions, templates, examples | ✅ Definitions: 41 present · A38/A40/A41 consolidated · B2 templates 6/41 done |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ✅ Phase A complete |

---

## 3. Open Issues — Immediate Actions Required

### 3.1 ✅ RESOLVED — Phase A QA Complete

All 47 skills upgraded to v1.1.0 on 2026-05-30. QA standard applied across all packs.

### 3.2 ✅ RESOLVED — Phase B1: Artifact Definitions Complete

All 24 originally missing artifact definitions confirmed present as of 2026-05-30.

**Consolidation decisions (Artifacts-V-1.0.5 authority):**

| Legacy Plan Entry | v1.0.5 Consolidation Decision | Rationale |
|---|---|---|
| A38 — AI Risk Register | **Consolidated into A37** (AI, Data, and Privacy Control Record) | v1.0.5 waste rule |
| A40 — OPM Maturity Assessment | **Consolidated into A36** (PMO Value, Maturity, and Improvement Record) | v1.0.5 consolidation rule |
| A41 — Benefits Realization Report | **Consolidated into A24 + A02** | v1.0.5 waste rule |

### 3.3 ⚠️ OPEN — Branch Protection

Verify `main` branch protection rules:
- Require pull request before merging
- Require at least 1 review
- Disallow force pushes
- Disallow branch deletion

### 3.4 ✅ RESOLVED — CHANGELOG.md Created

`CHANGELOG.md` created at root 2026-05-30. Commit: `848de34`. K2 resolved.

### 3.5 ⚠️ PENDING — SKILL-REGISTRY.md Sync

Verify `SKILL-REGISTRY.md` accurately reflects all 47 skills at v1.1.0 with correct YAML fields, artifact references, and status fields.

### 3.6 ✅ RESOLVED — A05 Duplicate in governance/

Only `A05-context-register.md` (11,437 bytes) remains in `artifacts/governance/`. The narrower variant `A05-context-register-eef-opa.md` (9,133 bytes) was removed. One canonical A05 per v1.0.5 standard.

### 3.7 ✅ RESOLVED — Stale Duplicate Definitions Deleted (2026-05-30)

9 stale lowercase/shorter duplicate definition files were deleted. Each artifact now has exactly one canonical definition.

| Deleted File | Folder | Size | Canonical Kept |
|---|---|---|---|
| `A14-integrated-project-management-plan.md` | `planning-and-baselines/` | 4,254b | `A14-Integrated-Project-Management-Plan.md` (7,327b) |
| `A15-schedule-model.md` | `planning-and-baselines/` | 4,462b | `A15-Schedule-Model-and-Baseline-Record.md` (7,755b) |
| `A16-financial-management-record.md` | `planning-and-baselines/` | 4,304b | `A16-Financial-Management-and-Cost-Baseline-Record.md` (8,384b) |
| `A19-risk-management-record.md` | `planning-and-baselines/` | 5,082b | `A19-Risk-Management-Record.md` in `monitoring-and-decisions/` (8,592b) |
| `A26-resource-management-record.md` | `planning-and-baselines/` | 4,408b | `A26-resource-capacity-acquisition-record.md` in `resources/` |
| `A17-performance-report.md` | `monitoring-and-decisions/` | 6,079b | `A17-Integrated-Performance-Reporting-Record.md` (8,274b) |
| `A18-issue-log.md` | `monitoring-and-decisions/` | 5,497b | `A18-Issue-Impediment-and-Action-Log.md` (5,848b) |
| `A21-lessons-learned-record.md` | `closing/` | 5,114b | `A21-Lessons-Learned-Record.md` in `monitoring-and-decisions/` (6,120b) |
| `A27-closure-record.md` | `closing/` | 5,888b | `A27-Project-Closure-Record.md` (9,370b) |

Commit chain: `cdba9e3` → `32943b2` → `f7ef8c2` → `126d2c6` → `183789b` → `3181d2d` → `f058553` → `b5bdf14` → `00aed28`

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
**Priority:** B1 ✅ Complete · B2 in progress · B3 not started

#### B1 — Missing Artifact Definitions
**Status:** ✅ COMPLETE — all 24 artifact definitions built and verified as of 2026-05-30.

#### B2 — Artifact Templates (all confirmed definitions → template files)

For every artifact with a definition file, create `*-template.md`:
- File naming: `A##-[name]-template.md`
- Location: same subdirectory as definition file
- Content: fillable Markdown with `[FIELD: description]` placeholder syntax
- Sections must match definition structure exactly

**B2 progress as of v2.4.0:**

| Artifact | Template File | Status |
|---|---|---|
| A04 — Project Charter | `artifacts/initiating/A04-project-charter-template.md` | ✅ Done |
| A06 — Tailoring Decision Record | `artifacts/planning-and-baselines/A06-tailoring-decision-record-template.md` | ✅ Done |
| A07 — Stakeholder Register | `artifacts/stakeholders/A07-stakeholder-register-template.md` | ✅ Done |
| A14 — Integrated Project Management Plan | `artifacts/planning-and-baselines/A14-integrated-project-management-plan-template.md` | ✅ Done |
| A15 — Schedule Model and Baseline Record | `artifacts/planning-and-baselines/A15-schedule-baseline-template.md` | ✅ Done |
| A16 — Financial Management and Cost Baseline Record | `artifacts/planning-and-baselines/A16-financial-baseline-template.md` | ✅ Done |
| A01, A02, A03, A05, A08–A13, A17–A13, A18–A39 remaining | — | ❌ Not yet built |

**Priority order for remaining templates:** A17 → A19 → A08 → A12 → A21 → A27 → A28 → A31 → A02 → A03 → A18 → remaining

#### B3 — Artifact Examples (top 10 most-referenced)

Create `*-example.md` with realistic, anonymized project scenario for:
A04, A06, A08, A14, A15, A16, A17, A19, A21, A27

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

One file per PMBOK 8 process. Build in batches: Initiating (2) → Planning (24) → Executing (10) → M&C (12) → Closing (2)

#### C5 — Registries
- `reference/inputs-outputs/inputs-outputs-registry.md`
- `reference/tools-techniques/tools-techniques-registry.md`

#### C6 — Appendices
- `reference/appendices/X2-pmo.md`
- `reference/appendices/X3-ai.md`
- `reference/appendices/X4-procurement.md`
- `reference/appendices/X5-evolution.md`

#### C7 — Lexicon / Glossary
Path: `reference/GLOSSARY.md`

---

### Phase D — Build Shared Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium

#### D1 — Routing Logic
- `shared/routing/threshold-router.md`
- `shared/routing/escalation-paths.md`

#### D2 — Validators
- `shared/validators/artifact-completeness-checker.md`
- `shared/validators/waste-test.md`
- `shared/validators/baseline-integrity-check.md`

#### D3 — Pack Readiness Checklists
- One file per pack: `shared/checklists/pack-readiness/pack-0X-readiness.md`

#### D4 — Reusable Field Components
- `shared/components/field-blocks/id-formats.md`
- `shared/components/field-blocks/status-fields.md`
- `shared/components/section-patterns/quality-criteria-section.md`

---

### Phase E — Build Tests Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium-High

#### E1 — Skill Test Files
Target: 9 test cases per skill × 47 skills = **423 test case files**

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

Create `mcp/` directory with architecture, tool schemas, resource schemas, prompt contracts, and endpoints.

Each tool schema must include: name, description, input schema, output schema, example request/response, error cases, auth requirements.

**Implementation notes:** Python preferred · stdio (local) + HTTP/SSE (remote) · API key auth · structured JSON logging · read-only resource access.

---

### Phase H — AI Agent Design
**Priority:** 🔵 Medium-Low · **Estimated effort:** High

Create `agents/` directory with 5 agent definitions (PM-AGENT-01 through PM-AGENT-05) plus shared safety rules and schema template.

Each agent definition must include: role definition · operating instructions · tool policy · memory policy · workflow · safety rules · escalation logic · evaluation criteria · sample prompts · skill cross-references.

---

### Phase I — Book Authoring Track
**Priority:** 🔵 Medium-Low · **Estimated effort:** Very High

Create `book/` directory with 14 chapters, style guide, and editorial log.

**Authoring rules:** Every statement must cite a PMBOK 8 section or companion reference. No paraphrasing of PMI copyrighted content — synthesize and interpret. Terminology must match `reference/GLOSSARY.md` at all times.

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
✅ **RESOLVED** — `CHANGELOG.md` created 2026-05-30. Commit: `848de34`.

#### K3 — GitHub Actions CI

Create `.github/workflows/`:
- `validate-skill-frontmatter.yml`
- `check-broken-links.yml`
- `lint-markdown.yml`
- `registry-sync-check.yml`

#### K4 — Versioning Policy

| Increment | Trigger |
|---|---|
| Patch (x.x.N) | Bug fix, typo, reference correction |
| Minor (x.N.0) | New skill(s), new artifact definition(s), new reference file(s) |
| Major (N.0.0) | New pack, structural reorganization, breaking schema change |

**Current version:** 2.4.0 (post Phase A + B1 + duplicate cleanup)
**Next milestone:** 2.5.0 — B2 second batch templates complete
**Target release:** 3.0.0 — All core layers complete (skills + artifacts + reference)

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | QA all 47 skills → v1.1.0 (YAML + Tests + Change Log) | Low–Medium | 🔴 Immediate | ✅ **Complete — 2026-05-30** |
| B1 | Missing artifact definitions — all 24 built | High | 🔴 High | ✅ **Complete — 2026-05-30** |
| B2 | Artifact templates (all confirmed definitions → templates) | Very High | 🟠 High | 🟡 6/41 done — in progress |
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
**Artifacts layer (B1): ✅ 41 definitions present. A38/A40/A41 consolidated. All duplicates resolved.**
**Artifacts layer (B2): 🟡 6 templates present (A04, A06, A07, A14, A15, A16). Remaining: ~35 templates pending.**

---

## 6. Recommended Session Order

1. **Next session:** Phase B2 continued — build templates for A17, A19, A08, A12, A21, A27, A28, A31
2. **Session +2:** Phase B2 continued — A02, A03, A18, A20, A22, A23, A24, A25
3. **Session +3:** Phase B2 final — remaining artifact templates
4. **Session +4:** Phase B3 — Artifact examples (top 10)
5. **Session +5:** Phase C1–C3 — Principles files (12) + Domain files (8)
6. **Session +6:** Phase C4–C5 — Process records (batch 10 at a time)
7. **Session +7:** Phase C6–C7 — Appendices + GLOSSARY
8. **Session +8:** Phase G — MCP server design documents
9. **Sessions beyond:** Phase D + E, Phase F, Phase H, Phase I (book)

---

## 7. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan — 7 phases · focused on skills + artifacts + reference layers |
| 2.0.0 | 2026-05-30 | Full rebuild: added MCP server (Phase G), AI agents (Phase H), book authoring (Phase I), CI/CD (Phase K), community standards, CHANGELOG, GLOSSARY, branch protection, extended packs F1/F2, artifact templates + examples |
| 2.1.0 | 2026-05-30 | Correction: Skills inventory updated after direct repo verification. All 47 core skills confirmed present. Phase A revised to QA-only. Scorecard and session order revised. |
| 2.2.0 | 2026-05-30 | Progress update: Phase A fully complete — all 47 skills upgraded to v1.1.0. Phase B1 marked In Progress. Artifact folder structure confirmed. 24 missing definitions listed with build order and folder assignments. |
| 2.3.0 | 2026-05-30 | Phase B1 confirmed complete. Artifact table corrected to actual v1.0.5 folder layout. A38/A40/A41 consolidation decisions documented. A26 duplicate deleted. CHANGELOG.md created (K2 resolved). A05 duplicate flagged. Scorecard updated. |
| 2.4.0 | 2026-05-30 | 9 stale duplicate definition files deleted (see Section 3.7). A05 duplicate confirmed resolved. Artifact table updated to clean post-dedup state. B2 progress table added (6 templates confirmed). Scorecard and session order updated. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-30 · Version 2.4.0*
