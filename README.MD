🚀 Host Monitor Pro

A lightweight, production-ready observability stack for Windows host metrics and Docker container logs using:

Prometheus • Grafana • Alertmanager • Loki • Promtail • Windows Exporter

📸 Dashboard Preview
<p align="center"> <img src="./images/dashboard.png" width="100%"> </p>
🔍 Overview

Host Monitor Pro provides:

Windows host metrics (CPU, RAM, Disk) via windows_exporter

Container logs via Promtail → Loki

Alerts with Prometheus → Alertmanager

Dashboards in Grafana

One-command deployment using Docker Compose

Works on Windows and AWS EC2 Ubuntu

🏗️ Architecture
Windows (windows_exporter)
        ↓
Prometheus → Alertmanager
        ↓
Grafana
        ↓
Loki ← Promtail (Docker logs)

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

🧰 Requirements
Windows

Docker Desktop

windows_exporter installed

Ubuntu (EC2)

Docker & Docker Compose installed

Open ports: 3000 (Grafana), 9090 (Prometheus), 9093, 3100

🚀 Setup
Start
sudo docker compose up -d

Stop
sudo docker compose down

Check
sudo docker compose ps

📊 Grafana Setup

Login: http://localhost:3000

admin / admin

Add datasources:

Prometheus → http://prometheus:9090

Loki → http://loki:3100

Import dashboard.json

📈 Useful PromQL

CPU Usage

100 * (1 - sum by(instance)(irate(windows_cpu_time_total{mode="idle"}[5m])) /
          sum by(instance)(irate(windows_cpu_time_total[5m])))


Memory Usage

100 * (1 - (windows_memory_available_bytes / windows_memory_physical_total_bytes))


Disk Usage

100 *
  avg by(instance, volume)(
    (windows_logical_disk_size_bytes - windows_logical_disk_free_bytes)
    / windows_logical_disk_size_bytes
  )

🔔 Alerts

Defined in prometheus_rules.yml:

High CPU

Low memory

High disk usage

Exporter down

Reload rules:

curl -X POST http://localhost:9090/-/reload

📜 Logs (Loki + Promtail)

View Promtail logs:

sudo docker compose logs promtail --tail 50


Query logs:

{job="docker_logs"}


Errors only:

{job="docker_logs"} |= "error"

☁️ Deploy on AWS EC2
ssh -i key.pem ubuntu@EC2_IP
scp -i key.pem -r ./host-monitorpro ubuntu@EC2_IP:/home/ubuntu/
cd host-monitorpro
sudo docker compose up -d


Tunnel (recommended):

ssh -i key.pem -L 3000:localhost:3000 ubuntu@EC2_IP

✅ Completed

✔ CPU / Memory / Disk metrics
✔ Alerts
✔ Log aggregation
✔ Docker Compose deployment
✔ Grafana dashboards
✔ EC2 support
