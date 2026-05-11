# cogs-lab-portfolio
COGS Tech Support Lab Portfolio
## My Lab Portfolio
Engineer: [Antariksh]
Started: 5 May 2026


This repository contains the end-to-end technical documentation and evidence for the **COGS Lab**. It serves as a professional record of cloud infrastructure deployment, monitoring integration.


## Global Tech Stack
* **Cloud:** AWS (Ubuntu 26.04 LTS)
* **Web Services:** Nginx Gateway
* **Observability:** Prometheus, Grafana, Node Exporter, Uptime Kuma
* **Security:** TLS 1.3, AES-256 Encryption, SSH Key-Based Auth

---


### Lab 1 & 2: Infrastructure & Gateway Setup
* **Objective:** Deploy a secure cloud environment and reverse proxy.
* **Key Tasks:** * Provisioned Linux VM with hardened SSH access.
    * Configured Nginx as a reverse proxy for internal lab applications.
    * Implemented firewall rules (Security Lists) for Port 80, 443, and 3000.

### Lab 3 & 4: Observability Stack Deployment
* **Objective:** Implement a full-stack monitoring and alerting system.
* **Key Tasks:** * Deployed **Node Exporter** for hardware-level telemetry.
    * Configured **Prometheus** for time-series data scraping.
    * Built **Grafana** dashboards to visualize CPU, Memory, and Network trends.
    * Integrated **Uptime Kuma** for real-time HTTP heartbeat monitoring and downtime alerting.

### Lab 5.1: Incident Management (P1 Simulation)
* **Objective:** Act as an Incident Commander to resolve a critical gateway outage.
* **Process:** * Detected outage via Uptime Kuma; triaged via GitHub P1 Ticket.
    * Analyzed resource spikes using Prometheus (identified 89% RAM exhaustion).
    * Executed recovery and conducted a post-mortem analysis.
* **Artifacts:**
    * Post-Incident Report (PIR)
    * PACE Shift Handover

### Lab 5.2: Change Management (TLS Upgrade)
* **Objective:** Execute a secure infrastructure upgrade under a Change Request (CR) framework.
* **Process:** * Migrated protocol from TLS 1.2 to TLS 1.3.
    * Demonstrated a **Success-and-Rollback** competency by intentionally failing and restoring the config in <120 seconds.
* **Artifacts:**
    * Change Request (CR)

