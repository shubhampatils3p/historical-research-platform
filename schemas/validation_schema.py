"""
validation_schema.py

Version : 1.0.0

Validation models for the Historical Research Platform.

Purpose
-------
Defines the standard format used by every validator.

No validation logic should exist in this file.
Only schemas.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# VALIDATION STATUS
# ==========================================================

class ValidationStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    WARNING = "warning"
    SKIPPED = "skipped"


# ==========================================================
# VALIDATION SEVERITY
# ==========================================================

class ValidationSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


# ==========================================================
# VALIDATION ERROR
# ==========================================================

class ValidationIssue(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    rule: str

    severity: ValidationSeverity

    message: str

    field: Optional[str] = None

    row_number: Optional[int] = None

    expected: Optional[str] = None

    actual: Optional[str] = None


# ==========================================================
# VALIDATION SUMMARY
# ==========================================================

class ValidationSummary(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    total_records: int

    passed_records: int

    failed_records: int

    warning_records: int

    duplicate_records: int

    null_records: int


# ==========================================================
# DATASET VALIDATION RESULT
# ==========================================================

class ValidationResult(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    dataset_name: str

    validation_time: datetime

    status: ValidationStatus

    summary: ValidationSummary

    issues: List[ValidationIssue]


# ==========================================================
# STANDARD VALIDATION RULES
# ==========================================================

class ValidationRules(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    timestamp_continuity: bool = True

    duplicate_check: bool = True

    null_check: bool = True

    primary_key_check: bool = True

    data_type_check: bool = True

    strike_validation: bool = True

    expiry_validation: bool = True

    ohlc_validation: bool = True

    oi_validation: bool = True

    volume_validation: bool = True

    price_validation: bool = True


# ==========================================================
# VALIDATION REPORT
# ==========================================================

class ValidationReport(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    validator_version: str

    dataset_version: str

    result: ValidationResult