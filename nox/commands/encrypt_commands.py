from __future__ import annotations

import click

from nox.domains.encrypt import EncryptionManager


@click.group()
def encrypt():
    """Encryption and Decryption commands."""
    pass

# Fernet Encryption Commands


@click.command()
@click.option('--text', help='Text to encrypt')
@click.option('--input', type=click.File('rb'), help='Path to the input file')
@click.option(
    '--output', type=click.File('wb'),
    help='Path to the output file',
)
@click.option('--key', required=True, help='Path to the encryption key')
def fernet(text, input, output, key) -> None:
    """Encrypt text or file using Fernet."""
    manager = EncryptionManager(
        input_text=text, input_file=input, key_file=key,
    )
    encrypted_data = manager.encrypt_fernet()
    if output:
        output.write(encrypted_data)
    else:
        click.echo(f"Encrypted text: {encrypted_data.decode()}")

# Base64 Encryption Commands


@click.command()
@click.option('--text', help='Text to encrypt')
@click.option('--input', type=click.File('rb'), help='Path to the input file')
@click.option(
    '--output', type=click.File('wb'),
    help='Path to the output file',
)
def base64(text: str, input, output) -> None:
    """Encrypt text or file using Base64."""
    manager = EncryptionManager(input_text=text, input_file=input)
    encrypted_data = manager.encrypt_base64()
    if output:
        output.write(encrypted_data)
    else:
        click.echo(f"Encrypted text: {encrypted_data.decode()}")

# RSA Encryption Commands


@click.command()
@click.option('--text', help='Text to encrypt')
@click.option(
    '--input', type=click.File('rb'),
    help='Path to the input file',
)
@click.option(
    '--output', type=click.File('wb'),
    help='Path to the output file',
)
@click.option('--key', required=True, help='Path to the RSA public key')
def rsa(text: str, input, output, key) -> None:
    """Encrypt text or file using RSA."""
    manager = EncryptionManager(
        input_text=text, input_file=input, key_file=key,
    )
    encrypted_data = manager.encrypt_rsa()
    if output:
        output.write(encrypted_data)
    else:
        click.echo(f"Encrypted text: {encrypted_data.decode()}")


# Adding Commands to the Group
encrypt.add_command(fernet)
encrypt.add_command(base64)
encrypt.add_command(rsa)
