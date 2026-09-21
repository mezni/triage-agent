import json

from support_agent.llm import ask_llm
from support_agent.models import SupportTicket, TriageResult
from support_agent.prompts import TRIAGE_SYSTEM_PROMPT


def triage_ticket(ticket: SupportTicket) -> TriageResult:
    raw_response = ask_llm(
        system_prompt=TRIAGE_SYSTEM_PROMPT,
        user_message=ticket.message,
    )

    data = json.loads(raw_response)

    return TriageResult.model_validate(data)