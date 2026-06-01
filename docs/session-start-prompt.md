---
doc_id: DOC-SESSION-PROMPT
doc_name: PMOSkills AI Agent Session Start Prompt
version: "1.0.0"
status: Active
authority: PMBOK8 Primary
file_path: "docs/session-start-prompt.md"
---

# PMOSkills — AI Agent Session Start Prompt
**Version:** 1.0.0
**Date:** 2026-06-01
**Purpose:** Reusable prompt to paste at the start of any AI agent session working on the PMOSkills repository. Grounds the agent in authority, current state, quality rules, and task before any file is created or modified.

---

## How to Use

1. Copy the **Prompt Template** section below in full.
2. Replace only the `[…]` field in `### Session Task`.
3. Paste into your AI agent session as the opening message.
4. The agent must read the three authority files before doing any work.

Update only the version numbers in the Authority Order block when `QUALITY-STANDARDS.md`, `MASTER-PLAN.md`, or `COMPLETION-PLAN-V4.md` are bumped.

---

## Prompt Template

```
## PMOSkills Repository — Session Start

### Authority Order (read in this order before doing anything)
1. `QUALITY-STANDARDS.md` (v2.0.0) — single authority for all quality rules,
   YAML schemas, structure standards, naming conventions, quality gates,
   enforcement protocol (L1/L2/L3), and the AI Agent Pre-Commit Checklist (§9).
2. `MASTER-PLAN.md` (v4.4.1) — current state tracker: directory audit,
   gap audit, task lists, session log, scorecard.
3. `COMPLETION-PLAN-V4.md` (v4.1.0) — phase blueprint: entry conditions,
   deliverables, phase quality gates, dependency map, session protocol.

### Repository
https://github.com/fakhruldeen/PMOSkills
Owner: fakhruldeen | Default branch: main

### Session Task
[Describe exactly what to build or fix this session. Examples:
  - "Execute Phase 0 tasks P0-A and P0-B: verify C4 duplication then delete."
  - "Build SKL-01-01, SKL-01-02, SKL-01-03 (Pack 01 — Organizational Setup)."
  - "Build reference/companion-references/PMO-Practice-Guide.md."]

### Mandatory Operating Rules (non-negotiable)
1. Read `MASTER-PLAN.md` §8 session log first — confirm which tasks are done.
2. Read `QUALITY-STANDARDS.md` §9 AI Agent Pre-Commit Checklist before
   creating or modifying any file.
3. Look up the file type code in `QUALITY-STANDARDS.md` §1 before creating
   any file. Apply the correct YAML schema (§2), structure (§3), and naming
   pattern (§4) for that type.
4. Work one file at a time. Commit after each file.
5. Every commit message must follow the convention in `MASTER-PLAN.md` §2.3.
6. Run the full Pre-Commit Checklist (§9) on every file before committing.
   A file that fails any L1 check must NOT be committed.
7. Never cite PMBOK 8 without a specific section number (e.g., §2.3.4).
8. Never pre-fill a `[FIELD: ...]` placeholder in a template file.
9. All artifact examples must use the Meridian CRM System Upgrade scenario.
10. At session end: bump `MASTER-PLAN.md` version, add session log entry,
    update `CHANGELOG.md`.

### Phase Entry Condition Check
Before starting the session task, confirm:
- [ ] Entry condition for the target phase is satisfied (per
      `COMPLETION-PLAN-V4.md` §4)
- [ ] No L1 violations exist in files you will touch (per
      `QUALITY-STANDARDS.md` §8)
- [ ] Task is not already marked complete in `MASTER-PLAN.md` §7 scorecard

### Quality Gate Reminder
After completing all files in this session:
- Run the applicable phase gate from `QUALITY-STANDARDS.md` §7.5
- Log results in `MASTER-PLAN.md` session log
- If any gate check fails, file an NC entry in `QUALITY-STANDARDS.md` §8.3
  before closing the session
```

---

## Ready-to-Use Variants

### Variant A — Phase 0 Structural Cleanup

Replace the `### Session Task` block with:

```
### Session Task
Execute Phase 0 operations per MASTER-PLAN.md §5 Phase 0 task list.
Start with the first uncompleted task in the P0-A through P0-S sequence.
For each operation: confirm precondition, execute, verify, commit with
`chore(root):` prefix. Do not proceed to next operation until current
one is fully committed and verified.
```

### Variant B — Skill File Build

Replace the `### Session Task` block with:

```
### Session Task
Build full skill content for [SKILL-ID-LIST] ([Pack Name]).
Files go in skills/[pack-dir]/.
File type: SKL. Apply QUALITY-STANDARDS.md §2.1 YAML schema and §3.1
structure. Pass the §7.2 skill gate and §9 pre-commit checklist before
each commit. Authority for skill content: [PMI source + section].
```

### Variant C — Reference File Build

Replace the `### Session Task` block with:

```
### Session Task
Build [file path] in reference/[subdir]/.
File type: REF. Apply QUALITY-STANDARDS.md §2.5 YAML schema and §3.5
structure. Must include pmbok8_source: with specific section number.
Must include short-code from pmi_reference_list.md if a companion
reference. Pass §7.4 REF gate and §9 pre-commit checklist before commit.
```

### Variant D — Artifact Build

Replace the `### Session Task` block with:

```
### Session Task
Build artifact [ART-DEF / ART-TPL / ART-EX] for [Artifact ID and Name].
File goes in artifacts/[canonical-subdir]/.
Apply QUALITY-STANDARDS.md §2.2/§2.3/§2.4 YAML schema and §3.2/§3.3/§3.4
structure as applicable. Run the 5-question waste test (§7.3) before
committing the definition. Examples must use Meridian CRM scenario.
```

### Variant E — Quality Audit / NC Resolution

Replace the `### Session Task` block with:

```
### Session Task
Run Phase 7 quality audit on [file path or directory].
For each file: apply the universal gate (QUALITY-STANDARDS.md §7.1) and
the applicable per-type gate (§7.2–§7.4). Log any failures as NC entries
in QUALITY-STANDARDS.md §8.3. Fix all L1 violations before closing
the session. Log L2 violations and schedule resolution.
```

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-06-01 | Initial creation. Full prompt template + 5 variants (A–E). |

---

## Related Files

| File | Role |
|---|---|
| [`QUALITY-STANDARDS.md`](../QUALITY-STANDARDS.md) | Single quality authority — read first every session |
| [`MASTER-PLAN.md`](../MASTER-PLAN.md) | Current state tracker — session log, scorecard, task lists |
| [`COMPLETION-PLAN-V4.md`](../COMPLETION-PLAN-V4.md) | Phase blueprint — entry conditions, deliverables, gates |
| [`CHANGELOG.md`](../CHANGELOG.md) | Change log — update at session end |
| [`pmi_reference_list.md`](../pmi_reference_list.md) | 23 companion references — short-codes for citation |

---

*Authority: PMBOK8 Primary · Org-defined*
*Repository: https://github.com/fakhruldeen/PMOSkills*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-06-01 · Version 1.0.0*
