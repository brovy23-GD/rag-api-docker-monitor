# RAG API Docker Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
# RAG API with Docker & Monitoring

![CI/CD](https://github.com/brovy23-GD/rag-api-docker-monitor/workflows/CI%2FCD/badge.svg?branch=master)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)

Dockerized RAG API with Terraform infrastructure deployment and Grafana/Prometheus monitoring.

**Features:**
- Containerized FastAPI application
- Infrastructure as Code (Terraform)
- Real-time monitoring with Grafana
- CI/CD pipeline with GitHub Actions

**Quick Start:** See docs/runbook.md  
**Live Demo:** coming soon


## 📋 Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Azure account (for deployment)
- Terraform 1.0+

## 🚀 Quick Start

### Local Development
\\\ash
# Clone the repo
git clone https://github.com/brovy23-GD/rag-api-docker-monitor.git
cd rag-api-docker-monitor

# Build and run
docker-compose up --build
\\\

## 📁 Project Structure
\\\
/docker/          # Dockerfile and configs
/terraform/       # Infrastructure as code
/monitoring/      # Grafana dashboards
/.github/         # CI/CD workflows
\\\

## 🔒 Security
See [SECURITY.md](SECURITY.md) for important security notices.

## 📄 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

> **Note:** This is a demo project for portfolio purposes. Not intended for production use.
