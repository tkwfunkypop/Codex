
# Codex Secure Sample (Python)

This is a minimal, security-conscious sample project you can give to Codex to practice:
- Safe dependency management (pinned versions)
- Linting and unit testing in CI
- Ready for Dependabot updates

## Quick start (local)

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py --name Kenta
pytest -q
```

## Repository hygiene
- All dependencies are pinned in `requirements.txt`.
- CI runs linting and tests on every push/PR.
- Dependabot keeps dependencies up to date via PRs.
- Do not commit secrets. Use `os.environ[...]` for tokens; store them in GitHub Secrets or local `.env` (not tracked).

## How to use with Codex
Start with prompts like:
- "Add a /health endpoint using Flask, write unit tests, and update CI."
- "Refactor app.py into a package structure (src/), keep tests passing."
- "Introduce input validation and handle errors safely without exposing stack traces."
This is a test change for CI.

## Endpoints

### `GET /health`
ヘルスチェック用。常に `{"status":"ok"}` を返します。

```bash
curl -s http://localhost:8000/health | jq
# => { "status": "ok" }
