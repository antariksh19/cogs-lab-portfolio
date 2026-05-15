# cogs-lab-portfolio
COGS Tech Support Lab Portfolio

## My Lab Portfolio
**Engineer:** Antariksh
**Started:** 5 May 2026

This repository contains the end-to-end technical documentation and evidence for the **COGS Lab**. It serves as a professional record of cloud infrastructure deployment, monitoring integration, and system administration.

---

## Global Tech Stack
* **Cloud:** AWS (Ubuntu 26.04 LTS)
* **Web Services:** Nginx Gateway
* **Observability:** Prometheus, Grafana, Node Exporter, Uptime Kuma
* **Security:** TLS 1.3, AES-256 Encryption, SSH Key-Based Auth

---

## Module 1: Infrastructure Setup
* **Objective:** Deploy a secure cloud environment and reverse proxy.
* **Key Tasks:** Provisioned Linux VM with hardened SSH access, configured Nginx reverse proxy, and implemented firewall rules for Ports 80, 443, and 3000.
* [Lab 1.1 Findings](./module-1/lab1.1/lab1.1-findings.md)
* [Lab 1.2 Findings](./module-1/lab1.2/lab1.2-findings.md)
* [Lab 1.3 Findings](./module-1/lab1.3/lab1.3-findings.md)

## Module 2: Identity & Access Management
* **Objective:** Configure user directories, SSO, and multi-factor authentication.
* [Lab 2.1 Findings](./module-2/lab2.1/lab2.1-findings.md)
* [Lab 2.2 Findings](./module-2/lab2.2/lab2.2-findings.md)
* [Lab 2.3 Findings](./module-2/lab2.3/lab2.3-findings.md)

## Module 3 & 4: Observability & Ticketing
* **Objective:** Implement a full-stack monitoring, alerting, and ITIL ticketing system.
* **Key Tasks:** Deployed Node Exporter, Prometheus, Grafana, and Uptime Kuma.
* [Lab 3.1 Findings](./module-3/lab3.1/lab3.1-findings.md)
* [Lab 3.2 Findings](./module-3/lab3.2/lab3.2-findings.md)
* [Lab 4.1 Findings](./module-4/lab4.1/lab4.1-findings.md)
* [Lab 4.2 Handover (18:00)](./module-4/lab4.2/handover-2026-05-07-1800.md)
* [Lab 4.2 PIR: MFA Bulk Failure](./module-4/lab4.2/PIR-2026-05-07-MFA-Bulk-Failure.md)

## Module 5: Incident & Change Management
* **Objective:** Act as Incident Commander for outages and execute secure infrastructure upgrades.
* **Process:** Detected outages, analyzed resource spikes, executed recovery, and migrated TLS protocols demonstrating success-and-rollback competency.
* [Lab 5.1 PIR: Gateway Crash](./module-5/lab5.1/PIR-2026-05-07-Gateway-Crash.md)
* [Lab 5.1 PACE Shift Handover](./module-5/lab5.1/handover-2026-05-07-P1.md)
* [Lab 5.2 CR: TLS Upgrade](./module-5/lab5.2/CHANGE-001-TLS-Upgrade.md)

## Capstone Lab: Mini Zero Trust Architecture (ZTNA)
* **Objective:** Design and deploy a mini enterprise-style Zero Trust architecture using secure tunnels, reverse proxying, TLS encryption, and infrastructure monitoring.
* **Key Tasks:** Configured WireGuard VPN, segmented backend applications, Nginx proxy, TLS 1.3, and Uptime Kuma. Troubleshot Docker, JVM optimization, and disk limits.
* [Mini ZTNA Findings Report](./capstone/mini_ztna_findings.md)

