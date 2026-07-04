# DevOps Internship — Task Manager API (Task 1: Git Workflow)

A small Flask REST API used to demonstrate a Git-based branching workflow.

## Branching Strategy Used
- `main` — stable, releases only (tagged)
- `develop` — integration branch
- `feature/task-api` — the API built and merged in from here

## Workflow Followed
1. Initialized repo on `main`
2. Created `develop` from `main`
3. Created `feature/task-api` from `develop`, built the app there
4. Merged `feature/task-api` → `develop` with `--no-ff`
5. Merged `develop` → `main`, tagged as `v1.0.0`

## Verify the history
```bash
git log --all --decorate --oneline --graph
git branch -a
git tag
```
