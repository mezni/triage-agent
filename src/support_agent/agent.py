from support_agent.llm import call_llm
from support_agent.prompts import TRIAGE_SYSTEM_PROMPT
from support_agent.tools import TOOL_REGISTRY, TOOL_SCHEMAS


class SupportAgent:

    def __init__(self, max_turns: int = 5):
        self.max_turns = max_turns

    def run(self, user_message: str):
        messages = [
            {
                "role": "user",
                "content": user_message,
            }
        ]

        for turn in range(self.max_turns):
            response = call_llm(
                system_prompt=TRIAGE_SYSTEM_PROMPT,
                messages=messages,
                tools=TOOL_SCHEMAS,
            )

            print(f"\n--- Turn {turn + 1} ---")
            print("Stop reason:", response.stop_reason)

            if response.stop_reason == "end_turn":
                return response

            if response.stop_reason == "tool_use":
                messages.append(
                    {
                        "role": "assistant",
                        "content": response.content,
                    }
                )

                tool_results = []

                for block in response.content:
                    if block.type != "tool_use":
                        continue

                    result = self._execute_tool(
                        block.name,
                        block.input,
                    )

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )

                messages.append(
                    {
                        "role": "user",
                        "content": tool_results,
                    }
                )

                continue

            raise RuntimeError(
                f"Unexpected stop reason: {response.stop_reason}"
            )

        raise RuntimeError(
            "Agent exceeded maximum number of turns."
        )

    def _execute_tool(self, name: str, arguments: dict) -> str:
        tool = TOOL_REGISTRY.get(name)

        if tool is None:
            return f"Unknown tool: {name}"

        try:
            result = tool(**arguments)
            return str(result)
        except Exception as exc:  # noqa: BLE001
            return f"Tool execution failed: {exc}"