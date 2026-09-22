# Session Handoff

Project: Support Ticket Triage Agent. See `PRD.md` for the full plan.

## Current Status

- **Phase 0 — Foundation:** complete. uv project, deps, `.env.example`, `.gitignore`, `src/` layout, `docs/`, sample data.
- **Phase 1 — First LLM Application:** complete. Models, config, prompts, LLM wrapper, triage orchestrator, CLI runner, tests.
- **Phase 2 — Agent Loop:** complete. Manual agent loop with the educational `get_customer_status` tool, schemas, registry, tool-result feedback.
- **Phase 3 — Knowledge-Base Tool:** complete. Keyword-search KB grounding, `search_knowledge_base` tool, result formatter, grounded prompt rules.
- **Phase 4 — Action Tools:** complete. `create_ticket` + `escalate_to_human` with an in-memory store, enum-constrained schemas, action prompt rules.
- **Phase 5 — Tool Schema Engineering:** complete. Deliberately broken `BAD_CREATE_TICKET_TOOL` schema experiment, offline schema-validation tests, clarified `CREATE_TICKET_TOOL` descriptions.
- **Phase 6 — Structured Extraction:** complete. `Sentiment` + `ExtractedTicket` models, extraction prompt, safe extraction wrapper, runner, tests, experiment doc.

## What's Built

- `src/support_agent/models.py` — `SupportTicket`, `TicketCategory`, `TicketPriority`, `TriageResult`, `KnowledgeArticle`, `SupportTicketRecord`, `EscalationRecord`, `Sentiment`, `ExtractedTicket`.
- `src/support_agent/config.py` — loads `ANTHROPIC_API_KEY` / `ANTHROPIC_MODEL` from `.env` (python-dotenv), raises if key missing.
- `src/support_agent/prompts.py` — `TRIAGE_SYSTEM_PROMPT` advertising the 4 tools plus grounding/action rules; `EXTRACTION_SYSTEM_PROMPT` for structured extraction.
- `src/support_agent/llm.py` — `call_llm(*, system_prompt, messages, tools=None)`.
- `src/support_agent/agent.py` — `SupportAgent(max_turns=5)` loop; `_execute_tool` returns error strings for unknown tools and tool failures.
- `src/support_agent/tools.py` — `get_customer_status`, `search_knowledge_base_tool`, `create_ticket`, `escalate_to_human`; `TOOL_SCHEMAS` (4) and `TOOL_REGISTRY`.
- `src/support_agent/knowledge_base.py` — `load_knowledge_base`, keyword-scoring `search_knowledge_base`.
- `src/support_agent/action_store.py` — in-memory `TICKETS` / `ESCALATIONS`.
- `src/support_agent/extraction.py` — `extract_ticket_information()` (prompt → LLM → JSON → Pydantic) with `ExtractionError` for invalid JSON/data.
- `src/support_agent/bad_tools.py` — `BAD_CREATE_TICKET_TOOL` for the bad-schema experiment.
- `src/support_agent/triage.py` — legacy non-agent pipeline with `_extract_json` (strips code fences; non-dict → `TypeError`).
- Runners: `main.py`, `run_agent.py`, `run_knowledge_agent.py`, `run_action_agent.py`, `run_extraction.py`.
- Data: `data/tickets.json` (T001–T005), `data/knowledge_base.json` (KB001–KB005).
- Tests: `tests/test_triage.py`, `tests/test_tools.py`, `tests/test_actions.py`, `tests/test_tool_schemas.py`, `tests/test_extraction.py` — **22 passed**.
- Docs: `docs/experiments/01_baseline.md` … `05_structured_extraction.md` (incl. `03_bad_tool_schema.md`), `docs/handoff.md` (this file).
- `README.md` (short overview) and `PRD.md` (full plan, renamed from README.md; diagrams beautified).

## Verified Live Runs

- Dark-mode question → agent searched KB, gave grounded answer.
- Biometric-authentication question → agent correctly admitted the KB had no relevant info.
- C002 double-charge request → agent created ticket `T-BF7B226E`; its final text **falsely claimed escalation** that never occurred (recorded in `04_action_tools.md` as an open design question).
- Bad-schema experiment hit expected failure (schema {{customer, type, level, description}} vs. function {customer_id, category, priority, summary}).

## Next Steps

1. Start Phase 7 — Memory Management: give the agent durable conversational memory/state across turns; write `docs/experiments/06_memory.md`.
2. Open design question from Phase 6: how to integrate structured extraction with agent state (see `05_structured_extraction.md`).

## Run

```bash
uv sync
uv run pytest -q
uv run ruff check .
uv run python -m support_agent.run_action_agent   # live agent demo
uv run python -m support_agent.run_extraction     # live extraction demo
```

## Loose Ends

- `ruff format .` is intentionally NOT applied (user hand-formats; `ruff format --check` flags it).
- Known open design question: how to handle/guard against model text contradicting tool records (see `04_action_tools.md`).