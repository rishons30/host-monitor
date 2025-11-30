**Host Monitor Pro**

A lightweight, production-ready observability stack for Windows host metrics and Docker container logs, using:

Prometheus, Grafana, Alertmanager, Loki, Promtail, Windows Exporter

Dashboard Preview

Overview

Host Monitor Pro provides:

Windows host metrics (CPU, RAM, Disk) via windows_exporter

Docker container logs via Promtail → Loki

Alerting via Prometheus → Alertmanager

Dashboards with Grafana

One-command deployment using Docker Compose

Works on Windows and AWS EC2 Ubuntu

Features
Metrics Monitoring (Prometheus)

CPU usage

Memory usage

Disk usage

Exporter health

Custom alert rules

Dashboards (Grafana)

Host monitoring dashboard

CPU / Memory / Disk graphs

Alerts panel

Logs panel

Log Aggregation (Loki + Promtail)

Collects Docker container logs

Full-text search

Label-based filtering

Alerts (Alertmanager)

High CPU

Low memory

High disk usage

Exporter down

Cloud Ready

Works on AWS EC2

SSH tunnel support

Same config works on Windows & Linux

Architecture
Windows Host (windows_exporter)
             ↓
      Prometheus → Alertmanager
             ↓
           Grafana
             ↓
       Loki ← Promtail

Folder Structure
HOST-MONITORPRO/
 ├── docker-compose.yml
 ├── prometheus.yml
 ├── prometheus_rules.yml
 ├── alertmanager.yml
 ├── loki-config.yaml
 ├── promtail-config.yml
 ├── dashboard.json
 ├── loki-data/
 ├── loki-wal/
 └── README.md

Requirements
Windows

Docker Desktop

windows_exporter installed

Ubuntu (AWS EC2)

Docker

Docker Compose

Open ports:

3000 (Grafana)

9090 (Prometheus)

9093 (Alertmanager)

3100 (Loki)

Setup
Start
sudo docker compose up -d

Stop
sudo docker compose down

Check Running Containers
sudo docker compose ps

Grafana Setup
Login

URL: http://localhost:3000

Username: admin

Password: admin

Add Data Sources

Prometheus

http://prometheus:9090


Loki

http://loki:3100

Import Dashboard

Go to Dashboards → Import

Upload dashboard.json

Select Prometheus datasource

Prometheus Queries
CPU Usage
100 * (1 - sum by(instance)(irate(windows_cpu_time_total{mode="idle"}[5m])) /
          sum by(instance)(irate(windows_cpu_time_total[5m])))

Memory Usage
100 * (1 - (windows_memory_available_bytes / windows_memory_physical_total_bytes))

Disk Usage
100 * avg by(instance, volume)(
  (windows_logical_disk_size_bytes - windows_logical_disk_free_bytes)
  / windows_logical_disk_size_bytes
)

Exporter Health
up{job="windows"}

Alerts

Alerts are defined in prometheus_rules.yml:

High CPU

Low memory

High disk usage

Exporter down

Reload alert rules:

curl -X POST http://localhost:9090/-/reload

Logs (Loki + Promtail)

Check Promtail logs:

sudo docker compose logs promtail --tail 50


Query logs:

{job="docker_logs"}


Errors only:

{job="docker_logs"} |= "error"

AWS EC2 Deployment
SSH into EC2
ssh -i key.pem ubuntu@EC2_PUBLIC_IP

Upload Project
scp -i key.pem -r ./host-monitorpro ubuntu@EC2_PUBLIC_IP:/home/ubuntu/

Start Services
cd ~/host-monitorpro
sudo docker compose up -d

Completed Features

CPU / Memory / Disk monitoring

Log aggregation

Alerts

Grafana dashboards

EC2 deployment

One-command startup
