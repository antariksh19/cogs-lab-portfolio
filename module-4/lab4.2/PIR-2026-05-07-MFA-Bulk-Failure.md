# Post-Incident Report (PIR)
**Incident ID:** INC-2026-0507-001
**Date:** 2026-05-07
**Severity:** P2
**Status:** Resolved

## Incident Summary
At 09:15 IST, a mid-size financial institution reported that 25 users in their Finance Department were unable to receive SMS OTPs for MFA. The issue was detected via customer report and confirmed through the Kaleyra provider dashboard. The incident was resolved by switching to a backup sender ID after identifying a carrier-level block.

## Timeline
| Time (IST) | Event |
| :--- | :--- |
| 09:15 | Customer reported MFA failure for 25 users |
| 09:18 | Ticket #1 created with priority P2 |
| 09:20 | First response sent to customer acknowledging the issue |
| 09:35 | Kaleyra dashboard checked; bulk REJECTED codes confirmed |
| 10:30 | Incident escalated to L2 for sender ID investigation |
| 11:30 | L2 identified root cause: Primary sender ID flagged for DND violation |
| 11:40 | Backup sender ID activated and verified with test numbers |
| 11:45 | Customer confirmed OTPs are working for all affected users |

## Root Cause
The technical root cause was a DND (Do Not Disturb) violation flag issued by TRAI against the primary Kaleyra sender ID. This occurred because another sender was sharing the same route, leading to a bulk block at the carrier level.

## Impact Assessment
* **Users Affected:** 25 users in the Finance Department.
* **Duration:** 2 hours and 30 minutes.
* **Business Impact:** Critical finance operations were delayed as users could not authenticate into the ZTNA gateway.

## Resolution Steps
1. Investigated logs in the Kaleyra provider dashboard to identify REJECTED status codes.
2. Escalated to L2 to coordinate with the telecom provider.
3. Re-routed traffic through a verified backup sender ID.

## Prevention Actions
* **Action:** Implement automated sender ID monitoring alerts in the Kaleyra dashboard.
  * **Owner:** Support Lead | **Due:** 2026-05-15
* **Action:** Establish a secondary pre-verified sender ID route for all Tier-1 financial tenants.
  * **Owner:** L3 Engineering | **Due:** 2026-05-20

## Open Items
- [ ] Create a Knowledge Base (KB) article regarding carrier-level DND blocks.