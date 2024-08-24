from __future__ import annotations

import click

from nox.commands import encrypt_commands
from nox.commands import init_command


@click.group()
def cli():
    """Nox CLI tool."""
    pass


# Register Init command
cli.add_command(init_command.init)

# Register built-in commands
cli.add_command(encrypt_commands.encrypt)


if __name__ == '__main__':
    cli()
