from support_agent.knowledge_base import (
    search_knowledge_base,
)


def get_customer_status(customer_id: str) -> str:
    customers = {
        "C001": "active",
        "C002": "active",
        "C003": "suspended",
    }

    return customers.get(customer_id, "unknown")


CUSTOMER_STATUS_TOOL = {
    "name": "get_customer_status",
    "description": (
        "Get the current account status of a customer. "
        "Use this when you need to verify whether a customer "
        "account is active, suspended, or unknown."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": "The unique customer identifier.",
            }
        },
        "required": ["customer_id"],
    },
}


SEARCH_KNOWLEDGE_BASE_TOOL = {
    "name": "search_knowledge_base",
    "description": (
        "Search the customer support knowledge base "
        "for information relevant to a customer question. "
        "Use this tool when you need company-specific "
        "information before answering a customer."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "The customer's question or the "
                    "information that needs to be found."
                ),
            },
            "category": {
                "type": "string",
                "description": (
                    "Optional knowledge category such as "
                    "account, billing, technical, product, "
                    "or shipping."
                ),
            },
        },
        "required": ["query"],
    },
}


TOOL_SCHEMAS = [
    CUSTOMER_STATUS_TOOL,
    SEARCH_KNOWLEDGE_BASE_TOOL,
]


def format_knowledge_results(
    results,
) -> str:
    if not results:
        return "No relevant knowledge base articles were found."

    formatted = []

    for article in results:
        formatted.append(
            f"ID: {article.id}\n"
            f"Title: {article.title}\n"
            f"Category: {article.category}\n"
            f"Content: {article.content}"
        )

    return "\n\n---\n\n".join(formatted)


def search_knowledge_base_tool(
    query: str,
    category: str | None = None,
) -> str:
    results = search_knowledge_base(
        query=query,
        category=category,
    )

    return format_knowledge_results(results)


TOOL_REGISTRY = {
    "get_customer_status": get_customer_status,
    "search_knowledge_base": search_knowledge_base_tool,
}