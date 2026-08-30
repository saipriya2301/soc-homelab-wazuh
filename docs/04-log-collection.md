# Log Collection

## Objective

The objective of this phase was to verify that the Windows endpoint was successfully sending security-relevant event data to the Wazuh manager for centralized monitoring and investigation.

The monitored endpoint in this lab was:

```text
Agent: SP-WIN-01
Operating System: Windows 11
```

The Windows endpoint used the Wazuh agent to forward event data to the Ubuntu-based Wazuh manager.

---

## Log Sources Collected

The Wazuh agent collected multiple Windows event channels, including:

- Windows Security logs
- Windows System logs
- Windows Application logs
- Microsoft Sysmon Operational logs

These sources provided visibility into authentication activity, process execution, system events, application events, and other endpoint telemetry.

---

## Windows Event Log Collection

Windows event channels were collected using Wazuh agent configuration entries in `ossec.conf`.

The agent configuration file is located at:

```text
C:\Program Files (x86)\ossec-agent\ossec.conf
```

The Wazuh agent monitors configured Windows event channels and forwards matching events to the Wazuh manager.

---

## Security Event Monitoring

Windows Security events were used during the lab to investigate authentication-related activity.

Examples observed during testing included:

```text
Event ID 4624 — Successful Logon
Event ID 4625 — Failed Logon
```

These events provided useful fields such as:

- User account
- Logon type
- Source IP address
- Authentication process
- Timestamp
- Process information

The events were reviewed in Wazuh to understand how Windows authentication telemetry appears inside the SIEM.

---

## System and Application Logs

Windows System and Application event channels were also collected.

These logs provided visibility into operating system and application activity and helped demonstrate centralized endpoint monitoring through Wazuh.

During investigation, some alerts were associated with legitimate software and Windows activity, reinforcing the need to review event context before treating an alert as malicious.

Examples of legitimate activity investigated during the project included:

- Windows Update activity
- Microsoft Defender activity
- Adobe-related processes

---

## Sysmon Event Collection

Microsoft Sysmon was later integrated to provide more detailed endpoint telemetry.

The following event channel was added to the Wazuh agent configuration:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

This allowed Sysmon events to be forwarded to the Wazuh manager.

A major focus was:

```text
Sysmon Event ID 1 — Process Creation
```

Process creation telemetry included fields such as:

- Process image
- Command line
- Parent process
- Parent command line
- Process ID
- User
- Integrity level
- Timestamp

---

## End-to-End Log Flow

The centralized collection pipeline used in the lab was:

```text
Windows Endpoint
      │
      ▼
Windows Event Logs / Sysmon
      │
      ▼
Wazuh Agent
      │
      ▼
Wazuh Manager
      │
      ▼
Wazuh Indexer
      │
      ▼
Wazuh Dashboard
```

This allowed endpoint activity to be searched and investigated from a centralized interface.

---

## Validation

Log collection was considered successful because:

1. The Windows endpoint appeared as an active Wazuh agent.
2. Windows events were visible in the Wazuh Dashboard.
3. Authentication events could be investigated.
4. Sysmon Process Creation events were successfully received.
5. Wazuh detection rules triggered on matching endpoint activity.
6. Event fields such as process path, command line, parent process, and rule information were available for investigation.

This confirmed that telemetry was flowing successfully from the Windows endpoint to the Wazuh monitoring environment.

---

## Example Detection Flow

One validated example was account discovery activity generated with:

```cmd
net user guest
```

The activity produced endpoint process telemetry that was collected by Wazuh and resulted in a security alert.

```text
Windows Command
      │
      ▼
Endpoint Telemetry
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
Wazuh Alert
```

This demonstrated that the collected logs could support both monitoring and detection.

---

## Skills Demonstrated

This phase demonstrated hands-on experience with:

- Centralized log collection
- Windows Event Logs
- Wazuh agent configuration
- Authentication event analysis
- Security event monitoring
- Sysmon event collection
- Process telemetry analysis
- SIEM event investigation
- End-to-end log pipeline validation

---

## Key Takeaways

The log collection phase established the foundation for the rest of the SOC homelab.

Without reliable telemetry collection, threat hunting, detection engineering, MITRE ATT&CK mapping, and Active Response would not be possible.

The successful flow of Windows and Sysmon events into Wazuh confirmed that the endpoint monitoring pipeline was functioning correctly and provided the telemetry required for later phases of the project.
