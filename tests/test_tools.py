from support_agent.knowledge_base import (
    search_knowledge_base,
)


def test_search_password_reset():
    results = search_knowledge_base(
        "password reset email"
    )

    assert len(results) > 0
    assert results[0].id == "KB001"


def test_search_dark_mode():
    results = search_knowledge_base(
        "dark mode"
    )

    assert len(results) > 0
    assert results[0].id == "KB004"


def test_search_with_category():
    results = search_knowledge_base(
        "charge",
        category="billing",
    )

    assert len(results) > 0

    for result in results:
        assert result.category == "billing"