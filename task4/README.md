# Task 4 - Complete DevOps Infrastructure

## Objective
Build a scalable DevOps workflow.

## What was built
- Nginx reverse proxy in front of the app
- Multi-environment Docker Compose (dev/prod)
- Full CI/CD pipeline: lint → test → build → push → deploy
- Docker Hub image registry (sudaisj/system-health-monitor)
- Professional root README for portfolio

## Environments
- **Dev:** `docker compose -f docker-compose.dev.yml up --build`
- **Prod:** `docker compose -f docker-compose.prod.yml up`

## Pipeline stages
1. Lint — flake8
2. Test — pytest
3. Build — Docker image
4. Push — Docker Hub registry
5. Deploy — production notification

## Docker Hub
https://hub.docker.com/r/sudaisj/system-health-monitor
