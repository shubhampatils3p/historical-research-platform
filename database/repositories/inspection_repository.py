"""
inspection_repository.py

Version : 1.1.0

Repository for inspection results.
"""

from database.database_manager import DatabaseManager


class InspectionRepository:

    def __init__(self):

        self.db = DatabaseManager()

        self.db.create_tables()

    # ==========================================================
    # SAVE
    # ==========================================================

    def save_result(
        self,
        file_path,
        row_count,
        column_count,
        missing_values,
        duplicate_rows,
        memory_mb,
        first_timestamp,
        last_timestamp,
        inspection_time,
    ):

        self.db.execute(
            """
            INSERT OR REPLACE INTO inspection_results
            (
                file_path,
                inspected_at,
                row_count,
                column_count,
                missing_values,
                duplicate_rows,
                inspection_status,
                memory_mb,
                first_timestamp,
                last_timestamp
            )
            VALUES
            (?, ?, ?, ?, ?, ?, 'completed', ?, ?, ?)
            """,
            (
                file_path,
                inspection_time,
                row_count,
                column_count,
                missing_values,
                duplicate_rows,
                memory_mb,
                first_timestamp,
                last_timestamp,
            )
        )

    # ==========================================================
    # READ
    # ==========================================================

    def get_all(self):

        return self.db.execute(
            """
            SELECT *
            FROM inspection_results
            ORDER BY inspected_at DESC
            """
        ).fetchall()

    def get_by_file(self, file_path):

        return self.db.execute(
            """
            SELECT *
            FROM inspection_results
            WHERE file_path = ?
            """,
            (file_path,)
        ).fetchone()

    # ==========================================================
    # DELETE
    # ==========================================================

    def delete(self, file_path):

        self.db.execute(
            """
            DELETE FROM inspection_results
            WHERE file_path = ?
            """,
            (file_path,)
        )

    def delete_all(self):

        self.db.execute(
            """
            DELETE FROM inspection_results
            """
        )

    # ==========================================================
    # STATS
    # ==========================================================

    def count(self):

        result = self.db.execute(
            """
            SELECT COUNT(*)
            FROM inspection_results
            """
        ).fetchone()

        return result[0]

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def close(self):

        self.db.close()