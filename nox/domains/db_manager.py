from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


class DBManager:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine = create_engine(self.connection_string)

    def run_query(self, query: str) -> list:
        """Run a SQL query on the database."""
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query))
                # Check if the query returns rows
                if result.returns_rows:
                    return result.fetchall()
                else:
                    connection.commit()
                    print('Query executed successfully.')
                    return []
        except SQLAlchemyError as e:
            print(f"Error running query: {e}")
            return []

    def list_tables(self) -> list:
        """List tables in the database."""
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        return self.run_query(query)

    def run_migration(self, migration_path: str):
        """Run a SQL migration file."""
        try:
            with open(migration_path) as file:
                migration_sql = file.read()
                self.run_query(migration_sql)
                print(f"Migration from {migration_path} applied successfully.")
        except FileNotFoundError:
            print(f"Migration file {migration_path} not found.")
        except SQLAlchemyError as e:
            print(f"Error applying migration: {e}")

    def backup_database(self, output_file: str):
        """Backup the database to a file."""
        # Implementation would depend on the type of database (PostgreSQL, MySQL, etc.)
        print('Backup functionality is database-specific and needs implementation.')

    def restore_database(self, input_file: str):
        """Restore the database from a backup file."""
        # Implementation would depend on the type of database (PostgreSQL, MySQL, etc.)
        print('Restore functionality is database-specific and needs implementation.')
