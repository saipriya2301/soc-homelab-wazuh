# SOC Homelab with Wazuh

A hands-on **Security Operations Center (SOC) homelab** built using **Wazuh, Ubuntu Server, Sysmon, and a Windows 11 endpoint**.

The project demonstrates an end-to-end Blue Team workflow covering endpoint telemetry collection, centralized security monitoring, threat hunting, file integrity monitoring, detection engineering, MITRE ATT&CK mapping, controlled attack simulation, false-positive analysis, and automated Active Response.

---

## Project Highlights

- Deployed a Wazuh-based SOC monitoring environment
- Enrolled and monitored a Windows 11 endpoint
- Integrated Microsoft Sysmon with Wazuh
- Collected Windows and Sysmon security telemetry
- Implemented File Integrity Monitoring (FIM)
- Performed threat hunting and alert investigation
- Developed and validated a custom Wazuh detection rule
- Performed controlled Windows discovery simulations
- Analyzed benign activity and false positives
- Mapped detected activity to MITRE ATT&CK
- Implemented a custom stateful Active Response
- Validated automated response and 30-second rollback

---

## Architecture

```text
Windows 11 Endpoint (SP-WIN-01)
        │
        │ Windows Events + Sysmon
        ▼
    Wazuh Agent
        │
        ▼
 Wazuh Manager
   (Ubuntu VM)
        │
        ▼
  Wazuh Indexer
        │
        ▼
 Wazuh Dashboard
        │
        ├── Threat Hunting
        ├── Detection Rules
        ├── Alert Investigation
        └── MITRE ATT&CK Analysis
```

---

## Environment

| Component | Technology |
|---|---|
| Endpoint | Windows 11 |
| SIEM / XDR | Wazuh 4.13.1 |
| Wazuh Manager OS | Ubuntu 24.04 |
| Endpoint Telemetry | Microsoft Sysmon |
| Virtualization | Oracle VirtualBox |
| Response Automation | Python |
| Threat Framework | MITRE ATT&CK |

---

## Endpoint Monitoring

The Windows 11 endpoint was enrolled in Wazuh as:

```text
SP-WIN-01
```

Security telemetry collected from the endpoint included:

- Windows Security logs
- Windows System logs
- Windows Application logs
- Microsoft Sysmon Operational logs
- File Integrity Monitoring events
- Process creation telemetry
- Authentication events
- Agent health information

This provided centralized visibility into endpoint activity through the Wazuh Dashboard.

---

## File Integrity Monitoring

Wazuh File Integrity Monitoring (FIM) was configured and tested to detect filesystem changes.

The implementation provided visibility into:

- File creation
- File modification
- File deletion

FIM alerts were investigated through the Wazuh Dashboard.

---

## Sysmon Integration

Microsoft Sysmon was integrated with the Wazuh Windows agent to provide detailed endpoint telemetry.

The Sysmon Operational event channel was collected by Wazuh:

```text
Microsoft-Windows-Sysmon/Operational
```

A major focus was:

```text
Sysmon Event ID 1 — Process Creation
```

The resulting telemetry provided information such as:

- Process image
- Command line
- Parent process
- Process ID
- User context
- Process creation timestamp

---

## Threat Hunting

Threat hunting was performed using Wazuh events and endpoint telemetry.

Investigated activity included:

- Successful Windows logons
- Failed authentication events
- Process creation
- Command-line execution
- Parent-child process relationships
- File and registry integrity activity
- Service-related activity
- Sysmon events

The investigations also included distinguishing suspicious-looking alerts from legitimate system and application activity.

---

## Detection Engineering

A custom Wazuh rule was developed to detect Notepad process creation using Sysmon Event ID 1.

### Custom Detection

```text
Rule ID:     100100
Rule Level:  5
Description: Custom Detection: Notepad process created
Data Source: Sysmon Event ID 1
```

### Detection Workflow

```text
Notepad.exe
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
Custom Rule 100100
     │
     ▼
Wazuh Alert
```

The rule was successfully validated using real process creation telemetry from the Windows endpoint.

---

## Controlled Attack Simulations

Benign Windows discovery commands were executed to generate security telemetry and validate Wazuh detections.

Examples included:

```cmd
whoami
net user
net user guest
```

The simulations generated Wazuh alerts that were investigated through the dashboard.

One notable detection was generated for:

```cmd
net user guest
```

with Wazuh Rule:

```text
92039
```

These tests demonstrated how endpoint discovery behavior can be identified through command-line and process telemetry.

All simulations were performed in a controlled lab environment.

---

## MITRE ATT&CK Mapping

Detected activity was analyzed using the **MITRE ATT&CK framework**.

The discovery simulations demonstrated how individual endpoint events can be interpreted as attacker behaviors rather than viewed only as isolated alerts.

This added threat context to the detection and investigation workflow.

---

## False-Positive Analysis

The lab also included investigation of alerts generated by legitimate system and application activity.

Examples included activity associated with:

- Microsoft Defender
- Windows Update
- Adobe software

Process paths, command lines, parent processes, and event context were examined before determining whether activity was suspicious.

This reinforced an important SOC principle:

> An alert is an investigation starting point, not automatic proof of malicious activity.

---

## Active Response

A custom **stateful Wazuh Active Response** was implemented and validated.

For safety, the response was intentionally designed to avoid making disruptive changes to the Windows endpoint.

The response was associated with custom Rule `100100`:

```text
Notepad.exe
      │
      ▼
Sysmon Event ID 1
      │
      ▼
Custom Rule 100100
      │
      ▼
Wazuh Active Response
      │
      ▼
Custom Python Script
```

The custom response executed on the **Ubuntu Wazuh manager**, not on the Windows endpoint.

When triggered, it created a harmless temporary marker:

```text
/tmp/wazuh-active-response-test.txt
```

The marker confirmed that the automated response had executed successfully.

---

## Stateful Response and Rollback

The Active Response was configured with a **30-second timeout**.

```text
Detection
    │
    ▼
Active Response
    │
    ▼
Marker Created
    │
    ▼
30-Second Timeout
    │
    ▼
Automatic Rollback
    │
    ▼
Marker Removed
```

Testing successfully confirmed both:

- Active Response execution
- Automatic timeout-based rollback

After validation and documentation, the test Active Response was **disabled**, while the underlying Sysmon monitoring and custom detection rule remained operational.

No Windows firewall, network, user account, registry, or other disruptive endpoint changes were performed by the response.

---

## End-to-End SOC Workflow

The completed project demonstrates:

```text
Endpoint Activity
       │
       ▼
Sysmon / Windows Logs
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Detection & Alerting
       │
       ▼
Threat Investigation
       │
       ▼
MITRE ATT&CK Mapping
       │
       ▼
Active Response
       │
       ▼
Automatic Rollback
```

---

## Documentation

Detailed implementation notes are available in the `docs/` directory:

- Project Setup
- Wazuh Installation
- Windows Agent Installation
- Log Collection
- Threat Hunting
- File Integrity Monitoring
- Sysmon Integration
- Custom Detection Rules
- Active Response
- MITRE ATT&CK Mapping
- Attack Simulations
- Project Summary

Evidence and validation screenshots are available in the `screenshots/` directory.

---

## Skills Demonstrated

- SIEM/XDR fundamentals
- Wazuh administration
- Windows endpoint monitoring
- Linux administration
- Microsoft Sysmon
- Windows Event Log analysis
- File Integrity Monitoring
- Threat hunting
- Detection engineering
- Custom Wazuh rule development
- Process and command-line analysis
- Parent-child process investigation
- Security alert triage
- False-positive analysis
- Controlled attack simulation
- MITRE ATT&CK mapping
- Active Response
- Python-based security automation
- Stateful response and rollback
- Technical documentation

---

## Repository Structure

```text
soc-homelab-wazuh/
│
├── configs/
│   └── Configuration files
│
├── docs/
│   └── Detailed project documentation
│
├── screenshots/
│   └── Detection and validation evidence
│
└── README.md
    └── Project overview
```

---

## Project Status

| Phase | Status |
|---|---|
| SOC Infrastructure | ✅ Complete |
| Windows Agent Monitoring | ✅ Complete |
| Log Collection | ✅ Complete |
| File Integrity Monitoring | ✅ Complete |
| Sysmon Integration | ✅ Complete |
| Threat Hunting | ✅ Complete |
| Custom Detection Engineering | ✅ Complete |
| Attack Simulation | ✅ Complete |
| MITRE ATT&CK Mapping | ✅ Complete |
| Active Response | ✅ Complete |
| Automatic Rollback Validation | ✅ Complete |
| Project Documentation | ✅ Complete |

---

## Key Takeaways

This project provided practical experience with the complete security monitoring lifecycle rather than only SIEM installation.

The lab progressed through:

```text
Telemetry
    ↓
Detection
    ↓
Alert
    ↓
Investigation
    ↓
Threat Context
    ↓
Response
    ↓
Rollback
```

It demonstrated how endpoint telemetry can be collected, analyzed, converted into custom detections, validated through controlled simulations, investigated for false positives, mapped to MITRE ATT&CK, and connected to safe automated response mechanisms.

---

## Final Result

**Completed ✅**

The SOC homelab successfully demonstrates an end-to-end Blue Team detection and response workflow using Wazuh and Sysmon.
