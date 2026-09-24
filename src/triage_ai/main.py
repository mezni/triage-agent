import typer
from rich import print

from triage_ai.config import settings


app = typer.Typer()


@app.callback()
def callback() -> None:
    """triage-ai command line interface."""


@app.command()
def info() -> None:
    """Display application information."""
    print(f"[bold]Application:[/bold] {settings.app_name}")
    print(f"[bold]Environment:[/bold] {settings.environment}")
    print(f"[bold]Debug:[/bold] {settings.debug}")


if __name__ == "__main__":
    app()