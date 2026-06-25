"""
settings.py

Global project configuration.

This is the ONLY place where project level settings
should be defined.
"""

from pathlib import Path
from enum import Enum


# ==========================================================
# PROJECT INFO
# ==========================================================

PROJECT_NAME = "Historical Research Platform"

PROJECT_VERSION = "0.1.0"

AUTHOR = "Shubham Patil"


# ==========================================================
# ENVIRONMENT
# ==========================================================

class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


CURRENT_ENVIRONMENT = Environment.DEVELOPMENT


# ==========================================================
# DATABASE
# ==========================================================

DATABASE_NAME = "research.duckdb"

PARQUET_COMPRESSION = "zstd"


# ==========================================================
# LOGGING
# ==========================================================

LOG_LEVEL = "INFO"

ENABLE_CONSOLE_LOG = True

ENABLE_FILE_LOG = True


# ==========================================================
# DATA
# ==========================================================

DEFAULT_TIMEFRAME = "1minute"

DEFAULT_EXCHANGE = "NSE"

DEFAULT_SEGMENT = "NFO"

DEFAULT_UNDERLYING = "NIFTY"


# ==========================================================
# VALIDATION
# ==========================================================

STRICT_VALIDATION = True

ALLOW_DUPLICATES = False

ALLOW_NULLS = False


# ==========================================================
# FEATURE ENGINE
# ==========================================================

GENERATE_FEATURES = True

GENERATE_MARKET_REGIME = True

GENERATE_AI_FEATURES = False


# ==========================================================
# DOWNLOAD
# ==========================================================

MAX_RETRIES = 3

DOWNLOAD_TIMEOUT = 60


# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent