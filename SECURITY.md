# Security Policy

## Scope

The PMO Skills Repository is a **knowledge and documentation repository** containing Markdown files, structured PM frameworks, artifact definitions, and skill instructions. It does not contain application code, authentication systems, APIs, databases, or executable software in production use.

However, this repository may contain:
- Configuration references for tool integrations (MCP server, CI/CD pipelines)
- Access control model definitions
- Future MCP server tool schemas and endpoint definitions

---

## Supported Versions

| Version | Supported |
|---------|----------|
| 1.3.x (current) | ✅ Active |
| < 1.3.0 | ❌ No longer maintained |

---

## What to Report

Please report any of the following if discovered in this repository:

- Accidentally committed secrets, tokens, API keys, or credentials
- Sensitive personal information (PII) committed in any file
- Malicious content introduced via a pull request or commit
- Tool integration configurations that expose sensitive endpoints
- Any content in `reference/`, `shared/`, or skill files that could be exploited if used as AI agent instructions (prompt injection patterns, jailbreak attempts, etc.)

---

## How to Report

**Do not open a public GitHub issue for security vulnerabilities.**

Report security concerns through one of these channels:
1. **GitHub Private Vulnerability Reporting** — use the “Report a vulnerability” button on the [Security tab](../../security/advisories/new) of this repository
2. **Direct contact** — contact the repository maintainer directly via GitHub profile

Include in your report:
- File path(s) affected
- Description of the issue
- Potential impact
- Suggested remediation (if known)

---

## Response Commitment

| Action | Target Timeline |
|--------|----------------|
| Acknowledge report | Within 48 hours |
| Initial assessment | Within 5 business days |
| Remediation (if confirmed) | Within 14 days for critical issues |
| Disclosure | Coordinated with reporter |

---

## Secret Scanning

This repository has GitHub secret scanning enabled. Any accidentally committed credentials will be automatically flagged. If you receive a secret scanning alert:
1. Immediately revoke the exposed credential at the source
2. Remove the secret from git history using `git filter-repo` or BFG Repo Cleaner
3. Force-push the cleaned history
4. Notify the maintainer

---

## AI Agent and MCP Server Considerations

This repository is designed to be used as a knowledge source for AI agents and MCP servers. When contributing content that will be used as agent instructions or tool schemas:
- Do not include prompt injection patterns
- Do not include instructions that could cause an AI agent to bypass governance rules
- Flag any content that could be misinterpreted by an LLM with a `# AGENT-NOTE:` comment

---

*PMO Skills Repository · Security Policy v1.0 · Last Updated: 2026-05-30*
