# 🛡️ tarasovAuth

**Plug-and-play authentication service** for modern backend systems.  
Built with FastAPI, PostgreSQL, and JWT. Production-ready, containerized, and developer-friendly.

---

## ✨ Features

- 🔐 **User registration and login**
- 🔁 **JWT access & refresh tokens**
- 🧑‍💻 **RBAC (Role-based access control)**
- 📦 **Containerized (Docker, docker-compose)**
- 🔍 **Observability-ready (Prometheus / OTEL)**
- 🔄 **CI/CD with GitHub Actions**
- ⚙️ **Configurable via `.env`**

---

## 📦 Stack

- **FastAPI** – async, typed, OpenAPI-ready
- **PostgreSQL** – persistent user store
- **PyJWT** – secure token generation
- **Bcrypt / Passlib** – password hashing
- **Docker** – isolation & deployment
- **GitHub Actions** – automated testing pipeline

---

## 🚀 Quickstart

```bash
# Clone repo
git clone https://github.com/yourname/tarasovAuth && cd tarasovAuth

# Copy env and run locally
cp .env.sample .env
docker-compose up --build

