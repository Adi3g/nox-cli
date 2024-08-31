from __future__ import annotations

import click

from nox.domains.db_manager import DBManager


@click.group()
def db():
    """Database management commands."""
    pass


@click.command()
@click.option('--db', 'connection_string', required=True, help='Database connection string')
@click.option('--query', required=True, help='SQL query to run')
def query(connection_string, query):
    """Run a SQL query on the database."""
    manager = DBManager(connection_string)
    results = manager.run_query(query)
    for row in results:
        click.echo(row)


@click.command()
@click.option('--db', 'connection_string', required=True, help='Database connection string')
def list_tables(connection_string):
    """List tables in the database."""
    manager = DBManager(connection_string)
    tables = manager.list_tables()
    for table in tables:
        click.echo(table[0])  # Assuming table names are in the first column


@click.command()
@click.option('--db', 'connection_string', required=True, help='Database connection string')
@click.option('--migration', required=True, help='Path to the SQL migration file')
def migrate(connection_string, migration):
    """Run a SQL migration file."""
    manager = DBManager(connection_string)
    manager.run_migration(migration)


@click.command()
@click.option('--db', 'connection_string', required=True, help='Database connection string')
@click.option('--output', required=True, help='Path to save the backup')
def backup(connection_string, output):
    """Backup the database to a file."""
    manager = DBManager(connection_string)
    manager.backup_database(output)


@click.command()
@click.option('--db', 'connection_string', required=True, help='Database connection string')
@click.option('--input', required=True, help='Path to the backup file')
def restore(connection_string, input):
    """Restore the database from a backup file."""
    manager = DBManager(connection_string)
    manager.restore_database(input)


# Add commands to the db group
db.add_command(query)
db.add_command(list_tables, name='list-tables')
db.add_command(migrate)
db.add_command(backup)
db.add_command(restore)
