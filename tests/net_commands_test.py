from __future__ import annotations

import pytest
from click.testing import CliRunner

from nox.commands.net_commands import arp
from nox.commands.net_commands import geoip
from nox.commands.net_commands import http
from nox.commands.net_commands import ifconfig
from nox.commands.net_commands import ping_sweep
from nox.commands.net_commands import speedtest
from nox.commands.net_commands import tcp_check
from nox.commands.net_commands import traceroute
from nox.commands.net_commands import whois


@pytest.fixture
def runner():
    return CliRunner()


def test_traceroute(runner):
    result = runner.invoke(traceroute, ['--host', 'example.com'])
    assert result.exit_code == 0
    assert '192.168.1.1' in result.output.lower()


def test_whois(runner):
    result = runner.invoke(whois, ['--domain', 'example.com'])
    assert result.exit_code == 0
    assert 'domain' in result.output.lower()


def test_geoip(runner):
    result = runner.invoke(geoip, ['--ip', '8.8.8.8'])
    assert result.exit_code == 0
    assert 'country' in result.output.lower()


def test_http(runner):
    result = runner.invoke(http, ['--url', 'https://example.com'])
    assert result.exit_code == 0
    assert 'status' in result.output.lower()


def test_speedtest(runner):
    result = runner.invoke(speedtest)
    assert result.exit_code == 0
    assert 'download speed' in result.output.lower()


def test_ping_sweep(runner):
    result = runner.invoke(ping_sweep, ['--subnet', '192.168.1.0/30'])
    assert result.exit_code == 0
    assert 'active hosts' in result.output.lower()


def test_tcp_check(runner):
    result = runner.invoke(
        tcp_check, ['--host', 'example.com', '--port', '80'],
    )
    assert result.exit_code == 0
    assert 'connection' in result.output.lower()


def test_arp(runner):
    result = runner.invoke(arp)
    assert result.exit_code == 0
    assert 'en1' in result.output.lower()


def test_ifconfig(runner):
    result = runner.invoke(ifconfig)
    assert result.exit_code == 0
    assert 'inet' in result.output.lower() or 'eth' in result.output.lower()
