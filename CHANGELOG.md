# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version Summary

| Version | Feature Domain | Key Objectives |
| --- | --- | --- |
| 0.1.0 (unreleased) | Phase 0 — Project Foundation | Set up the uv project, dependencies, environment variables, docs, Git hygiene, package layout, and sample data. |
| 0.1.0 (unreleased) | Phase 1 — First LLM Application | Build a simple LLM triage pipeline: domain models, config, prompts, Anthropic wrapper, orchestrator, CLI runner, and offline tests. |
| 0.1.0 (unreleased) | Phase 2 — Agent Loop | Implement a manual agent loop over the LLM with an educational tool, tool schemas, a tool registry, and execute-then-feed-back tool results. |
| 0.1.0 (unreleased) | Phase 3 — Knowledge-Base Tool | Ground agent answers by searching a fake knowledge base, with a search tool, result formatter, and grounded-generation prompt rules. |
| 0.1.0 (unreleased) | Phase 4 — Action Tools | Let the agent perform controlled actions by adding `create_ticket` and `escalate_to_human`, an in-memory action store, strict argument validation, and action rules. |

## [Unreleased]

### Phase 0 — Project Foundation

- Initialized `uv` project (`pyproject.toml`, `uv.lock`, virtualenv) with a `src` layout.
- Added runtime dependencies: `anthropic`, `pydantic`, `python-dotenv`.
- Added development dependency: `pytest`.
- Added `README.md` project overview and `PRD.md` full project plan.
- Added `.env.example` and gitignored local `.env`.
- Added `.gitignore` and CHANGELOG.
- Scaffolded package layout under `src/support_agent/` and `tests/`.
- Added sample ticket dataset `data/tickets.json`.

### Phase 1 — First LLM Application

- Added domain models in `src/support_agent/models.py`:
  `SupportTicket`, `TicketCategory`, `TicketPriority`, `TriageResult`.
- Added `src/support_agent/config.py` loading `ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` from the environment.
- Added `src/support_agent/prompts.py` with the triage system prompt requesting structured JSON output.
- Added `src/support_agent/llm.py` `ask_llm()` wrapper around the Anthropic Messages API (replaced by `call_llm()` in Phase 2).
- Added `src/support_agent/triage.py` `triage_ticket()` orchestrating prompt → LLM → Pydantic validation.
- Added `src/support_agent/main.py` CLI runner that triages the first ticket.
- Added offline model tests in `tests/test_triage.py` (no API dependency).
- Added baseline experiment documentation `docs/experiments/01_baseline.md`.
- Added `docs/handoff.md` for session continuity.

### Phase 2 — Agent Loop

- Added `src/support_agent/tools.py` with the educational `get_customer_status` tool, its `CUSTOMER_STATUS_TOOL` schema, `TOOL_SCHEMAS`, and `TOOL_REGISTRY`.
- Replaced `ask_llm()` with `call_llm()` in `src/support_agent/llm.py` (accepts a message history and optional tool schemas).
- Added `src/support_agent/agent.py` `SupportAgent` implementing the agent loop: `tool_use` dispatch, tool-result feedback, `stop_reason` handling, and a maximum-turn guard.
- Updated `TRIAGE_SYSTEM_PROMPT` in `src/support_agent/prompts.py` to advertise the available tool.
- Updated `src/support_agent/triage.py` to use `call_llm()` and added a robust JSON-extraction helper (`_extract_json`) that strips markdown code fences.
- Added `src/support_agent/run_agent.py` CLI runner that runs the agent on a sample request.
- Added offline tests for the tool registry, tool behavior, JSON extraction, and unknown-tool failure handling.
- Added agent-loop experiment documentation `docs/experiments/02_agent_loop.md`.
- Fixed a `JSONDecodeError` caused by the model wrapping JSON in code fences.

### Phase 3 — Knowledge-Base Tool

- Added `KnowledgeArticle` model in `src/support_agent/models.py`.
- Added fake knowledge base `data/knowledge_base.json` with five articles.
- Added `src/support_agent/knowledge_base.py` (`load_knowledge_base`, keyword-scoring `search_knowledge_base` with optional category filter).
- Added `SEARCH_KNOWLEDGE_BASE_TOOL` schema and registered it in `TOOL_SCHEMAS`.
- Added `format_knowledge_results()` and the `search_knowledge_base_tool` registry wrapper returning a formatted string for the LLM.
- Updated `TRIAGE_SYSTEM_PROMPT` with grounding rules (use the KB, don't invent policies, admit insufficient information).
- Added `src/support_agent/run_knowledge_agent.py` runner and knowledge-base search tests in `tests/test_tools.py`.
- Added knowledge-base experiment documentation `docs/experiments/03_knowledge_base.md`.

### Phase 4 — Action Tools

- Added `SupportTicketRecord` and `EscalationRecord` models in `src/support_agent/models.py`.
- Added `src/support_agent/action_store.py` in-memory `TICKETS` and `ESCALATIONS` stores (no database yet).
- Added `create_ticket` + `CREATE_TICKET_TOOL` and `escalate_to_human` + `ESCALATE_TO_HUMAN_TOOL` in `src/support_agent/tools.py`, with enum-constrained schemas; registered both in `TOOL_SCHEMAS` and `TOOL_REGISTRY`.
- Updated `TRIAGE_SYSTEM_PROMPT` with action rules (don't create/escalate unnecessarily, don't claim unperformed actions).
- Added `tests/test_actions.py` covering ticket creation, escalation, and rejection of invalid category input.
- Added `src/support_agent/run_action_agent.py` runner.
- Added action-tools experiment documentation `docs/experiments/04_action_tools.md`, including a recorded observation of the model falsely claiming an escalation that never occurred.