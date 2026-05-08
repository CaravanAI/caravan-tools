---
name: ai-ops-readout
description: "Create an AI operations readout from logs, OpenTelemetry traces, Honeycomb queries, Claude analytics, ChatGPT/Codex telemetry, screenshots, CSV exports, or narrative observations. Use when the user wants a daily or weekly summary of AI adoption, cost, depth of use, quality, risk, prompt patterns, team usage, productive token spend, or what leaders should do next."
---

# AI Ops Readout

Turn AI telemetry into a short management readout that helps the organization learn.

## Inputs To Look For

Use whatever the user provides:

- Analytics screenshots or exports
- Honeycomb queries or trace samples
- OTEL logs/events/traces
- Cost or token reports
- Session transcripts or prompt histories
- Security/policy exception lists
- Team or workflow context

If data is missing, say what is missing and produce a readout scaffold with the best available evidence. Do not invent numbers.

## Analysis Model

Organize findings into five metric families:

- Adoption: who is using AI, how often, and where
- Cost: spend, token use, model mix, and cost drivers
- Depth of use: whether AI is used as a toy, assistant, coworker, or operating layer
- Quality: whether sessions became usable work
- Risk: policy, data, permission, and security exceptions

Then translate telemetry into decisions:

- What should be coached?
- What should be automated or turned into a skill?
- What should be constrained by policy?
- Where should the team spend more tokens?
- Where is spend unproductive?

## Output Format

Return a concise brief:

1. Executive summary: 3 bullets
2. Numbers that matter: adoption, cost, depth, quality, risk
3. What changed since the prior period, if baseline exists
4. Productive token spend: where spend appears useful
5. Waste or friction: where sessions stalled, failed, or repeated
6. Risk and policy exceptions
7. Coaching opportunities
8. Skills or workflow improvements to build next
9. Recommended actions for the coming week

## Tone

Write for managers and operators, not observability specialists. Be concrete. Avoid shame. The point is to improve the system, not rank people publicly.

## Privacy Defaults

Aggregate by team or workflow when possible. Include user-level detail only when the user has asked for individual coaching, investigation, or policy review and the data access model supports it.
