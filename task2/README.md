# Task 2 - CI/CD Pipeline

## What is CI/CD?
CI (Continuous Integration) automatically tests your code every time
you push to GitHub. CD (Continuous Deployment) automatically deploys
it if tests pass.

## Tool Used
GitHub Actions — runs directly from your GitHub repo, no separate
server needed.

## Pipeline Stages
1. **Lint** — checks code style with flake8
2. **Test** — runs the pytest suite automatically

## How it works
Every push to `main` or `develop` triggers the pipeline automatically.
No manual steps needed.

## How to verify
Push any code change to GitHub and open the Actions tab on your repo:
https://github.com/SudaisJ/devops-taskmanager-DevAlpha-/actions
