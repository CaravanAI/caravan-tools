---
name: ai-otel-setup-advisor
description: "Design a practical AI telemetry or OpenTelemetry setup for Claude, ChatGPT, Codex, internal agents, or multi-tool AI programs. Use when the user asks how to turn on AI logging, connect AI tools to Honeycomb or another OTEL backend, decide what to log or redact, create a first telemetry rollout plan, or point an AI assistant at vendor monitoring docs and ask what makes sense for an organization."
---

# AI OTEL Setup Advisor

Help the user turn AI telemetry on in a way that answers real management questions without over-collecting sensitive data.

## First Move

Identify the target setup:

- Tools: Claude, Claude Code, ChatGPT, Codex, internal agents, MCP servers, or other AI products
- Backend: Honeycomb, SIEM, Datadog, Grafana, Langfuse, OTEL collector, warehouse, or unknown
- Scope: one person, one team, pilot group, or whole organization
- Primary goal: coaching, cost, policy, quality, risk, autonomy, or all of these
- Sensitivity: whether prompt and response content may be stored, and who can see it

If exact vendor configuration matters, check current official docs before giving commands. Defaults and environment variables change.

## Recommended Setup Shape

Start with observe-only telemetry:

- Enable out-of-the-box analytics first
- Export OTEL metrics, logs/events, and traces where available
- Keep prompt and response content redacted by default
- Capture stable identifiers: user, team, session, model, product, workflow, and tool
- Capture operational signals: tokens, cost, latency, errors, tool calls, permissions, and outcomes
- Define retention, access, aggregation, and escalation rules before broad rollout

## Event Model

Design around the five metric families:

- Adoption: active users, sessions, active time, repeat use, product mix
- Cost: spend, tokens, cost per user, cost per team, cost per session, cost per workflow
- Depth of use: tool calls, files touched, MCP/server usage, model mix, permission requests
- Quality: accepted output, retries, completed workflows, rework, satisfaction, failure modes
- Risk: sensitive data categories, external access, denied requests, policy exceptions, audit trails

Use a single `session_id` or trace identifier wherever possible so work can be followed across tools.

## Privacy And Governance

Do not treat telemetry as surveillance by default. Recommend layered visibility:

- Individuals see their own detailed data first
- Teams see aggregate patterns
- Leaders see system health, cost, value, adoption, and exceptions
- Security sees policy-relevant exceptions and audit trails

Flag any design that stores raw prompts, responses, secrets, personal data, or customer data. Require an explicit consent, retention, redaction, and access model before recommending raw-content logging.

## Output Format

Return:

1. Recommended v0 architecture
2. What to turn on first
3. What to avoid collecting at first
4. Core fields and metric families
5. First dashboards or queries
6. Privacy and governance decisions
7. Rollout plan for the next week
8. Open questions for IT, security, legal, or leadership
