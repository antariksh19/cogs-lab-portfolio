# Lab 2.1 Findings: OpenLDAP Directory
**Author:** Antariksh Mohapatra
**Date:** May 6, 2026

---

## 1. Directory Setup
I configured the **slapd** service on my local environment to act as our primary identity store. 

*(Configuration aligned with the [Official Ubuntu OpenLDAP Server Guide](https://ubuntu.com/server/docs/service-ldap)).*
- **Base DN:** `dc=lab,dc=instasafe,dc=local`
- **Tooling:** Used `ldap-utils` (installed via the `apt` package manager).

## 2. Evidence of Success

### User Search (ldapsearch)
The search command successfully returned the records for both Alice and Bob. This proves the directory tree is correctly populated and indexed.
![LDAP Users](../../screenshots/ldap_users.png)

### Authentication (Bind)
- **Success:** The `ldapwhoami` command confirmed Alice can successfully bind and authenticate against the directory.
![LDAP Success](../../screenshots/ldap_bind_success.png)
- **Failure:** Submitting incorrect passwords intentionally triggered an 
**Error 49 (Invalid Credentials)**, proving the authentication logic and password verification are actively enforcing security. 

*(Cross-referenced with the official [IETF RFC 4511 LDAP Protocol Specifications](https://datatracker.ietf.org/doc/html/rfc4511#section-4.1.9)).*

![LDAP Error 49](../../screenshots/ldap_error_49.png)

---

## 3. Support Engineering Insights

- **Root Cause Analysis:** If the **InstaSafe Gateway** cannot reach this directory server, the first troubleshooting step is verifying the **Port 389** listener status using `systemctl status slapd` and ensuring the network firewall allows inbound LDAP traffic.
- **AD Sync / ZTNA Integration:** In a production **Zero Trust Network Access (ZTNA)** environment, the **Controller** acts as the LDAP client. It binds to this server to securely verify user identities and group memberships before dynamically granting access to downstream applications. 

*(To review the architectural relationship between Identity Providers and Zero Trust enforcement, I referenced [Cloudflare's IAM vs. ZTNA Guide](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)).*