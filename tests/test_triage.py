import pytest

from support_agent.models import (
    SupportTicket,
    TicketCategory,
    TicketPriority,
    TriageResult,
)
from support_agent.tools import TOOL_REGISTRY, get_customer_status
from support_agent.triage import _extract_json


def test_customer_status_tool_exists():
    assert "get_customer_status" in TOOL_REGISTRY


def test_customer_status_known_vs_unknown():
    assert get_customer_status("C001") == "active"
    assert get_customer_status("C003") == "suspended"
    assert get_customer_status("C999") == "unknown"


def test_valid_triage_result():
    result = TriageResult(
        category=TicketCategory.BILLING,
        priority=TicketPriority.HIGH,
        reasoning="The customer reports a duplicate charge.",
        response="We can help investigate the duplicate charge.",
    )

    assert result.category == TicketCategory.BILLING
    assert result.priority == TicketPriority.HIGH


def test_support_ticket():
    ticket = SupportTicket(
        ticket_id="T001",
        customer_id="C001",
        message="I cannot log into my account.",
    )

    assert ticket.ticket_id == "T001"
    assert ticket.customer_id == "C001"


def test_triage_result():
    result = TriageResult(
        category=TicketCategory.ACCOUNT,
        priority=TicketPriority.HIGH,
        reasoning="The customer cannot access their account.",
        response="Let's help you recover access to your account.",
    )

    assert result.category == TicketCategory.ACCOUNT
    assert result.priority == TicketPriority.HIGH


def test_extract_json_from_plain_response():
    data = _extract_json('{"category": "billing", "priority": "high"}')

    assert data == {"category": "billing", "priority": "high"}


def test_extract_json_from_fenced_response():
    raw = '```json\n{"category": "billing", "priority": "high"}\n```'
    data = _extract_json(raw)

    assert data == {"category": "billing", "priority": "high"}


def test_extract_json_rejects_non_object():
    with pytest.raises(TypeError):
        _extract_json("[1, 2, 3]")


def test_unknown_tool_returns_error_message():
    from support_agent.agent import SupportAgent

    agent = SupportAgent()
    result = agent._execute_tool("no_such_tool", {})

    assert result == "Unknown tool: no_such_tool"