from __future__ import annotations

import click

from nox.domains.hash_manager import HashManager


@click.group()
def hash():
    """Hashing commands for generating and verifying hashes."""
    pass


@click.command()
@click.option(
    '--file', 'file_path', required=True,
    help='Path to the file to hash',
)
@click.option(
    '--algorithm', default='md5',
    type=click.Choice(['md5', 'sha256', 'sha512']),
    help='Hashing algorithm to use',
)
def generate(file_path, algorithm):
    """Generate a hash for a file."""
    manager = HashManager()
    file_hash = manager.generate_hash(file_path, algorithm)
    if file_hash:
        click.echo(f"{algorithm.upper()} hash for {file_path}: {file_hash}")


@click.command()
@click.option(
    '--file', 'file_path', required=True,
    help='Path to the file to verify',
)
@click.option(
    '--hash', 'expected_hash', required=True,
    help='Expected hash value',
)
@click.option(
    '--algorithm', default='md5',
    type=click.Choice(['md5', 'sha256', 'sha512']),
    help='Hashing algorithm to use',
)
def verify(file_path, expected_hash, algorithm):
    """Verify a file's hash against the expected hash."""
    manager = HashManager()
    if manager.verify_hash(file_path, expected_hash, algorithm):
        click.echo(f"Hash matches for {file_path}.")
    else:
        click.echo(f"Hash does not match for {file_path}.")


# Add commands to the hash group
hash.add_command(generate)
hash.add_command(verify)
