# Session Handoff

Project: Support Ticket Triage Agent. See `PRD.md` for the full plan.

## Current Status

- **Phase 0 — Foundation:** complete. uv project, deps, `.env.example`, `.gitignore`, `src/` layout, `docs/`, test scaffold.
- **Phase 1 — First LLM Application:** in progress. Domain models, ticket dataset, and first tests are in place; the LLM layer is still to be implemented.

## What's Built

- `pyproject.toml` / `uv.lock` — Python 3.12, anthropic, pydantic, python-dotenv; dev: pytest (managed via uv, src layout with hatchling).
- `src/support_agent/models.py` — `SupportTicket`, `TicketCategory`, `TicketPriority`, `TriageResult`.
- `data/tickets.json` — 5 fake tickets (`message` field).
- `tests/test_triage.py` — passing model tests (2 passed).
- `.env.example` / `.env` (local, gitignored), `.gitignore`, `docs/experiments/` (empty, ready for experiment reports).
- README.md (short overview) and PRD.md (full plan, renamed from README.md).

## Next Steps

1. Finish Phase 1:
   - `config.py` — load `.env` (python-dotenv), expose `settings`.
   - `prompts.py` — system prompt for triage.
   - `llm.py` — Anthropic client call with structured output, Pydantic-validated `TriageResult`.
   - `triage.py` — orchestrates ticket → prompt → LLM → result.
2. Add real `ANTHROPIC_API_KEY` to `.env`.
3. Start Phase 2 — agent loop.

## Run

```bash
uv sync
uv run pytest
```

## Loose Ends

- `.env` contains a placeholder key.
- `config.py`, `prompts.py`, `llm.py`, `triage.py`, `__init__.py` are intentionally empty placeholders.
- `docs/experiments/` is empty and waiting for the first experiment reports (Phase 5).