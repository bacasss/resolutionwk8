import os
import sys
from slack_cli_hooks.hooks.get_manifest import get_manifest, find_file_path
from slack_cli_hooks.protocol import build_protocol

if __name__ == "__main__":
    PROTOCOL = build_protocol(argv=sys.argv)
    PROTOCOL.respond(get_manifest(os.getcwd()))