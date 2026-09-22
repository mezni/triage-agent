import json

from pydantic import ValidationError

from support_agent.llm import call_llm
from support_agent.models import ExtractedTicket
from support_agent.prompts import EXTRACTION_SYSTEM_PROMPT


class ExtractionError(Exception):
    pass


def extract_ticket_information(
    message: str,
) -> ExtractedTicket:

    response = call_llm(
        system_prompt=EXTRACTION_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    text = next(
        block.text
        for block in response.content
        if block.type == "text"
    )

    try:
        data = json.loads(text)

    except json.JSONDecodeError as exc:
        raise ExtractionError(
            "LLM returned invalid JSON."
        ) from exc

    try:
        return ExtractedTicket.model_validate(data)

    except ValidationError as exc:
        raise ExtractionError(
            "LLM returned invalid ticket data."
        ) from exc