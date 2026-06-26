"""
cleaning_rules.py

Version : 1.0.0

Cleaning Engine

Business logic for dataset cleaning.

Responsibilities
----------------
1. Remove duplicate rows
2. Remove empty rows
3. Remove empty columns
4. Standardize column names
5. Sort timestamps
6. Convert data types
"""

from datetime import datetime

import pandas as pd

from config.cleaning_config import (
    REMOVE_DUPLICATE_ROWS,
    KEEP_DUPLICATE,
    REMOVE_EMPTY_ROWS,
    REMOVE_EMPTY_COLUMNS,
    STANDARDIZE_COLUMN_NAMES,
    CONVERT_TO_LOWERCASE,
    REPLACE_SPACES,
    SPACE_REPLACEMENT,
    STRIP_COLUMN_NAMES,
    SORT_BY_TIMESTAMP,
    TIMESTAMP_ASCENDING,
    AUTO_CONVERT_TYPES,
    CONVERT_NUMERIC_COLUMNS,
    CONVERT_TIMESTAMP_COLUMNS,
)

from schemas.common.data_contract import (
    TimeFields,
)

from schemas.cleaning_schema import (
    CleaningAction,
    CleaningIssue,
    CleaningSummary,
    CleaningResult,
    CleaningStatus,
)


class CleaningRules:

    # ==========================================================
    # Remove Duplicate Rows
    # ==========================================================

    @staticmethod
    def _remove_duplicate_rows(df):

        before = len(df)

        if REMOVE_DUPLICATE_ROWS:

            df = df.drop_duplicates(
                keep=KEEP_DUPLICATE
            )

        removed = before - len(df)

        return df, removed

    # ==========================================================
    # Remove Empty Rows
    # ==========================================================

    @staticmethod
    def _remove_empty_rows(df):

        before = len(df)

        if REMOVE_EMPTY_ROWS:

            df = df.dropna(
                how="all"
            )

        removed = before - len(df)

        return df, removed

    # ==========================================================
    # Remove Empty Columns
    # ==========================================================

    @staticmethod
    def _remove_empty_columns(df):

        before = len(df.columns)

        removed_columns = []

        if REMOVE_EMPTY_COLUMNS:

            removed_columns = list(
                df.columns[
                    df.isna().all()
                ]
            )

            df = df.dropna(
                axis=1,
                how="all"
            )

        removed = before - len(df.columns)

        return df, removed, removed_columns

    # ==========================================================
    # Standardize Column Names
    # ==========================================================

    @staticmethod
    def _standardize_column_names(df):

        before = list(df.columns)

        if STANDARDIZE_COLUMN_NAMES:

            columns = []

            for column in df.columns:

                name = str(column)

                if STRIP_COLUMN_NAMES:

                    name = name.strip()

                if CONVERT_TO_LOWERCASE:

                    name = name.lower()

                if REPLACE_SPACES:

                    name = name.replace(
                        " ",
                        SPACE_REPLACEMENT
                    )

                columns.append(name)

            df.columns = columns

        changed = sum(

            1

            for old, new in zip(before, df.columns)

            if old != new

        )

        return df, changed
    
    # ==========================================================
    # Sort Timestamp
    # ==========================================================

    @staticmethod
    def _sort_timestamp(df):

        if not SORT_BY_TIMESTAMP:

            return df

        if TimeFields.TIMESTAMP not in df.columns:

            return df

        df = df.sort_values(

            by=TimeFields.TIMESTAMP,

            ascending=TIMESTAMP_ASCENDING

        )

        df = df.reset_index(drop=True)

        return df

    # ==========================================================
    # Convert Data Types
    # ==========================================================

    @staticmethod
    def _convert_data_types(df):

        converted = 0

        if not AUTO_CONVERT_TYPES:

            return df, converted

        for column in df.columns:

            original_dtype = df[column].dtype

            try:

                if (
                    CONVERT_TIMESTAMP_COLUMNS
                    and
                    column == TimeFields.TIMESTAMP
                ):

                    df[column] = pd.to_datetime(
                        df[column],
                        errors="ignore"
                    )

                elif CONVERT_NUMERIC_COLUMNS:

                    df[column] = pd.to_numeric(
                        df[column],
                        errors="ignore"
                    )

                if df[column].dtype != original_dtype:

                    converted += 1

            except Exception:

                continue

        return df, converted

    # ==========================================================
    # Clean Dataset
    # ==========================================================

    @staticmethod
    def clean_dataset(

        dataframe: pd.DataFrame,

        dataset_name: str

    ) -> CleaningResult:

        df = dataframe.copy()

        issues = []

        rows_before = len(df)

        # ------------------------------------------------------

        df, duplicates_removed = (
            CleaningRules._remove_duplicate_rows(df)
        )

        if duplicates_removed > 0:

            issues.append(

                CleaningIssue(

                    action=CleaningAction.DUPLICATES_REMOVED,

                    message=f"{duplicates_removed} duplicate rows removed.",

                    affected_rows=duplicates_removed

                )

            )

        # ------------------------------------------------------

        df, null_rows_removed = (
            CleaningRules._remove_empty_rows(df)
        )

        if null_rows_removed > 0:

            issues.append(

                CleaningIssue(

                    action=CleaningAction.NULL_ROWS_REMOVED,

                    message=f"{null_rows_removed} empty rows removed.",

                    affected_rows=null_rows_removed

                )

            )

        # ------------------------------------------------------

        (
            df,
            null_columns_removed,
            removed_columns

        ) = CleaningRules._remove_empty_columns(df)

        if null_columns_removed > 0:

            issues.append(

                CleaningIssue(

                    action=CleaningAction.NULL_COLUMNS_REMOVED,

                    message=f"{null_columns_removed} empty columns removed.",

                    affected_columns=removed_columns

                )

            )

        # ------------------------------------------------------

        df, standardized = (

            CleaningRules._standardize_column_names(df)

        )

        if standardized > 0:

            issues.append(

                CleaningIssue(

                    action=CleaningAction.COLUMN_NAMES_STANDARDIZED,

                    message=f"{standardized} column names standardized."

                )

            )

        # ------------------------------------------------------

        df = CleaningRules._sort_timestamp(df)

        # ------------------------------------------------------

        df, converted = (

            CleaningRules._convert_data_types(df)

        )

        if converted > 0:

            issues.append(

                CleaningIssue(

                    action=CleaningAction.DATA_TYPES_CONVERTED,

                    message=f"{converted} columns converted."

                )

            )

        # ------------------------------------------------------

        summary = CleaningSummary(

            rows_before=rows_before,

            rows_after=len(df),

            duplicates_removed=duplicates_removed,

            null_rows_removed=null_rows_removed,

            null_columns_removed=null_columns_removed,

            columns_standardized=standardized,

            data_types_converted=converted

        )

        # ------------------------------------------------------

        status = CleaningStatus.COMPLETED

        if len(df) == 0:

            status = CleaningStatus.FAILED

        elif len(issues) > 0:

            status = CleaningStatus.PARTIAL

        # ------------------------------------------------------

        result = CleaningResult(

            dataset_name=dataset_name,

            cleaning_time=datetime.now(),

            status=status,

            summary=summary,

            issues=issues

        )

        return result, df