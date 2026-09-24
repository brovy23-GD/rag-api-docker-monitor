![RAG API Docker Monitoring Banner](RAG%20GIT%20BANNER.png)

# RAG API, Docker and Monitoring

**Python service and infrastructure learning project** by [Bobby Rovy](https://github.com/brovy23-GD) | [LinkedIn](https://www.linkedin.com/in/bobbyrovy)

## Current status

This repository contains a working FastAPI monitoring demonstration. The API runs locally with Docker Compose, and Prometheus scrapes its metrics. The application does not perform retrieval-augmented generation or call a language model.

## Implemented features

- `GET /health` returns the service status.
- `POST /echo` accepts a JSON body with a required `text` field and returns that text.
- `GET /metrics` exposes Prometheus request counters and latency histograms.
- Docker Compose starts the API and Prometheus. The API has a container health check.
- A GitHub Actions workflow installs the development dependencies and runs pytest on Python 3.11.

## Run with Docker Compose

From the repository root:

```powershell
docker compose up --build -d
docker compose ps

```

The API documentation is at http://127.0.0.1:8000/docs. Prometheus is at http://127.0.0.1:9090.

Try the API from PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8000/echo' -ContentType 'application/json' -Body '{"text":"Testing my Docker Monitor API"}'
```

In Prometheus, check **Status > Targets** for the `demo-api` target. It scrapes `api:8000/metrics`. Stop the containers with `docker compose down`.

## Run the tests locally

Create and activate a Python 3.11 virtual environment, then run:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

## Repository scope

`terraform/main.tf` is an initial configuration, not a tested Azure deployment. `monitoring/grafana-dashboard.json` is a placeholder, not a working dashboard. No RAG pipeline, Grafana dashboard, or Azure deployment is claimed here.

For a separate working local RAG prototype, see [Azure RAG Demo](https://github.com/brovy23-GD/azure-rag-demo).
