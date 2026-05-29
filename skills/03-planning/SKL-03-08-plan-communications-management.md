# SKL-03-08 — Plan Communications Management
**Skill ID:** SKL-03-08  
**Skill Name:** Plan Communications Management  
**Version:** 1.0.0-draft  
**Lifecycle Pack:** 03-Planning  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-08-plan-communications-management.md`

---

## Purpose

Translate stakeholder information needs and engagement strategies — already defined in A07 — into a concrete, actionable communication architecture. The output is **A28 (Communications and Reporting Record)**, the single managed record that defines: who needs what information, in what format, through which channel, at what cadence, delivered by whom, and with what feedback route.

This skill operationalizes PMBOK8 §2.5.2.3 Plan Communications Management. It sits directly downstream of SKL-03-07 (Plan Stakeholder Engagement) and feeds everything needed to execute communications (SKL-Execute-Manage Communications) and monitor them (SKL-Monitor-Monitor Communications).

Communication planning is not a documentation exercise. Its purpose is to ensure that the right people receive the right information in time to act on it — and that the information flow actually supports the engagement levels defined in A07.

---

## Scope

**In scope:**
- Translating A07 engagement strategies and information needs into communication entries in A28
- Analyzing stakeholder communication requirements (what, when, format, channel, access level)
- Selecting communication technologies and methods per stakeholder context
- Designing reporting products (status reports, dashboards, briefings) for each audience
- Setting feedback routes for every communication entry
- Defining escalation paths and confidentiality constraints
- Aligning A28 with the schedule (A15) for timing of recurring communications
- Updating the Stakeholder Engagement Plan (A07) where communication design reveals new engagement decisions

**Out of scope:**
- Initial stakeholder identification → SKL-02-02
- Engagement strategy development → SKL-03-07 (must precede this skill)
- Actual communication delivery and execution → Executing-pack skill (Manage Communications)
- Monitoring whether communications are effective → Monitoring-pack skill (Monitor Communications)
- Detailed records retention rules → A34 (Information Retention and Records Control Record)

---

## Authority and Governance

| Field | Value |
|-------|-------|
| **Primary PMI Source** | PMBOK8 |
| **Exact Section** | Guide §2.5.2.3 Plan Communications Management · Guide Figure 2-35 · Guide §2.5.1 Key Concepts · Guide Figure 5-2 Communication Model for Cross-Cultural Communication |
| **Purpose of Citation** | Establish communications planning as a process that analyses stakeholder information needs and produces an actionable plan governing collection, distribution, format, and storage of project information |
| **Source Type** | PMI-derived |
| **Governance Layer** | Project Governance |
| **Artifact Produced** | A28 — Communications and Reporting Record |
| **Artifact Updated** | A07 — Stakeholder Register and Engagement Strategy (Stakeholder Engagement Plan updates) · A15 — Schedule Model (communication event additions) |
| **Owner** | Project Manager (or Communications Lead if assigned) |
| **Approval Authority** | Sponsor or governance body for high-sensitivity reporting models; routine updates managed by PM within thresholds |
| **Threshold Band** | T2 — reporting models that involve executive escalation, sensitive financial data, or external disclosure require sponsor awareness |
| **Escalate When** | Communication design requires access controls, legal review, multi-language production, or a formal external disclosure process beyond PM authority |

---

## Performance Domains and Principles

**Performance Domains:** Stakeholders · Governance  
**Focus Areas:** Planning · Executing · Monitoring and Controlling

| Principle | Application in This Skill |
|-----------|--------------------------|
| P5 Engage Stakeholders | Communication planning is the practical implementation layer of engagement planning — without it, engagement strategies exist only on paper |
| P2 Focus on Value | Every communication event must serve a decision, action, or relationship need; information produced without a purpose is waste |
| P8 Build Quality Into Processes | Communication quality is designed in at the planning stage — vague audience definitions and missing feedback routes are structural defects |
| P1 Adopt a Holistic View | Communication flows must account for cross-cultural, cross-organizational, and cross-domain interactions; a siloed view produces information gaps |
| P7 Embrace Adaptability | Communications plans are updated when stakeholder needs change, the schedule changes, or monitoring signals a failure in information flow |

---

## PMBOK 8 Process: Plan Communications Management

### Inputs (per PMBOK8 Guide Figure 2-35)

| Input | Artifact / Source | Mandatory? | Notes |
|-------|------------------|-----------|-------|
| Project charter | A04 | Yes | Sponsor identity, PM authority, project purpose, and initial stakeholder context |
| Resource management plan | A26 — Resource Capacity and Acquisition Record | Recommended | Identifies who on the team is available to produce, review, and distribute communications |
| **Stakeholder engagement plan** | **A07 — Stakeholder Register and Engagement Strategy** | **Yes — Primary Input** | Engagement strategies, information needs, current and target engagement levels; this is the primary driver of all communication decisions |
| Requirements documentation | A08 — Scope and Requirements Decision Record | Recommended | Stakeholder information requirements identified during requirements elicitation may surface specific communication needs |
| Stakeholder register | A07 (identification section) | Yes | Stakeholder details, roles, contact information, organizational position — foundational for audience mapping |
| Enterprise environmental factors (EEFs) | A05 — Context Register | Yes | Organizational culture, communication norms, approved tools and platforms, language preferences, geographic distribution, political sensitivities |
| Organizational process assets (OPAs) | A05 — Context Register | Yes | Communication templates, lessons from prior projects, reporting standards, approved channels, confidentiality policies |
| Project management plan (other components) | A14 — Integrated PM Plan | Recommended | On re-runs: other subsidiary plans may constrain or shape communication design (risk plan affects risk reporting, change process affects notification rules) |

### Tools and Techniques (per PMBOK8 Guide Figure 2-35)

| Tool / Technique | When to Use | Output |
|-----------------|------------|--------|
| **Expert judgment** | Always — PM applies knowledge of the stakeholder landscape, organizational politics, and communication culture | Informed, context-sensitive communication design |
| **Communication requirements analysis** | Always — the core analytical technique of this skill | List of information needs matched to audiences, formats, cadence, and channels |
| **Communication technology** | Always — determines which tools and platforms are appropriate for each communication type | Technology selection per audience segment |
| **Communication models** | When cross-functional, cross-cultural, or cross-organizational communication is involved | Communication model design that accounts for noise, encoding, decoding, and feedback |
| **Communication methods** | Always — classifies each communication as interactive, push, or pull | Method classification per entry in A28 |
| **Interpersonal and team skills — Communication styles assessment** | When stakeholder preferences, cultural context, or organizational hierarchy affect how information should be presented | Adjusted format and tone for each audience |
| **Interpersonal and team skills — Political awareness** | When high-stakes stakeholders require careful framing, sequencing, or confidentiality handling | Sensitivity flags applied to relevant A28 entries |
| **Interpersonal and team skills — Cultural awareness** | When distributed teams or stakeholders span different national or organizational cultures | Language, tone, and format adjustments per audience |
| **Data representation — Stakeholder Engagement Assessment Matrix** | When validating that communication design supports the engagement approach defined in A07 | Confirmation that channel and cadence choices align with desired engagement levels |
| **Meetings** | For complex projects or when communication architecture needs stakeholder input or sponsor validation | Validated communication design prior to A28 baseline |

#### Communication Requirements Analysis — Core Technique

This analysis drives every entry in A28. For each stakeholder or group, answer the following questions:

| Question | Output |
|----------|--------|
| What information does this stakeholder need? | Information category and content description |
| Why do they need it? | Decision, awareness, action, or compliance need |
| When do they need it? | Date, milestone, phase gate, sprint event, or on-demand |
| How frequently? | One-time, recurring (daily/weekly/monthly), triggered by event |
| In what format? | Dashboard, written report, briefing deck, verbal update, email, meeting |
| Through which channel? | Email, PMIS, video call, face-to-face, portal, messaging platform |
| What access level applies? | Open, project-team-only, sponsor-only, external-controlled |
| Who produces or sends it? | Named sender or role — not "the PM" generically |
| What is the feedback or response route? | How does the stakeholder respond, raise questions, or request changes? |
| Is there a confidentiality constraint? | Any legal, contractual, or organizational restriction on disclosure |

#### Communication Methods Classification

| Method | Description | Use Case |
|--------|-------------|---------|
| **Interactive** | Real-time, two-way exchange between two or more parties | Meetings, video calls, phone calls, facilitated workshops — use when speed, nuance, or negotiation is needed |
| **Push** | Information sent to stakeholders without requiring them to seek it | Emails, status reports, memos, briefing packs — use for routine updates to defined audiences |
| **Pull** | Information stored centrally; stakeholders access it on demand | PMIS portals, intranets, document repositories — use for reference material, templates, large files |

> A well-designed communications plan uses all three methods. Heavy reliance on push-only communication is a common design failure — it produces information without confirming receipt, comprehension, or action.

#### Communication Technology Selection Criteria

Not all platforms are appropriate for all audiences. Apply the following criteria when selecting technology:

| Criterion | Consideration |
|-----------|-------------|
| **Urgency of information** | Real-time issues require interactive or immediate push methods; reference material suits pull |
| **Availability of technology** | Confirm that all intended recipients have access to the selected platform |
| **Geographic distribution** | Distributed teams and stakeholders require asynchronous options or time-zone-aware scheduling |
| **Project environment and sensitivity** | Sensitive or confidential content must not pass through unsecured or unapproved channels |
| **Ease of use** | Technology that requires significant training or is unfamiliar to stakeholders increases communication failure risk |
| **Organizational standards** | Preferred platforms from OPAs (A05) should be used unless a specific need justifies deviation |

### Outputs (per PMBOK8 Guide Figure 2-35)

| Output | Artifact ID | Description |
|--------|------------|-------------|
| **Communications management plan** | **A28 — Communications and Reporting Record** | Primary output — full audience map with information need, channel, format, cadence, sender, feedback route, and access level |
| **Stakeholder engagement plan updates** | A07 (updated) | Communication design may reveal new engagement decisions; A07 must reflect any changes (e.g., a newly identified communication channel creates an engagement opportunity) |
| **Project document updates** | A15 (schedule entries) · A07 (engagement updates) | Communication events are added to the project schedule; schedule constraints may shape communication timing |

---

## Instructions

### Step 1 — Confirm Prerequisites

Before starting, verify:

- [ ] A07 is fully populated — both the Identification section (from SKL-02-02) and the Engagement Strategy section (from SKL-03-07)
- [ ] Every stakeholder in A07 has a defined engagement approach and at least one named engagement action
- [ ] A04 (Project Charter) is available
- [ ] A05 (Context Register) is available with EEF and OPA content

If A07 engagement strategies are incomplete, **return to SKL-03-07** before proceeding.

### Step 2 — Extract Information Needs from A07

For every stakeholder or group in A07:

1. Review the engagement approach (Inform / Consult / Involve / Collaborate / Empower)
2. Identify the information each approach implies:
   - **Inform** → status updates, milestone notifications, decisions made, changes approved
   - **Consult** → draft documents for review, request for input, feedback forms, review meetings
   - **Involve** → working sessions, workshops, co-creation sessions, prototype reviews
   - **Collaborate** → shared decision forums, joint planning sessions, real-time workspaces
   - **Empower** → delegation notifications, authority confirmations, performance visibility tools
3. Identify any specific information requests stated in A07 (e.g., "Finance Lead requires weekly cost variance report")
4. Note any confidentiality, language, access, or cultural constraints noted in A07 or A05

**Output of this step:** A stakeholder-by-stakeholder list of information needs, ready for conversion into A28 entries.

### Step 3 — Apply Communication Requirements Analysis

For each information need identified in Step 2, work through the ten-question analysis in the core technique above. This produces the raw content for each A28 row.

**Critical check — Purpose alignment:** Every communication must have a clear purpose. Apply this filter:
- If the purpose is "keep them informed" → define what decision or awareness outcome that information serves
- If no specific outcome can be stated → challenge whether the communication should exist at all
- If the communication is purely compliance-driven (governance reporting, regulatory notification) → mark it as mandatory regardless of strategic value

### Step 4 — Classify Each Communication by Method

Apply the Interactive / Push / Pull classification to each entry:

- Interactive methods require scheduling (add to A15)
- Push methods require a sender, cadence, and distribution list
- Pull methods require a storage location, access control, and version management approach

> **Avoid the push-only trap:** A communications plan consisting entirely of status email blasts, with no interactive or pull components, is a structural defect. It produces information delivery without confirmation of receipt or value.

### Step 5 — Select Communication Technology

For each entry, select the delivery technology against the six criteria in the core technique section. Document the rationale for any deviation from organizational standards (OPAs in A05).

**Access-level assignment:** Assign one of the following access levels to each entry:
- **Open** — available to all project stakeholders
- **Team-only** — restricted to project team members
- **Sponsor-only** — restricted to sponsor and named governance stakeholders
- **External-controlled** — involves parties outside the organization; requires additional handling rules
- **Confidential** — legally or contractually restricted; document specific handling rules

### Step 6 — Apply Communication Model Thinking for High-Risk Entries

For any communication entry involving:
- Cross-cultural or multi-language stakeholders
- High-power resistant stakeholders
- Regulatory or external audiences
- Complex technical content translated for non-technical executives

Apply the PMBOK8 Communication Model (Guide Figure 5-2):

| Model Element | Action Required |
|--------------|----------------|
| **Sender encoding** | Is the message framed correctly for the recipient's context, language, and knowledge level? |
| **Channel/medium selection** | Is the channel free of significant noise (distortion, technical barriers, language gaps)? |
| **Receiver decoding** | Will the receiver interpret the message as intended? Is confirmation of understanding planned? |
| **Feedback** | How does the receiver signal receipt, understanding, or disagreement? Is there a response route? |
| **Noise identification** | What could distort this message (language, culture, political context, information overload)? |

Document the noise risks and mitigation for any flagged communication entry.

### Step 7 — Design Reporting Products

For each stakeholder audience that requires a reporting product (status report, dashboard, executive briefing, risk report, financial summary), design the product:

| Reporting Product Field | Guidance |
|------------------------|---------|
| **Product name** | Specific name: e.g., "Weekly Project Status Report," "Monthly Executive Dashboard," "Sprint Review Summary" |
| **Primary audience** | Named audience segment from A07 |
| **Content sections** | What sections must appear: progress, schedule variance, financial variance, risks, decisions needed, action items |
| **Level of detail** | Executive summary (1 page) vs. detailed management report vs. team-level operational view |
| **Format** | Email text, PDF report, presentation slide deck, live dashboard, verbal briefing, shared portal page |
| **Production owner** | Named person responsible for preparing the product each cycle |
| **Review and approval before distribution** | Is review required before sending? Who reviews? How long does review take? |
| **Cadence** | Frequency and timing relative to schedule milestones, governance meetings, or sprint events |
| **Distribution list** | Explicit list — not "all stakeholders" |
| **Feedback mechanism** | How recipients comment, question, or escalate concerns about this product |

### Step 8 — Build the Communication Architecture in A28

Populate A28 with one row (or record set) per communication entry. The minimum complete entry has all core fields populated:

| Field | Mandatory? | Guidance |
|-------|-----------|---------|
| **Stakeholder / audience** | Yes | Named person, role, or group from A07 |
| **Information need** | Yes | Specific content description, not just a category label |
| **Purpose** | Yes | Decision, awareness, action, compliance, or feedback |
| **Communication method** | Yes | Interactive / Push / Pull |
| **Channel and format** | Yes | Platform and document/communication type |
| **Cadence / timing** | Yes | Frequency, specific dates, milestones, or event triggers |
| **Sender / owner** | Yes | Named individual responsible for production and delivery |
| **Feedback / response route** | Yes | How the receiver acknowledges, responds, or escalates |
| **Access level** | Yes | Open / Team-only / Sponsor-only / External-controlled / Confidential |
| **Confidentiality constraints** | Conditional | Required for any entry marked External-controlled or Confidential |
| **Language / cultural notes** | Conditional | Required when cross-cultural or multi-language communication is involved |
| **Technology / platform** | Yes | Named tool or medium; must be on the approved list or deviation documented |
| **Record storage location** | Recommended | Where the communication artifact is archived or accessible |
| **Last reviewed date** | Yes | Tracks currency for monitoring and re-run control |

### Step 9 — Add Communication Events to the Schedule

For every **interactive** communication and every **push communication with a fixed deadline**, create or confirm an entry in A15 (Schedule Model and Baseline Record):

- Recurring governance meetings (weekly, monthly, quarterly steering)
- Phase gate reviews and briefings
- Sprint Review, Sprint Planning, Daily Standups (adaptive)
- Stakeholder-specific required briefings timed to decision points
- Regulatory or contractual notification deadlines

> **Timing rule:** Communication events that are intended to influence a decision must be scheduled **before** the decision event — not after. Retrospective communication of a decision that was made without stakeholder input destroys engagement value.

### Step 10 — Update A07 with Communication-Driven Engagement Insights

Review whether communication design has surfaced any new engagement decisions:

- Did a channel or format choice reveal a better engagement opportunity than the strategy in A07?
- Did technology or access constraints reveal that a proposed engagement action is not feasible?
- Did the communication requirements analysis identify a stakeholder information need not captured in A07?

If yes → update A07 accordingly. A07 and A28 must remain internally consistent at all times.

### Step 11 — Validate the Plan and Present for Awareness

Before baselining A28:

- [ ] Every stakeholder in A07 has at least one communication entry in A28
- [ ] No communication entry exists in A28 for an audience not in A07 (would indicate an unidentified stakeholder)
- [ ] All interactive events are on the schedule (A15)
- [ ] All high-power stakeholders have their communication entries confirmed with them or the sponsor
- [ ] No communication entry is missing a feedback route
- [ ] Confidentiality and access controls are applied to all sensitive entries

Present the completed A28 to the sponsor for awareness, particularly:
- Executive reporting products and their cadence
- Any external or regulatory communication obligations
- Any high-sensitivity communications involving confidential content

---

## Tailoring Guidance

| Context | Tailoring Decision |
|---------|-------------------|
| Small, low-complexity project | A28 may be a simple one-page communication matrix embedded in A07; no separate document needed; reduce mandatory fields to: audience, information need, channel, cadence, sender |
| Agile / adaptive project | Communication is primarily event-driven (Sprint Review, Daily Standup, Planning, Retrospective); A28 captures the cadence of ceremonies as communication events; pull methods dominate (backlog visibility, dashboard); reporting products are typically lightweight and iterative |
| Large predictive project | Full A28 with detailed entries per audience; formal reporting products for each governance tier; explicit confidentiality and access controls; PM may need a Communications Lead as production owner |
| Multi-language / cross-cultural project | Communication model analysis (Step 6) is mandatory for all cross-cultural entries; language access levels must be assigned; translation needs must be resourced and scheduled |
| External client-facing project | Communication entries with the client have contractual implications; timing, format, and approval-before-distribution rules must align with contract terms; document in A31 (Procurement and Supplier Management Record) as well |
| Highly regulated project | Regulatory notification entries are mandatory and not subject to tailoring; timing is compliance-driven; escalation and documentation rules apply |
| Transformation / high-change project | A28 and A29 (Change Readiness and Adoption Record) must be designed together; communication about change must be timed to readiness actions |

**Do not tailor away:**
- Feedback route on every communication entry (P8 — design quality)
- Communication timing aligned to decision points (P2 — value focus)
- Access-level assignment on all entries (information security and governance)
- At least one communication entry per stakeholder in A07 (completeness check)

---

## Failure Cases

| Failure | Indicator | Corrective Action |
|---------|-----------|-----------------|
| A07 not fully populated before A28 is built | Communication entries exist for stakeholders with no engagement strategy | Return to SKL-03-07; A28 must be downstream of A07, not parallel |
| Communication entries without a feedback route | A28 rows end with "send weekly email" — no response mechanism defined | Add a feedback route to every entry; push-only design without feedback is incomplete |
| Communication events not on the schedule | Interactive meetings and fixed-deadline reports not in A15 | Add all schedule-relevant communication events to A15 |
| Communication intended to influence a decision is scheduled after the decision | Status report to the steering committee arrives after the phase gate | Reschedule to precede the decision event |
| All communications classified as Push | A28 consists entirely of email and status reports | Review whether interactive and pull methods are needed; redesign accordingly |
| No access-level assignment | All entries marked "Open" without analysis | Re-apply Step 5 to assign appropriate access controls |
| Separate communications plan document maintained outside A28 | A28 and a "Communications Management Plan.docx" both exist | Merge into A28; retire the standalone document (waste rule §3.2) |
| A28 not updated after A07 is updated | A07 engagement strategy changes but A28 still reflects old approach | Re-run triggered by A07 update; the two must remain consistent |
| Communication plan produced without OPA reference | Standard templates, preferred channels, and lessons from prior projects not used | Re-apply Step 3 with A05 OPA content explicitly reviewed |
| No escalation path defined for any entry | A28 has information flow but no route for raising concerns, disputes, or urgent issues | Add an escalation path to at least governance-tier and high-power stakeholder entries |

---

## Outputs Produced by This Skill

| Output | Location | Notes |
|--------|---------- |-------|
| A28 — Communications and Reporting Record (baselined) | `artifacts/templates/A28-communications-reporting-record.md` | Full audience map with all core fields populated |
| A07 updates | Stakeholder Register and Engagement Strategy | Any communication-driven engagement insights incorporated |
| A15 updates | Schedule Model and Baseline Record | Interactive and fixed-deadline communication events added |
| A14 reference update | Integrated PM Plan (subsidiary plan index) | A28 is now the referenced communications management plan subsidiary |

---

## Re-Run Schedule

| Trigger | Re-Run Type |
|---------|------------|
| Phase gate (predictive) | Full re-run; reporting products and cadence must reflect the new phase's audience needs |
| Sprint / iteration start (adaptive) | Lightweight check; confirm ceremonies are still aligned with stakeholder needs; update if backlog or team composition has changed |
| New stakeholder identified (SKL-02-02 re-run) | Targeted addition of new communication entries for the new stakeholder |
| A07 engagement strategy updated (SKL-03-07 re-run) | Targeted update to align A28 with the revised engagement approach |
| Communication monitoring signals a failure (Monitor Communications) | Targeted re-run for the failing communication; root cause; redesign entry |
| Major change approved affecting scope, schedule, or stakeholder authority (A12) | Partial re-run for affected stakeholders |
| Project enters deployment or transition phase | Full re-run; end-user and operational audience communication needs become primary |
| Technology platform changes (approved in A06) | Update affected A28 entries; re-confirm access controls |

---

## Integration Points

| Connected Artifact or Skill | Relationship |
|----------------------------|-------------|
| A04 Project Charter | Input — sponsor identity and project context |
| A05 Context Register | Input — EEFs (culture, language, approved platforms) and OPAs (templates, lessons, communication standards) |
| A07 Stakeholder Register and Engagement Strategy | **Primary input** — engagement strategies and information needs drive all A28 entries; also updated as output |
| A08 Scope and Requirements Decision Record | Input — stakeholder information requirements identified during requirements analysis |
| A12 Change and Exception Decision Log | Input on re-runs — approved changes that affect communication obligations |
| A14 Integrated Project Management Plan | Downstream — A28 is the referenced communications management plan subsidiary |
| A15 Schedule Model and Baseline Record | Bidirectional — communication events are added to the schedule; schedule constraints shape communication timing |
| A18 Issue, Impediment, and Action Log | Input on re-runs — open issues may indicate communication failures |
| A19 Risk Management Record | Input — communication-related risks (e.g., language barriers, information security breach) may feed into A19 |
| A26 Resource Capacity and Acquisition Record | Input — confirms who has capacity to produce and distribute communications |
| A29 Change Readiness and Adoption Record | Downstream (transformation projects) — communication design for change-impacted stakeholders must align with adoption actions |
| A31 Procurement and Supplier Management Record | Cross-reference for external client/supplier communication entries that carry contractual obligations |
| A34 Information Retention and Records Control Record | Downstream — communication artifacts require defined retention and archival rules |
| SKL-02-02 | Upstream prerequisite (two levels) — stakeholder identification must exist before engagement planning |
| SKL-03-07 | **Upstream prerequisite** — A07 engagement strategies are the primary input; must be complete before this skill runs |
| SKL-Execute-Manage Communications | Downstream — executes the delivery plan defined here |
| SKL-Monitor-Monitor Communications | Downstream — measures whether information flow is working and triggers re-runs |

---

## Tests

### Test T-1: A07 Prerequisite Check
**Given:** A07 exists but engagement strategies are not yet populated (only identification section complete)  
**When:** SKL-03-08 is initiated  
**Then:** Skill must block execution and return a prerequisite failure; A07 must have SKL-03-07 output before A28 can be built

### Test T-2: Complete Coverage Check
**Given:** A07 lists eight stakeholders/groups with completed engagement strategies  
**When:** A28 is baselined  
**Then:** Every stakeholder in A07 must have at least one entry in A28; any stakeholder with zero entries is a coverage failure

### Test T-3: No Orphan Entries
**Given:** A28 contains an entry for "PMO Director" but "PMO Director" does not appear in A07  
**When:** A28 validation is run  
**Then:** Skill must flag the orphan entry and require either adding the stakeholder to A07 (triggering SKL-02-02 re-run) or removing the A28 entry

### Test T-4: Feedback Route Mandatory
**Given:** An A28 entry reads: "Weekly status email to Finance Lead — sent by PM every Monday"  
**When:** Completeness check is applied  
**Then:** Entry must fail for missing feedback route; skill must require addition of a response mechanism (e.g., reply to PM email, raise issue in weekly meeting, comment in PMIS portal)

### Test T-5: Push-Only Design Rejection
**Given:** A28 for a 12-stakeholder project contains 14 entries, all classified as Push  
**When:** Method balance check is applied  
**Then:** Skill must flag the push-only design; PM must confirm whether any interactive or pull entries are appropriate, and document rationale if push-only is intentional

### Test T-6: Schedule Alignment Check
**Given:** A28 includes a "Monthly Steering Committee Briefing" classified as Interactive  
**When:** Schedule cross-reference check is applied  
**Then:** The briefing must appear in A15 as a scheduled recurring event; if it is absent from A15, skill must flag the gap

### Test T-7: Pre-Decision Timing Check
**Given:** A28 includes a "Phase 2 Readiness Report" to the Sponsor; the Phase 2 kickoff gate is scheduled for Week 8; the report is scheduled for Week 9  
**When:** Decision-alignment check is applied  
**Then:** Skill must flag the timing failure; the report must be rescheduled to Week 7 or earlier

### Test T-8: Access Level Assignment
**Given:** A28 entry for "Board Financial Summary" has access level "Open"  
**When:** Access-level review is applied  
**Then:** Financial reporting to a board-level audience must be assessed for restricted access; "Open" for board-level financial data must be challenged; if the access level is intentionally Open, the PM must confirm and document the rationale

### Test T-9: Waste Check — Duplicate Document
**Given:** A28 (Communications and Reporting Record) is maintained alongside a separate "Communications Management Plan v2.docx"  
**When:** Waste check is applied  
**Then:** Skill must flag the duplicate; recommend merge; retire the separate document per §3.2 consolidation rule

### Test T-10: Cross-Cultural Entry Check
**Given:** A28 includes communication with an Arabic-speaking regulatory body; the entry shows "Email in English" with no language or cultural note  
**When:** Cross-cultural check is applied (Step 6)  
**Then:** Skill must require a communication model analysis for this entry; the entry must document: language availability, translation plan if needed, and confirmation-of-understanding route

---

## Examples

### Example A — Predictive IT Migration (Full Plan)

**Excerpt from A28 after SKL-03-08 execution:**

| Audience | Information Need | Purpose | Method | Channel / Format | Cadence | Sender | Feedback Route | Access |
|---------|-----------------|---------|--------|-----------------|---------|--------|---------------|--------|
| VP Operations (Sponsor) | Progress summary, milestone status, decisions needed, key risks | Governance oversight and sponsor decisions | Interactive + Push | Monthly 30-min briefing + one-page written summary | Monthly — 5 days before steering meeting | PM | Direct response in meeting; follow-up email within 48h | Sponsor-only |
| IT Director | Technical progress, resource status, dependency blockers | Operational coordination | Interactive | Weekly 30-min sync call | Wednesdays 10:00 AM | PM | Verbal in meeting; action log updated after | Team-only |
| Finance Team Lead | Schedule and cost variance | Budget awareness and approval triggers | Push | Bi-weekly cost variance email | Every 2nd Friday | PM | Reply to PM with any queries within 3 business days | Team-only |
| End Users — Ops Staff | Migration timeline, training schedule, what changes for them | Awareness and readiness for change | Push + Pull | Email update + FAQ page on intranet | Monthly email; FAQ updated weekly | PM + IT Director | Survey link at bottom of email; IT helpdesk for questions | Open |
| Compliance Officer | Data privacy impact assessment status, compliance signoffs | Compliance oversight | Push + Interactive | Monthly status note + ad-hoc review meeting if issues arise | Monthly or as triggered | PM | Email response required within 5 business days; escalation to VP if unresolved | External-controlled |

---

### Example B — Adaptive Digital Product (Sprint-Based)

**Communication Architecture for A28:**

| Audience | Communication Type | Method | Cadence / Event | Format |
|---------|-------------------|--------|----------------|--------|
| Product Owner | Sprint Planning | Interactive | Start of each sprint | Facilitated session |
| Product Owner | Daily Standup | Interactive | Daily | 15-min standup |
| Product Owner + Stakeholders | Sprint Review | Interactive | End of each sprint | Demo + discussion session |
| Delivery Team | Sprint Retrospective | Interactive | End of each sprint | Facilitated retrospective |
| Sponsor | Sprint Outcome Summary | Push | Within 2 days of Sprint Review | Email with increment summary and value delivered |
| Marketing Lead | Feature Release Notes | Push + Pull | Per feature release | Email notification + product changelog in portal |
| Legal Counsel | Compliance Impact Review | Interactive | As triggered — minimum once per quarter | Ad-hoc meeting when regulatory content is in scope |

---

### Example C — Communication Model Application (Cross-Cultural Entry)

**Entry:** Communication with Egyptian regulatory authority (Arabic-speaking)

**Communication Model Analysis:**
- **Sender encoding:** Regulatory submissions are technical; PM must ensure language is formal, clear, and legally precise
- **Channel:** Formal written channel (official submission portal or registered correspondence); no informal email
- **Noise risks:** Language difference (English → Arabic translation required); regulatory terminology may not map directly; cultural formality expectations (formal address, titles)
- **Receiver decoding:** Confirm that translation is reviewed by a qualified legal translator, not automated translation
- **Feedback route:** Formal written acknowledgment required; escalation path if no response within the required compliance window
- **Action in A28:** Entry marked External-controlled; legal review required before submission; named translation resource assigned; PM notified of any response within 24 hours

---

## Core Fields Reference — A28 Communications and Reporting Record

| Field | Mandatory | Type |
|-------|----------|------|
| Stakeholder / audience | Yes | Text — named individual, role, or group |
| Information need | Yes | Text — specific content description |
| Purpose | Yes | Category — Decision / Awareness / Action / Compliance / Feedback |
| Communication method | Yes | Classification — Interactive / Push / Pull |
| Channel and format | Yes | Platform + document or communication type |
| Cadence / timing | Yes | Frequency, date pattern, or event trigger |
| Sender / production owner | Yes | Named individual or role |
| Feedback / response route | Yes | How receiver acknowledges, responds, or escalates |
| Access level | Yes | Open / Team-only / Sponsor-only / External-controlled / Confidential |
| Confidentiality constraints | Conditional | Required when access is External-controlled or Confidential |
| Language / cultural notes | Conditional | Required for cross-cultural or multi-language entries |
| Technology / platform | Yes | Named tool; deviation from OPA standard documented |
| Record storage location | Recommended | Archive location or portal path |
| Last reviewed date | Yes | Date of most recent review or update |

---

## Companion References

| Alias | Source | Relevant Section |
|-------|--------|-----------------|
| PMBOK8 | PMBOK Guide 8th Edition | §2.5.2.3 Plan Communications Management · Figure 2-35 · §2.5.1 Key Concepts · Figure 5-2 Communication Model |
| PMBOK8 | The Standard for Project Management | §3.7 P5 Engage Stakeholders · §3.3 P2 Focus on Value · §3.10 P8 Build Quality |
| Process-Groups | Process Groups Practice Guide | Planning Process Group · Plan Communications Management |
| PMI-BA | Business Analysis Practice Guide | Stakeholder communication requirements |
| Forms-Book | PMI Practice Standard Forms | Communications matrix reference |

---

*Source Type: PMI-derived*  
*Governance Layer: Project Governance*  
*Authority: PMBOK8 §2.5.2.3 · Figure 2-35 · Standard §3.7 P5*  
*Linked Artifact: A28 — Communications and Reporting Record · A07 (updated) · A15 (updated)*  
*Related Skills: SKL-03-07 · SKL-Execute-Manage Communications · SKL-Monitor-Monitor Communications*  
*Re-run: Yes — periodic; triggered by phase gates, A07 updates, monitoring signals, and change events*
