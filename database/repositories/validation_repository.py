"""
validation_repository.py

Version : 1.0.0

Repository for validation results.
"""

from database.database_manager import DatabaseManager


class ValidationRepository:

    def __init__(self):

        self.db = DatabaseManager()

        self.db.create_tables()

    # ==========================================================
    # SAVE
    # ==========================================================

    def save_result(
        self,
        dataset_name,
        file_path,
        validation_time,
        validation_status,
        total_records,
        passed_records,
        failed_records,
        warning_records,
        duplicate_records,
        null_records,
        total_issues,
        report_path
    ):

        self.db.execute(
            """
            INSERT OR REPLACE INTO validation_results
            (
                dataset_name,
                file_path,
                validation_time,
                validation_status,
                total_records,
                passed_records,
                failed_records,
                warning_records,
                duplicate_records,
                null_records,
                total_issues,
                report_path
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dataset_name,
                file_path,
                validation_time,
                validation_status,
                total_records,
                passed_records,
                failed_records,
                warning_records,
                duplicate_records,
                null_records,
                total_issues,
                report_path
            )
        )

    # ==========================================================
    # READ
    # ==========================================================

    def get_all(self):

        return self.db.execute(
            """
            SELECT *
            FROM validation_results
            ORDER BY validation_time DESC
            """
        ).fetchall()

    def get_by_file(self, file_path):

        return self.db.execute(
            """
            SELECT *
            FROM validation_results
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
            DELETE FROM validation_results
            WHERE file_path = ?
            """,
            (file_path,)
        )

    def delete_all(self):

        self.db.execute(
            """
            DELETE FROM validation_results
            """
        )

    # ==========================================================
    # STATS
    # ==========================================================

    def count(self):

        result = self.db.execute(
            """
            SELECT COUNT(*)
            FROM validation_results
            """
        ).fetchone()

        return result[0]

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def close(self):

        self.db.close()