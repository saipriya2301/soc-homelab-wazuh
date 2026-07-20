# Wazuh Manager Installation

## Objective

Deploy the Wazuh platform on an Ubuntu Server virtual machine to serve as the central Security Information and Event Management (SIEM) solution for collecting, processing, and analyzing security events from monitored endpoints.

---

## Lab Environment

| Component | Details |
|----------|---------|
| Host Operating System | Windows 11 |
| Virtualization Platform | Oracle VirtualBox |
| Guest Operating System | Ubuntu Server 24.04 LTS |
| SIEM Platform | Wazuh 4.13.1 |

---

## Installation Overview

The Wazuh platform was installed on an Ubuntu Server virtual machine following the official installation guide. The deployment included:

- Wazuh Manager
- Wazuh Indexer
- Wazuh Dashboard

After the installation completed successfully, the Wazuh services were started automatically and the dashboard became accessible through a web browser.

---

## Verification

The installation was verified by confirming:

- All Wazuh services were running successfully.
- The Wazuh Dashboard was accessible.
- The dashboard loaded without errors.
- The manager was ready to receive endpoint agents.

---

## Outcome

The Wazuh platform was successfully deployed and configured as the central monitoring server for the Home SOC environment.

This installation established the foundation required for endpoint monitoring, security event collection, threat detection, and future incident investigations.

---

## Skills Demonstrated

- Ubuntu Server Administration
- Wazuh Deployment
- SIEM Configuration
- Virtual Machine Management
- Security Monitoring Infrastructure

---

## References

- Official Wazuh Documentation: https://documentation.wazuh.com/
