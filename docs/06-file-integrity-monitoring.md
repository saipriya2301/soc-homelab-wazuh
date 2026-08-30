# File Integrity Monitoring (FIM)

## Objective

The objective of this phase was to configure **File Integrity Monitoring (FIM)** using Wazuh to detect file system changes on the Windows endpoint. This enables real-time monitoring of file creation, modification, and deletion events for critical directories.

---

## What is File Integrity Monitoring?

File Integrity Monitoring (FIM) continuously monitors files and directories for unauthorized or unexpected changes.

Wazuh detects activities such as:

- File creation
- File modification
- File deletion

FIM is commonly used to monitor sensitive files and detect potential tampering or malicious activity.

---

## Lab Environment

| Component | Version |
|----------|---------|
| Ubuntu | 24.04 |
| Wazuh | 4.13.1 |
| Windows | Windows 11 |

---

## Wazuh Agent Configuration

A directory on the Windows endpoint was configured for real-time monitoring by updating the Wazuh Agent configuration (`ossec.conf`).

The following configuration was added:

```xml
<directories realtime="yes">D:\priya\Projects\FIM-Test</directories>
```

This configuration instructs the Wazuh Agent to monitor the specified directory and immediately report file system changes.

After updating the configuration, the **Wazuh Agent service** was restarted successfully.

---

## Test Directory

The following directory was created for testing:

```
D:\priya\Projects\FIM-Test
```

This directory was used to safely simulate file activity without affecting system files.

---

## Validation

### Test 1 – File Creation

A new file named:

```
test1.txt
```

was created inside the monitored directory.

Wazuh successfully generated an alert indicating that a new file had been added.

---

### Test 2 – File Modification

The contents of **test1.txt** were modified and saved.

Wazuh detected the integrity checksum change and generated a file modification alert.

---

### Test 3 – File Deletion

The file **test1.txt** was deleted from the monitored directory.

Wazuh successfully detected the deletion event and generated the corresponding alert.

---

## Detection Workflow

```
File Created / Modified / Deleted
               │
               ▼
     Wazuh Agent (Windows)
               │
               ▼
        Wazuh Manager
               │
               ▼
      File Integrity Module
               │
               ▼
         Wazuh Dashboard
```

---

## Validation Results

The following events were successfully detected:

- File creation
- File modification
- File deletion

Alerts were visible within the Wazuh Dashboard under Threat Hunting, confirming successful end-to-end event collection.

---

## Screenshots

The following screenshots demonstrate the successful File Integrity Monitoring implementation:

1. Wazuh Agent FIM configuration
2. Test directory and file
3. File creation alert
4. File modification alert
5. File deletion alert

---

## Skills Demonstrated

- File Integrity Monitoring (FIM)
- Wazuh Agent Configuration
- Endpoint Monitoring
- Windows File System Monitoring
- Real-Time Event Collection
- Threat Hunting
- Security Monitoring
- Log Analysis
- Event Validation

---

## Key Takeaways

- Successfully configured File Integrity Monitoring using Wazuh.
- Monitored a Windows directory in real time.
- Validated file creation, modification, and deletion events.
- Verified end-to-end event collection from the Windows endpoint to the Wazuh Dashboard.
- Demonstrated the ability to detect unauthorized file system changes using Wazuh.
