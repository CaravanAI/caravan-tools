#!/usr/bin/env python3
"""Plugin version-bump guard.

VENDORED from CaravanAI/caravan-plugins/.github/actions/plugin-version-guard.
That repo is the canonical copy. This is a standalone copy because cross-repo
resolution of a composite action from a private repo's subpath does not work
even with org "allow all" + repo Access=organization (returns "not found").
If you change the guard logic, change it in caravan-plugins first, then re-copy
here. Keep in sync.

Shared across all CaravanAI plugin marketplaces.

Fails a PR if any plugin's content changed without bumping that plugin's
`plugin.json` `version`. The `plugin.json` version is the cache key Claude
Code uses: edits committed under the same version are a silent no-op for
every consumer (they keep the stale cached copy). See the
`feedback_plugin_version_bump` memory for the why.

Layout-agnostic: discovers plugins by globbing `*/.claude-plugin/plugin.json`
(any depth), so it works for both `plugins/<x>/...` monorepos and
single-plugin repos.

Env (set by the composite action):
  BASE_SHA           base ref to diff against (PR base). Falls back to
                     merge-base with origin/main.
  MARKETPLACE_CHECK  warn | fail | off  — when a plugin's plugin.json bumps,
                     whether to also require its marketplace.json entry version
                     to move. Default: warn. (Equality is NOT enforced — the
                     two version lines are independent; we only require they
                     move together, matching the bump-both convention.)

Exit 1 on any error; 0 otherwise. Stdlib only.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def sh(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(args, capture_output=True, text=True)


def base_ref() -> str:
    b = os.environ.get("BASE_SHA", "").strip()
    if b:
        return b
    sh("git", "fetch", "origin", "main", "--depth=100")
    r = sh("git", "merge-base", "origin/main", "HEAD")
    return r.stdout.strip() or "HEAD~1"


def changed_files(base: str) -> list[str]:
    r = sh("git", "diff", "--name-only", f"{base}...HEAD")
    return [line for line in r.stdout.splitlines() if line.strip()]


def discover_plugin_dirs() -> dict[str, str]:
    """Return {plugin_dir -> manifest_path}, posix-style, excluding repo root."""
    out: dict[str, str] = {}
    for mf in Path(".").glob("**/.claude-plugin/plugin.json"):
        if ".git" in mf.parts:
            continue
        pdir = mf.parent.parent
        key = pdir.as_posix()
        if key in (".", ""):  # repo-root marketplace manifest, not a plugin
            continue
        out[key] = mf.as_posix()
    return out


def version_at(ref: str, path: str) -> str | None:
    r = sh("git", "show", f"{ref}:{path}")
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout).get("version")
    except json.JSONDecodeError:
        return None


def head_version(path: str) -> str | None:
    try:
        return json.loads(Path(path).read_text()).get("version")
    except (json.JSONDecodeError, FileNotFoundError):
        return None


def marketplace_versions(ref: str | None) -> dict[str, str | None]:
    """Map {plugin_dir -> marketplace-entry version} from .claude-plugin/marketplace.json."""
    mpath = ".claude-plugin/marketplace.json"
    if ref is None:
        try:
            data = json.loads(Path(mpath).read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    else:
        r = sh("git", "show", f"{ref}:{mpath}")
        if r.returncode != 0:
            return {}
        try:
            data = json.loads(r.stdout)
        except json.JSONDecodeError:
            return {}
    out: dict[str, str | None] = {}
    for p in data.get("plugins", []):
        src = p.get("source")
        if isinstance(src, str):
            out[src.lstrip("./").rstrip("/")] = p.get("version")
    return out


def main() -> int:
    mkt_mode = os.environ.get("MARKETPLACE_CHECK", "warn").lower()
    base = base_ref()
    changed = changed_files(base)
    plugin_dirs = discover_plugin_dirs()

    mkt_head = marketplace_versions(None)
    mkt_base = marketplace_versions(base)

    errors: list[str] = []
    warnings: list[str] = []
    ok: list[str] = []

    for pdir, manifest in sorted(plugin_dirs.items()):
        prefix = pdir + "/"
        if not any(f.startswith(prefix) for f in changed):
            continue  # this plugin's tree is untouched
        base_v = version_at(base, manifest)
        head_v = head_version(manifest)
        if base_v is None:
            ok.append(f"{pdir}: new plugin (v{head_v})")
            continue
        if head_v == base_v:
            errors.append(
                f"{pdir}: content changed but plugin.json version is still "
                f"{base_v}. Bump it (the version is the cache key)."
            )
            continue
        ok.append(f"{pdir}: {base_v} -> {head_v}")
        if mkt_mode != "off":
            mb, mh = mkt_base.get(pdir), mkt_head.get(pdir)
            if mb is not None and mh == mb:
                msg = (
                    f"{pdir}: plugin.json bumped ({base_v}->{head_v}) but the "
                    f"marketplace.json entry version did not move ({mb}). "
                    f"Bump both (see feedback_plugin_version_bump)."
                )
                (errors if mkt_mode == "fail" else warnings).append(msg)

    print("== Plugin version guard ==")
    print(f"base: {base}  |  changed files: {len(changed)}  |  marketplace-check: {mkt_mode}")
    for line in ok:
        print(f"  ok   {line}")
    for w in warnings:
        print(f"  warn {w}")
    for e in errors:
        print(f"  FAIL {e}")
    if not ok and not errors:
        print("  (no plugin content changed — nothing to enforce)")

    if errors:
        print("\nVersion guard failed. Bump the plugin.json `version` for each "
              "changed plugin so consumers actually receive the change.")
        return 1
    print("\nVersion guard passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
