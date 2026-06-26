"""
cleaning_schema.py

Version : 1.0.0

Cleaning models for the Historical Research Platform.

Purpose
-------
Defines the standard models used by the Cleaning Engine.

No cleaning logic should exist in this file.
Only schemas.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# CLEANING STATUS
# ==========================================================

class CleaningStatus(str, Enum):

    COMPLETED = "completed"

    PARTIAL = "partial"

    FAILED = "failed"

    SKIPPED = "skipped"


# ==========================================================
# CLEANING ACTION
# ==========================================================

class CleaningAction(str, Enum):

    DUPLICATES_REMOVED = "duplicates_removed"

    NULL_ROWS_REMOVED = "null_rows_removed"

    NULL_COLUMNS_REMOVED = "null_columns_removed"

    COLUMN_NAMES_STANDARDIZED = "column_names_standardized"

    TIMESTAMP_SORTED = "timestamp_sorted"

    DATA_TYPES_CONVERTED = "data_types_converted"


# ==========================================================
# CLEANING ISSUE
# ==========================================================

class CleaningIssue(BaseModel):

    model_config = ConfigDict(

        frozen=True,

        extra="forbid"

    )

    action: CleaningAction

    message: str

    affected_rows: int = 0

    affected_columns: Optional[List[str]] = None


# ==========================================================
# CLEANING SUMMARY
# ==========================================================

class CleaningSummary(BaseModel):

    model_config = ConfigDict(

        frozen=True,

        extra="forbid"

    )

    rows_before: int

    rows_after: int

    duplicates_removed: int

    null_rows_removed: int

    null_columns_removed: int

    columns_standardized: int

    data_types_converted: int


# ==========================================================
# CLEANING RESULT
# ==========================================================

class CleaningResult(BaseModel):

    model_config = ConfigDict(

        extra="forbid"

    )

    dataset_name: str

    cleaning_time: datetime

    status: CleaningStatus

    summary: CleaningSummary

    issues: List[CleaningIssue]


# ==========================================================
# CLEANING CONFIG
# ==========================================================

class CleaningRules(BaseModel):

    model_config = ConfigDict(

        frozen=True,

        extra="forbid"

    )

    remove_duplicates: bool = True

    remove_empty_rows: bool = True

    remove_empty_columns: bool = True

    standardize_column_names: bool = True

    sort_timestamp: bool = True

    convert_data_types: bool = True


# ==========================================================
# CLEANING REPORT
# ==========================================================

class CleaningReport(BaseModel):

    model_config = ConfigDict(

        extra="forbid"

    )

    cleaner_version: str

    dataset_version: str

    result: CleaningResult