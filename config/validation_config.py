"""
validation_config.py

Version : 1.0.0

Central configuration for the Validation Engine.

Purpose
-------
Defines which validation rules are enabled.

No validation logic should exist in this file.
"""

# ==========================================================
# VALIDATION ENGINE
# ==========================================================

VALIDATION_ENGINE_VERSION = "1.0.0"


# ==========================================================
# CORE VALIDATIONS
# ==========================================================

ENABLE_EMPTY_FILE_CHECK = True

ENABLE_REQUIRED_COLUMNS_CHECK = True

ENABLE_DUPLICATE_ROWS_CHECK = True

ENABLE_DUPLICATE_TIMESTAMP_CHECK = True

ENABLE_NULL_CHECK = True

ENABLE_DATA_TYPE_CHECK = True


# ==========================================================
# MARKET DATA VALIDATIONS
# ==========================================================

ENABLE_OHLC_VALIDATION = True

ENABLE_VOLUME_VALIDATION = True

ENABLE_PRICE_VALIDATION = True


# ==========================================================
# OPTION DATA VALIDATIONS
# ==========================================================

ENABLE_STRIKE_VALIDATION = True

ENABLE_EXPIRY_VALIDATION = True

ENABLE_OPTION_TYPE_VALIDATION = True

ENABLE_OI_VALIDATION = True


# ==========================================================
# TIME VALIDATIONS
# ==========================================================

ENABLE_TIMESTAMP_CONTINUITY = True

ENABLE_SESSION_VALIDATION = True

ENABLE_WEEKEND_VALIDATION = True


# ==========================================================
# RESEARCH VALIDATIONS
# ==========================================================

ENABLE_OUTLIER_CHECK = True

ENABLE_GAP_DETECTION = True


# ==========================================================
# REPORTING
# ==========================================================

GENERATE_JSON_REPORT = True

GENERATE_TEXT_REPORT = True

SAVE_VALIDATION_RESULTS = True


# ==========================================================
# FAIL FAST
# ==========================================================

STOP_ON_CRITICAL_ERROR = False