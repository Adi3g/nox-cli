from __future__ import annotations

import click

from nox.domains.net_manager import NetworkManager


@click.group()
def net() -> None:
    """Network operations."""
    pass


@click.command()
@click.option('--host', required=True, help='The host to ping')
@click.option('--count', default=4, help='Number of ping requests to send')
def ping(host: str, count: int) -> None:
    """Ping a host and check if it is reachable."""
    result = NetworkManager.ping(host, count)
    click.echo(result)


@click.command()
@click.option(
    '--domain', required=True,
    help='The domain to perform DNS lookup for',
)
def dns(domain: str) -> None:
    """Perform a DNS lookup for a domain."""
    result = NetworkManager.dns_lookup(domain)
    click.echo(result)


@click.command()
@click.option('--host', required=True, help='The host to scan')
@click.option(
    '--ports', required=True,
    help='Port range to scan (e.g., 20-80)',
)
def scan(host: str, ports: str) -> None:
    """Scan a range of ports on a specified host."""
    result = NetworkManager.port_scan(host, ports)
    click.echo(result)


# Add commands to the group
net.add_command(ping)
net.add_command(dns)
net.add_command(scan)
