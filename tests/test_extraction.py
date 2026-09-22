import pytest
from pydantic import ValidationError

from support_agent.models import (
    ExtractedTicket,
    Sentiment,
)


def test_valid_extracted_ticket():

    result = ExtractedTicket(
        customer_id="C002",
        product="subscription",
        sentiment=Sentiment.NEGATIVE,
        priority="high",
        category="billing",
    )

    assert result.customer_id == "C002"
    assert result.category.value == "billing"
    assert result.priority.value == "high"


def test_invalid_sentiment():

    with pytest.raises(ValidationError):

        ExtractedTicket(
            customer_id="C002",
            product="subscription",
            sentiment="angry",
            priority="high",
            category="billing",
        )


def test_invalid_priority():

    with pytest.raises(ValidationError):

        ExtractedTicket(
            customer_id="C002",
            product="subscription",
            sentiment="negative",
            priority="critical",
            category="billing",
        )


def test_invalid_category():

    with pytest.raises(ValidationError):

        ExtractedTicket(
            customer_id="C002",
            product="subscription",
            sentiment="negative",
            priority="high",
            category="finance",
        )