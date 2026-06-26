"""
validation_rules.py

Version : 1.0.0

Validation Engine

Purpose
-------
Contains all dataset validation rules.

Responsibilities
----------------
- Validate dataframe quality
- Return ValidationIssue objects
- No database operations
- No report generation
- No file writing
"""

from typing import List
from datetime import datetime
import pandas as pd

from schemas.validation_schema import (
    ValidationIssue,
    ValidationSeverity
)

from schemas.common.data_contract import (
    TimeFields,
    UnderlyingFields
)

from schemas.validation_schema import (
    ValidationIssue,
    ValidationResult,
    ValidationSummary,
    ValidationStatus,
    ValidationSeverity
)


class ValidationRules:

    """
    Collection of reusable validation rules.
    """

    # ==========================================================
    # EMPTY DATASET
    # ==========================================================

    @staticmethod
    def check_empty_dataset(df: pd.DataFrame) -> List[ValidationIssue]:

        issues = []

        if df.empty:

            issues.append(

                ValidationIssue(

                    rule="empty_dataset",

                    severity=ValidationSeverity.CRITICAL,

                    message="Dataset contains no records."

                )

            )

        return issues

    # ==========================================================
    # REQUIRED COLUMNS
    # ==========================================================

    @staticmethod
    def check_required_columns(
        df: pd.DataFrame,
        required_columns: list[str]
    ) -> List[ValidationIssue]:

        issues = []

        missing = [

            column

            for column in required_columns

            if column not in df.columns

        ]

        if missing:

            issues.append(

                ValidationIssue(

                    rule="required_columns",

                    severity=ValidationSeverity.CRITICAL,

                    message=f"Missing required columns: {', '.join(missing)}"

                )

            )

        return issues

    # ==========================================================
    # DUPLICATE ROWS
    # ==========================================================

    @staticmethod
    def check_duplicate_rows(
        df: pd.DataFrame
    ) -> List[ValidationIssue]:

        issues = []

        duplicates = int(df.duplicated().sum())

        if duplicates > 0:

            issues.append(

                ValidationIssue(

                    rule="duplicate_rows",

                    severity=ValidationSeverity.WARNING,

                    message=f"{duplicates} duplicate rows found."

                )

            )

        return issues

    # ==========================================================
    # NULL VALUES
    # ==========================================================

    @staticmethod
    def check_null_values(
        df: pd.DataFrame
    ) -> List[ValidationIssue]:

        issues = []

        for column in df.columns:

            null_count = int(df[column].isna().sum())

            if null_count > 0:

                issues.append(

                    ValidationIssue(

                        rule="null_values",

                        severity=ValidationSeverity.WARNING,

                        message=f"{null_count} null values found.",

                        field=column

                    )

                )

        return issues

    # ==========================================================
    # DUPLICATE TIMESTAMP
    # ==========================================================

    @staticmethod
    def check_duplicate_timestamp(
        df: pd.DataFrame,
        timestamp_column: str = TimeFields.TIMESTAMP
    ) -> List[ValidationIssue]:

        issues = []

        if timestamp_column not in df.columns:

            return issues

        duplicates = int(

            df[timestamp_column].duplicated().sum()

        )

        if duplicates > 0:

            issues.append(

                ValidationIssue(

                    rule="duplicate_timestamp",

                    severity=ValidationSeverity.ERROR,

                    message=f"{duplicates} duplicate timestamps found.",

                    field=timestamp_column

                )

            )

        return issues

    # ==========================================================
    # TIMESTAMP SORTING
    # ==========================================================

    @staticmethod
    def check_timestamp_order(
        df: pd.DataFrame,
        timestamp_column: str = TimeFields.TIMESTAMP
    ) -> List[ValidationIssue]:

        issues = []

        if timestamp_column not in df.columns:

            return issues

        timestamps = pd.to_datetime(df[timestamp_column])

        if not timestamps.is_monotonic_increasing:

            issues.append(

                ValidationIssue(

                    rule="timestamp_order",

                    severity=ValidationSeverity.ERROR,

                    message="Timestamp column is not sorted.",

                    field=timestamp_column

                )

            )

        return issues

    # ==========================================================
    # OHLC VALIDATION
    # ==========================================================

    @staticmethod
    def check_ohlc(
        df: pd.DataFrame
    ) -> List[ValidationIssue]:

        issues = []

        required = [

            UnderlyingFields.OPEN,

            UnderlyingFields.HIGH,

            UnderlyingFields.LOW,

            UnderlyingFields.CLOSE

        ]

        if not all(

            column in df.columns

            for column in required

        ):

            return issues

        invalid = df[
            (df[UnderlyingFields.HIGH] < df[UnderlyingFields.OPEN]) |
            (df[UnderlyingFields.HIGH] < df[UnderlyingFields.CLOSE]) |
            (df[UnderlyingFields.HIGH] < df[UnderlyingFields.LOW]) |
            (df[UnderlyingFields.LOW] > df[UnderlyingFields.OPEN]) |
            (df[UnderlyingFields.LOW] > df[UnderlyingFields.CLOSE])
        ]

        if not invalid.empty:

            issues.append(

                ValidationIssue(

                    rule="ohlc_validation",

                    severity=ValidationSeverity.ERROR,

                    message=f"{len(invalid)} invalid OHLC rows."

                )

            )

        return issues

    # ==========================================================
    # POSITIVE PRICE
    # ==========================================================

    @staticmethod
    def check_positive_prices(
        df: pd.DataFrame
    ) -> List[ValidationIssue]:

        issues = []

        price_columns = [

            column

            for column in [

                UnderlyingFields.OPEN,

                UnderlyingFields.HIGH,

                UnderlyingFields.LOW,

                UnderlyingFields.CLOSE

            ]

            if column in df.columns

        ]

        for column in price_columns:

            invalid = int(

                (df[column] <= 0).sum()

            )

            if invalid > 0:

                issues.append(

                    ValidationIssue(

                        rule="positive_price",

                        severity=ValidationSeverity.ERROR,

                        message=f"{invalid} invalid prices.",

                        field=column

                    )

                )

        return issues

    # ==========================================================
    # POSITIVE VOLUME
    # ==========================================================

    @staticmethod
    def check_volume(
        df: pd.DataFrame,
        volume_column: str = UnderlyingFields.VOLUME
    ) -> List[ValidationIssue]:

        issues = []

        if volume_column not in df.columns:

            return issues

        invalid = int(

            (df[volume_column] < 0).sum()

        )

        if invalid > 0:

            issues.append(

                ValidationIssue(

                    rule="volume_validation",

                    severity=ValidationSeverity.ERROR,

                    message=f"{invalid} invalid volume values.",

                    field=volume_column

                )

            )

        return issues
    
    @staticmethod
    def validate_dataset(
        df: pd.DataFrame,
        dataset_name: str
    ) -> ValidationResult:

        issues = []

        # ------------------------------------------------------
        # Execute All Validation Rules
        # ------------------------------------------------------

        issues.extend(
            ValidationRules.check_empty_dataset(df)
        )

        issues.extend(
            ValidationRules.check_duplicate_rows(df)
        )

        issues.extend(
            ValidationRules.check_null_values(df)
        )

        issues.extend(
            ValidationRules.check_duplicate_timestamp(df)
        )

        issues.extend(
            ValidationRules.check_timestamp_order(df)
        )

        issues.extend(
            ValidationRules.check_ohlc(df)
        )

        issues.extend(
            ValidationRules.check_positive_prices(df)
        )

        issues.extend(
            ValidationRules.check_volume(df)
        )

        # ------------------------------------------------------
        # Summary
        # ------------------------------------------------------

        total_records = len(df)

        duplicate_records = int(df.duplicated().sum())

        null_records = int(df.isna().sum().sum())

        warning_records = sum(
            1
            for issue in issues
            if issue.severity == ValidationSeverity.WARNING
        )

        failed_records = sum(
            1
            for issue in issues
            if issue.severity in (
                ValidationSeverity.ERROR,
                ValidationSeverity.CRITICAL
            )
        )

        passed_records = max(
            total_records - failed_records,
            0
        )

        summary = ValidationSummary(

            total_records=total_records,

            passed_records=passed_records,

            failed_records=failed_records,

            warning_records=warning_records,

            duplicate_records=duplicate_records,

            null_records=null_records

        )

        # ------------------------------------------------------
        # Status
        # ------------------------------------------------------

        if failed_records > 0:

            status = ValidationStatus.FAILED

        elif warning_records > 0:

            status = ValidationStatus.WARNING

        else:

            status = ValidationStatus.PASSED

        # ------------------------------------------------------
        # Result
        # ------------------------------------------------------

        return ValidationResult(

            dataset_name=dataset_name,

            validation_time=datetime.now(),

            status=status,

            summary=summary,

            issues=issues

        )