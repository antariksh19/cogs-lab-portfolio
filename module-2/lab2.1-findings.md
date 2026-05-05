# Lab 2.1 Findings: OpenLDAP

## 1. Directory Structure
I have successfully configured the base DN as `dc=lab,dc=instasafe,dc=local` and created two organizational units (OUs): `People` and `Groups`.

## 2. Verification Results

### User Discovery
Running `ldapsearch` correctly returns both Alice and Bob with their assigned `mail` attributes.
![LDAP Users List](../screenshots/ldap_users.png)

### Authentication (Bind) Success
`ldapwhoami` returns a success message for Alice using the password `Alice@123`.
![LDAP Bind Success](../screenshots/ldap_bind_success.png)

### Authentication (Bind) Failure
Using an incorrect password triggers **LDAP Error 49 (Invalid Credentials)**.
![LDAP Error 49](../screenshots/ldap_error_49.png)

## 3. InstaSafe Connection (Support Engineering)
* **Base DN:** In InstaSafe, this tells the Controller exactly where to look for users in a customer's Active Directory[cite: 1].
* **Bind DN:** This is the service account InstaSafe uses to talk to the AD server. If it lacks permissions, the sync fails[cite: 1].
* **Error 49:** When this appears in InstaSafe logs, it means the service account password is wrong or expired[cite: 1].