---
name: ai-autonomy-readiness
description: "Assess whether an AI workflow, agent, tool, or team process is ready for more autonomy. Use when the user asks whether an agent can run with less supervision, what guardrails are needed, how observability supports autonomy, how to approve tool use, or how to create an autonomy-readiness review from logs, traces, evaluations, policy, and workflow evidence."
---

# AI Autonomy Readiness

Use telemetry to decide where AI can safely get more permission.

## Core Principle

The more autonomy an AI system gets, the more observability it needs. Do not recommend autonomy based on confidence alone. Look for evidence.

## Readiness Levels

Use these levels unless the user has a different scale:

- Level 0: Assist only. Human performs all actions.
- Level 1: Draft. AI prepares work; human reviews and executes.
- Level 2: Execute with approval. AI can take bounded actions after explicit approval.
- Level 3: Bounded autonomy. AI can act within a narrow scope with audit trails and rollback.
- Level 4: Managed autonomy. AI can run recurring work with monitoring, exceptions, and periodic review.

## Evidence To Review

- Recent traces or session histories
- Tool calls and external systems touched
- Failure modes and exception reports
- Cost and latency
- Quality outcomes and human rework
- Policy constraints
- Permission model
- Reversibility and rollback
- Blast radius
- Human review points
- Monitoring and alerting

## Assessment Workflow

1. Define the workflow and intended autonomy increase.
2. Identify possible harms: bad output, data leak, wrong action, excess cost, brand risk, compliance risk.
3. Check whether each harm is observable.
4. Check whether each harm is reversible or containable.
5. Review recent quality and exception evidence.
6. Recommend the highest safe autonomy level.
7. Specify guardrails and telemetry gaps before moving up a level.

## Output Format

Return:

1. Recommended autonomy level
2. Why this level is appropriate
3. What the agent may do autonomously
4. What still requires approval
5. Required telemetry
6. Required guardrails
7. Stop conditions and escalation triggers
8. Next safe experiment

## Non-Negotiables

Do not recommend increased autonomy if:

- The workflow cannot be traced
- Actions are high impact and irreversible
- Sensitive data access is invisible
- Tool permissions are unclear
- There is no exception review path
- Cost can run away without limits
- Quality has not been reviewed in real work
