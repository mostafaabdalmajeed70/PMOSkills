# Contributing to PMO Skills Repository

Thank you for your interest in contributing. This repository is the authoritative PMO reference grounded in PMI PMBOK 8th Edition. All contributions must maintain that standard.

---

## Before You Contribute

1. Read the [Code of Conduct](CODE_OF_CONDUCT.md)
2. Read the [Security Policy](SECURITY.md)
3. Review `SKILL-REGISTRY.md` to understand the current state of the repository
4. Review `README.md` for repository structure and authority model
5. Review `source-authority.md` for the source hierarchy rules

---

## Authority Rules

All contributions must respect the source authority order:

| Priority | Source | Usage |
|----------|--------|-------|
| 1 | PMBOK8 — Standard + Guide 8th Edition | Primary authority for all PM content |
| 2 | PMI Companion References (see `pmi_reference_list.md`) | Supporting references |
| 3 | Organization-defined methods | Explicitly labeled as such |

**Never introduce content that contradicts PMBOK 8 without explicit labeling as an alternative interpretation or organization-defined method.**

---

## What You Can Contribute

| Type | Description |
|------|-------------|
| 🐛 Bug fix | Factual error, broken link, incorrect PMBOK reference, schema inconsistency |
| 📝 Content addition | New artifact definition, reference file, checklist, or validator |
| ⚙️ Structure improvement | Folder organization, naming consistency, index updates |
| 🧪 Test cases | Skill test cases following the schema in `tests/README.md` |
| 📖 Reference layer | Principle, domain, process, or I/O files under `reference/` |
| 🛠️ Shared components | Validators, routing logic, checklists under `shared/` |

---

## Contribution Workflow

### 1. Open an Issue First
For anything beyond a minor typo fix, open an issue before starting work. Use the appropriate issue template:
- `bug_report.md` — for errors or inaccuracies
- `content_addition.md` — for new content proposals
- `improvement.md` — for structural or quality improvements

### 2. Fork and Branch
```
git checkout -b [type]/[short-description]
```
Branch naming conventions:
- `fix/` — bug fixes and corrections
- `feat/` — new content or features
- `docs/` — documentation improvements
- `test/` — test case additions
- `refactor/` — structural changes without content change

### 3. Make Your Changes
- Follow the file naming convention: `A##-kebab-case.md` for artifacts, `SKL-PP-NN-kebab-case.md` for skills
- Follow semantic versioning for any versioned files
- Cite PMBOK 8 section references explicitly (e.g., `PMBOK8 Guide §2.1.6.2`)
- Label all non-PMI content as `synthesis` or `organization-defined`

### 4. Submit a Pull Request
- Use the pull request template
- Reference the related issue number
- Complete all checklist items before requesting review
- Keep PRs focused — one logical change per PR

---

## Content Quality Standards

All content contributions must:
- [ ] Cite the specific PMBOK 8 section (e.g., `§2.3.2.1`) or companion reference
- [ ] Use consistent terminology matching the PMBOK 8 Lexicon
- [ ] Follow the artifact or skill schema defined in the relevant README
- [ ] Not duplicate content already present in another file (cross-reference instead)
- [ ] Include a `Last Updated` and `Patch` label at the bottom of the file
- [ ] Pass a basic consistency check against `SKILL-REGISTRY.md` if adding/modifying a skill

---

## Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org):

```
<type>(scope): short description

[optional body]
[optional footer]
```

**Types:** `feat` · `fix` · `docs` · `chore` · `refactor` · `test`

**Examples:**
```
feat(artifacts): add A09 quality management plan definition
fix(skills): correct PMBOK8 section reference in SKL-03-06
docs(reference): add P04-value principle file
```

---

## What Will Be Rejected

- Content not grounded in PMI sources (unless explicitly labeled)
- Duplicate files or content already covered elsewhere
- PRs that mix unrelated changes
- Files that do not follow naming conventions
- Contributions that introduce terminology inconsistent with PMBOK 8

---

## Questions?

Open a GitHub Discussion or tag the issue with `question`. We’re here to help you contribute effectively.

---

*PMO Skills Repository · Authority: PMBOK 8 Primary · Version: 1.3.0*
