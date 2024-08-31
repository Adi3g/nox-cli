from __future__ import annotations

import click

from nox.domains.env_manager import EnvManager


@click.group()
def env():
    """Environment management commands."""
    pass


@click.command()
@click.option('--file', 'file_path', default='.env', help='Path to the environment file to load')
def load(file_path):
    """Load environment variables from a file."""
    manager = EnvManager()
    manager.load_env_file(file_path)


@click.command()
@click.option('--key', required=True, help='Environment variable key')
@click.option('--value', required=True, help='Environment variable value')
def set(key, value):
    """Set an environment variable."""
    manager = EnvManager()
    manager.set_env_variable(key, value)


@click.command()
@click.option('--key', required=True, help='Environment variable key')
def get(key):
    """Get the value of an environment variable."""
    manager = EnvManager()
    value = manager.get_env_variable(key)
    if value:
        click.echo(f"{key}={value}")
    else:
        click.echo(f"Environment variable {key} not found.")


@click.command()
@click.option('--key', required=True, help='Environment variable key')
def unset(key):
    """Unset an environment variable."""
    manager = EnvManager()
    manager.unset_env_variable(key)


@click.command()
def list():
    """List all environment variables."""
    manager = EnvManager()
    manager.list_env_variables()


# Add commands to the env group
env.add_command(load)
env.add_command(set)
env.add_command(get)
env.add_command(unset)
env.add_command(list, name='list')
