# SOC Home Lab with Wazuh

## Overview

This project documents the creation of a Security Operations Center (SOC) Home Lab using Wazuh for Windows event monitoring and threat detection.

The goal of this project is to gain hands-on experience with SIEM technologies, Windows log collection, security monitoring, threat hunting, and incident investigation.

This repository will be continuously updated as additional security use cases, attack simulations, detections, and dashboards are implemented.

---

## Objectives

- Build a SOC home lab from scratch
- Deploy Wazuh Manager on Ubuntu
- Install and configure a Windows Wazuh Agent
- Collect Windows Event Logs
- Monitor Security, System, and Application events
- Perform basic threat hunting
- Investigate Windows security events
- Document findings professionally

---

## Lab Architecture

```
Windows 11 Machine
        │
        │ Wazuh Agent
        │
        ▼
Ubuntu Server (VirtualBox)
        │
        ▼
Wazuh Manager
        │
        ▼
Wazuh Dashboard
```

---

## Environment

| Component | Version |
|-----------|---------|
| Host OS | Windows 11 |
| Virtualization | Oracle VirtualBox |
| Guest OS | Ubuntu Server 24.04 LTS |
| SIEM | Wazuh 4.13.1 |
| Agent | Wazuh Windows Agent |
| Browser | Google Chrome |

---

## Completed So Far

- Installed Ubuntu Server
- Updated Ubuntu packages
- Installed Wazuh Platform
- Accessed Wazuh Dashboard
- Deployed Windows Agent
- Connected Windows Agent to Wazuh Manager
- Verified agent communication
- Collected Windows Event Logs
- Investigated Windows Event ID 4624 (Successful Logon)
- Performed basic event searches using Wazuh Dashboard

---

## Sample Events Observed

- Event ID 4624 – Successful Logon
- Event ID 7040 – Service Startup Type Changed
- Registry Integrity Monitoring Events

---

## Skills Demonstrated

- SIEM Administration
- Wazuh
- Ubuntu Linux
- Windows Event Logs
- Threat Hunting
- Security Monitoring
- Log Analysis
- VirtualBox
- Incident Investigation

---

## Project Status

🚧 In Progress

Upcoming tasks include:

- Sysmon integration
- Detection rules
- MITRE ATT&CK mapping
- Brute-force attack simulation
- PowerShell attack detection
- Malware detection
- Custom Wazuh rules
- Active Response
- Dashboards
- Documentation

---

## Author

Sai Priya MVN
