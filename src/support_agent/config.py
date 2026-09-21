"""Application configuration."""

from dataclasses import dataclass

from dotenv import load_dotenv

import os


@dataclass(frozen=True)
class Settings:
    anthropic_api_key: str
    anthropic_model: str
    anthropic_max_tokens: int

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        return cls(
            anthropic_api_key=_require("ANTHROPIC_API_KEY"),
            anthropic_model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5"),
            anthropic_max_tokens=int(os.getenv("ANTHROPIC_MAX_TOKENS", "1024")),
        )


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value