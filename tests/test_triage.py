"""Tests for the triage component."""

from support_agent.models import Category, Priority
from support_agent.triage import load_tickets, sample_result


def test_sample_result_fields():
    result = sample_result()
    assert result.customer_id == "cust_123"
    assert result.category == Category.BILLING
    assert result.priority == Priority.HIGH
    assert result.escalate is False


def test_load_tickets_from_fixture():
    tickets = load_tickets("data/tickets.json")
    assert len(tickets) == 3
    assert tickets[0].ticket_id == "T-1001"
    assert tickets[0].text


def test_ticket_requires_text():
    from pydantic import ValidationError

    from support_agent.models import Ticket

    try:
        Ticket(ticket_id="x", text="")
    except ValidationError:
        pass
    else:
        raise AssertionError("expected ValidationError for empty ticket text")