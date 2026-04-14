# Enterprise Python DevSecOps Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.2-black)
![Security](https://img.shields.io/badge/Security-Bandit%20%7C%20Trivy-yellow)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

This repository demonstrates a **Python Flask Application** integrated with a complete **DevSecOps GitHub Actions Pipeline**. It showcases modern "Shift-Left" security practices, including code linting, Static Application Security Testing (SAST), and container vulnerability scanning.

## 🚀 Application Overview
A lightweight Python web service built with Flask and served via Gunicorn. It serves a dynamic landing page that displays:
- A customizable welcome message.
- The current system Date and Time.
- **Traceability:** The Hostname (or Kubernetes Pod ID) serving the request.

## 🏗️ Project Architecture

The repository is structured to separate application logic from pipeline deployment:
- `.github/workflows/`: The declarative CI/CD DevSecOps pipeline.
- `app.py`: The core application logic.
- `requirements.txt`: Pinned application dependencies.
- `Dockerfile-GithubActions`: A minimal, multi-stage Alpine Linux container designed for production.

## 🛡️ DevSecOps Pipeline Stages

### 1. Continuous Integration & SAST (`build-test-and-secure`)
- **Environment:** Ubuntu-latest with Python 3.11.
- **Dependency Caching:** Uses `actions/setup-python` pip caching to optimize CI runtime.
- **Linting:** Runs **Flake8** to enforce PEP-8 standards and catch severe syntax errors.
- **SAST (Static Analysis):** Runs **Bandit** to scan the Python source code for common security flaws (e.g., hardcoded passwords, dangerous shell injections).

### 2. Containerization & OS Scanning (`dockerize`)
- **Docker Build:** Packages the app using a custom Dockerfile into a minimal Alpine runtime.
- **Container Scan:** Uses **Trivy** to scan the Alpine OS layers and installed Python libraries.
    - *Security Gate:* The pipeline will automatically **fail** if `CRITICAL` or `HIGH` vulnerabilities are found.
- **Distribution:** Pushes the secure, scanned image to Docker Hub, tagged with the exact GitHub Commit SHA and Run Number for 100% traceability.

## 🔑 Prerequisites & Setup

### Local Development
To run this application locally for testing:
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Linux/Mac) or `source venv/Scripts/activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Access the app in your browser at: `http://localhost:5000`

### GitHub Secrets Configuration
To enable the automated pipeline, add the following secrets to your repository (**Settings > Secrets and variables > Actions**):

| Secret Name | Description |
| :--- | :--- |
| `DOCKER_USERNAME` | Your Docker Hub ID (e.g., `rajkumaraute`) |
| `DOCKER_PASSWORD` | Docker Hub Personal Access Token (PAT) |

## 🔒 Security Best Practices Implemented
- **Production Web Server:** Uses `gunicorn` instead of the default Flask development server.
- **Non-Root Execution:** The Docker container dynamically creates and switches to a restricted `appuser`.
- **Cache Destruction:** Uses `pip install --no-cache-dir` inside the Dockerfile to prevent caching package artifacts, reducing image bloat and attack surface.
- **Immutable Tags:** Overwrites the `latest` tag anti-pattern by explicitly tagging deployments with unique Git SHAs.

---
*Maintained by [Rajkumar Aute](https://devsecopsguru.in)*