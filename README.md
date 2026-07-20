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

* Ubuntu VM configured in VirtualBox
* Bridged networking enabled
* Wazuh 4.13.1 installed (Manager, Indexer, Dashboard)

### Endpoint Monitoring

* Windows 11 agent enrolled successfully
* Agent status verified as **Active**
* Security, System, and Application logs collected centrally

### Threat Hunting

* Event searches performed in Wazuh
* Windows Security Event ID **4624** (successful logon) identified and validated
* Registry integrity monitoring events observed
* Service configuration change events analyzed

## Skills Demonstrated

* SIEM deployment and administration
* Endpoint log collection
* Windows Event Log analysis
* Threat hunting
* Network configuration
* Security monitoring
* Incident investigation fundamentals

## Environment

| Component      | Version           |
| -------------- | ----------------- |
| Ubuntu         | 24.04             |
| Wazuh          | 4.13.1            |
| Windows        | Windows 11        |
| Virtualization | Oracle VirtualBox |

## Project Status

**In Progress** — Additional detections, dashboards, and documentation will be added as the homelab evolves.
