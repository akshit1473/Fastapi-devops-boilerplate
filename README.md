# FastAPI DevOps Boilerplate

A hardened, containerized **FastAPI** starter kit built with DevOps practices baked in from the start — non-root container isolation, strict runtime payload validation, and input-sanitization middleware — so you can focus on business logic instead of re-implementing security basics on every new service.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Run with Docker Compose (recommended)](#run-with-docker-compose-recommended)
  - [Run locally with a virtual environment](#run-locally-with-a-virtual-environment)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Security Design](#security-design)
- [Tech Stack](#tech-stack)


---

## Features

- 🔒 **Non-root container by default** — the runtime image drops root privileges and runs as a dedicated `appuser` (UID/GID `10001`) on a slim `python:3.11-slim` base, following least-privilege principles.
- 🐳 **Multi-stage Docker build** — a separate build stage compiles dependencies into a virtual environment, keeping the final runtime image small and free of build tooling.
- 🧱 **SELinux-friendly volumes** — `docker-compose.yml` uses `:Z` volume labeling out of the box, so the project runs cleanly on hardened distros like Fedora and RHEL without permission errors.
- 🛡️ **Schema-first validation** — Pydantic v2 models enforce strict input boundaries and help guard against malformed payloads and null-byte (`\x00`) injection attempts.
- 🧹 **Input sanitization middleware** — regex-based filtering strips suspicious patterns (including basic prompt-injection style payloads) before requests reach your business logic.
- ⚙️ **Environment-based configuration** — `pydantic-settings` + `.env` / `.env.example` keep local secrets out of version control while making configuration explicit and typed.
- ♻️ **Hot-reload dev workflow** — Docker Compose runs Uvicorn with `--reload` so code changes are picked up instantly during development.

---

## Project Structure

```
Fastapi-devops-boilerplate/
├── app/
│   ├── main.py          # FastAPI app factory, routes, and middleware wiring
│   ├── schemas.py        # Pydantic request/response models and validation rules
│   └── security.py       # Sanitization middleware and injection-detection logic
├── .env                  # Local environment values (git-ignored)
├── .env.example           # Template for required environment variables
├── .gitignore
├── Dockerfile             # Multi-stage, non-root production build
├── docker-compose.yml     # Local dev orchestration
└── requirements.txt       # Python dependencies
```

---

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (recommended path)
- `git`

---

## Getting Started

### Run with Docker Compose (recommended)

```bash
# 1. Clone the repository
git clone https://github.com/akshit1473/Fastapi-devops-boilerplate.git
cd Fastapi-devops-boilerplate

# 2. Copy the example environment file and adjust as needed
cp .env.example .env

# 3. Build and start the service
docker compose up --build
```

The API will be available at **http://localhost:8000**, with interactive docs at **http://localhost:8000/docs**.

### Run locally with a virtual environment

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy environment variables
cp .env.example .env

# 4. Start the dev server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Configuration

Configuration is managed via environment variables, loaded through `pydantic-settings` and `.env` files. Copy `.env.example` to `.env` and adjust values for your environment.

| Variable      | Description                                  | Default       |
|---------------|-----------------------------------------------|---------------|
| `ENVIRONMENT` | Runtime environment name (`development`, `production`, etc.) | `development` |
| `PORT`        | Port the app listens on                       | `8000`        |

> Check `.env.example` for the full, up-to-date list of variables as the project evolves.

---
## API Reference

Once the server is running, FastAPI's auto-generated docs are available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI schema: `http://localhost:8000/openapi.json`

---
## Security Design

This boilerplate is opinionated about security so that insecure defaults don't leak into production:

1. **Least-privilege container execution** — the final image never runs as root; a dedicated system user/group (`appuser:appgroup`, UID `10001`) owns and runs the application.
2. **Small attack surface** — the multi-stage build ensures compilers and build-only dependencies never ship in the runtime image.
3. **Defense-in-depth input handling** — Pydantic schemas validate shape and types at the boundary, while middleware in `app/security.py` performs additional pattern-based sanitization against malicious or malformed payloads.
4. **Secret hygiene** — `.env` is git-ignored by default, and `.env.example` documents required variables without exposing real values.

> This project provides a *foundation*, not a complete security audit. Review and adapt the sanitization rules and dependency versions to your own threat model before deploying to production.

---
## Tech Stack

| Component            | Purpose                                  |
|-----------------------|-------------------------------------------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework / API layer |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation and settings management |
| [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Typed environment configuration |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | `.env` file loading |
| Docker (multi-stage) | Containerized, hardened deployment |
---
## Roadmap

- [ ] Add automated tests (pytest) and CI workflow (GitHub Actions)
- [ ] Add structured logging and health-check endpoint
- [ ] Add rate limiting middleware
- [ ] Publish a production `docker-compose.prod.yml` example
- [ ] Add pre-commit hooks (lint, format, security scan)
---
## To Be Added:
 CI/ CD pipeline that automates checks

