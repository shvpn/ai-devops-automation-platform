# Architecture

## Current Week 1 Architecture

```text
Developer PC
  |
  | runs locally
  v
FastAPI application
  |
  | exposes
  v
/health and /ask endpoints
```

## Planned Target Architecture

```text
Developer PC
  |
  | git push
  v
GitHub
  |
  | GitHub Actions
  v
Container Registry
  |
  | deploy
  v
AWS EC2
  |
  | runs
  v
K3s
  |
  | hosts
  v
AI Support API + n8n automation
```

## Notes

- The current app runs locally during Week 1.
- Docker, AWS, Terraform, K3s, and n8n will be added in later weeks.
- The `/health` endpoint is used to verify that the service is running.
