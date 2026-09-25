import json
import os
import subprocess
from typing import Any, Callable, Dict, List

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "Read",
            "description": "Read and return the contents of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to read",
                    }
                },
                "required": ["file_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "Write",
            "description": "Write content to a file",
            "parameters": {
                "type": "object",
                "required": ["file_path", "content"],
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path of the file to write to",
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write to the file",
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "Bash",
            "description": "Execute a shell command",
            "parameters": {
                "type": "object",
                "required": ["command"],
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to execute",
                    },
                },
            },
        },
    },
]


def execute_read(file_path: str) -> str:
    """Read and return the contents of a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


def execute_write(file_path: str, content: str = "") -> str:
    """Write content to a file, creating parent directories if necessary."""
    try:
        parent_dir = os.path.dirname(file_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return "File written successfully"
    except Exception as e:
        return f"Error writing file: {e}"


def execute_bash(command: str) -> str:
    """Execute a shell command and capture combined stdout and stderr."""
    try:
        proc = subprocess.run(command, shell=True, capture_output=True, text=True)
        return proc.stdout + proc.stderr
    except Exception as e:
        return f"Error executing command: {e}"


TOOL_HANDLERS: Dict[str, Callable[..., str]] = {
    "Read": lambda args: execute_read(args.get("file_path", "")),
    "Write": lambda args: execute_write(args.get("file_path", ""), args.get("content", "")),
    "Bash": lambda args: execute_bash(args.get("command", "")),
}


def execute_tool(name: str, arguments_str: str) -> str:
    """Dispatch and execute a tool by name with JSON string arguments."""
    try:
        arguments = json.loads(arguments_str) if arguments_str else {}
    except Exception as e:
        return f"Error parsing tool arguments: {e}"

    handler = TOOL_HANDLERS.get(name)
    if not handler:
        return f"Unknown tool: {name}"

    return handler(arguments)
