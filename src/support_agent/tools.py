import uuid

from support_agent.action_store import (
    ESCALATIONS,
    TICKETS,
)
from support_agent.knowledge_base import (
    search_knowledge_base,
)
from support_agent.models import (
    EscalationRecord,
    SupportTicketRecord,
    TicketCategory,
    TicketPriority,
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


def create_ticket(
    customer_id: str,
    category: str,
    priority: str,
    summary: str,
) -> str:

    ticket = SupportTicketRecord(
        ticket_id=f"T-{uuid.uuid4().hex[:8].upper()}",
        customer_id=customer_id,
        category=TicketCategory(category),
        priority=TicketPriority(priority),
        summary=summary,
    )

    TICKETS.append(ticket)

    return (
        f"Support ticket created successfully. "
        f"Ticket ID: {ticket.ticket_id}"
    )


CREATE_TICKET_TOOL = {
    "name": "create_ticket",
    "description": (
        "Create a support ticket when a customer issue "
        "requires follow-up or cannot be resolved immediately."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": (
                    "The unique identifier of the customer."
                ),
            },
            "category": {
                "type": "string",
                "enum": [
                    "account",
                    "billing",
                    "technical",
                    "product",
                    "shipping",
                    "other",
                ],
                "description": (
                    "The category of the customer's issue."
                ),
            },
            "priority": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                    "urgent",
                ],
                "description": (
                    "The urgency of the support issue."
                ),
            },
            "summary": {
                "type": "string",
                "description": (
                    "A concise description of the customer's issue."
                ),
            },
        },
        "required": [
            "customer_id",
            "category",
            "priority",
            "summary",
        ],
    },
}


def escalate_to_human(
    ticket_id: str,
    reason: str,
) -> str:

    escalation = EscalationRecord(
        ticket_id=ticket_id,
        reason=reason,
    )

    ESCALATIONS.append(escalation)

    return (
        f"Ticket {ticket_id} has been escalated "
        f"to a human support representative."
    )


ESCALATE_TO_HUMAN_TOOL = {
    "name": "escalate_to_human",
    "description": (
        "Escalate a support ticket to a human support "
        "representative when automated handling is "
        "insufficient or human intervention is required."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "ticket_id": {
                "type": "string",
                "description": "The support ticket identifier.",
            },
            "reason": {
                "type": "string",
                "description": (
                    "Why human intervention is required."
                ),
            },
        },
        "required": [
            "ticket_id",
            "reason",
        ],
    },
}


TOOL_SCHEMAS = [
    CUSTOMER_STATUS_TOOL,
    SEARCH_KNOWLEDGE_BASE_TOOL,
    CREATE_TICKET_TOOL,
    ESCALATE_TO_HUMAN_TOOL,
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
    "create_ticket": create_ticket,
    "escalate_to_human": escalate_to_human,
}