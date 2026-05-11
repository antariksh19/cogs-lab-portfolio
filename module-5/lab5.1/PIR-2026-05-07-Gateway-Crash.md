# Post-Incident Report (PIR)

**Incident ID:** INC-2026-0507-002  
**Date:** 2026-05-07  
**Severity:** P1  
**Status:** Resolved  

## Incident Summary
At 12:48 IST, the Nginx gateway became unresponsive, resulting in a total loss of access for all lab users. The issue was detected through Uptime Kuma monitoring and investigated using Prometheus metrics. The incident was resolved by manually restarting the Nginx service after identifying a resource exhaustion event.

## Evidence of Detection
![Uptime Kuma Red Alert](../../screenshots/uptime-kuma-red.png)

## Timeline

| Time (IST) | Event |
| :--- | :--- |
| 12:48 | Gateway became unresponsive; Uptime Kuma heartbeats turned RED |
| 12:50 | P1 incident ticket created; acknowledgement update posted |
| 12:51 | Prometheus analysis confirmed Memory usage spike to 89.4% |
| 12:52 | CPU usage identified peaking at 21.3% concurrently |
| 12:53 | Investigation notes documented regarding resource exhaustion |
| 12:54 | Manual service intervention initiated via terminal |
| 12:55 | Nginx service restarted; system metrics began normalizing |
| 12:57 | Uptime Kuma heartbeats returned to GREEN; resolution confirmed |

## Resource Analysis
Below is the Prometheus data captured during the investigation phase:

![Prometheus Memory Spike](../../screenshots/prometheus-memory.png)

![Prometheus CPU Spike](../../screenshots/prometheus-cpu.png)

## Root Cause
The technical root cause was **Resource Exhaustion**. High memory utilization (89%) caused the Nginx process to hang and stop responding to monitoring heartbeats.

## Impact Assessment
* **Users Affected:** 100% of lab environment users.
* **Duration:** Approximately 9 minutes of total downtime.
* **Business Impact:** Complete interruption of ZTNA gateway application routing.

## Resolution Steps
1. Validated hardware and resource metrics using Prometheus.
2. Executed `sudo systemctl start nginx` to restore service availability.
3. Verified successful recovery through Uptime Kuma heartbeats.

## Recovery Verification
![Uptime Kuma Green Recovery](../../screenshots/uptime-kuma-green.png)

## Prevention Actions
* **Action:** Configure Grafana alerts for Memory usage exceeding 80%.
  * **Owner:** Antariksh Mohapatra | **Due:** 2026-05-10

* **Action:** Enable `systemctl` auto-restart policy for the Nginx service.
  * **Owner:** Antariksh Mohapatra | **Due:** 2026-05-12

## Open Items
- [ ] Review system logs to identify the exact process responsible for the memory spike.