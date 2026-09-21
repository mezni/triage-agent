"""High-level triage orchestration."""

from pathlib import Path

import json

from anthropic import Anthropic

from support_agent.config import Settings
from support_agent.llm import classify_ticket
from support_agent.models import Category, Priority, Ticket, TriageResult


def triage_ticket(client: Anthropic, settings: Settings, ticket: Ticket) -> TriageResult:
    """Run the triage pipeline for a single ticket."""
    return classify_ticket(client, settings, ticket.text)


def load_tickets(path: Path | str = "data/tickets.json") -> list[Ticket]:
    """Load JSON tickets from disk."""
    data = json.loads(Path(path).read_text())
    return [Ticket(**item) for item in data]


def sample_result() -> TriageResult:
    """A canned result for offline demos/tests (no LLM call)."""
    return TriageResult(
        customer_id="cust_123",
        category=Category.BILLING,
        priority=Priority.HIGH,
        summary="Customer was charged twice for their subscription.",
        escalate=False,
    )