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


class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class ExtractedTicket(BaseModel):
    customer_id: str | None = None
    product: str | None = None
    sentiment: Sentiment
    priority: TicketPriority
    category: TicketCategory


class KnowledgeArticle(BaseModel):
    id: str
    title: str
    category: str
    content: str


class SupportTicketRecord(BaseModel):
    ticket_id: str
    customer_id: str
    category: TicketCategory
    priority: TicketPriority
    summary: str
    status: str = "open"


class EscalationRecord(BaseModel):
    ticket_id: str
    reason: str
    status: str = "pending"