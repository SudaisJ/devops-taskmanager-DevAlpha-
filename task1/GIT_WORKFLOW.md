# Git Workflow

## Branching Model
This repo follows a simplified Gitflow model:
- `main` — always deployable, tagged releases only
- `develop` — integration branch, feature branches merge here first
- `feature/*` — one branch per unit of work, branched from `develop`

## Process
1. Create a feature branch from `develop`: `git checkout -b feature/xyz`
2. Commit work with clear, scoped messages (e.g. `feat(api): add endpoint`)
3. Merge back into `develop` with `--no-ff` to preserve merge history
4. When ready to release, merge `develop` into `main` and tag it

## Verify
git log --all --decorate --oneline --graph
git branch -a
git tag
