# Session Handoff

Project: Support Ticket Triage Agent. See `PRD.md` for the full plan.

## Current Status

- **Phase 0 — Foundation:** complete. uv project, deps, `.env.example`, `.gitignore`, `src/` layout, `docs/`, sample data.
- **Phase 1 — First LLM Application:** complete. Models, config, prompts, LLM wrapper, triage orchestrator, CLI runner, tests.
- **Phase 2 — Agent Loop:** complete. Manual agent loop with the educational `get_customer_status` tool, schemas, registry, tool-result feedback.
- **Phase 3 — Knowledge-Base Tool:** complete. Keyword-search KB grounding, `search_knowledge_base` tool, result formatter, grounded prompt rules.
- **Phase 4 — Action Tools:** complete. `create_ticket` + `escalate_to_human` with an in-memory store, enum-constrained schemas, action prompt rules.

## What's Built

- `src/support_agent/models.py` — `SupportTicket`, `TicketCategory`, `TicketPriority`, `TriageResult`, `KnowledgeArticle`, `SupportTicketRecord`, `EscalationRecord`.
- `src/support_agent/config.py` — loads `ANTHROPIC_API_KEY` / `ANTHROPIC_MODEL` from `.env` (python-dotenv), raises if key missing.
- `src/support_agent/prompts.py` — `TRIAGE_SYSTEM_PROMPT` advertising the 4 tools plus grounding/action rules.
- `src/support_agent/llm.py` — `call_llm(*, system_prompt, messages, tools=None)`.
- `src/support_agent/agent.py` — `SupportAgent(max_turns=5)` loop; `_execute_tool` returns error strings for unknown tools and tool failures.
- `src/support_agent/tools.py` — `get_customer_status`, `search_knowledge_base_tool`, `create_ticket`, `escalate_to_human`; `TOOL_SCHEMAS` (4) and `TOOL_REGISTRY`.
- `src/support_agent/knowledge_base.py` — `load_knowledge_base`, keyword-scoring `search_knowledge_base`.
- `src/support_agent/action_store.py` — in-memory `TICKETS` / `ESCALATIONS`.
- `src/support_agent/triage.py` — legacy non-agent pipeline with `_extract_json` (strips code fences; non-dict → `TypeError`).
- Runners: `main.py`, `run_agent.py`, `run_knowledge_agent.py`, `run_action_agent.py`.
- Data: `data/tickets.json` (T001–T005), `data/knowledge_base.json` (KB001–KB005).
- Tests: `tests/test_triage.py`, `tests/test_tools.py`, `tests/test_actions.py` — **15 passed**.
- Docs: `docs/experiments/01_baseline.md` … `04_action_tools.md`, `docs/handoff.md` (this file).
- `README.md` (short overview) and `PRD.md` (full plan, renamed from README.md; diagrams beautified).

## Verified Live Runs

- Dark-mode question → agent searched KB, gave grounded answer.
- Biometric-authentication question → agent correctly admitted the KB had no relevant info.
- C002 double-charge request → agent created ticket `T-BF7B226E`; its final text **falsely claimed escalation** that never occurred (recorded in `04_action_tools.md` as an open design question).

## Next Steps

1. Start Phase 5 — Tool Schema Engineering: intentionally define a `BAD TOOL SCHEMA`, observe failures, diagnose, fix, compare behavior; write `docs/experiments/05_bad_tool_schema.md`.

## Run

```bash
uv sync
uv run pytest -q
uv run ruff check .
uv run python -m support_agent.run_action_agent   # live agent demo
```

## Loose Ends

- `ruff format .` is intentionally NOT applied (user hand-formats; `ruff format --check` flags it).
- Known open design question: how to handle/guard against model text contradicting tool records (see `04_action_tools.md`).