# Threat Hunting with Wazuh

## Objective

The objective of this phase was to use the Wazuh Dashboard to investigate Windows endpoint activity and develop a practical understanding of security event analysis.

Rather than treating every alert as malicious, events were reviewed using process, command-line, authentication, and other contextual information to determine what activity occurred on the monitored endpoint.

The monitored endpoint was:

```text
Agent: SP-WIN-01
Operating System: Windows 11
```

---

## Threat Hunting Approach

Threat hunting was performed using endpoint telemetry collected by Wazuh.

The investigation focused on:

- Windows authentication events
- Process creation
- Command-line activity
- Parent-child process relationships
- Sysmon telemetry
- File and registry integrity events
- Wazuh rule information
- Alert severity
- Event timestamps

The Wazuh Threat Hunting interface was used to search, filter, and inspect individual events.

---

## Windows Authentication Activity

Windows authentication events were reviewed to understand logon activity on the endpoint.

Events investigated during the lab included:

```text
Event ID 4624 — Successful Logon
Event ID 4625 — Failed Logon
```

Important fields considered during authentication analysis included:

- Username
- Source IP address
- Logon type
- Authentication process
- Process information
- Timestamp

This demonstrated how Windows authentication telemetry can be investigated through a centralized SIEM.

---

## Process Creation Analysis

Microsoft Sysmon provided detailed process creation telemetry through:

```text
Sysmon Event ID 1 — Process Creation
```

Process events were investigated using fields such as:

```text
Process Image
Command Line
Parent Process
Parent Command Line
User
Process ID
Integrity Level
Timestamp
```

These fields helped determine what executable ran, how it was started, and which process launched it.

---

## Command-Line Investigation

Command-line telemetry was particularly useful during controlled detection testing.

Commands executed during the project included:

```cmd
whoami
net user
net user guest
```

These commands generated endpoint activity that could be analyzed through Wazuh.

A notable detection occurred when executing:

```cmd
net user guest
```

Wazuh generated:

```text
Rule ID: 92039
Description: A net.exe account discovery command was initiated
Level: 3
```

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
```

This confirmed that the account discovery activity performed on the endpoint was successfully captured and detected.

---

## Parent-Child Process Analysis

Parent-child process relationships were reviewed during threat hunting to understand how processes were launched.

This is useful because the same executable can represent different behavior depending on:

- Which process launched it
- The supplied command-line arguments
- The user context
- The executable path
- Related activity occurring around the same time

For example, Rule `92039` showed:

```text
Parent:
net.exe

Child:
net1.exe

Command:
net user guest
```

This provided additional context for understanding the detected account discovery activity.

---

## False-Positive Investigation

An important part of the threat-hunting phase was recognizing that a Wazuh alert does not automatically indicate malicious activity.

One example involved:

```text
Rule ID: 92032
Description: Suspicious Windows cmd shell execution
```

Investigation showed activity involving:

```text
C:\Program Files\Adobe\Acrobat DC\Acrobat\Browser\WCChromeExtn\WCChromeNativeMessagingHost.exe
```

The executable was associated with Adobe Acrobat and was launched through `cmd.exe`.

Although the behavior matched a Wazuh command-shell detection rule, the available process context indicated legitimate Adobe-related activity rather than a confirmed attack.

This demonstrated the importance of investigating the surrounding context before classifying an alert.

---

## Additional Benign Activity

Other alerts observed during the project were associated with legitimate system activity, including:

- Windows Update
- Microsoft Defender
- Adobe software

For example, an executable observed under:

```text
C:\Windows\SoftwareDistribution\Download\Install\
```

was associated with Windows update / Microsoft Defender activity.

Rather than immediately treating the alert as malicious, the executable path, parent process, and event context were reviewed.

---

## MITRE ATT&CK Context

Threat hunting was also connected to the MITRE ATT&CK framework.

The controlled account discovery activity:

```cmd
net user guest
```

was associated with:

```text
Technique: Account Discovery
Technique ID: T1087
Tactic: Discovery
```

This demonstrated how endpoint events can be translated into standardized attacker behavior for further investigation.

---

## Threat Hunting Workflow

The investigation process followed a workflow similar to:

```text
Wazuh Alert
     │
     ▼
Identify Endpoint
     │
     ▼
Review Rule
     │
     ▼
Inspect Process
     │
     ▼
Inspect Command Line
     │
     ▼
Review Parent Process
     │
     ▼
Check User / Timestamp / Path
     │
     ▼
Compare with Expected Activity
     │
     ▼
MITRE ATT&CK Context
     │
     ▼
Analyst Assessment
```

This helped move from simply viewing alerts to understanding why they occurred.

---

## Key Analyst Questions

During event investigation, the following questions were considered:

1. Which endpoint generated the event?
2. Which Wazuh rule triggered?
3. What process was executed?
4. What command-line arguments were supplied?
5. Which parent process launched it?
6. Which user executed the process?
7. Is the executable running from an expected path?
8. Does the activity match legitimate system or application behavior?
9. Is the event associated with a MITRE ATT&CK technique?
10. Is additional investigation required?

---

## Detection Coverage Observation

During testing, not every Windows command produced a security alert.

This highlighted an important distinction:

```text
Endpoint Activity
       ↓
Telemetry Generated
       ↓
Telemetry Collected
       ↓
Detection Rule Match?
       │
       ├── Yes → Alert
       │
       └── No  → No Alert
```

The absence of an alert does not necessarily mean that no endpoint activity occurred.

It may instead mean that the collected telemetry did not match a configured detection rule.

This observation later helped motivate custom detection engineering within the project.

---

## Skills Demonstrated

This phase provided hands-on experience with:

- Threat hunting
- Wazuh event investigation
- Windows Event Log analysis
- Sysmon telemetry analysis
- Process investigation
- Command-line analysis
- Parent-child process analysis
- Authentication event analysis
- Alert triage
- False-positive investigation
- MITRE ATT&CK interpretation
- Detection validation
- SOC analyst investigation workflow

---

## Key Takeaways

Threat hunting requires more than reviewing alert severity or rule descriptions.

The project demonstrated the importance of analyzing:

```text
Alert
  +
Process Context
  +
Command Line
  +
Parent Process
  +
User Context
  +
Event Source
  +
MITRE ATT&CK Context
        ↓
Analyst Assessment
```

The threat-hunting phase provided practical experience investigating endpoint activity, validating detections, and distinguishing potentially suspicious behavior from legitimate Windows and application activity.
