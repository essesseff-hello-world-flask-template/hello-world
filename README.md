# hello-world Application (Flask)

Python Flask implementation with trunk-based development and event-driven deployments via essesseff platform.

## Architecture

* **Branch Strategy**: Single `main` branch (trunk-based)
* **Auto-Deploy**: DEV only
* **Manual Deploy**: QA, STAGING, PROD (via essesseff)

## Development Workflow

```bash
# 1. Create feature branch
git checkout -b feature/my-feature

# 2. Make changes and commit
git commit -am "Add feature"

# 3. Push and create PR
git push origin feature/my-feature

# 4. After review, merge to main
# This triggers automatic build and deploy to DEV

# 5. Use essesseff UI for promotions:
#    - Developer declares Release Candidate
#    - QA accepts RC → deploys to QA (or alternatively rejects the promotion of the RC to QA)
#    - QA marks as Stable (or alternatively rejects the promotion to Stable)
#    - Release Engineer deploys from Stable Release to STAGING/PROD
```

## Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Or run with gunicorn
gunicorn --bind 0.0.0.0:8080 --workers 2 app:app
```

## Docker

```bash
# Build container
docker build -t hello-world-flask:local .

# Run container
docker run -p 8080:8080 hello-world-flask:local
```

## Endpoints

* `/` - Main page with version information
* `/health` - Health check (returns JSON)
* `/ready` - Readiness check (returns JSON)

## Environment Variables

* `PORT` - Port to run the application on (default: 8080)

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container definition
├── semver.txt         # Version tracking
├── .gitignore         # Git ignore patterns
└── README.md          # This file
```

## Related Repositories

* Source: hello-world (this repo)
* Config DEV: hello-world-config-dev
* Config QA: hello-world-config-qa
* Config STAGING: hello-world-config-staging
* Config PROD: hello-world-config-prod
* Argo CD Config DEV: hello-world-argocd-dev
* Argo CD Config QA: hello-world-argocd-qa
* Argo CD Config STAGING: hello-world-argocd-staging
* Argo CD Config PROD: hello-world-argocd-prod 


## Testing

```bash
# Test health endpoint
curl http://localhost:8080/health

# Test readiness endpoint
curl http://localhost:8080/ready

# Test main page
curl http://localhost:8080/
```
