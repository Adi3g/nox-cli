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


@click.command()
@click.option(
    '--host', required=True,
    help='The host to perform traceroute on',
)
@click.option('--max-hops', default=30, help='Maximum number of hops')
def traceroute(host: str, max_hops: int) -> None:
    """Perform a traceroute to a specified host."""
    result = NetworkManager.traceroute(host, max_hops)
    click.echo(result)


@click.command()
@click.option(
    '--domain', required=True,
    help='The domain to perform WHOIS lookup on',
)
def whois(domain: str) -> None:
    """Perform a WHOIS lookup to get information about a domain."""
    result = NetworkManager.whois_lookup(domain)
    click.echo(result)


@click.command()
@click.option(
    '--ip', required=True,
    help='The IP address to get geolocation info for',
)
def geoip(ip: str) -> None:
    """Get geolocation information for an IP address."""
    result = NetworkManager.geoip_lookup(ip)
    click.echo(result)


@click.command()
@click.option(
    '--url', required=True,
    help='The URL to perform an HTTP GET request on',
)
def http(url: str) -> None:
    """Perform an HTTP GET request to a URL
    and display the response status and headers."""
    result = NetworkManager.http_request(url)
    click.echo(result)


@click.command()
def speedtest() -> None:
    """Test the download and upload bandwidth to/from a server."""
    result = NetworkManager.speedtest()
    click.echo(result)


@click.command()
@click.option(
    '--subnet', required=True,
    help='The subnet to perform a ping sweep on (e.g., 192.168.1.0/24)',
)
def ping_sweep(subnet: str) -> None:
    """Perform a ping sweep over a range of IP addresses
    to see which hosts are active."""
    result = NetworkManager.ping_sweep(subnet)
    click.echo(result)


@click.command()
@click.option(
    '--host', required=True,
    help='The host to check TCP connection',
)
@click.option(
    '--port', required=True,
    type=int, help='The port to check TCP connection',
)
def tcp_check(host: str, port: int) -> None:
    """Check if a TCP connection to a specified port on a host is possible."""
    result = NetworkManager.tcp_check(host, port)
    click.echo(result)


@click.command()
def arp() -> None:
    """Display the ARP (Address Resolution Protocol)
    cache on the local machine."""
    result = NetworkManager.arp_cache()
    click.echo(result)


@click.command()
def ifconfig() -> None:
    """Display information about network interfaces on the local machine."""
    result = NetworkManager.ifconfig()
    click.echo(result)


# Add commands to the group
net.add_command(ping)
net.add_command(dns)
net.add_command(scan)
net.add_command(traceroute)
net.add_command(whois)
net.add_command(geoip)
net.add_command(http)
net.add_command(speedtest)
net.add_command(ping_sweep)
net.add_command(tcp_check)
net.add_command(arp)
net.add_command(ifconfig)
