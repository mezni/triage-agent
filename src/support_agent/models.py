"""Pydantic models for the triage agent."""

from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    PRODUCT = "product"
    OTHER = "other"


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Ticket(BaseModel):
    """A free-form customer support ticket."""

    ticket_id: str = Field(description="Unique ticket identifier")
    customer_id: str | None = Field(default=None, description="Identified customer, if known")
    text: str = Field(description="Free-form ticket body")


class TriageResult(BaseModel):
    """Structured classification of a support ticket."""

    customer_id: str | None = Field(default=None, description="Identified customer, if any")
    category: Category = Field(description="Ticket category")
    priority: Priority = Field(description="Ticket priority")
    summary: str = Field(description="One-sentence summary of the issue")
    escalate: bool = Field(default=False, description="Whether a human should handle this ticket")

    def __str__(self) -> str:
        return (
            f"TriageResult(customer_id={self.customer_id!r}, category={self.category.value}, "
            f"priority={self.priority.value}, escalate={self.escalate}, summary={self.summary!r})"
        )