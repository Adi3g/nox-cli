from __future__ import annotations

import json

import pytest
from click.testing import CliRunner

from nox.commands.jwt_commands import generate
from nox.commands.jwt_commands import verify
from nox.domains.jwt_manager import JWTManager


@pytest.fixture
def temp_key_file(tmp_path):
    key_file = tmp_path / 'key.pem'
    key_file.write_text('supersecretkey')
    return str(key_file)


@pytest.fixture
def temp_claims_file(tmp_path):
    claims_file = tmp_path / 'claims.json'
    claims_data = {
        'user_id': '12345',
        'role': 'admin',
    }
    claims_file.write_text(json.dumps(claims_data))
    return str(claims_file)


def test_jwt_generate(temp_key_file, temp_claims_file):
    runner = CliRunner()
    result = runner.invoke(
        generate, [
            '--env', 'prod',
            '--key', temp_key_file,
            '--claims', temp_claims_file,
        ],
    )

    assert result.exit_code == 0
    assert 'Generated JWT:' in result.output

    # Extract the token from the output for further testing
    generated_token = result.output.split('Generated JWT: ')[1].strip()
    assert generated_token

    # Verify that the generated token can be decoded using the same key
    manager = JWTManager(secret='supersecretkey')
    decoded = manager.verify_token(generated_token)
    assert decoded['user_id'] == '12345'
    assert decoded['role'] == 'admin'
    assert decoded['env'] == 'prod'


def test_jwt_verify(temp_key_file, temp_claims_file):
    runner = CliRunner()

    # First, generate a token to verify
    generate_result = runner.invoke(
        generate, [
            '--env', 'prod',
            '--key', temp_key_file,
            '--claims', temp_claims_file,
        ],
    )
    generated_token = generate_result.output.split('Generated JWT: ')[
        1
    ].strip()

    # Now, verify the generated token
    verify_result = runner.invoke(
        verify, [
            '--token', generated_token,
            '--key', temp_key_file,
        ],
    )

    assert verify_result.exit_code == 0
    assert 'Token is valid. Payload:' in verify_result.output
    assert "'user_id': '12345'" in verify_result.output
    assert "'role': 'admin'" in verify_result.output
    assert "'env': 'prod'" in verify_result.output


def test_jwt_verify_invalid_token(temp_key_file):
    runner = CliRunner()
    invalid_token = 'this.is.not.a.valid.token'

    verify_result = runner.invoke(
        verify, [
            '--token', invalid_token,
            '--key', temp_key_file,
        ],
    )

    assert verify_result.exit_code == 0
    assert 'Token verification failed' in verify_result.output
