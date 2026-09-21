from enum import Enum

from pydantic import BaseModel


class SupportTicket(BaseModel):
    ticket_id: str
    customer_id: str
    message: str


class TicketCategory(str, Enum):
    ACCOUNT = "account"
    BILLING = "billing"
    TECHNICAL = "technical"
    PRODUCT = "product"
    SHIPPING = "shipping"
    OTHER = "other"


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TriageResult(BaseModel):
    category: TicketCategory
    priority: TicketPriority
    reasoning: str
    response: str


class KnowledgeArticle(BaseModel):
    id: str
    title: str
    category: str
    content: str