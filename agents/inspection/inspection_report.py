"""
inspection_report.py

Version : 1.0.0

Dataset Inspection Report Builder

Converts inspection results into
human-readable reports.

Author:
Chief Architect
"""

from datetime import datetime
from pathlib import Path
import json


class InspectionReport:

    def __init__(self, summary: dict):

        self.summary = summary

    # ======================================================
    # CONSOLE REPORT
    # ======================================================

    def to_console(self):

        print(self.to_text())

    # ======================================================
    # TEXT REPORT
    # ======================================================

    def to_text(self):

        lines = []

        lines.append("=" * 70)
        lines.append("DATASET INSPECTION REPORT")
        lines.append("=" * 70)

        lines.append("")
        lines.append(f"Generated At : {datetime.now()}")
        lines.append("")

        lines.append("GENERAL")
        lines.append("-" * 70)

        lines.append(f"Rows              : {self.summary.get('rows')}")
        lines.append(f"Columns           : {self.summary.get('columns')}")
        lines.append(f"Memory (MB)       : {self.summary.get('memory_mb')}")

        lines.append("")
        lines.append("QUALITY")
        lines.append("-" * 70)

        lines.append(f"Missing Values    : {self.summary.get('missing_values')}")
        lines.append(f"Duplicate Rows    : {self.summary.get('duplicate_rows')}")

        lines.append("")
        lines.append("TIME")
        lines.append("-" * 70)

        lines.append(f"First Timestamp   : {self.summary.get('first_timestamp')}")
        lines.append(f"Last Timestamp    : {self.summary.get('last_timestamp')}")
        lines.append(f"Unique Dates      : {self.summary.get('unique_dates')}")

        lines.append("")
        lines.append("OPTION DATA")
        lines.append("-" * 70)

        lines.append(f"Underlying        : {self.summary.get('underlying')}")
        lines.append(f"Strike Count      : {self.summary.get('strike_count')}")
        lines.append(f"Expiry Count      : {self.summary.get('expiry_count')}")
        lines.append(f"Option Types      : {self.summary.get('option_types')}")

        lines.append("")
        lines.append("PRICE COLUMNS")
        lines.append("-" * 70)

        for column in self.summary.get("price_columns", []):
            lines.append(f"  • {column}")

        lines.append("")
        lines.append("COLUMN NAMES")
        lines.append("-" * 70)

        for column in self.summary.get("column_names", []):
            lines.append(f"  • {column}")

        lines.append("")
        lines.append("DATA TYPES")
        lines.append("-" * 70)

        for column, dtype in self.summary.get("data_types", {}).items():
            lines.append(f"{column:<30} {dtype}")

        lines.append("")
        lines.append("MISSING VALUES BY COLUMN")
        lines.append("-" * 70)

        for column, value in self.summary.get("missing_by_column", {}).items():
            lines.append(f"{column:<30} {value}")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    # ======================================================
    # JSON REPORT
    # ======================================================

    def to_json(self):

        return json.dumps(
            self.summary,
            indent=4,
            default=str
        )

    # ======================================================
    # SAVE JSON
    # ======================================================

    def save_json(self, path):

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as fp:

            json.dump(
                self.summary,
                fp,
                indent=4,
                default=str
            )

        return path

    # ======================================================
    # SAVE TEXT
    # ======================================================

    def save_text(self, path):

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as fp:

            fp.write(self.to_text())

        return path