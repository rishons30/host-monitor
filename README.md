Host Monitor Pro

A lightweight observability stack for monitoring Windows host metrics and Docker container logs.

Uses: Prometheus, Grafana, Alertmanager, Loki, Promtail, Windows Exporter

Overview

Host Monitor Pro provides:

Windows host metrics (CPU, RAM, Disk) via windows_exporter

Docker container logs via Promtail → Loki

Alerts using Prometheus → Alertmanager

Dashboards using Grafana

One-command deployment using Docker Compose

Works on Windows and AWS EC2 Ubuntu

Architecture
Windows Exporter
       ↓
  Prometheus → Alertmanager
       ↓
     Grafana
       ↓
Loki ← Promtail (Docker logs)

Setup

Start the stack:

sudo docker compose up -d


Stop the stack:

sudo docker compose down


Check running containers:

sudo docker compose ps

Grafana

URL: http://localhost:3000

Username: admin

Password: admin

Add Prometheus:

http://prometheus:9090


Add Loki:

http://loki:3100

AWS Deployment
ssh -i key.pem ubuntu@EC2_IP
scp -i key.pem -r ./host-monitorpro ubuntu@EC2_IP:/home/ubuntu/
cd host-monitorpro
sudo docker compose up -d

Folder Structure
HOST-MONITORPRO/
 ├── docker-compose.yml
 ├── prometheus.yml
 ├── alertmanager.yml
 ├── promtail-config.yml
 ├── loki-config.yaml
 ├── dashboard.json
 └── README.md

Features Completed

CPU / Memory / Disk monitoring

Log aggregation

Alerts

Grafana dashboards

EC2 deployment
