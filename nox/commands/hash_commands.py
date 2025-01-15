from __future__ import annotations

import click

from nox.domains.hash_manager import HashManager


@click.group()
def hash():
    """Hashing commands for generating and verifying hashes."""
    pass


@click.command()
@click.option(
    '--file', 'file_path',
    help='Path to the file to hash',
)
@click.option(
    '--text', 'text_to_hash',
    help='Text to hash',
)
@click.option(
    '--algorithm', default='md5',
    type=click.Choice(['md5', 'sha256', 'sha512']),
    help='Hashing algorithm to use',
)
def generate(file_path, text_to_hash, algorithm):
    """Generate a hash for a file or a text."""
    manager = HashManager()

    if file_path and text_to_hash:
        click.echo("Error: Please provide either --file or --text, not both.")
        return

    if file_path:
        file_hash = manager.generate_hash_from_file(file_path, algorithm)
        if file_hash:
            click.echo(f"{algorithm.upper()} hash for file {file_path}: {file_hash}")
    elif text_to_hash:
        text_hash = manager.generate_hash_from_text(text_to_hash, algorithm)
        if text_hash:
            click.echo(f"{algorithm.upper()} hash for text: {text_hash}")
    else:
        click.echo("Error: Please provide either --file or --text.")

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
    if manager.verify_hash_from_file(file_path, expected_hash, algorithm):
        click.echo(f"Hash matches for {file_path}.")
    else:
        click.echo(f"Hash does not match for {file_path}.")


# Add commands to the hash group
hash.add_command(generate)
hash.add_command(verify)
