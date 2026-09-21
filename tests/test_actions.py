import pytest

from support_agent.action_store import (
    ESCALATIONS,
    TICKETS,
)
from support_agent.tools import (
    create_ticket,
    escalate_to_human,
)


def test_create_ticket():
    TICKETS.clear()

    result = create_ticket(
        customer_id="C001",
        category="billing",
        priority="high",
        summary="Customer was charged twice.",
    )

    assert "created successfully" in result
    assert len(TICKETS) == 1
    assert TICKETS[0].customer_id == "C001"
    assert TICKETS[0].category.value == "billing"


def test_escalate_to_human():
    ESCALATIONS.clear()

    result = escalate_to_human(
        ticket_id="T001",
        reason="Requires human investigation.",
    )

    assert "escalated" in result
    assert len(ESCALATIONS) == 1
    assert ESCALATIONS[0].ticket_id == "T001"


def test_invalid_category_is_rejected():
    with pytest.raises(ValueError):
        create_ticket(
            customer_id="C001",
            category="finance",
            priority="high",
            summary="Test",
        )