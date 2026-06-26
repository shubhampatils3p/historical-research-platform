"""
validation_report.py

Version : 1.0.0

Validation Report Generator

Purpose
-------
Generates validation reports in
TXT and JSON format.

Responsibilities
----------------
- Generate TXT report
- Generate JSON report
- No validation logic
- No database operations
"""

from pathlib import Path
import json

from config.storage_contract import VALIDATION_REPORTS
from schemas.validation_schema import ValidationResult


class ValidationReport:

    def __init__(self):

        VALIDATION_REPORTS.mkdir(
            parents=True,
            exist_ok=True
        )

    # ==========================================================
    # TXT REPORT
    # ==========================================================

    def save_txt(
        self,
        result: ValidationResult
    ) -> Path:

        file_path = (
            VALIDATION_REPORTS /
            f"{result.dataset_name}.txt"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as report:

            report.write("=" * 60 + "\n")
            report.write("DATASET VALIDATION REPORT\n")
            report.write("=" * 60 + "\n\n")

            report.write(
                f"Dataset : {result.dataset_name}\n"
            )

            report.write(
                f"Validation Time : {result.validation_time}\n"
            )

            report.write(
                f"Status : {result.status.value}\n\n"
            )

            report.write("SUMMARY\n")
            report.write("-" * 60 + "\n")

            report.write(
                f"Total Records      : {result.summary.total_records}\n"
            )

            report.write(
                f"Passed Records     : {result.summary.passed_records}\n"
            )

            report.write(
                f"Failed Records     : {result.summary.failed_records}\n"
            )

            report.write(
                f"Warning Records    : {result.summary.warning_records}\n"
            )

            report.write(
                f"Duplicate Records  : {result.summary.duplicate_records}\n"
            )

            report.write(
                f"Null Records       : {result.summary.null_records}\n"
            )

            report.write("\n")

            report.write("VALIDATION ISSUES\n")
            report.write("-" * 60 + "\n")

            if not result.issues:

                report.write("No validation issues found.\n")

            else:

                for issue in result.issues:

                    report.write(
                        f"[{issue.severity.value.upper()}] "
                        f"{issue.rule} : "
                        f"{issue.message}\n"
                    )

                    if issue.field:

                        report.write(
                            f"Field : {issue.field}\n"
                        )

                    if issue.row_number is not None:

                        report.write(
                            f"Row : {issue.row_number}\n"
                        )

                    report.write("\n")

        return file_path

    # ==========================================================
    # JSON REPORT
    # ==========================================================

    def save_json(
        self,
        result: ValidationResult
    ) -> Path:

        file_path = (
            VALIDATION_REPORTS /
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