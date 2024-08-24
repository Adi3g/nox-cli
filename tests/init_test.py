from __future__ import annotations

from click.testing import CliRunner

from nox.commands.init_command import init


def test_init_bash():
    runner = CliRunner()
    result = runner.invoke(init, ['--shell', 'bash'])
    assert result.exit_code == 0
    assert 'Auto-completion script generated at' in result.output


def test_init_zsh():
    runner = CliRunner()
    result = runner.invoke(init, ['--shell', 'zsh'])
    assert result.exit_code == 0
    assert 'Auto-completion script generated at' in result.output


def test_init_fish():
    runner = CliRunner()
    result = runner.invoke(init, ['--shell', 'fish'])
    assert result.exit_code == 0
    assert 'Auto-completion script generated at' in result.output
