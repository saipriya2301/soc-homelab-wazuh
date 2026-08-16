# Attack Simulations & Detection Validation

## Objective

The objective of this phase was to simulate common Windows discovery activity on the monitored endpoint and validate that Wazuh could detect the resulting activity through Windows event logs and Sysmon telemetry.

The simulations were performed on the Windows endpoint:

* **Agent:** `SP-WIN-01`
* **IP:** `192.168.1.8`
* **Operating System:** Windows 11
* **SIEM:** Wazuh
* **Telemetry Source:** Windows Event Logs and Sysmon

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

These commands were used to enumerate the current user and Windows user accounts.

---

## 2. Detection Results

The activity generated multiple Wazuh alerts on the `SP-WIN-01` agent.

| Rule ID | Detection                                             | Level |
| ------- | ----------------------------------------------------- | ----- |
| 92033   | Discovery activity spawned via PowerShell execution   | 3     |
| 92039   | A net.exe account discovery command was initiated     | 3     |
| 92052   | Windows command prompt started by an abnormal process | 4     |
| 92032   | Suspicious Windows cmd shell execution                | 3     |

### Primary Detection

The most relevant detection for the `net user guest` simulation was:

**Rule ID:** `92039`

**Description:**

> A net.exe account discovery command was initiated

**Detection Level:** 3

This rule identified the use of the Windows `net.exe` utility for account discovery.

---

## 3. Detection Workflow

The activity followed the complete monitoring and detection pipeline:

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

* Agent name
* Timestamp
* Rule ID
* Rule description
* Process execution
* Parent process
* Command line
* Event source
* Detection level

The alerts confirmed that the commands executed on the Windows endpoint were successfully collected and analyzed by Wazuh.

---

## 5. MITRE ATT&CK Mapping

The primary behavior observed during this simulation corresponds to:

| Attribute    | Mapping                                      |
| ------------ | -------------------------------------------- |
| Tactic       | Discovery                                    |
| Technique    | Account Discovery                            |
| Technique ID | T1087                                        |
| Activity     | Windows account enumeration using `net user` |

The Wazuh detection for `net user guest` was mapped to **MITRE ATT&CK T1087 (Account Discovery)**.

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

This validates the end-to-end detection pipeline from endpoint activity to SIEM alert.

---

## 7. Evidence

Screenshots captured during the validation include:

* Wazuh Threat Hunting results showing rules `92033`, `92039`, `92052`, and `92032`.
* Wazuh alert details for the account discovery activity.
* Windows endpoint activity used to generate the detection.

Screenshots are stored in the project's `screenshots/` directory.

---

## 8. Conclusion

The account discovery simulation successfully demonstrated the ability of the SOC homelab to monitor Windows endpoint activity and detect account enumeration behavior.

The exercise validated:

* Windows endpoint monitoring
* Sysmon integration
* Wazuh log collection
* Wazuh detection rules
* Threat hunting
* Alert investigation
* MITRE ATT&CK mapping
* End-to-end detection validation

This simulation forms part of the project's attack simulation and detection engineering workflow.

