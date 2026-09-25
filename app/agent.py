import sys
from typing import Any, Dict, List
from openai import OpenAI
from app.tools import TOOLS, execute_tool


class ClaudeCodeAgent:
    """Agent loop managing conversation history, LLM calls, and tool execution."""

    def __init__(self, client: OpenAI, model: str = "anthropic/claude-haiku-4.5"):
        self.client = client
        self.model = model

    def run(self, prompt: str) -> None:
        """Run the agent loop for the given prompt until task completion."""
        messages: List[Dict[str, Any]] = [{"role": "user", "content": prompt}]

        while True:
            chat = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=TOOLS,
            )

            if not chat.choices:
                raise RuntimeError("No choices in LLM response")

            message = chat.choices[0].message
            messages.append(message)

            if not message.tool_calls:
                if message.content:
                    print(message.content)
                break

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = tool_call.function.arguments

                result = execute_tool(tool_name, tool_args)

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
