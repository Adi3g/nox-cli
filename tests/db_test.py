from __future__ import annotations

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from nox.domains.db_manager import DBManager


@pytest.fixture
def db_manager():
    """Fixture to create a DBManager instance with a mocked connection string."""
    return DBManager('sqlite:///:memory:')


@patch('nox.domains.db_manager.create_engine')
def test_run_query_with_error(mock_create_engine, db_manager):
    """Test running a SQL query that raises an error."""
    mock_engine = MagicMock()
    mock_connection = mock_engine.connect.return_value.__enter__.return_value
    mock_create_engine.return_value = mock_engine

    # Simulate an error during query execution
    mock_connection.execute.side_effect = SQLAlchemyError('Query failed')

    result = db_manager.run_query('SELECT * FROM test;')
    assert result == [], 'Expected empty result on query failure.'


@patch('nox.domains.db_manager.DBManager.run_query')
def test_list_tables(mock_run_query, db_manager):
    """Test listing tables in the database."""
    mock_run_query.return_value = [('table1',), ('table2',)]

    tables = db_manager.list_tables()
    assert tables == [('table1',), ('table2',)], 'Expected table list does not match.'


@patch('nox.domains.db_manager.DBManager.run_query')
def test_run_migration(mock_run_query, db_manager, tmp_path):
    """Test running a SQL migration file."""
    migration_file = tmp_path / 'migration.sql'
    migration_file.write_text('CREATE TABLE test (id INTEGER);')

    db_manager.run_migration(str(migration_file))

    # Check if the migration SQL was executed
    mock_run_query.assert_called_once_with('CREATE TABLE test (id INTEGER);')


@patch('nox.domains.db_manager.DBManager.run_query')
def test_run_migration_file_not_found(mock_run_query, db_manager):
    """Test running a migration when the file does not exist."""
    db_manager.run_migration('non_existent_file.sql')
    mock_run_query.assert_not_called()  # Ensure no query is run


@patch('nox.domains.db_manager.DBManager.run_query')
def test_backup_database(mock_run_query, db_manager):
    """Test backup database command."""
    # Backup functionality is database-specific and not yet implemented.
    # Placeholder test to ensure it runs without crashing.
    db_manager.backup_database('backup.sql')
    mock_run_query.assert_not_called()


@patch('nox.domains.db_manager.DBManager.run_query')
def test_restore_database(mock_run_query, db_manager):
    """Test restore database command."""
    # Restore functionality is database-specific and not yet implemented.
    # Placeholder test to ensure it runs without crashing.
    db_manager.restore_database('backup.sql')
    mock_run_query.assert_not_called()
