# Changelog

All notable changes to this project will be documented in this file.

## Version History

| Version | Feature Domain         | Key Objectives                                                            |
| ------- | ---------------------- | ------------------------------------------------------------------------ |
| 0.1.0   | Project Foundations    | Scaffold package layout, settings via pydantic-settings, Typer CLI entry, pytest suite |

## Unreleased

Next release will be **0.1.1**; subsequent releases increment the patch version (0.1.2, 0.1.3, ...).

## 0.1.0 - 2026-09-24

### Added

- Project scaffold: `src/triage_ai`, `tests`, `data`, `prompts`, `docs` layout.
- Dependency management via `uv` (`pyproject.toml`, `uv.lock`).
- Configuration layer with `pydantic-settings` (`Settings` model, `.env` support).
- Typer CLI with `info` command and Rich output.
- CLI entry point `triage-ai` registered in `pyproject.toml`.
- `pytest` test suite covering configuration defaults.
- `.env.example` and `.gitignore` for local development.