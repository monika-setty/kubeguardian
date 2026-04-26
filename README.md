# KubeGuardian 🛡️

Open source Kubernetes cluster health monitor that reads from 
Linux kernel interfaces to detect anomalies before they cause incidents.

## What it does
- Monitors pod health in real time
- Exposes health endpoints for Kubernetes probes
- Shows which pod is serving each request
- Built for Google Distributed Cloud and GKE

## Architecture
- Python Flask application
- Deployed as Kubernetes Deployment with 3 replicas
- Service load balances across all pods
- Liveness and readiness probes for zero downtime

## Quick Start

### Run locally with Docker
```bash
docker build -t kubeguardian:1.0.0 .
docker run -p 5001:5000 kubeguardian:1.0.0
```

### Deploy to Kubernetes
```bash
kubectl apply -f kubeguardian-deployment.yaml
kubectl apply -f kubeguardian-service.yaml
minikube service kubeguardian-service --url
```

## Endpoints
- `GET /` → cluster health status and pod name
- `GET /health` → liveness/readiness probe endpoint

## Built with
- Python Flask
- Docker
- Kubernetes
- Minikube

## Author
Mounika — aspiring Google SWE