# Changelog

All notable changes to this repository are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Authority: PMBOK 8 Primary · PMI Companion References Secondary.

---

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
