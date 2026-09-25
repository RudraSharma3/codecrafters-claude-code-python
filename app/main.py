import argparse
import os
import sys

from openai import OpenAI
from app.agent import ClaudeCodeAgent

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main() -> None:
    parser = argparse.ArgumentParser(description="Claude Code AI Coding Assistant")
    parser.add_argument("-p", required=True, help="Prompt to execute")
    args = parser.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY environment variable is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    agent = ClaudeCodeAgent(client=client)
    agent.run(prompt=args.p)


if __name__ == "__main__":
    main()
