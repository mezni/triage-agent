# Support Ticket Triage Agent

A production-oriented AI customer-support agent, built from scratch.

We are building this project **incrementally** so every layer is understood before abstractions are introduced. It is both a working application and a learning laboratory for AI engineering.

## 1. Business Problem

A customer-support team receives free-form support tickets such as:

> "I've been charged twice for my subscription and I need this fixed."

The system should be able to:

- understand the ticket
- identify the customer
- classify the category
- determine priority
- search relevant knowledge
- draft a grounded response
- create a ticket when necessary
- escalate to a human when appropriate

Later it will also research similar historical tickets and use persistent customer memory.

## 2. System Overview

The final conceptual flow:

```
                            ┌───────────────────────┐
                            │     Support Ticket    │
                            └───────────┬───────────┘
                                        ▼
                            ┌───────────────────────┐
                            │    Memory Retrieval   │
                            └───────────┬───────────┘
                                        ▼
                            ┌───────────────────────┐
                            │      Triage Agent     │
                            └───────────┬───────────┘
                                        │
                    ┐───────────────────┼───────────────────┌
                    ▼                   ▼                   ▼
           ┌─────────────────┐
           │  Knowledge Base │
           └────────┬────────┘
                               ┌─────────────────┐
                               │  Research Agent │
                               └────────┬────────┘
                                                   ┌─────────────────┐
                                                   │   Action Tools  │
                                                   └────────┬────────┘
                                                            ├── Create Ticket
                                                            ├── Escalate
                    │                   │                   │
                    └───────────────────┬───────────────────┘
                                        ▼
                            ┌───────────────────────┐
                            │     Final Response    │
                            └───────────┬───────────┘
                                        ▼
                            ┌───────────────────────┐
                            │   Memory Management   │
                            └───────────┬───────────┘
                                        │
                    ┐───────────────────┴───────────────────┌
                    ▼                                       ▼
           ┌─────────────────┐
           │    Evaluation   │
           └────────┬────────┘
                                                   ┌─────────────────┐
                                                   │  Observability  │
                                                   └────────┬────────┘
                    │                   │                   │
                    └───────────────────┬───────────────────┘
                                        ▼
                            ┌───────────────────────┐
                            │         CI/CD         │
                            └───────────────────────┘
```

## 3. What You Will Learn

The project covers the major AI-engineering concerns:

- **LLM engineering** — API integration, prompts, system instructions, conversation context, structured outputs, Pydantic validation
- **Agent engineering** — agent loops, tool calling, tool results, stopping conditions, agent state, tool schemas
- **Grounding** — knowledge-base search, retrieved context, grounded answers, handling insufficient information
- **Memory** — conversation history, working memory, persistent customer memory, memory extraction/retrieval/updates, conflicts, stale memories, memory evaluation
- **Multi-agent systems** — specialized agents, handoffs, context transfer, shared state, loops, redundant calls, context loss
- **AI reliability** — validation, retries, timeouts, fallbacks, failure handling, guardrails, authority boundaries
- **Evaluation** — evaluation datasets, expected outputs, regression testing, tool-use evaluation, memory evaluation, response evaluation
- **Production engineering** — CI/CD, structured logging, metrics, tracing, latency, token usage, failure diagnosis

## 4. Technology Stack

We start deliberately simple:

- Python
- uv
- Anthropic API
- Pydantic
- pytest
- python-dotenv
- Git
- GitHub Actions

Initially **no agent framework** — we implement the core agent loop ourselves so you understand what frameworks abstract away. MCP and other abstractions come later.

## 5. Project Structure

The project will evolve toward:

```
support-ticket-triage/
│
├── pyproject.toml
├── uv.lock
├── README.md
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   └── experiments/
│       ├── 01_baseline.md
│       ├── 02_bad_tool_schema.md
│       ├── 03_fixed_tool_schema.md
│       └── ...
│
├── src/
│   └── support_agent/
│       ├── config.py
│       ├── models.py
│       ├── prompts.py
│       ├── llm.py
│       ├── tools.py
│       ├── agent.py
│       ├── triage.py
│       ├── research.py
│       └── observability.py
│
├── data/
│   ├── tickets.json
│   ├── knowledge_base.json
│   └── evaluation_tickets.json
│
└── tests/
    ├── test_triage.py
    ├── test_tools.py
    ├── test_extraction.py
    └── test_evaluation.py
```

We do **not** create all of this at once — each phase introduces only the pieces needed for that phase.

## 6. Project Phases

### Phase 0 — Project Foundation

**Goal:** Build the Python project and understand the business problem.

**Learn:** project setup, uv, dependencies, environment variables, Git hygiene, Pydantic models, fake test data, project documentation

**Deliverable:** Clean runnable project.

### Phase 1 — First LLM Application

**Goal:** Understand a basic LLM application before building an agent.

**Learn:** Anthropic client, API requests, system prompts, user messages, responses, prompt design, structured output, Pydantic validation

**Architecture:**

```
        ┌────────────────┐
        │     Ticket     │
        └────────┬───────┘
                 ▼
        ┌────────────────┐
        │     Prompt     │
        └────────┬───────┘
                 ▼
        ┌────────────────┐
        │      LLM       │
        └────────┬───────┘
                 ▼
        ┌────────────────┐
        │   Structured   │
        │     Result     │
        └────────────────┘
```

**Deliverable:** Simple ticket classifier/responder.

### Phase 2 — Agent Loop

**Goal:** Understand what makes an LLM application agentic.

**Learn:** tool_use, stop_reason, message history, agent loop, tool requests, tool results, maximum turns, stopping conditions

**Architecture:**

```
                  ┌──────────────────────┐
                  │         LLM          │◄─────────┐
                  └───────────┬──────────┘       │
                              ▼                     │
                  ┌──────────────────────┐       │
                  │       Decision       │       │
                  └───────────┬──────────┘       │
                              │                     │
                ┐─────────────┴───────────┌       │
        tool_use                stop_reason         │
                │                           │       │
                ▼                         ▼         │
       ┌────────────────┐        ┌────────────────┐ │
       │  Execute Tool  │        │ Final Response │ │
       └────────┬───────┘        └────────────────┘ │
                └────────── tool result ─────────────┘
        (append tool result to message history, then loop again)
```

**Deliverable:** Minimal manually implemented agent.

### Phase 3 — Knowledge-Base Tool

**Goal:** Give the agent access to external knowledge.

**Learn:** tool definition, tool schema, tool registry, search, retrieved context, grounded generation

**Tools:** `search_knowledge_base`

**Deliverable:** Agent capable of answering using a fake support KB.

### Phase 4 — Action Tools

**Goal:** Allow the agent to perform controlled actions.

**Learn:** action tools, argument validation, tool results, authority boundaries, human escalation

**Tools:** `create_ticket`, `escalate_to_human`

**Deliverable:** Agent capable of deciding between answering, creating a ticket, or escalating.

### Phase 5 — Tool Schema Engineering

**Goal:** Understand that a tool schema is an interface between the LLM and your application.

We intentionally create:

```
        ┌──────────────────────┐
        │   Bad Tool Schema    │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │   Observe failures   │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │       Diagnose       │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │      Fix schema      │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │   Compare behavior   │
        └──────────────────────┘
```

**Learn:** schema ambiguity, descriptions, required fields, enums, argument validation, tool misuse, interface design

**Deliverable:** Experiment reports documenting the failure and fix.

### Phase 6 — Structured Extraction

**Goal:** Reliably extract structured information from free-form tickets.

Extract things such as: `customer_id`, `product`, `sentiment`, `priority`, `category`

**Learn:** extraction prompts, schemas, validation, malformed outputs, missing fields, ambiguous inputs, prompt/schema tuning

**Deliverable:** Robust extraction component with tests.

### Phase 7 — Memory Management

**Goal:** Understand and implement AI memory correctly.

**7.1 Conversation memory** — `messages[]`
Learn: conversation history, context windows, history management

**7.2 Working memory** — `AgentState`
Learn: temporary task state, state transitions, intermediate results

**7.3 Long-term customer memory** — `Customer` → persistent memories
Learn: memory storage, memory retrieval, memory extraction, memory updates

**7.4 Memory lifecycle**
Learn: create, update, delete, expiration, stale information, conflicting memories

**7.5 Memory evaluation**
Measure: extraction accuracy, retrieval relevance, update correctness, conflict handling

**Deliverable:** A simple persistent memory subsystem with tests.

### Phase 8 — MCP

**Goal:** Learn standardized tool/data integration.

**Learn:** MCP concepts, MCP client, MCP server, resources/tools, integration boundaries

We'll expose functionality such as knowledge-base search through MCP.

**Deliverable:** Working MCP integration.

### Phase 9 — Multi-Agent System

**Goal:** Introduce specialized agents.

**Architecture:**

```
           ┌────────────────┐
           │     Ticket     │
           └────────┬───────┘
                    ▼
           ┌────────────────┐
           │  Triage Agent  │
           └────────┬───────┘
                    ▼
           ┌────────────────┐
           │ Need research? │
           └────────┬───────┘
      no                      yes
        ┐───────────┴───────────┌
        │                       │
        ▼                       ▼
        │              ┌────────────────┐
        │              │ Research Agent │
        │              └────────┬───────┘
        │                       │
        │                      Research
        │                       │
        └───────────┬───────────┘
                    ▼
           ┌────────────────┐
           │  Triage Agent  │
           └────────┬───────┘
                    ▼
           ┌────────────────┐
           │     Final      │
           │    Response    │
           └────────────────┘
```

**Learn:** specialization, handoffs, context passing, shared state, agent boundaries, loops, redundant calls, context loss

**Deliverable:** Triage + Research agent system.

### Phase 10 — Claude Code

**Goal:** Learn how an AI coding assistant fits into software development.

**Learn:** repository understanding, scaffolding, refactoring, test generation, code review, Git workflow, reviewing AI-generated code

**Deliverable:** AI-assisted development workflow.

### Phase 11 — Evaluation

**Goal:** Move from "it seems to work" to "we can measure whether it works".

Create a fixed evaluation dataset and evaluate: classification, priority, tool selection, tool arguments, response quality, grounding, memory behavior

**Learn:** golden datasets, expected results, automated evaluation, regression detection

**Deliverable:** Automated agent evaluation suite.

### Phase 12 — CI/CD

**Goal:** Automatically detect regressions.

**Architecture:**

```
        ┌────────────────────────┐
        │        Git Push        │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │     GitHub Actions     │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │       Unit Tests       │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │    Agent Evaluation    │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │  Regression Detection  │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │      Pass / Fail       │
        └────────────────────────┘
```

**Learn:** GitHub Actions, automated testing, evaluation in CI, regression protection

**Deliverable:** CI pipeline that protects agent behavior.

### Phase 13 — Reliability Engineering

**Goal:** Make the agent resilient to real-world failures.

Handle: LLM failure, API timeout, rate limit, tool failure, validation failure, malformed output, network failure, agent loop

**Learn:** retries, exponential backoff, timeouts, fallbacks, error classification, maximum turns, graceful degradation

**Deliverable:** Resilient agent runtime.

### Phase 14 — Guardrails

**Goal:** Control what the agent is allowed to do.

**Learn:** input validation, output validation, tool authorization, action boundaries, escalation rules, unsupported-claim prevention, sensitive-data handling

**Example:**

```
        ┌──────────────────────────────────┐
        │ Agent wants to perform an action │
        └─────────────────┬────────────────┘
                          ▼
        ┌──────────────────────────────────┐
        │         Guardrail Check          │
        └─────────────────┬────────────────┘
                          │
              ┐───────────┴───────────┌
              ▼                       ▼
      ┌──────────────┐          ┌──────────────┐
      │   Allowed    │          │   Blocked    │
      └──────────────┘          └──────────────┘
```

**Deliverable:** Explicit safety and authority layer.

### Phase 15 — Observability

**Goal:** Make agent behavior diagnosable.

Add structured logs, metrics, traces. Track: request ID, agent decisions, tool calls, tool latency, LLM latency, failures, token usage, number of tool calls, memory retrieval, memory updates

**Deliverable:** Observable agent runtime.

### Phase 16 — Diagnostic Engineering

**Goal:** Practice debugging AI systems systematically.

We deliberately introduce failures: bad prompt, bad schema, bad tool result, missing context, invalid structured output, memory conflict, context loss, infinite loop, tool timeout, evaluation regression.

For every problem:

```
        ┌──────────────────────┐
        │       Observe        │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │      Reproduce       │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │   Collect evidence   │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │ Identify root cause  │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │         Fix          │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │ Add regression test  │
        └───────────┬──────────┘
                    ▼
        ┌──────────────────────┐
        │        Verify        │
        └──────────────────────┘
```

**Deliverable:** A collection of experiment reports showing how real agent failures were diagnosed.

## 7. The Learning Journey

The project ultimately follows this progression:

```
                AI ENGINEERING JOURNEY

      ┌────────────────────────────┐
      │            LLM             │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │ Structured LLM Application │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │         Agent Loop         │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │          Tool Use          │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │   Grounding / Knowledge    │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │  Tool Schema Engineering   │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │   Structured Extraction    │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │     Memory Management      │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │            MCP             │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │ Multi-Agent Orchestration  │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │  AI-Assisted Development   │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │         Evaluation         │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │           CI/CD            │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │        Reliability         │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │         Guardrails         │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │       Observability        │
      └──────────────┬─────────────┘
                     ▼
      ┌────────────────────────────┐
      │    Production Diagnosis    │
      └────────────────────────────┘
```

## Getting Started

> Instructions are added as phases land. Spot-check `docs/` after Phase 0.

```bash
uv sync
```

## Contributing / Workflow

This repository is built incrementally, phase by phase. Each phase produces a working deliverable plus documentation (`docs/experiments/`) explaining what was learned.