---
name: ai-prompt-coach
description: "Review AI prompts, responses, traces, tool calls, or session histories and turn them into coaching for better AI use. Use when the user asks why an AI session worked or failed, how to improve a prompt, how to reduce retries, how to get better outputs from Claude/ChatGPT/Codex, or how telemetry can improve human and AI effectiveness."
---

# AI Prompt Coach

Use telemetry as a coaching loop for the human and the AI system.

## Coaching Frame

Treat the session as evidence about the workflow, not as a personal performance review. Look for:

- Goal clarity
- Context quality
- Prompt structure
- Tool choice and sequencing
- Model choice
- Retrieval or data issues
- Permission or environment blockers
- Retry loops and dead ends
- Output usefulness
- Follow-up work required

## Review Workflow

1. Identify the user's intended outcome.
2. Trace the session: prompt -> response -> tool call -> outcome -> cost -> review.
3. Separate human-side issues from system-side issues.
4. Identify the smallest change that would have improved the result.
5. Recommend whether this should become a reusable prompt, checklist, workflow, or skill.

## Output Format

Return:

1. What the user was trying to accomplish
2. What worked
3. What got in the way
4. Better next prompt or workflow
5. Tool/model/context changes to try
6. Telemetry fields that would make this easier to coach next time
7. Whether this should become a skill

When helpful, include a rewritten prompt in a fenced code block.

## Quality Signals

Use these signals when available:

- Accepted output or edit
- Rejected output or rework
- Number of retries
- Tool failure rate
- Latency and waiting time
- Cost and token use
- Files or systems touched
- Human intervention points
- Whether the output was reused

## Privacy Defaults

Only inspect raw prompt or response content when the user provided it or explicitly authorized access. If content is redacted, coach from metadata and ask for a small excerpt only if necessary.
