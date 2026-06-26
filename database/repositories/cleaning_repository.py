"""
cleaning_repository.py

Version : 1.0.0

Repository for cleaning results.
"""

from database.database_manager import DatabaseManager


class CleaningRepository:

    def __init__(self):

        self.db = DatabaseManager()

        self.db.create_tables()

    # ==========================================================
    # SAVE
    # ==========================================================

    def save_result(
        self,
        file_path,
        cleaning_time,
        cleaning_status,
        rows_before,
        rows_after,
        duplicates_removed,
        null_rows_removed,
        null_columns_removed,
        columns_standardized,
        data_types_converted,
        output_path
    ):

        self.db.execute(
            """
            INSERT OR REPLACE INTO cleaning_results
            (
                file_path,
                cleaned_at,
                cleaning_status,
                rows_before,
                rows_after,
                duplicates_removed,
                null_rows_removed,
                null_columns_removed,
                columns_standardized,
                data_types_converted,
                output_path
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_path,
                cleaning_time,
                cleaning_status,
                rows_before,
                rows_after,
                duplicates_removed,
                null_rows_removed,
                null_columns_removed,
                columns_standardized,
                data_types_converted,
                output_path
            )
        )

    # ==========================================================
    # READ
    # ==========================================================

    def get_all(self):

        return self.db.execute(
            """
            SELECT *
            FROM cleaning_results
            ORDER BY cleaned_at DESC
            """
        ).fetchall()

    def get_by_file(self, file_path):

        return self.db.execute(
            """
            SELECT *
            FROM cleaning_results
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
            DELETE FROM cleaning_results
            WHERE file_path = ?
            """,
            (file_path,)
        )

    def delete_all(self):

        self.db.execute(
            """
            DELETE FROM cleaning_results
            """
        )

    # ==========================================================
    # STATS
    # ==========================================================

    def count(self):

        result = self.db.execute(
            """
            SELECT COUNT(*)
            FROM cleaning_results
            """
        ).fetchone()

        return result[0]

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def close(self):

        self.db.close()