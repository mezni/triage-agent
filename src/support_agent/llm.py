from anthropic import Anthropic

from support_agent.config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
)

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def call_llm(
    *,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None,
):
    kwargs = {
        "model": ANTHROPIC_MODEL,
        "max_tokens": 1000,
        "system": system_prompt,
        "messages": messages,
    }

    if tools:
        kwargs["tools"] = tools

    return client.messages.create(**kwargs)