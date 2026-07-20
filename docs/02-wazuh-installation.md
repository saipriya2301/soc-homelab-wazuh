# Wazuh Manager Installation

## Objective

Deploy the Wazuh platform on an Ubuntu Server virtual machine to establish the Security Information and Event Management (SIEM) solution for the Home SOC lab.

---

## Why Wazuh?

Wazuh is an open-source SIEM and Extended Detection and Response (XDR) platform that provides centralized log collection, security monitoring, file integrity monitoring, vulnerability detection, and threat hunting capabilities. It was selected for this project because it is widely adopted in the cybersecurity community and offers enterprise-grade security monitoring features suitable for hands-on learning.

---

## Prerequisites

Before installing Wazuh, the following environment was prepared:

- Ubuntu Server 24.04 LTS installed on Oracle VirtualBox
- System packages updated to the latest version
- Internet connectivity configured
- Sufficient system resources allocated for the virtual machine

---

## Installation Process

The official Wazuh installation assistant was used to deploy the platform.

The installation included the following components:

- Wazuh Manager
- Wazuh Indexer
- Wazuh Dashboard

After the installation completed successfully, the Wazuh services were started automatically.

---

## Verification

The installation was verified by performing the following checks:

- Successfully accessed the Wazuh Dashboard through a web browser.
- Confirmed that the Wazuh Manager service was running.
- Verified that the dashboard loaded without errors.
- Confirmed the server was ready to receive endpoint agents.

---

## Outcome

The Wazuh platform was successfully deployed as the central monitoring solution for the Home SOC environment.

This deployment provides the foundation for endpoint monitoring, centralized log management, threat detection, and security investigations.

---

## Skills Demonstrated

- Ubuntu Server Administration
- SIEM Deployment
- Wazuh Platform Installation
- Linux System Management
- Virtual Machine Administration

---

## References

- Wazuh Documentation: https://documentation.wazuh.com/
