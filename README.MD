🚀 Host Monitor Pro

A lightweight, production-style observability stack for Windows host metrics & container logs.

<p align="center"> <b>Prometheus • Grafana • Alertmanager • Loki • Promtail • Windows Exporter</b> </p>
📸 Dashboard Preview
<p align="center"> <img src="./images/dashboard.png" alt="Grafana Dashboard Screenshot" width="100%"> </p>


📚 Table of Contents

Overview

Features

Architecture

Folder Structure

Requirements

Setup & Usage

Grafana Configuration

Prometheus Queries

Alerts

Logs

AWS Deployment Guide

Completed Features

🔍 Overview

Host Monitor Pro is a full observability stack built for:

Windows OS host metrics via windows_exporter

Container logs via Promtail → Loki

Alerting via Prometheus → Alertmanager

Visualization via Grafana

Works seamlessly on local Windows and AWS EC2 Ubuntu.

🚀 Features
✅ 1. Metrics Monitoring (Prometheus)

CPU usage

Memory usage

Disk utilization

Exporter health

Alert rules

🎨 2. Dashboards (Grafana)

Prebuilt “Host Monitoring” dashboard

CPU / Memory / Disk graphs

Exporter status

Logs panel from Loki

Alerts overview

📄 3. Log Aggregation (Promtail + Loki)

Scrapes Docker logs

Stores logs in Loki

Query logs in Grafana Explore

Full-text search, labels, filters

🔔 4. Alerts (Alertmanager)

High CPU

Low memory

High disk usage

Exporter down

Email/Slack/Webhook routing

☁️ 5. Cloud Ready

Works on AWS EC2 (t2.micro / t3.micro)

Production Docker Compose

SSH tunneling support

🏗️ Architecture
+----------------------+
|     Windows Host     |
|  windows_exporter    |
+----------+-----------+
           |
           v
+----------------------+         +----------------+
|     Prometheus       |  --->  |  Alertmanager  |
+----------+-----------+         +----------------+
           |
           v
+----------------------+
|       Grafana        |
+----------+-----------+
           |
           v
+----------------------+
| Loki <--- Promtail   |
| (Logs Storage)       |
+----------------------+

📂 Folder Structure
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

🔧 Requirements
🖥️ Windows

Docker Desktop

windows_exporter

☁️ EC2 Ubuntu

Docker + Docker Compose

Open ports: 22, 3000, 9090, 9093, 3100

🐳 Setup & Usage

Start the stack:

sudo docker compose up -d


Check running containers:

sudo docker compose ps


Stop:

sudo docker compose down

📊 Grafana Configuration
Default Login

URL: http://localhost:3000

User: admin

Pass: admin

Add Data Sources

Prometheus: http://prometheus:9090
Loki: http://loki:3100

Import Dashboard

Dashboards → Import → Upload dashboard.json

📈 Key Prometheus Queries
CPU Usage
100 * (1 - (
  sum by (instance) (irate(windows_cpu_time_total{mode="idle"}[5m]))
  /
  sum by (instance) (irate(windows_cpu_time_total[5m]))
))

Memory Usage
100 * (1 - (windows_memory_available_bytes / windows_memory_physical_total_bytes))

Disk Usage
100 * avg by (instance, volume) (
  (windows_logical_disk_size_bytes - windows_logical_disk_free_bytes) /
  windows_logical_disk_size_bytes
)

Exporter Health
up{job="windows"}

🔥 Alerts (Prometheus → Alertmanager)

Located in prometheus_rules.yml:

High CPU

Low memory

High disk

Exporter down

Reload:

curl -X POST http://localhost:9090/-/reload


Alerts page:

http://localhost:9090/alerts

📜 Logs (Loki + Promtail)

Check Promtail logs:

sudo docker compose logs promtail --tail 50


Loki queries:

{job="docker_logs"}


Errors only:

{job="docker_logs"} |= "error"

☁️ Deploying on AWS EC2
1. SSH
ssh -i hostkeypair.pem ubuntu@EC2_PUBLIC_IP

2. Upload project
scp -i "hostkeypair.pem" -r F:\host-monitorpro\* ubuntu@EC2_PUBLIC_IP:/home/ubuntu/host-monitorpro/

3. Start
sudo docker compose up -d

4. SSH Tunnel
ssh -i "hostkeypair.pem" -L 3000:localhost:3000 -L 9090:localhost:9090 ubuntu@EC2_PUBLIC_IP

⭐ Status / Completed Features

✔ CPU monitoring
✔ Memory monitoring
✔ Disk monitoring
✔ Exporter health
✔ Prometheus rules
✔ Alertmanager routing
✔ Loki log storage
✔ Promtail container logs
✔ Grafana dashboards
✔ EC2 deployment
✔ SSH tunnels
✔ Production-ready Docker Compose
