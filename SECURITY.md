
# Security Policy

- Never commit secrets or private data. Use GitHub Secrets for CI or local .env (not committed).
- Keep dependencies pinned and updated via Dependabot.
- CI must pass linting and tests before merging to main.
- Review PRs and require at least 1 approval before merge.
- Turn on branch protection (require status checks + signed commits if possible).
