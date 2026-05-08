#!/usr/bin/env python3
"""Lightweight checks for the ai-telemetry skill pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILL_EXPECTATIONS = {
    "ai-otel-setup-advisor": [
        "Recommended v0 architecture",
        "What to turn on first",
        "What to avoid collecting at first",
        "Privacy and governance decisions",
    ],
    "ai-ops-readout": [
        "Executive summary",
        "Numbers that matter",
        "Productive token spend",
        "Recommended actions for the coming week",
    ],
    "ai-prompt-coach": [
        "What the user was trying to accomplish",
        "What worked",
        "What got in the way",
        "Better next prompt or workflow",
    ],
    "ai-policy-monitor": [
        "Policy rule",
        "Observable signal",
        "Highest-risk blind spots",
        "Privacy and access controls",
    ],
    "ai-cost-optimizer": [
        "Spend summary",
        "Where to spend less",
        "Where to spend more",
        "cost per meaningful output",
    ],
    "ai-autonomy-readiness": [
        "Recommended autonomy level",
        "What still requires approval",
        "Stop conditions and escalation triggers",
        "Do not recommend increased autonomy",
    ],
}

DRY_RUN_CASES = {
    "ai-otel-setup-advisor": {
        "prompt": "We use Claude Code and ChatGPT, want Honeycomb, and need privacy-safe logging for a 20-person pilot.",
        "must_route_to": ["tools", "backend", "scope", "redacted", "dashboards"],
    },
    "ai-ops-readout": {
        "prompt": "Summarize this week's telemetry: 18 active users, 220 sessions, $184 spend, 12 tool failures, 3 policy exceptions.",
        "must_route_to": ["adoption", "cost", "quality", "risk", "actions"],
    },
    "ai-prompt-coach": {
        "prompt": "Review this trace: user asked for a board memo, model made three unsupported claims, then retried twice.",
        "must_route_to": ["intended outcome", "worked", "got in the way", "better next prompt"],
    },
    "ai-policy-monitor": {
        "prompt": "Policy: no customer PII in unapproved AI tools. Map this to telemetry checks.",
        "must_route_to": ["policy rule", "observable", "blind spots", "intervention"],
    },
    "ai-cost-optimizer": {
        "prompt": "Analyze $2,400 in token spend by team and tell me where to spend less or more.",
        "must_route_to": ["productive token spend", "outcomes", "where to spend less", "where to spend more"],
    },
    "ai-autonomy-readiness": {
        "prompt": "Can this invoice-drafting agent send invoices without review?",
        "must_route_to": ["autonomy level", "approval", "guardrails", "stop conditions"],
    },
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - failure path is the test result
        fail(f"{path} is not valid JSON: {exc}")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md missing YAML frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_plugin_manifest() -> None:
    manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")
    assert manifest["name"] == "ai-telemetry"
    assert manifest["skills"] == "./skills/"
    assert "TODO" not in json.dumps(manifest)
    assert manifest["interface"]["displayName"] == "AI Telemetry"

    claude_manifest = load_json(ROOT / ".claude-plugin" / "plugin.json")
    assert claude_manifest["name"] == "ai-telemetry"
    assert "TODO" not in json.dumps(claude_manifest)


def check_skill(skill_dir: Path) -> None:
    skill_name = skill_dir.name
    text = (skill_dir / "SKILL.md").read_text()
    meta = frontmatter(text)
    assert meta["name"] == skill_name
    assert "TODO" not in text
    assert "Use when" in meta["description"]
    assert "Output Format" in text
    assert "Privacy" in text or "policy" in text.lower() or "guardrail" in text.lower()
    for expected in SKILL_EXPECTATIONS[skill_name]:
        assert expected in text, f"{skill_name} missing expected phrase {expected!r}"

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    assert agent_yaml.exists()
    agent_text = agent_yaml.read_text()
    assert "display_name:" in agent_text
    assert "short_description:" in agent_text
    assert "default_prompt:" in agent_text
    assert "TODO" not in agent_text


def check_dry_run_contracts() -> None:
    for skill_name, case in DRY_RUN_CASES.items():
        text = (ROOT / "skills" / skill_name / "SKILL.md").read_text().lower()
        missing = [needle for needle in case["must_route_to"] if needle.lower() not in text]
        assert not missing, f"{skill_name} dry-run prompt lacks routing terms: {missing}"


def main() -> None:
    check_plugin_manifest()
    for skill_name in sorted(SKILL_EXPECTATIONS):
        check_skill(ROOT / "skills" / skill_name)
    check_dry_run_contracts()
    print("ai-telemetry skill pack evals passed")


if __name__ == "__main__":
    main()
