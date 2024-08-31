from __future__ import annotations

import click

from nox.commands import db_commands
from nox.commands import docker_commands
from nox.commands import encrypt_commands
from nox.commands import hash_commands
from nox.commands import init_command
from nox.commands import jwt_commands
from nox.commands import net_commands
from nox.commands import s3_commands
from nox.commands import secret_commands
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
cli.add_command(net_commands.net)
cli.add_command(s3_commands.s3)
cli.add_command(hash_commands.hash)
cli.add_command(secret_commands.secrets)
cli.add_command(docker_commands.docker)
cli.add_command(db_commands.db)

if __name__ == '__main__':
    cli()
