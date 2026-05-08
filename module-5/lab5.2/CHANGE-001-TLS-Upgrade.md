# Change Request (CR): TLS 1.3 Upgrade
**Change ID:** CR-2026-05-08-001
**Requested By:** Antariksh Mohapatra
**Priority:** Normal
**Risk Level:** Medium

## 1. Description of Change
Update the Nginx configuration to enable and prioritize TLS 1.3 for all HTTPS traffic to improve security and performance.

## 2. Impact Assessment
* **Service:** Nginx Gateway (Port 443).
* **Users:** All users connecting via HTTPS.
* **Downtime:** Approximately 30 seconds for a service reload.

## 3. Execution Plan (Step-by-Step)
1. SSH into the cloud VM.
2. Backup the current Nginx config: `sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak`.
3. Open the config: `sudo nano /etc/nginx/sites-available/default`.
4. Locate the `ssl_protocols` line and change it to: `ssl_protocols TLSv1.2 TLSv1.3;`.
5. Add: `ssl_prefer_server_ciphers on;`.
6. Test the configuration: `sudo nginx -t`.
7. Reload Nginx: `sudo systemctl reload nginx`.

## 4. Rollback Plan
If the configuration test fails or service goes offline:
1. Restore the backup: `sudo mv /etc/nginx/sites-available/default.bak /etc/nginx/sites-available/default`.
2. Reload Nginx: `sudo systemctl reload nginx`.

## 5. Verification Plan
* Run `curl -I -v --tlsv1.3 https://localhost` (if certificate is present) or check Uptime Kuma for a green status.

## 6. Implementation Results
* **Status:** IN PROGRESS
* **Outcome:** Success.
* **Verification of Step 3:** Confirmed `nginx -t` returned "syntax is ok" and "test is successful" before reloading.
* **Verification of TLS:** `openssl` check confirmed `Protocol: TLSv1.3` and rejected TLS 1.2 connections.
* **Rollback Test Execution:** 
    1. Manually removed a semicolon from `/etc/nginx/sites-available/lab-tls`.
    2. Ran `sudo nginx -t` and received error
    3. Executed rollback using `lab-tls.backup`.
    4. Verified recovery with `sudo nginx -t`: 
       "test is successful"
* **Verification of TLS:** Final `openssl` check confirmed `Protocol: TLSv1.3`.