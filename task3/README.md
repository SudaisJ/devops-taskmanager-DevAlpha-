# Task 3 - Containerization Project

## Objective
Use modern deployment practices to containerize the System Health Monitor.

## Tool Used
Docker + Docker Compose

## What Was Built

### Dockerfile (system-health-monitor/Dockerfile)
- Multi-stage build (builder + runtime)
- Stage 1: installs Python dependencies into /install
- Stage 2: copies only app code + installed packages — no build tools in final image
- Runs as non-root user (security best practice)
- HEALTHCHECK built in — Docker auto-restarts if app hangs
- Exposes port 5000

### docker-compose.yml (system-health-monitor/docker-compose.yml)
- Single command to build and run: docker compose up --build
- Container restarts automatically if it crashes
- Health check monitors the /health endpoint

## How to Run
```bash
cd system-health-monitor
docker compose up --build
```
Then open: http://localhost:5000

## How to Verify
```bash
docker ps                          # confirm container is running
docker logs health-monitor         # check app logs
curl http://localhost:5000/health  # confirm app responds
```
