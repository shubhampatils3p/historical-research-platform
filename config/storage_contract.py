"""
storage_contract.py

Version : 1.0.0

Defines the complete storage layout of the
Historical Research Platform.

This is the only place where folder paths are defined.
"""

from pathlib import Path


# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==========================================================
# STORAGE ROOT
# ==========================================================

STORAGE_ROOT = PROJECT_ROOT / "storage"


# ==========================================================
# RAW DATA
# ==========================================================

RAW_DATA = STORAGE_ROOT / "raw"


RAW_INDEX = RAW_DATA / "index"

RAW_OPTIONS = RAW_DATA / "options"

RAW_OPTION_CHAIN = RAW_DATA / "option_chain"

RAW_VIX = RAW_DATA / "vix"


# ==========================================================
# VALIDATED
# ==========================================================

VALIDATED_DATA = STORAGE_ROOT / "validated"


# ==========================================================
# CLEANED
# ==========================================================

CLEANED_DATA = STORAGE_ROOT / "cleaned"


# ==========================================================
# FEATURES
# ==========================================================

FEATURE_STORE = STORAGE_ROOT / "features"


# ==========================================================
# DATABASE
# ==========================================================

DATABASE = STORAGE_ROOT / "database"

DUCKDB_DATABASE = DATABASE / "research.duckdb"


# ==========================================================
# REPORTS
# ==========================================================

REPORTS = PROJECT_ROOT / "reports"

VALIDATION_REPORTS = REPORTS / "validation"

DISCOVERY_REPORTS = REPORTS / "discovery"

FEATURE_REPORTS = REPORTS / "features"

INSPECTION_REPORTS = REPORTS / "inspection"


# ==========================================================
# LOGS
# ==========================================================

LOGS = PROJECT_ROOT / "logs"


# ==========================================================
# CREATE DIRECTORIES
# ==========================================================

DIRECTORIES = [

    RAW_DATA,

    RAW_INDEX,

    RAW_OPTIONS,

    RAW_OPTION_CHAIN,

    RAW_VIX,

    VALIDATED_DATA,

    CLEANED_DATA,

    FEATURE_STORE,

    DATABASE,

    REPORTS,

    VALIDATION_REPORTS,

    DISCOVERY_REPORTS,

    FEATURE_REPORTS,
    
    INSPECTION_REPORTS,

    LOGS

]


def create_project_structure():

    """
    Creates complete folder hierarchy.
    """

    for directory in DIRECTORIES:
        directory.mkdir(
            parents=True,
            exist_ok=True
        )