# Caravan Tools

Public plugin marketplace for Caravan tools.

## Plugins

- [`ai-telemetry`](./plugins/ai-telemetry): skills for turning AI telemetry, logging, and OpenTelemetry traces into coaching, cost management, policy enforcement, and autonomy-readiness decisions.

## Marketplace Structure

This repository is formatted as a plugin marketplace:

- `.agents/plugins/marketplace.json` for Codex marketplace discovery
- `.claude-plugin/marketplace.json` for Claude plugin marketplace discovery
- `plugins/<plugin-name>/` for each installable plugin

The `ai-telemetry` plugin includes both Codex and Claude plugin manifests.

## Validation

Run the plugin eval from the repository root:

```bash
python3 plugins/ai-telemetry/evals/test_skill_pack.py
```
