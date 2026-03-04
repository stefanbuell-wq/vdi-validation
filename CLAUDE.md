# CLAUDE.md — VDI Validation

## Project Overview

**vdi-validation** is a repository for validation of VDI (Virtual Desktop Infrastructure) products. The project is in its early stages with the foundational structure being established.

## Repository Structure

```
vdi-validation/
├── README.md          # Project description
└── CLAUDE.md          # This file — guidance for AI assistants
```

## Development Workflow

### Branch Strategy

- **master**: Main branch containing stable, reviewed code.
- Feature branches should be created off `master` for new work.

### Git Conventions

- Write clear, descriptive commit messages that explain *why* a change was made, not just what.
- Keep commits focused — one logical change per commit.
- Push feature branches and open pull requests for review before merging to `master`.

## Coding Conventions

These conventions should be followed as the codebase grows:

- Prefer clarity over cleverness in all code.
- Keep files focused on a single responsibility.
- Add comments only where the logic is non-obvious — avoid redundant comments.
- Do not over-engineer; implement only what is needed for the current task.

## For AI Assistants

- **Read before editing**: Always read existing files before proposing changes.
- **Minimal changes**: Only modify what is necessary to accomplish the task. Do not refactor or "improve" unrelated code.
- **No guessing**: If a requirement is ambiguous, ask for clarification rather than assuming.
- **Security**: Never commit secrets, credentials, or sensitive configuration. Watch for `.env` files, API keys, and tokens.
- **Testing**: When tests exist, run them before and after making changes to verify nothing breaks.
