#!/usr/bin/env python3

import json
import os
import sys

MARKER_FILE = "/tmp/wazuh-active-response-test.txt"

def read_message():
    line = sys.stdin.readline()
    if not line:
        return {}
    return json.loads(line)

def main():
    message = read_message()
    command = message.get("command", "")

    if command == "add":
        alert = message.get("parameters", {}).get("alert", {})
        rule_id = str(alert.get("rule", {}).get("id", "unknown"))

        check_keys = {
            "version": 1,
            "origin": {
                "name": sys.argv[0],
                "module": "active-response"
            },
            "command": "check_keys",
            "parameters": {
                "keys": [rule_id]
            }
        }

        print(json.dumps(check_keys))
        sys.stdout.flush()

        response = read_message()

        if response.get("command") != "continue":
            return

        with open(MARKER_FILE, "w", encoding="utf-8") as f:
            f.write(
                f"Wazuh Active Response test triggered successfully "
                f"by rule {rule_id}.\n"
            )

    elif command == "delete":
        if os.path.exists(MARKER_FILE):
            os.remove(MARKER_FILE)

if __name__ == "__main__":
    main()
