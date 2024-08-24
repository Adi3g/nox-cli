from __future__ import annotations

import uuid

from click.testing import CliRunner

from nox.commands.uuid_commands import uuid1
from nox.commands.uuid_commands import uuid4


def test_uuid1_command() -> None:
    runner = CliRunner()
    result = runner.invoke(uuid1)

    # Check that the command was successful
    assert result.exit_code == 0

    # Validate the output is a valid UUID1
    generated_uuid = result.output.strip().split(': ')[1]
    assert isinstance(generated_uuid, str)
    parsed_uuid = uuid.UUID(generated_uuid)
    assert parsed_uuid.version == 1


def test_uuid4_command() -> None:
    runner = CliRunner()
    result = runner.invoke(uuid4)

    # Check that the command was successful
    assert result.exit_code == 0

    # Validate the output is a valid UUID4
    generated_uuid = result.output.strip().split(': ')[1]
    assert isinstance(generated_uuid, str)
    parsed_uuid = uuid.UUID(generated_uuid)
    assert parsed_uuid.version == 4
