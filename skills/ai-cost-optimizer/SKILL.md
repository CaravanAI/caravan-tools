---
name: ai-cost-optimizer
description: "Analyze AI token spend, model spend, session costs, team usage, or workflow costs and recommend how to reduce waste while increasing productive token spend. Use when the user asks about AI cost control, salary-scale token budgets, cost per meaningful output, cost per user/team/session/model/workflow, or how to decide where to spend more on AI."
---

# AI Cost Optimizer

Optimize for productive token spend, not minimum token spend.

## Core Frame

The goal is not to minimize AI spend. The goal is to raise the ceiling on spend that creates useful work.

Ask:

What would need to be true for the organization to feel great about spending salary-scale dollars on AI assistance for every person?

## Inputs To Look For

- Total spend and token use
- Spend by user, team, product, model, workflow, and session
- Session counts and active users
- Model mix and context size
- Tool calls, retries, errors, and latency
- Outcome labels: accepted, reused, shipped, rejected, stalled, or reworked
- Human review time or rework time

If outcomes are missing, make that the primary recommendation. Spend without outcome data is hard to interpret.

## Analysis Workflow

1. Segment spend by user, team, model, workflow, and session.
2. Identify high-cost/high-value patterns to expand.
3. Identify high-cost/low-value patterns to investigate.
4. Identify low-cost/high-value patterns to standardize or train.
5. Identify low-usage areas where the problem may be adoption, not cost.
6. Recommend better model routing, prompt patterns, context design, or skills.

## Cost-Per-Meaningful-Output

Use this as the north-star metric when data allows:

```text
cost per meaningful output =
  (AI spend + tool spend + review cost) / accepted outcomes
```

Define "meaningful output" with the user. Examples:

- Accepted code change
- Draft sent
- Report completed
- Customer issue resolved
- Workflow completed
- Reusable asset created
- Human hours avoided or upgraded

## Output Format

Return:

1. Spend summary
2. Productive token spend signals
3. Waste or friction signals
4. Cost-per-meaningful-output estimate, if possible
5. Where to spend less
6. Where to spend more
7. Instrumentation gaps that block better cost decisions
8. Next experiments

Always distinguish "reduce this spend" from "instrument this spend better."

## Privacy And Aggregation

Cost data can become surveillance if it is exposed carelessly. Prefer:

- Individual-level detail for self-coaching, debugging, or approved investigation
- Team-level aggregates for managers
- Workflow-level analysis for investment decisions
- Organization-level totals for leadership

Avoid publishing individual spend rankings without context. High spend may indicate productive leverage, not waste.
