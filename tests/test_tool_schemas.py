from support_agent.tools import (
    CREATE_TICKET_TOOL,
)


def test_create_ticket_schema_has_required_fields():

    schema = CREATE_TICKET_TOOL["input_schema"]

    assert schema["type"] == "object"

    required = schema["required"]

    assert "customer_id" in required
    assert "category" in required
    assert "priority" in required
    assert "summary" in required


def test_create_ticket_schema_has_valid_category_enum():

    properties = CREATE_TICKET_TOOL[
        "input_schema"
    ]["properties"]

    categories = properties[
        "category"
    ]["enum"]

    assert "billing" in categories
    assert "technical" in categories
    assert "account" in categories


def test_create_ticket_schema_has_valid_priority_enum():

    properties = CREATE_TICKET_TOOL[
        "input_schema"
    ]["properties"]

    priorities = properties[
        "priority"
    ]["enum"]

    assert "low" in priorities
    assert "medium" in priorities
    assert "high" in priorities
    assert "urgent" in priorities