# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- Added `src/support_agent/llm.py` `ask_llm()` wrapper around the Anthropic Messages API.
- Added `src/support_agent/triage.py` `triage_ticket()` orchestrating prompt → LLM → Pydantic validation.
- Added `src/support_agent/main.py` CLI runner that triages the first ticket.
- Added offline model tests in `tests/test_triage.py` (no API dependency).
- Added baseline experiment documentation `docs/experiments/01_baseline.md`.
- Added `docs/handoff.md` for session continuity.