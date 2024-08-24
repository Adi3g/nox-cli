from __future__ import annotations

import click

from nox.domains.uuid_generator import UUIDGenerator


@click.group()
def gen() -> None:
    """Generator commands."""
    pass


@click.command()
def uuid1() -> None:
    """Generate a UUID based on the host ID and current time."""
    generator = UUIDGenerator()
    click.echo(f"UUID1: {generator.generate_uuid1()}")


@click.command()
def uuid4() -> None:
    """Generate a random UUID."""
    generator = UUIDGenerator()
    click.echo(f"UUID4: {generator.generate_uuid4()}")


# Adding Commands to the Group
gen.add_command(uuid1)
gen.add_command(uuid4)
