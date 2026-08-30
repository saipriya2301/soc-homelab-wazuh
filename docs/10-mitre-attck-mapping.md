# MITRE ATT&CK Mapping

## Overview

MITRE ATT&CK is a knowledge base of adversary tactics and techniques based on real-world attacker behavior.

In this SOC homelab, MITRE ATT&CK is used to classify detected security activity and provide additional context about the behavior associated with Wazuh alerts.

Mapping detections to MITRE ATT&CK helps answer two important questions:

- What behavior was detected?
- What attacker tactic or technique could this behavior represent?

This project maps only detections that were observed and validated within the homelab environment.

---

## Detection Mapping

The following MITRE ATT&CK techniques were observed during detection testing and attack simulations.

| Activity | Wazuh Rule | MITRE Technique | Technique ID | Tactic |
|---|---|---|---|---|
| `net user guest` account enumeration | 92039 | Account Discovery | T1087 | Discovery |
| Windows command shell activity | 92032 | Windows Command Shell | T1059.003 | Execution |

> Only techniques validated through observed Wazuh alerts are included in the current mapping.

---

# 1. Account Discovery

## MITRE ATT&CK Technique

**Technique:** Account Discovery  
**Technique ID:** T1087  
**Tactic:** Discovery

Account Discovery refers to activity used to identify accounts that exist on a system or within an environment.

An attacker who has gained access to a Windows endpoint may attempt to enumerate user accounts to better understand the compromised system.

---

## Simulation

A controlled account discovery simulation was performed on the monitored Windows endpoint.

The following command was executed from PowerShell:

```powershell
net user guest
```

The command queries information about the local Windows Guest account.

The simulation was performed on the monitored endpoint:

```text
Agent: SP-WIN-01
Operating System: Windows 11
```

---

## Detection

After executing the command, Wazuh generated an alert associated with account discovery activity.

The primary detection was:

```text
Rule ID: 92039
Description: A net.exe account discovery command was initiated
```

The alert was mapped by Wazuh to:

```text
MITRE ATT&CK Technique: Account Discovery
Technique ID: T1087
Tactic: Discovery
```

---

## Process Investigation

The alert was investigated using the event information available in Wazuh Threat Hunting.

The underlying process telemetry showed:

```text
Process:
C:\Windows\System32\net1.exe

Command Line:
C:\WINDOWS\system32\net1 user guest

Parent Process:
C:\Windows\System32\net.exe

Parent Command Line:
net.exe user guest

Integrity Level:
Medium
```

This process information confirmed that the account discovery command executed on the Windows endpoint was successfully captured and analyzed by Wazuh.

---

## Detection Flow

The account discovery detection followed this path:

```text
PowerShell
     │
     ▼
net user guest
     │
     ▼
Windows Process Execution
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
Rule 92039
     │
     ▼
Account Discovery Alert
     │
     ▼
MITRE ATT&CK T1087
```

This validated the complete monitoring pipeline from endpoint activity to MITRE ATT&CK-mapped detection.

---

# 2. Windows Command Shell

## MITRE ATT&CK Technique

**Technique:** Command and Scripting Interpreter: Windows Command Shell  
**Technique ID:** T1059.003  
**Tactic:** Execution

Windows Command Shell (`cmd.exe`) can be used to execute commands and scripts on Windows systems.

Because command shells are commonly used during legitimate administration as well as attacker activity, command-shell detections require additional investigation and context.

---

## Wazuh Detection

During Sysmon process monitoring, Wazuh generated the following detection:

```text
Rule ID: 92032
Description: Suspicious Windows cmd shell execution
```

The alert contained MITRE ATT&CK mapping including:

```text
T1059.003 - Windows Command Shell
```

---

## Alert Investigation

One observed Rule `92032` alert was investigated to understand the activity that caused the detection.

The event contained:

```text
Parent Process:
C:\Windows\System32\cmd.exe

Child Process:
C:\Program Files\Adobe\Acrobat DC\Acrobat\Browser\WCChromeExtn\WCChromeNativeMessagingHost.exe
```

The child process was associated with Adobe Acrobat.

The process was launched through `cmd.exe`, which caused the Wazuh command-shell detection rule to trigger.

---

## Analyst Assessment

Although Wazuh classified the activity as suspicious command-shell execution, investigation of the process information showed that the child executable was associated with Adobe Acrobat.

This demonstrates an important SOC principle:

> A security alert identifies activity that requires investigation, but an alert alone does not prove that malicious activity occurred.

A SOC analyst should examine additional context such as:

- Process path
- Command line
- Parent process
- Parent command line
- User account
- File hashes
- Software publisher
- Timestamp
- Related endpoint activity

before determining whether an event represents malicious or legitimate behavior.

This alert therefore provided an example of alert triage and investigation rather than a confirmed attack.

---

# Detection Coverage

The current validated MITRE ATT&CK coverage in the homelab includes:

## Discovery

### T1087 — Account Discovery

Validated through controlled execution of:

```powershell
net user guest
```

Detected by:

```text
Wazuh Rule 92039
```

---

## Execution

### T1059.003 — Windows Command Shell

Observed through Sysmon process creation telemetry involving:

```text
cmd.exe
```

Detected by:

```text
Wazuh Rule 92032
```

---

# Detection Validation Workflow

MITRE ATT&CK mapping is incorporated into the SOC detection workflow as follows:

```text
Endpoint Activity
       │
       ▼
Windows / Sysmon Telemetry
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Detection Rule
       │
       ▼
Security Alert
       │
       ▼
Alert Investigation
       │
       ▼
MITRE ATT&CK Mapping
```

This workflow allows endpoint activity to be translated into standardized attacker behavior that can be understood and investigated by a SOC analyst.

---

# Detection Testing Observations

During detection testing, several Windows discovery commands were executed.

Commands such as:

```powershell
ipconfig /all
```

and:

```powershell
tasklist
```

were tested but did not generate corresponding Wazuh alerts using the detection rules configured at the time of testing.

This demonstrated an important distinction between:

```text
Endpoint Activity
        ↓
Telemetry Generation
        ↓
SIEM Detection Rule
        ↓
Security Alert
```

Not every command executed on an endpoint necessarily results in a security alert.

An alert is generated when collected telemetry matches a configured detection rule.

This observation helped identify areas where future detection coverage could potentially be expanded.

---

# Key Takeaways

This phase of the SOC homelab demonstrated:

- MITRE ATT&CK mapping
- Account Discovery detection
- Windows command-shell monitoring
- Sysmon process telemetry analysis
- Wazuh rule investigation
- Parent-child process analysis
- Command-line analysis
- Alert triage
- Detection validation
- Distinguishing suspicious alerts from confirmed malicious activity
- Identification of detection coverage gaps

---

# Future Enhancements

Future detection engineering work can expand MITRE ATT&CK coverage to additional techniques such as:

- PowerShell execution
- Process discovery
- Network discovery
- Credential-related activity
- Persistence techniques
- Defense evasion
- Additional command and scripting interpreter techniques

New MITRE ATT&CK techniques will be added to the validated detection mapping only after the corresponding activity has been tested and successfully observed within the SOC homelab.

---

# Conclusion

MITRE ATT&CK mapping provides a standardized framework for understanding the security behaviors detected by the SOC homelab.

The Account Discovery simulation demonstrated that Wazuh could identify controlled discovery activity and map the resulting detection to **T1087 — Account Discovery**.

Investigation of the Windows Command Shell alert also demonstrated how a SOC analyst must analyze process context before deciding whether detected activity represents malicious behavior.

Together, these exercises demonstrate the transition from basic log collection to detection validation, alert investigation, and MITRE ATT&CK-based security analysis.
