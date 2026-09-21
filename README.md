# Support Ticket Triage Agent

An AI engineering learning project that progressively builds a
customer-support ticket triage agent from a simple LLM application
into a production-oriented agentic system.

## Goal

Given a customer support ticket, the system will eventually:

- classify the ticket
- determine priority
- search a knowledge base
- draft a grounded response
- create tickets
- escalate to humans
- use customer memory
- collaborate with specialized agents
- evaluate its own behavior
- operate with reliability and observability

## Learning Goals

This project covers:

- LLM applications
- prompt engineering
- structured outputs
- agent loops
- tool calling
- tool schemas
- grounding
- structured extraction
- memory management
- MCP
- multi-agent orchestration
- evaluation
- CI/CD
- reliability
- guardrails
- observability

## Stack

- Python
- uv
- Anthropic API
- Pydantic
- pytest
- GitHub Actions

## Development Philosophy

The system is built incrementally.

The initial implementation avoids agent frameworks so that the
underlying mechanics of LLM applications and agent loops can be
understood before introducing higher-level abstractions.