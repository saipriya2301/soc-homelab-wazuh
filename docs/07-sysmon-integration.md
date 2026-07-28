# Sysmon Integration with Wazuh

## Objective

The objective of this phase was to integrate **Microsoft Sysmon** with **Wazuh** to enhance Windows endpoint visibility and enable detailed process monitoring for threat hunting and detection engineering.

---

## Why Sysmon?

Windows Event Logs provide basic operating system events, but they do not capture detailed endpoint activity.

Microsoft Sysmon extends Windows logging by recording security-relevant events such as:

- Process creation
- Network connections
- Driver loading
- Image loading
- Registry modifications
- File creation events

Integrating Sysmon with Wazuh provides richer telemetry for threat hunting and custom detection development.

---

## Lab Environment

| Component | Version |
|----------|---------|
| Ubuntu | 24.04 |
| Wazuh | 4.13.1 |
| Windows | Windows 11 |
| Sysmon | Latest |

---

## Sysmon Installation

Microsoft Sysmon was installed on the Windows 11 endpoint using an administrator Command Prompt along with a Sysmon configuration file.

After installation, Sysmon began recording detailed Windows endpoint activity under the **Microsoft-Windows-Sysmon/Operational** event channel.

---

## Wazuh Agent Configuration

To collect Sysmon logs, the following configuration was added to the Windows Wazuh Agent configuration file (`ossec.conf`).

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

After updating the configuration, the **Wazuh Agent service** was restarted successfully.

---

## Validation

To verify that Sysmon was generating events correctly:

1. Opened **Command Prompt** as Administrator.
2. Executed:

```cmd
notepad.exe
```

3. Verified that **Event ID 1 (Process Create)** appeared in:

```
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```

This confirmed that Sysmon was successfully monitoring process creation events.

---

## Initial Observation

Although the Sysmon Process Creation event appeared in Windows Event Viewer, it did not immediately generate an alert in Wazuh.

Further investigation showed that:

- The Wazuh Agent was successfully collecting Sysmon events.
- Wazuh only generated alerts for activities that matched existing built-in detection rules.

For example, executing:

```cmd
net user guest
```

generated the following built-in detection:

- **Rule ID:** 92039
- **Description:** A net.exe account discovery command was initiated
- **MITRE ATT&CK:** T1087 – Account Discovery

However, launching **Notepad** did not trigger an alert because no built-in rule existed for that process.

---

## Custom Detection

To demonstrate custom detection engineering, a new Wazuh rule was created to detect **Notepad process creation** using Sysmon Event ID 1.

The rule was added to:

```
/var/ossec/etc/rules/local_rules.xml
```

The custom rule matches Sysmon Process Creation events where the process image is **notepad.exe**.

After saving the rule, the **Wazuh Manager** was restarted successfully.

---

## Detection Workflow

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
Wazuh Alert
```

---

## Validation Results

After restarting the Wazuh Manager:

- Launched **Notepad**
- Sysmon generated **Event ID 1**
- Wazuh matched the custom detection rule
- A custom alert was successfully generated in the Wazuh Dashboard

This confirmed that the complete event pipeline—from Windows endpoint to Wazuh detection—was functioning correctly.

---

## Screenshots

The following screenshots demonstrate the successful integration:

1. Custom Wazuh detection rule
2. Sysmon Process Create (Event ID 1) in Windows Event Viewer
3. Custom Notepad detection alert in Wazuh Dashboard

---

## Skills Demonstrated

- Sysmon Deployment
- Windows Event Collection
- Endpoint Telemetry
- Wazuh Agent Configuration
- Sysmon Integration
- Detection Engineering
- Custom Wazuh Rule Development
- Threat Hunting
- Windows Process Monitoring
- Log Analysis
- Troubleshooting

---

## Key Takeaways

- Successfully integrated Microsoft Sysmon with Wazuh.
- Configured Wazuh to collect Sysmon Operational logs.
- Validated Windows Process Creation (Event ID 1) events.
- Investigated why built-in rules did not detect Notepad execution.
- Developed and tested a custom Wazuh detection rule.
- Verified end-to-end event collection and alert generation from the Windows endpoint to the Wazuh Dashboard.
