#!/usr/bin/env python
import json
import sys

from slack_cli_hooks.protocol import DefaultProtocol, MessageBoundaryProtocol, Protocol, build_protocol

PROTOCOL: Protocol

# Wrap sys.executable in quotes to prevent execution failures if a white space is present in the absolute python path
EXEC = "C:\\Users\\tanyu\\whatever-you-wish\\run_hook.bat"


hooks_payload = {
    "hooks": {
        "get-manifest": f"{EXEC} get_manifest.py",
        "start": f"{EXEC} app.py",
        "doctor": f"{EXEC} get_doctor.py",
    },
    "config": {
        "protocol-version": [MessageBoundaryProtocol.name, DefaultProtocol.name],
        "sdk-managed-connection-enabled": True,
        "watch": {
            "app": {
                "filter-regex": "\\.py$",
                "paths": ["."],
            },
            "manifest": {
                "paths": ["manifest.json"],
            },
        },
    },
    "runtime": "python",
}

if __name__ == "__main__":
    PROTOCOL = build_protocol(argv=sys.argv)
    PROTOCOL.respond(json.dumps(hooks_payload))
