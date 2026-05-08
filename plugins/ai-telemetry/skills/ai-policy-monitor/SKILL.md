---
name: ai-policy-monitor
description: "Turn AI policy into telemetry checks, dashboards, alerts, exception reviews, or governance questions. Use when the user asks how logs support AI policy, how security can understand AI usage, how to detect risky AI behavior, how to enforce acceptable-use rules, or how to map a policy document to observable AI telemetry."
---

# AI Policy Monitor

Help transform AI policy from a static document into a feedback loop.

## Core Principle

Do not claim a policy can be enforced unless the required behavior is observable. Logging is the foundation for policy because it can answer:

- Who is using AI?
- With what tools?
- Against what data?
- With which permissions?
- What left the boundary?
- What was blocked or rejected?
- What exceptions need review?

## Policy Mapping Workflow

1. Read the policy or the user's stated rules.
2. Convert each rule into an observable question.
3. Map each question to telemetry fields, events, traces, or missing data.
4. Mark each rule as observable, partially observable, or not observable yet.
5. Recommend dashboards, queries, alerts, review cadences, and escalation paths.
6. Separate coaching interventions from enforcement interventions.

## Common Telemetry Signals

- User, team, role, and account
- Product and model
- Session and trace identifiers
- Tool calls and external systems touched
- Data categories or sensitivity labels
- Permission requests, approvals, denials, and mode changes
- Prompt and response metadata
- Redaction status
- Blocked or failed requests
- Policy exception type
- Audit trail for autonomous or externally visible actions

## Output Format

Return a policy-to-telemetry table:

| Policy rule | Observable signal | Current status | Query/dashboard | Intervention |
|---|---|---|---|---|

Then include:

1. Highest-risk blind spots
2. Minimum logging needed to close those gaps
3. Privacy and access controls
4. Security review workflow
5. Recommended next policy edits

## Surveillance Guardrail

Flag surveillance risk explicitly. Prefer:

- Individual detail for self-coaching and investigations
- Team-level aggregates for managers
- Organization-level system health for leaders
- Exception-based review for security

Recommend raw-content access only for narrow, justified, auditable cases.
