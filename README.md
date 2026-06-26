# Python Portfolio with CI/CD

A Flask portfolio website demonstrating **Continuous Integration (CI)** and **Continuous Deployment (CD)** using GitHub Actions YAML workflows.

## Project Structure

```
ci_cd_portfolio/
├── app/                    # Flask application
├── templates/              # HTML templates
├── static/css/             # Stylesheets
├── tests/                  # pytest test suite
├── .github/workflows/
│   ├── ci.yml              # CI pipeline (lint, test, build)
│   └── cd.yml              # CD pipeline (deploy on main)
├── Dockerfile
├── requirements.txt
└── run.py
```

## Run Locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements-dev.txt
python run.py
```

Open [http://localhost:5000](http://localhost:5000)

## CI Pipeline (`ci.yml`)

Triggered on every **push** and **pull request** to `main` or `develop`:

| Job   | Purpose                                      |
|-------|----------------------------------------------|
| Lint  | Ruff lint + format checks                    |
| Test  | pytest with 80% coverage minimum           |
| Build | Validates Docker image builds successfully   |

## CD Pipeline (`cd.yml`)

Triggered **after CI passes** on `master`/`main`:

| Step        | Purpose                                    |
|-------------|--------------------------------------------|
| Smoke test  | Verifies `/health` before deploy           |
| Deploy      | Triggers Render to publish your live site  |

### Get a live URL (Render — free)

CI only **tests and builds**. CD **deploys** to a hosting platform. Without this setup, you get no public website.

1. **Create a Render account** — [render.com](https://render.com)

2. **New → Web Service → Connect GitHub repo** `Kanu004/ci_cd_portfolio`

3. **Settings:**
   - **Branch:** `master`
   - **Runtime:** Docker
   - **Plan:** Free
   - **Health check path:** `/health`
   - Turn **Auto-Deploy** OFF (GitHub Actions will deploy instead)

4. **Copy your live URL** from Render (e.g. `https://ci-cd-portfolio.onrender.com`)

5. **Create a Deploy Hook** in Render:  
   **Settings → Deploy Hook → Create** → copy the URL

6. **Add GitHub secrets** (repo **Settings → Secrets and variables → Actions**):

   | Secret | Value |
   |--------|-------|
   | `RENDER_DEPLOY_HOOK_URL` | Deploy hook URL from step 5 |
   | `RENDER_SERVICE_URL` | Your Render live URL from step 4 |

7. **Push any commit** to `master` → CI runs → CD deploys → open your Render URL

> **Why CD showed green but no site?** The old workflow only tried Docker Hub push (missing credentials) and used `continue-on-error`, so failures were hidden. It never deployed to a web host.

## Docker

```bash
docker build -t portfolio .
docker run -p 5000:5000 portfolio
```

## Customize

Edit portfolio data in `app/routes.py` (`PORTFOLIO` dict) — name, skills, projects, and links.
