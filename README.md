
# Fastapi-devops-boilerplate

A hardened, containerized FastAPI microservice boilerplate engineered with built-in DevSecOps guardrails, non-root container isolation, runtime payload validation, and prompt-injection defense mechanisms.

---

## Key Features

* **Non-Root Container Security:** Uses a multi-stage Docker build running under `USER 10001` (`appuser`) on a `python:3.11-slim` image to enforce least-privilege security.
* **SELinux Ready:** Configured with Docker Compose volume labels (`:Z`) for seamless cross-platform execution on security-hardened Linux distributions (e.g., Fedora, RHEL).
* **Automated Data Validation:** Powered by Pydantic schema controls to prevent memory floods and strip hidden null-byte (`\x00`) attack signatures.
* **Prompt-Injection Defense:** Includes regex sanitization middleware to filter malicious user inputs and prompt overrides before hitting core business logic.
* **Local vs. Remote Isolation:** Structured environment configurations using `.env` and `.env.example` templates to ensure credentials are never leaked.

---

## Project Structure

```text
Fastapi-devops-boilerplate/
├── app/
│   ├── main.py          # FastAPI initialization and security-mapped endpoints
│   ├── schemas.py       # Pydantic request models and input boundaries
│   └── security.py      # Regex sanitization and injection detection rules
├── .env                 # Local secrets (ignored by Git)
├── .env.example         # Template environment file for configuration setup
├── .gitignore           # File exclusion rules for git tracking
├── Dockerfile           # Multi-stage, non-root runtime specification
├── docker-compose.yml   # Local orchestration service definitions
└── requirements.txt     # Python dependency stack
