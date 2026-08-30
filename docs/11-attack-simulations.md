# Attack Simulations & Detection Validation

## Objective

The objective of this phase was to simulate common Windows discovery activity on the monitored endpoint and validate that Wazuh could detect the resulting activity through Windows event logs and Sysmon telemetry.

The simulations were performed on the Windows endpoint:

- **Agent:** `SP-WIN-01`
- **IP:** `192.168.1.8`
- **Operating System:** Windows 11
- **SIEM:** Wazuh
- **Telemetry Source:** Windows Event Logs and Sysmon

---

## 1. Account Discovery Simulation

### Objective

Simulate account discovery activity using native Windows commands and verify that Wazuh detects the activity.

### Commands Executed

The following commands were executed on the Windows endpoint:

```powershell
whoami
```

```powershell
net user
```

```powershell
net user guest
```

These commands were used to identify the current user and enumerate Windows user accounts.

The commands were executed only as controlled and benign lab simulations.

---

## 2. Detection Results

The activity generated multiple Wazuh alerts on the `SP-WIN-01` agent.

Observed detections included:

| Rule ID | Detection |
|---|---|
| 92033 | Discovery activity spawned via PowerShell execution |
| 92039 | A net.exe account discovery command was initiated |
| 92052 | Windows command prompt started by an abnormal process |
| 92032 | Suspicious Windows cmd shell execution |

### Primary Detection

The most relevant detection for the `net user guest` simulation was:

```text
Rule ID: 92039
Description: A net.exe account discovery command was initiated
```

This rule identified the use of the Windows `net.exe` utility for account discovery activity.

---

## 3. Detection Workflow

The activity followed the monitoring and detection pipeline:

```text
Windows Endpoint
      │
      ▼
PowerShell / Windows Command
      │
      ▼
Windows Event Logging / Sysmon
      │
      ▼
Wazuh Agent
      │
      ▼
Wazuh Manager
      │
      ▼
Detection Rules
      │
      ▼
Wazuh Alert
      │
      ▼
SOC Analyst Investigation
```

---

## 4. Analyst Investigation

The generated alerts were reviewed in the Wazuh Threat Hunting interface.

The investigation focused on:

- Agent name
- Timestamp
- Rule ID
- Rule description
- Process execution
- Parent process
- Command line
- Event source
- Detection context

The alerts confirmed that the commands executed on the Windows endpoint generated telemetry that was collected and analyzed by Wazuh.

The event details were then reviewed to understand the activity associated with each detection.

---

## 5. MITRE ATT&CK Mapping

The primary behavior observed during the account discovery simulation corresponds to:

| Attribute | Mapping |
|---|---|
| Tactic | Discovery |
| Technique | Account Discovery |
| Technique ID | T1087 |
| Activity | Windows account enumeration using `net user` |

The Wazuh detection for:

```powershell
net user guest
```

was mapped to:

```text
T1087 — Account Discovery
```

This connected the observed endpoint behavior with a standardized MITRE ATT&CK technique.

---

## 6. Validation

The detection was considered successful because:

1. A controlled discovery command was executed on the Windows endpoint.
2. Windows/Sysmon telemetry was generated.
3. The Wazuh agent collected the event.
4. The Wazuh manager processed the event.
5. Wazuh detection rules were triggered.
6. The resulting alerts were visible in the Wazuh Threat Hunting interface.
7. The activity could be investigated using the associated event fields.

This validated the end-to-end detection pipeline from endpoint activity to SIEM alert and analyst investigation.

---

## 7. Evidence

### 7.1 Account Discovery Command Execution

The following screenshot shows the `net user guest` command executed from PowerShell on the monitored Windows endpoint.

![Net User Guest Command](../screenshots/attack%20simulations/01-net-user-guest-command.png.png)

The command successfully queried information about the local Guest account.

---

### 7.2 Wazuh Detection

After executing the command, Wazuh generated alerts associated with the discovery activity.

The primary detection was:

```text
Rule ID: 92039
Description: A net.exe account discovery command was initiated
```

Related detections were also observed, including Rules `92033`, `92032`, and `92052`.

![Account Discovery Alerts](../screenshots/attack%20simulations/02-account-discovery-alerts.png.png)

---

### 7.3 Alert Investigation

The Rule `92039` event was inspected to verify the underlying process activity.

Important event fields included:

```text
Agent:
SP-WIN-01

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

![Rule 92039 Event Details](../screenshots/attack%20simulations/03-rule-92039-details.png.png)

The process telemetry confirmed that the account discovery command executed on the endpoint was successfully captured and associated with the Wazuh detection.

---

## 8. Analyst Interpretation

The simulations demonstrated that native Windows commands can generate security-relevant endpoint telemetry.

However, the presence of a detection does not automatically mean malicious activity occurred.

In this lab, the commands were intentionally executed by the analyst as controlled tests.

The investigation therefore focused on understanding:

```text
What executed?
      ↓
How was it executed?
      ↓
Which process launched it?
      ↓
Which Wazuh rule detected it?
      ↓
What MITRE ATT&CK behavior does it represent?
      ↓
Is the activity expected or suspicious?
```

This reflects the difference between simply generating alerts and performing SOC alert investigation.

---

## 9. Safety Considerations

All simulations in this phase were designed to be benign and non-destructive.

The tests did not intentionally:

- Modify Windows firewall rules
- Disable user accounts
- Change network routes
- Modify registry settings
- Alter endpoint security configuration
- Delete system files
- Disrupt normal network connectivity

The commands were used only to generate observable endpoint telemetry for detection validation.

---

## 10. Conclusion

The account discovery simulation successfully demonstrated the ability of the SOC homelab to monitor Windows endpoint activity and detect account enumeration behavior.

The exercise validated:

- Windows endpoint monitoring
- Sysmon integration
- Wazuh log collection
- Wazuh detection rules
- Threat hunting
- Process and command-line investigation
- Parent-child process analysis
- MITRE ATT&CK mapping
- Alert investigation
- End-to-end detection validation

The primary controlled simulation:

```powershell
net user guest
```

successfully produced an Account Discovery detection associated with:

```text
Rule 92039
MITRE ATT&CK T1087 — Account Discovery
```

This simulation forms part of the project's broader detection engineering and SOC investigation workflow.
