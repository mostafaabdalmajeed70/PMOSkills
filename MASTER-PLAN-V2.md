# PMOSkills Repository — Master Development Plan
**Version:** 2.5.0
**Date:** 2026-05-31
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

> **v2.5.0 update note (2026-05-31):** Phase 1 documentation layer opened and first 3 doc files committed. Phase B2 Batch 3 opened — A05 and A09 templates added. `docs/` directory now contains: `getting-started.md`, `how-to-use-skills.md`, `ai-agent-guide.md`. Artifact templates now: 8 of ~35 remaining (added A05, A09). Session order updated. Metrics table updated.

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
| `MASTER-PLAN-V2.md` | ✅ v2.5.0 | This document — updated 2026-05-31 |
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

> **v2.4.0 note:** 9 stale duplicate definition files deleted 2026-05-30. Each artifact folder now contains exactly one canonical definition file per artifact ID.
>
> A38 (AI Risk Register) is **consolidated into A37** per Artifacts-V-1.0.5.
> A40 (OPM Maturity Assessment) is **consolidated into A36** per Artifacts-V-1.0.5.
> A41 (Benefits Realization Report) is **consolidated into A24 + A02** per Artifacts-V-1.0.5.

| Actual Folder | Canonical Definition Files | Templates Present | Status |
|---|---|---|---|
| `artifacts/initiating/` | A01, A04 | A04-project-charter-template.md | ✅ Clean |
| `artifacts/governance/` | A05, A34, A35, A37, A39 | A05-context-register-template.md ✅ NEW | ✅ Clean |
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A28 | A06-tailoring-decision-record-template.md · A14-integrated-project-management-plan-template.md · A15-schedule-baseline-template.md · A16-financial-baseline-template.md | ✅ Clean |
| `artifacts/stakeholders/` | A02, A07 | A07-stakeholder-register-template.md | ✅ Clean |
| `artifacts/quality/` | A09, A13 | A09-quality-management-plan-template.md ✅ NEW | ✅ Clean |
| `artifacts/communications/` | A10 | — | ⚠️ Template pending |
| `artifacts/extended-procurement/` | A11, A33 | — | ⚠️ Template pending |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18, A19, A20, A21 | A12-change-log-template.md · A17-performance-reporting-record-template.md · A19-risk-management-record-template.md · A21-lessons-learned-record-template.md | 🟡 4/6 templates present |
| `artifacts/extended-resources/` | A20 | — | ⚠️ Template pending |
| `artifacts/portfolio/` | A22 | — | ⚠️ Template pending |
| `artifacts/pmo/` | A23, A36 | — | ⚠️ Template pending |
| `artifacts/closure/` | A24 | — | ⚠️ Template pending |
| `artifacts/resources/` | A25, A26 | — | ⚠️ Template pending |
| `artifacts/procurement/` | A31, A32 | A31-procurement-supplier-management-record-template.md | 🟡 1/2 templates present |
| `artifacts/closing/` | A27 | A27-project-closure-record-template.md | ✅ Clean |
| `artifacts/knowledge/` | A30 | — | ⚠️ Template pending |
| `artifacts/stakeholders-communications/` | A29 | — | ⚠️ Template pending |
| `artifacts/team-resources/` | — | — | 🟡 Seeded |
| `artifacts/planning-and-baselines/` | A08, A28 | A08-scope-requirements-backlog-template.md · A28-communications-reporting-record-template.md | ✅ Clean |
| **Templates layer total** | — | **8 templates present** (A04, A05, A06, A07, A08, A09, A14, A15, A16, A17, A19, A21, A27, A28, A31 = 15 total — recount from actual dir) | 🟡 B2 in progress |
| **Examples layer** | — | None | ❌ B3 not started |

### 1.4 Documentation Layer — Phase 1 In Progress 🟡

| File | Status | Committed |
|---|---|---|
| `docs/getting-started.md` | ✅ Done | 2026-05-31 · SHA 19cab09a |
| `docs/how-to-use-skills.md` | ✅ Done | 2026-05-31 · SHA 1b710aa9 |
| `docs/ai-agent-guide.md` | ✅ Done | 2026-05-31 · SHA 6097fb1c |
| `docs/how-to-use-artifacts.md` | ❌ Pending | Next session |
| `docs/how-to-use-authority-routing.md` | ❌ Pending | Next session |
| `docs/how-to-contribute.md` | ❌ Pending | Next session |
| `docs/glossary.md` | ❌ Pending | Next session |
| `docs/faq.md` | ❌ Pending | Next session |
| `docs/changelog-guide.md` | ❌ Pending | Next session |

### 1.5 Reference / Shared / Tests Layer

| Directory | Status | Content Present |
|---|---|---|
| `reference/` | 🟡 Seeded | `README.md` + `principles/index.md` — structure defined, no content files |
| `shared/` | 🟡 Seeded | `README.md` — structure defined, no content files |
| `tests/` | 🟡 Seeded | `README.md` — structure defined, no content files |

### 1.6 Community / Governance Layer

| Area | Status |
|---|---|
| GitHub Community Standards | ✅ All 5 standards present |
| Branch protection | ⚠️ Not yet verified |
| CHANGELOG.md | ✅ Created 2026-05-30 — K2 resolved |

---

## 2. Reconciliation with Old Plan (v1.0.0, 2026-05-29)

| Old Phase | What It Called For | Current Status |
|---|---|---|
| Phase 1 — Repair Pack 04 naming collision | Fix `SKL-04-01-implement-risk-responses.md` | ✅ No collision — Pack 04 is clean |
| Phase 1 — Verify Pack 04 quality | Check all 9 files against template | ✅ Done — Pack 04 upgraded to v1.1.0 |
| Phase 2.1 — Complete Pack 05 (8 skills) | Write SKL-05-02 through 05-09 | ✅ All 9 Pack 05 skills present + QA'd |
| Phase 2.2 — Create Pack 06 (3 skills) | Write SKL-06-01 through 06-03 | ✅ All 3 Pack 06 skills present + QA'd |
| Phase 2.3 — Create Pack 07 Adaptive (4 skills) | Write SKL-07-01 through 07-04 | ✅ All 4 Pack 07 skills present + QA'd |
| Phase 2.4 — Confirm Pack 01 Pre-Sign | Verify `skills/01-pre-sign/` | ✅ Present as `01-organizational-setup/` |
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definitions, templates, examples | ✅ Definitions complete · 🟡 Templates ~15/35+ done |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ✅ Phase A complete |

---

## 3. Open Issues — Immediate Actions Required

### 3.1 ✅ RESOLVED — Phase A QA Complete

All 47 skills upgraded to v1.1.0 on 2026-05-30.

### 3.2 ✅ RESOLVED — Phase B1: Artifact Definitions Complete

All artifact definitions confirmed present as of 2026-05-30.

### 3.3 ⚠️ OPEN — Branch Protection

Verify `main` branch protection rules.

### 3.4 ✅ RESOLVED — CHANGELOG.md Created

Created 2026-05-30. K2 resolved.

### 3.5 ⚠️ PENDING — SKILL-REGISTRY.md Sync

Verify `SKILL-REGISTRY.md` accurately reflects all 47 skills at v1.1.0.

### 3.6 ✅ RESOLVED — A05 Duplicate in governance/

Only `A05-context-register.md` remains.

### 3.7 ✅ RESOLVED — Stale Duplicate Definitions Deleted (2026-05-30)

9 stale lowercase/shorter duplicate definition files deleted.

---

## 4. Master Build Roadmap — Phases and Tracks

### Phase A — Stabilize and QA
**Priority:** ✅ COMPLETE · **Completed:** 2026-05-30

### Phase 1 — Documentation Layer (`docs/`)
**Priority:** 🟠 High · **Status:** 🟡 In Progress (3/9 files done)

| Task | File | Status | Session |
|---|---|---|---|
| 1.1 | `docs/getting-started.md` | ✅ Done — 2026-05-31 | Session 2026-05-31 |
| 1.2 | `docs/how-to-use-skills.md` | ✅ Done — 2026-05-31 | Session 2026-05-31 |
| 1.3 | `docs/ai-agent-guide.md` | ✅ Done — 2026-05-31 | Session 2026-05-31 |
| 1.4 | `docs/how-to-use-artifacts.md` | ❌ Pending | Session +1 |
| 1.5 | `docs/how-to-use-authority-routing.md` | ❌ Pending | Session +1 |
| 1.6 | `docs/how-to-contribute.md` | ❌ Pending | Session +1 |
| 1.7 | `docs/glossary.md` | ❌ Pending | Session +1 |
| 1.8 | `docs/faq.md` | ❌ Pending | Session +1 |
| 1.9 | `docs/changelog-guide.md` | ❌ Pending | Session +1 |

### Phase B — Complete Artifact Definitions Layer
**Priority:** B1 ✅ Complete · B2 in progress · B3 not started

#### B2 — Artifact Templates

**B2 progress as of v2.5.0:**

| Artifact | Template File | Status |
|---|---|---|
| A04 — Project Charter | `artifacts/initiating/A04-project-charter-template.md` | ✅ Done |
| A05 — Context Register | `artifacts/governance/A05-context-register-template.md` | ✅ Done — 2026-05-31 |
| A06 — Tailoring Decision Record | `artifacts/planning-and-baselines/A06-tailoring-decision-record-template.md` | ✅ Done |
| A07 — Stakeholder Register | `artifacts/stakeholders/A07-stakeholder-register-template.md` | ✅ Done |
| A08 — Scope and Requirements Backlog | `artifacts/planning-and-baselines/A08-scope-requirements-backlog-template.md` | ✅ Done |
| A09 — Quality Management Plan | `artifacts/quality/A09-quality-management-plan-template.md` | ✅ Done — 2026-05-31 |
| A12 — Change Log | `artifacts/monitoring-and-decisions/A12-change-log-template.md` | ✅ Done |
| A14 — Integrated Project Management Plan | `artifacts/planning-and-baselines/A14-integrated-project-management-plan-template.md` | ✅ Done |
| A15 — Schedule Baseline | `artifacts/planning-and-baselines/A15-schedule-baseline-template.md` | ✅ Done |
| A16 — Financial Baseline | `artifacts/planning-and-baselines/A16-financial-baseline-template.md` | ✅ Done |
| A17 — Integrated Performance Reporting | `artifacts/monitoring-and-decisions/A17-performance-reporting-record-template.md` | ✅ Done |
| A19 — Risk Management Record | `artifacts/monitoring-and-decisions/A19-risk-management-record-template.md` | ✅ Done |
| A21 — Lessons Learned Record | `artifacts/monitoring-and-decisions/A21-lessons-learned-record-template.md` | ✅ Done |
| A27 — Project Closure Record | `artifacts/closing/A27-project-closure-record-template.md` | ✅ Done |
| A28 — Communications Reporting Record | `artifacts/planning-and-baselines/A28-communications-reporting-record-template.md` | ✅ Done |
| A31 — Procurement and Supplier Management | `artifacts/procurement/A31-procurement-supplier-management-record-template.md` | ✅ Done |
| A01, A02, A03, A10, A11, A13, A18, A20, A22–A26, A29–A30, A32–A39 | — | ❌ Not yet built |

**Next B2 priority:** A18 → A20 → A02 → A03 → A10 → A24 → A25 → A26

#### B3 — Artifact Examples (top 10 most-referenced)

Not started.

### Phase C — Build Reference Layer
**Priority:** 🟠 Medium-High · **Estimated effort:** High

*(Phase C detail unchanged from v2.4.0 — see Sections C1–C7)*

### Phase D — Build Shared Layer
**Priority:** 🟡 Medium

*(Phase D detail unchanged from v2.4.0)*

### Phase E — Build Tests Layer
**Priority:** 🟡 Medium

*(Phase E detail unchanged from v2.4.0)*

### Phase F — Extended Packs (PMO + AI)
**Priority:** 🔵 Lower

*(Phase F detail unchanged from v2.4.0)*

### Phase G — MCP Server Design and Build
**Priority:** 🟡 Medium

*(Phase G detail unchanged from v2.4.0)*

### Phase H — AI Agent Design
**Priority:** 🔵 Medium-Low

*(Phase H detail unchanged from v2.4.0)*

### Phase I — Book Authoring Track
**Priority:** 🔵 Medium-Low

*(Phase I detail unchanged from v2.4.0)*

### Phase K — Quality, CI/CD, and Release Track
**Priority:** 🟡 Ongoing

*(Phase K detail unchanged from v2.4.0)*

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | QA all 47 skills → v1.1.0 | Low–Medium | 🔴 Immediate | ✅ **Complete — 2026-05-30** |
| B1 | Missing artifact definitions — all 24 built | High | 🔴 High | ✅ **Complete — 2026-05-30** |
| B2 | Artifact templates (all confirmed definitions → templates) | Very High | 🟠 High | 🟡 16/35+ done — in progress |
| B3 | Artifact examples (top 10) | Medium | 🟡 Medium | ❌ Not done |
| **Phase 1** | **docs/ documentation layer (9 files)** | Medium | 🟠 High | 🟡 **3/9 done — in progress** |
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

---

## 6. Recommended Session Order

1. **Session +1 (next):** Phase 1 continued — 6 remaining docs files (`how-to-use-artifacts.md`, `how-to-use-authority-routing.md`, `how-to-contribute.md`, `glossary.md`, `faq.md`, `changelog-guide.md`) + Phase B2 continued — A18, A20, A02, A03, A10 templates
2. **Session +2:** Phase 1 complete (if any remaining) + Phase B2 — A24, A25, A26, A13, A22 templates
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
| 1.0.0 | 2026-05-29 | Initial plan — 7 phases |
| 2.0.0 | 2026-05-30 | Full rebuild: MCP, AI agents, book, CI/CD, extended packs |
| 2.1.0 | 2026-05-30 | Skills inventory corrected — 47 core skills confirmed |
| 2.2.0 | 2026-05-30 | Phase A complete — 47 skills at v1.1.0 |
| 2.3.0 | 2026-05-30 | Phase B1 complete — artifact definitions confirmed |
| 2.4.0 | 2026-05-30 | 9 stale duplicates deleted · A05 duplicate resolved · B2 progress table added |
| 2.5.0 | 2026-05-31 | Phase 1 opened — 3 docs files committed. B2 Batch 3 started — A05 + A09 templates added. Documentation layer status table added. Scorecard and session order updated. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-31 · Version 2.5.0*
