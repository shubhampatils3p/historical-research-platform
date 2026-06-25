"""
dataset_repository.py

Version : 2.0.0

Repository for dataset registry.

Author:
Chief Architect
"""

from datetime import datetime

from database.database_manager import DatabaseManager


class DatasetRepository:

    def __init__(self):

        self.db = DatabaseManager()

        self.db.create_tables()

    # ==========================================================
    # CREATE
    # ==========================================================

    def insert_dataset(
        self,
        dataset_name,
        file_name,
        file_path,
        extension,
        size_bytes,
        created_at,
        modified_at,
        status="registered",
        rows=0,
        columns=0
    ):

        self.db.execute(
            """
            INSERT OR REPLACE INTO dataset_registry
            (
                file_path,
                dataset_name,
                file_name,
                extension,
                size_bytes,
                created_at,
                modified_at,
                status,
                rows,
                columns
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_path,
                dataset_name,
                file_name,
                extension,
                size_bytes,
                created_at,
                modified_at,
                status,
                rows,
                columns
            )
        )

    # ==========================================================
    # READ
    # ==========================================================

    def get_all(self):

        return self.db.execute(
            """
            SELECT *
            FROM dataset_registry
            ORDER BY dataset_name
            """
        ).fetchall()

    def dataset_exists(self, file_path):

        result = self.db.execute(
            """
            SELECT COUNT(*)
            FROM dataset_registry
            WHERE file_path = ?
            """,
            (file_path,)
        ).fetchone()

        return result[0] > 0

    def get_uninspected_datasets(self):

        return self.db.execute(
            """
            SELECT *
            FROM dataset_registry
            WHERE status IN ('registered', 'failed')
            ORDER BY dataset_name
            """
        ).fetchall()

    def get_inspected_datasets(self):

        return self.db.execute(
            """
            SELECT *
            FROM dataset_registry
            WHERE status='inspected'
            """
        ).fetchall()

    # ==========================================================
    # UPDATE
    # ==========================================================

    def update_status( 
        self,
        file_path, 
        status, 
    ):

        self.db.execute(
            """
            UPDATE dataset_registry
            SET 
                status=?
            WHERE file_path=?
            """, 
            (
                status,
                file_path,
            )
        )

    def update_inspection(
        self,
        file_path,
        rows,
        columns
    ):

        self.db.execute(
            """
            UPDATE dataset_registry
            SET
                rows=?,
                columns=?,
                status='inspected'
            WHERE file_path=?
            """,
            (
                rows,
                columns,
                file_path
            )
        )

    def mark_validated(self, file_path):

        self.db.execute(
            """
            UPDATE dataset_registry
            SET status='validated'
            WHERE file_path=?
            """,
            (file_path,)
        )

    def mark_cleaned(self, file_path):

        self.db.execute(
            """
            UPDATE dataset_registry
            SET status='cleaned'
            WHERE file_path=?
            """,
            (file_path,)
        )

    def mark_feature_generated(self, file_path):

        self.db.execute(
            """
            UPDATE dataset_registry
            SET status='feature_generated'
            WHERE file_path=?
            """,
            (file_path,)
        )

    # ==========================================================
    # DELETE
    # ==========================================================

    def delete_dataset(self, file_path):

        self.db.execute(
            """
            DELETE FROM dataset_registry
            WHERE file_path=?
            """,
            (file_path,)
        )

    def delete_all(self):

        self.db.execute(
            """
            DELETE FROM dataset_registry
            """
        )

    # ==========================================================
    # STATS
    # ==========================================================

    def count(self):

        result = self.db.execute(
            """
            SELECT COUNT(*)
            FROM dataset_registry
            """
        ).fetchone()

        return result[0]

    def status_summary(self):

        return self.db.execute(
            """
            SELECT
                status,
                COUNT(*)
            FROM dataset_registry
            GROUP BY status
            ORDER BY status
            """
        ).fetchall()

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def close(self):

        self.db.close()