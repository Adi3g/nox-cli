from __future__ import annotations

import click

from nox.domains.redis_manager import RedisManager

# Initialize Redis manager
redis_manager = RedisManager()


@click.group()
def redis():
    """Redis management commands."""
    pass


@click.command()
@click.option('--key', required=True, help='Key to set in Redis')
@click.option('--value', required=True, help='Value to set for the key')
def set_key(key, value):
    """Set a key in Redis."""
    result = redis_manager.set_key(key, value)
    click.echo(result)


@click.command()
@click.option('--key', required=True, help='Key to get from Redis')
def get_key(key):
    """Get a key from Redis."""
    result = redis_manager.get_key(key)
    click.echo(result)


@click.command()
@click.option('--key', required=True, help='Key to delete from Redis')
def delete_key(key):
    """Delete a key from Redis."""
    result = redis_manager.delete_key(key)
    click.echo(result)


@click.command()
@click.option('--pattern', default='*', help='Pattern to match keys (default: *)')
def list_keys(pattern):
    """List keys in Redis."""
    result = redis_manager.list_keys(pattern)
    click.echo('\n'.join(result))


@click.command()
def flush_db():
    """Flush the current Redis database."""
    result = redis_manager.flush_database()
    click.echo(result)


@click.command()
def info():
    """Get Redis server information."""
    result = redis_manager.info()
    click.echo(result)


# Add commands to the redis group
redis.add_command(set_key)
redis.add_command(get_key)
redis.add_command(delete_key)
redis.add_command(list_keys)
redis.add_command(flush_db)
redis.add_command(info)
