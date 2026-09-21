import json
import re

from support_agent.llm import call_llm
from support_agent.models import SupportTicket, TriageResult
from support_agent.prompts import TRIAGE_SYSTEM_PROMPT


def _extract_json(raw_response: str) -> dict:
    """Extract a JSON object from an LLM response.

    The model sometimes wraps JSON in markdown code fences or adds
    surrounding prose, both of which break a direct ``json.loads``.
    """
    text = raw_response.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    data = json.loads(text)

    if not isinstance(data, dict):
        raise TypeError("Expected a JSON object, got: {data!r}")

    return data


def triage_ticket(ticket: SupportTicket) -> TriageResult:
    response = call_llm(
        system_prompt=TRIAGE_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": ticket.message,
            }
        ],
    )

    raw_response = response.content[0].text
    data = _extract_json(raw_response)

    return TriageResult.model_validate(data)