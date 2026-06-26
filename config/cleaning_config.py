"""
cleaning_config.py

Version : 1.0.0

Configuration for the Cleaning Engine.

Purpose
-------
Centralized configuration used by all cleaning rules.

No cleaning logic should exist in this file.
Only configuration values.
"""

from pathlib import Path


# ==========================================================
# ENGINE
# ==========================================================

CLEANING_ENGINE_VERSION = "1.0.0"


# ==========================================================
# OUTPUT
# ==========================================================

SAVE_CLEANED_DATASET = True

OVERWRITE_EXISTING = True

EXPORT_FORMAT = "csv"


# ==========================================================
# STORAGE
# ==========================================================

RAW_DATASET_DIRECTORY = Path(
    "storage/raw"
)

CLEANED_DATASET_DIRECTORY = Path(
    "storage/cleaned"
)

REPORT_DIRECTORY = Path(
    "reports/cleaning"
)


# ==========================================================
# DUPLICATES
# ==========================================================

REMOVE_DUPLICATE_ROWS = True

KEEP_DUPLICATE = "first"


# ==========================================================
# NULL VALUES
# ==========================================================

REMOVE_EMPTY_ROWS = True

REMOVE_EMPTY_COLUMNS = True

NULL_THRESHOLD = 1.0


# ==========================================================
# COLUMN STANDARDIZATION
# ==========================================================

STANDARDIZE_COLUMN_NAMES = True

CONVERT_TO_LOWERCASE = True

REPLACE_SPACES = True

SPACE_REPLACEMENT = "_"

STRIP_COLUMN_NAMES = True


# ==========================================================
# SORTING
# ==========================================================

SORT_BY_TIMESTAMP = True

TIMESTAMP_ASCENDING = True


# ==========================================================
# DATA TYPES
# ==========================================================

AUTO_CONVERT_TYPES = True

CONVERT_NUMERIC_COLUMNS = True

CONVERT_TIMESTAMP_COLUMNS = True


# ==========================================================
# LOGGING
# ==========================================================

VERBOSE = True