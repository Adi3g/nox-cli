from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from nox.domains.env_manager import EnvManager


@pytest.fixture
def env_manager():
    """Fixture to create an EnvManager instance with a mocked .env file."""
    return EnvManager('.env')


@patch('nox.domains.env_manager.load_dotenv')
def test_load_env_file(mock_load_dotenv, env_manager):
    """Test loading environment variables from a file."""
    env_manager.load_env_file('test.env')
    mock_load_dotenv.assert_called_once_with('test.env')
    print('Environment variables loaded from test.env.')


@patch('nox.domains.env_manager.set_key')
@patch.dict(os.environ, {}, clear=True)
def test_set_env_variable(mock_set_key, env_manager):
    """Test setting an environment variable."""
    env_manager.set_env_variable('TEST_VAR', 'test_value')
    assert os.environ['TEST_VAR'] == 'test_value', 'Environment variable not set correctly.'
    mock_set_key.assert_called_once_with('.env', 'TEST_VAR', 'test_value')
    print('Environment variable TEST_VAR set to test_value.')


@patch.dict(os.environ, {'EXISTING_VAR': 'existing_value'}, clear=True)
def test_get_env_variable(env_manager):
    """Test getting an environment variable."""
    value = env_manager.get_env_variable('EXISTING_VAR')
    assert value == 'existing_value', 'Expected environment variable value does not match.'


@patch('nox.domains.env_manager.unset_key')
@patch.dict(os.environ, {'TEST_VAR': 'test_value'}, clear=True)
def test_unset_env_variable(mock_unset_key, env_manager):
    """Test unsetting an environment variable."""
    env_manager.unset_env_variable('TEST_VAR')
    assert 'TEST_VAR' not in os.environ, 'Environment variable not removed correctly.'
    mock_unset_key.assert_called_once_with('.env', 'TEST_VAR')
    print('Environment variable TEST_VAR removed.')


@patch.dict(os.environ, {'VAR1': 'value1', 'VAR2': 'value2'}, clear=True)
def test_list_env_variables(env_manager, capsys):
    """Test listing all environment variables."""
    env_manager.list_env_variables()
    captured = capsys.readouterr()
    assert 'VAR1: value1' in captured.out, 'Environment variable VAR1 not listed correctly.'
    assert 'VAR2: value2' in captured.out, 'Environment variable VAR2 not listed correctly.'
