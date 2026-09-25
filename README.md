[![progress-banner](https://backend.codecrafters.io/progress/claude-code/0388b3ae-654e-4af5-bdb4-a35000aa6b33)](https://app.codecrafters.io/users/RudraSharma3?r=2qF)

# Build Your Own Claude Code (Python)

A lightweight, LLM-powered autonomous coding assistant built in Python from scratch, based on the [CodeCrafters "Build Your Own Claude Code" Challenge](https://codecrafters.io/challenges/claude-code).

## 🚀 Overview

This assistant implements an autonomous **agent loop** using OpenAI-compatible APIs (OpenRouter / Anthropic Claude 3.5/4.5 Haiku) capable of:
- Inspecting codebases and reading local files
- Writing and updating source files (with automatic parent directory creation)
- Executing bash/shell commands and capturing stdout/stderr
- Iteratively solving multi-step tasks until completion

---

## 🛠️ Architecture

The codebase is organized into clean, decoupled modules:

```text
├── app/
│   ├── __init__.py       # Package marker
│   ├── agent.py          # ClaudeCodeAgent (Agent loop & conversation manager)
│   ├── tools.py          # Tool schemas (Read, Write, Bash) & execution handlers
│   └── main.py           # CLI entry point
├── your_program.sh       # Local runner script
├── pyproject.toml        # Project configuration and dependencies
└── README.md
```

### Key Components

- **`ClaudeCodeAgent` (`app/agent.py`)**: Manages the conversation state (`messages`), queries the LLM with tool schemas, catches tool calls, dispatches tool execution, feeds results back as `tool` messages, and prints the final output once the assistant finishes.
- **Tools (`app/tools.py`)**:
  - `Read`: Reads and returns the contents of any file at `file_path`.
  - `Write`: Writes `content` to `file_path` with directory creation.
  - `Bash`: Runs shell commands via `subprocess` and captures output.

---

## ⚡ Getting Started

### Prerequisites

- Python `>=3.14`
- [`uv`](https://github.com/astral-sh/uv) package manager
- OpenRouter API Key

### Environment Variables

Set your OpenRouter API key:

```bash
export OPENROUTER_API_KEY="your-openrouter-api-key"
```

### Running Locally

Execute prompts directly using `uv` or the runner script:

```bash
# Using your_program.sh
./your_program.sh -p "Read README.md and summarize it in 2 bullet points."

# Or directly with uv
uv run python -m app.main -p "List all files in the current directory and explain their purpose."
```

---

## 🧪 Testing

Submit and test with the CodeCrafters CLI:

```bash
codecrafters submit
```
