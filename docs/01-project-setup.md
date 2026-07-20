# Project Setup

## Project Overview

This project documents the design and implementation of a Home Security Operations Center (Home SOC) using Wazuh SIEM in a virtual lab environment.

The objective is to gain practical experience in deploying a SIEM platform, monitoring Windows endpoints, collecting security logs, performing threat hunting, and documenting security investigations.

---

## Project Objectives

- Build a functional Home SOC using Wazuh.
- Monitor a Windows endpoint from a centralized SIEM.
- Collect and analyze Windows Event Logs.
- Perform threat hunting using security events.
- Develop practical SOC analyst skills through hands-on exercises.

---

## Lab Environment

| Component | Details |
|----------|---------|
| Host Operating System | Windows 11 |
| Virtualization Platform | Oracle VirtualBox |
| Guest Operating System | Ubuntu Server 24.04 LTS |
| SIEM Platform | Wazuh 4.13.1 |
| Endpoint | Windows 11 |
| Agent | Wazuh Windows Agent |

---

## Architecture

```text
Windows 11 Endpoint
        │
        │ Wazuh Agent
        ▼
Ubuntu Server 24.04 (VirtualBox)
        │
        ▼
Wazuh Manager
Wazuh Indexer
Wazuh Dashboard
```

---

## Technologies Used

- Wazuh SIEM
- Ubuntu Server 24.04 LTS
- Windows 11
- Oracle VirtualBox
- Windows Event Logs

---

## Current Progress

- Ubuntu Server deployed
- Wazuh platform installed
- Wazuh Dashboard configured
- Windows endpoint connected
- Security event collection verified
- Initial threat hunting performed

---

## Skills Demonstrated

- Virtual Machine Deployment
- Linux Administration
- SIEM Deployment
- Endpoint Monitoring
- Security Event Analysis
- Threat Hunting
- Technical Documentation
