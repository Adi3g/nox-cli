from __future__ import annotations

import click

from nox.domains.jwt_manager import JWTManager


@click.group()
def jwt() -> None:
    """JWT commands."""
    pass


@click.command()
@click.option('--env', required=True, help='Environment (e.g., prod, dev)')
@click.option('--key', required=True, help='Path to the key file')
@click.option('--claims', required=True, help='Path to the claims JSON file')
@click.option(
    '--expires-in', default=3600,
    help='Expiration time in seconds(default: 3600)',
)
def generate(env: str, key: str, claims: str, expires_in: int) -> None:
    """Generate a JWT token based on the environment, key file, and claims."""
    # Load the secret key from the provided key file
    with open(key) as key_file:
        secret = key_file.read().strip()

    # Load the claims from the provided JSON file
    claims_data = JWTManager.load_claims(claims)

    # Add environment information to claims
    claims_data['env'] = env

    # Initialize the JWTManager and generate the token
    manager = JWTManager(secret=secret)
    token = manager.generate_token(claims_data, expires_in)

    click.echo(f"Generated JWT: {token}")


@click.command()
@click.option('--token', required=True, help='The JWT token to verify')
@click.option('--key', required=True, help='Path to the public key file')
def verify(token: str, key: str) -> None:
    """Verify a JWT token using the public key."""
    # Load the public key from the provided key file
    with open(key) as key_file:
        public_key = key_file.read().strip()

    # Initialize the JWTManager with the public key and verify the token
    manager = JWTManager(secret=public_key)
    try:
        decoded = manager.verify_token(token)
        click.echo(f"Token is valid. Payload: {decoded}")
    except ValueError as e:
        click.echo(f"Token verification failed: {str(e)}")


# Adding Commands to the Group
jwt.add_command(generate)
jwt.add_command(verify)
