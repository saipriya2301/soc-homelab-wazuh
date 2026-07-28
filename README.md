# SOC Homelab with Wazuh

A resume-ready Security Operations Center (SOC) homelab built using **Wazuh**, **Ubuntu Server**, and a **Windows 11 endpoint agent**. This project demonstrates endpoint monitoring, centralized log collection, threat hunting, and basic detection engineering in a virtualized environment.

## Project Overview

The lab consists of:

* **Wazuh Manager + Indexer + Dashboard** running on Ubuntu (VirtualBox)
* **Windows 11 endpoint** enrolled as a Wazuh agent
* Centralized collection of Windows Security, System, and Application event logs
* Threat hunting using Wazuh dashboards and event queries
* Detection validation using real Windows events (including Event ID 4624 logon activity)

## Architecture

Windows 11 Endpoint (SP-WIN-01)
|
v
Wazuh Agent
|
v
Wazuh Manager (Ubuntu VM)
|
v
Wazuh Indexer
|
v
Wazuh Dashboard

## What Has Been Implemented

### Infrastructure

* Ubuntu 24.04 virtual machine
* Oracle VirtualBox
* Bridged networking
* Wazuh 4.13.1 deployment
* Windows 11 endpoint enrollment

### Endpoint Monitoring

* Windows Security log collection
* Windows System log collection
* Windows Application log collection
* Microsoft Sysmon Operational log collection
* Agent health monitoring

### Threat Hunting

* Event ID 4624 (Successful Logon)
* Registry Integrity Monitoring (FIM)
* Service configuration changes
* Sysmon Process Creation (Event ID 1)

### Detection Engineering

* Integrated Sysmon Event ID 1 (Process Creation) into Wazuh
* Developed a custom Wazuh rule to detect Notepad process creation
* Validated the detection using Sysmon-generated Windows events
* Verified end-to-end log collection from Windows → Wazuh Manager → Dashboard

## Detection Engineering

Implemented a custom Wazuh detection rule for Sysmon Process Creation events.

### Detection Workflow

```
Windows Process
        │
        ▼
Sysmon Event ID 1
        │
        ▼
Wazuh Agent
        │
        ▼
Wazuh Manager
        │
        ▼
Custom Detection Rule
        │
        ▼
Security Alert
```

### Custom Detection

- Data Source: Microsoft-Windows-Sysmon/Operational
- Event ID: 1 (Process Creation)
- Custom Rule: Detect Notepad execution
- Alert generated successfully in Wazuh Threat Hunting

## Skills Demonstrated

* SIEM Deployment
* Wazuh Administration
* Sysmon Integration
* Windows Event Logging
* Detection Engineering
* Threat Hunting
* Endpoint Monitoring
* Log Analysis
* Incident Investigation
* Custom Rule Development
* Sysmon Integration
* Custom SIEM Rule Development
* Windows Process Monitoring
  

## Environment

| Component | Version |
|----------|---------|
| Ubuntu | 24.04 |
| Wazuh | 4.13.1 |
| Sysmon | Latest |
| Windows | Windows 11 |
| Virtualization | Oracle VirtualBox |

## Project Status

✅ Infrastructure Complete

✅ Windows Agent Monitoring

✅ File Integrity Monitoring

✅ Sysmon Integration

✅ Custom Detection Engineering

🚧 Next:
- Active Response
- MITRE ATT&CK Mapping
- Attack Simulations
- Dashboards
