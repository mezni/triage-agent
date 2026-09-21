"""Anthropic LLM client wrapper."""

from anthropic import Anthropic

from support_agent.config import Settings
from support_agent.models import TriageResult
from support_agent.prompts import SYSTEM_PROMPT, triage_user_prompt


def classify_ticket(client: Anthropic, settings: Settings, ticket_text: str) -> TriageResult:
    """Classify a ticket and return a validated structured result."""
    message = client.messages.create(
        model=settings.anthropic_model,
        max_tokens=settings.anthropic_max_tokens,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": triage_user_prompt(ticket_text)}],
    )
    return _parse_triage_result(message.content)


def _parse_triage_result(content: list[object]) -> TriageResult:
    text = "".join(block.text for block in content if hasattr(block, "text"))
    return TriageResult.model_validate_json(text)