from __future__ import annotations

import click

from nox.domains.secret_manager import SecretsManager


@click.group()
def secrets():
    """Secrets management commands."""
    pass


@click.command()
@click.option('--name', required=True, help='Name of the secret')
@click.option('--value', required=True, help='Value of the secret')
@click.option('--region', default='us-west-2', help='AWS region')
def store(name, value, region):
    """Store a secret."""
    manager = SecretsManager(region_name=region)
    manager.store_secret(name, value)


@click.command()
@click.option('--name', required=True, help='Name of the secret')
@click.option('--region', default='us-west-2', help='AWS region')
def get(name, region):
    """Retrieve a secret."""
    manager = SecretsManager(region_name=region)
    secret = manager.get_secret(name)
    if secret:
        click.echo(f"Secret value: {secret}")


@click.command()
@click.option('--region', default='us-west-2', help='AWS region')
def list(region):
    """List all secrets."""
    manager = SecretsManager(region_name=region)
    manager.list_secrets()


@click.command()
@click.option('--name', required=True, help='Name of the secret to delete')
@click.option('--region', default='us-west-2', help='AWS region')
def delete(name, region):
    """Delete a secret."""
    manager = SecretsManager(region_name=region)
    manager.delete_secret(name)


# Add commands to the secrets group
secrets.add_command(store)
secrets.add_command(get)
secrets.add_command(list, name='list')
secrets.add_command(delete)
