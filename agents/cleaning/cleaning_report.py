"""
cleaning_report.py

Version : 1.0.0

Cleaning Report Generator

Purpose
-------
Generates TXT and JSON reports for
the Cleaning Engine.

Responsibilities
----------------
1. Generate TXT report
2. Generate JSON report
3. No cleaning logic
4. No database operations
"""

import json
from pathlib import Path

from config.cleaning_config import REPORT_DIRECTORY
from schemas.cleaning_schema import CleaningResult


class CleaningReport:

    def __init__(self):

        REPORT_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )

    # ==========================================================
    # TXT REPORT
    # ==========================================================

    def save_txt(
        self,
        result: CleaningResult
    ) -> Path:

        file_path = (
            REPORT_DIRECTORY /
            f"{result.dataset_name}.txt"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as report:

            report.write("=" * 60 + "\n")
            report.write("DATASET CLEANING REPORT\n")
            report.write("=" * 60 + "\n\n")

            report.write(
                f"Dataset : {result.dataset_name}\n"
            )

            report.write(
                f"Cleaning Time : {result.cleaning_time}\n"
            )

            report.write(
                f"Status : {result.status.value}\n\n"
            )

            report.write("SUMMARY\n")
            report.write("-" * 60 + "\n")

            report.write(
                f"Rows Before           : {result.summary.rows_before}\n"
            )

            report.write(
                f"Rows After            : {result.summary.rows_after}\n"
            )

            report.write(
                f"Duplicates Removed    : {result.summary.duplicates_removed}\n"
            )

            report.write(
                f"Null Rows Removed     : {result.summary.null_rows_removed}\n"
            )

            report.write(
                f"Null Columns Removed  : {result.summary.null_columns_removed}\n"
            )

            report.write(
                f"Columns Standardized  : {result.summary.columns_standardized}\n"
            )

            report.write(
                f"Data Types Converted  : {result.summary.data_types_converted}\n"
            )

            report.write("\n")

            report.write("CLEANING ACTIONS\n")
            report.write("-" * 60 + "\n")

            if not result.issues:

                report.write(
                    "No cleaning actions were required.\n"
                )

            else:

                for issue in result.issues:

                    report.write(
                        f"[{issue.action.value}] "
                        f"{issue.message}\n"
                    )

                    if issue.affected_rows:

                        report.write(
                            f"Affected Rows : {issue.affected_rows}\n"
                        )

                    if issue.affected_columns:

                        report.write(
                            "Affected Columns : "
                        )

                        report.write(
                            ", ".join(issue.affected_columns)
                        )

                        report.write("\n")

                    report.write("\n")

        return file_path

    # ==========================================================
    # JSON REPORT
    # ==========================================================

    def save_json(
        self,
        result: CleaningResult
    ) -> Path:

        file_path = (
            REPORT_DIRECTORY /
            f"{result.dataset_name}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as report:

            json.dump(

                result.model_dump(
                    mode="json"
                ),

                report,

                indent=4,

                ensure_ascii=False

            )

        return file_path