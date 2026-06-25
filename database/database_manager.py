"""
database_manager.py

Version : 1.0.0

Central database manager for the Historical Research Platform.

All database operations must go through this class.

Database : DuckDB
"""

from pathlib import Path

import duckdb

from config.storage_contract import DUCKDB_DATABASE
from database.database_schema import TABLES

class DatabaseManager:

    def __init__(self):

        self.database_path = Path(DUCKDB_DATABASE)

        self.connection = None

    # ---------------------------------------------------------

    def connect(self):

        if self.connection is None:

            self.connection = duckdb.connect(
                str(self.database_path)
            )

        return self.connection

    # ---------------------------------------------------------

    def disconnect(self):

        if self.connection is not None:

            self.connection.close()

            self.connection = None

    # ---------------------------------------------------------

    def execute(self, query, parameters=None):

        conn = self.connect()

        if parameters is None:

            return conn.execute(query)

        return conn.execute(query, parameters)

    # ---------------------------------------------------------

    def create_tables(self):

        """
        Creates all core system tables.
        """

        conn = self.connect()

        # ---------------------------------------------
        # DATASET REGISTRY
        # ---------------------------------------------

        for query in TABLES.values():
            
            conn.execute(query)
    # ---------------------------------------------------------

    def vacuum(self):

        self.execute("VACUUM")

    # ---------------------------------------------------------

    def close(self):

        self.disconnect()