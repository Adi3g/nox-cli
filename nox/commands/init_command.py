from __future__ import annotations

import click

from nox.domains.Initializer import NoxInitializer


@click.command()
@click.option(
    '--shell', type=click.Choice(['bash', 'zsh', 'fish']),
    required=True, help='Shell type for auto-completion setup',
)
def init(shell: str) -> None:
    """Initialize Nox CLI with auto-completion."""
    initializer = NoxInitializer(shell)
    initializer.generate_completion_script()
    initializer.update_rc_file()
