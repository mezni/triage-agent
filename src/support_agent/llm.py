from anthropic import Anthropic

from support_agent.config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
)

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def ask_llm(system_prompt: str, user_message: str) -> str:
    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
    )

    return response.content[0].text