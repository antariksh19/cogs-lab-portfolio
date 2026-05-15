# Lab 1.1 Findings
**Author:** Antariksh Mohapatra
**Date:** May 6, 2026

## My VM Details
- **Provider:** AWS
- **Region:** ap-south-1 (Mumbai)
- **OS:** Ubuntu 26.04 LTS

## Experiment Results

### Ping to 8.8.8.8
- **Average RTT:** 1.224 ms
- **TTL value observed:** 117

**Question:** **What does TTL tell us about the path?**

**Answer:**
TTL (Time to Live) is a mechanism that limits the lifespan of data in a network to prevent infinite loops. Each router the packet crosses decrements the TTL by 1. A value of 117 suggests the packet started at a standard base (like 128) and passed through roughly 11 hops before reaching its destination.

![Ping Result](../../screenshots/ping_result.png)

### Traceroute to google.com
- **Number of hops:** 18

**Question:** **Any * * * hops? At which hop number?** **Answer:** Yes, hops 10 through 17 showed `* * *` timeouts. This indicates that those specific routers are configured to prioritize forwarding traffic over responding to ICMP diagnostic requests (Traceroute), likely for security or resource management. 

*(For a deeper understanding of packet lifespans and routing, I referenced [Cloudflare's Guide to Time-to-Live](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)).*

![Traceroute Result](../../screenshots/traceroute_result.png)

### DNS Comparison
- **Result from default DNS:** 142.251.167.100
- **Result from 1.1.1.1:** 172.253.122.100

**Question:** **Are they different? Why might they differ?** **Answer:**
Yes, they are different. DNS providers use Anycast and geo-routing to return the IP address of the edge server that is geographically or logically closest to the requester to reduce latency.

<img src="../../screenshots/DNS_comparission1.png" alt="DNS Comparission1" width="500" />
<img src="../../screenshots/DNS_comparission2.png" alt="DNS Comparission2" width="500" />

### google.com TLS Certificate
- **Issuer:** Google Trust Services, CN=WR2
- **Expiry date:** July 1, 2026
- **TLS version used:** TLSv1.3

 *(To understand the exact cryptographic handshake optimizations in this protocol, I referenced [Cloudflare's Technical Breakdown of TLS 1.3](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/)).*

![TLS Certificate](../../screenshots/tls_certificate.png)