# Experiment 04 — Action Tools

## Objective

Teach the support agent to perform controlled actions
rather than only retrieve information.

## Tools

### create_ticket

Creates a support ticket.

### escalate_to_human

Escalates a ticket to human support.

## Architecture

Customer
    ↓
Agent
    ↓
Tool Decision
    ↓
Python Tool
    ↓
Application State

## Important Boundary

The LLM requests an action.

The application executes the action.

The LLM does not directly modify application state.

## Tests

Test:

- valid ticket creation
- invalid category
- invalid priority
- escalation
- agent-generated ticket creation

## Observations

Record:

- which tools the agent selected
- whether arguments were valid
- whether unnecessary actions occurred
- whether the final response accurately described the action

### Actual Result (first run, 2026-09-21)

- The agent selected `create_ticket` with valid arguments and a real ticket
  was created (`T-BF7B226E`).
- The final response **inaccurately claimed** the ticket had been
  escalated, although `escalate_to_human` was never called.
- This is a grounding/veracity failure of the kind the prompt rules try to
  prevent: "do not claim an action was performed unless the corresponding
  tool performed it."
- The application state was always correct (only a ticket existed, no
  escalation record), but the customer-facing text was misleading.

Open question: what should we do when the model's text contradicts the
tool record — post-edit the response, or force it to report exactly what
tools returned?

## Lessons Learned

Record what you learned about:

- action tools
- state changes
- validation
- tool schemas
- agent autonomy

## Next Experiment

Deliberately introduce a bad tool schema and observe
how the agent behaves.