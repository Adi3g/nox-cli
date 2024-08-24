from __future__ import annotations

import click

from nox.commands import encrypt_commands
from nox.commands import init_command
from nox.commands import jwt_commands
from nox.commands import uuid_commands


@click.group()
def cli():
    """Nox CLI tool."""
    pass


# Register Init command
cli.add_command(init_command.init)

# Register built-in commands
cli.add_command(encrypt_commands.encrypt)
cli.add_command(uuid_commands.gen)
cli.add_command(jwt_commands.jwt)

if __name__ == '__main__':
    cli()
