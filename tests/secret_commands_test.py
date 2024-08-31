from __future__ import annotations

import boto3
import pytest
from moto import mock_aws

from nox.domains.secret_manager import SecretsManager


@pytest.fixture
def secrets_manager():
    with mock_aws():
        # Initialize the mock AWS Secrets Manager service
        yield SecretsManager(region_name='us-west-2')


def test_store_secret(secrets_manager):
    """Test storing a secret."""
    secrets_manager.store_secret(name='test-secret', value='secret-value')
    client = boto3.client('secretsmanager', region_name='us-west-2')
    response = client.get_secret_value(SecretId='test-secret')
    assert response['SecretString'] == 'secret-value', 'Stored secret value mismatch.'


def test_get_secret(secrets_manager):
    """Test retrieving a secret."""
    client = boto3.client('secretsmanager', region_name='us-west-2')
    client.create_secret(Name='test-secret', SecretString='secret-value')

    secret_value = secrets_manager.get_secret(name='test-secret')
    assert secret_value == 'secret-value', 'Retrieved secret value mismatch.'


def test_list_secrets(secrets_manager, capsys):
    """Test listing secrets."""
    client = boto3.client('secretsmanager', region_name='us-west-2')
    client.create_secret(Name='test-secret1', SecretString='secret-value1')
    client.create_secret(Name='test-secret2', SecretString='secret-value2')

    secrets_manager.list_secrets()

    # Capture the output
    captured = capsys.readouterr()
    assert 'test-secret1' in captured.out, "Secret 'test-secret1' not listed."
    assert 'test-secret2' in captured.out, "Secret 'test-secret2' not listed."


def test_delete_secret(secrets_manager):
    """Test deleting a secret."""
    client = boto3.client('secretsmanager', region_name='us-west-2')
    client.create_secret(Name='test-secret', SecretString='secret-value')

    secrets_manager.delete_secret(name='test-secret')

    # Try to retrieve the secret to ensure it was deleted
    with pytest.raises(client.exceptions.ResourceNotFoundException):
        client.get_secret_value(SecretId='test-secret')
