# Windows Agent Installation

## Objective

Install and configure the Wazuh agent on a Windows 11 endpoint to enable centralized security monitoring and log collection by the Wazuh Manager.

---

## Endpoint Information

| Component | Details |
|----------|---------|
| Operating System | Windows 11 |
| Agent Name | SP-WIN-01 |
| Wazuh Manager | homesoc1 |
| Communication | Secure agent-to-manager connection |

---

## Why Install the Wazuh Agent?

The Wazuh agent collects security telemetry from the endpoint and forwards it to the Wazuh Manager for analysis.

The agent enables monitoring of:

- Windows Security Events
- System Events
- Application Events
- File Integrity Monitoring (FIM)
- Security Policy Changes
- Process Activity
- Registry Changes

---

## Installation Process

The Windows Wazuh agent was installed on the Windows 11 endpoint using the official installer.

During installation:

- The manager IP address was configured.
- The agent was assigned the name **SP-WIN-01**.
- The Wazuh service was started successfully after installation.

---

## Verification

The installation was verified by:

- Confirming the Wazuh service was running.
- Verifying the agent appeared in the Wazuh Dashboard.
- Confirming the agent status was **Active**.
- Ensuring communication with the Wazuh Manager was successful.

---

## Outcome

The Windows endpoint was successfully onboarded to the Home SOC environment.

The endpoint is now capable of forwarding security events to the Wazuh Manager for continuous monitoring and threat detection.

---

## Skills Demonstrated

- Windows Endpoint Administration
- Endpoint Onboarding
- Wazuh Agent Deployment
- SIEM Configuration
- Security Monitoring

---

## References

- Wazuh Agent Documentation: https://documentation.wazuh.com/current/installation-guide/wazuh-agent/
