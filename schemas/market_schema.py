"""
market_schema.py

Version : 1.0.0

Purpose
-------
Defines the canonical market snapshot schema used throughout the
Historical Research Platform.

This schema represents ONE timestamp of market data.

Author:
Chief Architect

Rules:
- Immutable historical snapshot
- Strong typing
- Pydantic validation
- AI-friendly
"""

from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# TIME
# ==========================================================

class TimeSnapshot(BaseModel):
    """Time related information."""

    model_config = ConfigDict(frozen=True)

    timestamp: datetime
    trading_date: date
    trading_time: str

    year: int
    month: int
    week: int
    weekday: str

    session: str

    days_to_expiry: int

    is_expiry: bool
    is_weekly_expiry: bool
    is_monthly_expiry: bool


# ==========================================================
# UNDERLYING INDEX
# ==========================================================

class UnderlyingSnapshot(BaseModel):
    """Underlying index information."""

    model_config = ConfigDict(frozen=True)

    exchange: str
    segment: str

    underlying: str

    index_open: float
    index_high: float
    index_low: float
    index_close: float

    index_ltp: float

    previous_close: float

    index_volume: Optional[int] = None

    gap: Optional[float] = None
    gap_percent: Optional[float] = None


# ==========================================================
# VOLATILITY
# ==========================================================

class VolatilitySnapshot(BaseModel):
    """Market volatility snapshot."""

    model_config = ConfigDict(frozen=True)

    india_vix: Optional[float] = None

    historical_volatility: Optional[float] = None

    realized_volatility: Optional[float] = None


# ==========================================================
# MARKET SNAPSHOT
# ==========================================================

class MarketSnapshot(BaseModel):
    """
    Represents complete market information
    excluding option contract data.

    Option data is stored separately.
    """

    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True,
        extra="forbid"
    )

    version: str = Field(default="1.0")

    time: TimeSnapshot

    underlying: UnderlyingSnapshot

    volatility: VolatilitySnapshot


# ==========================================================
# FILE METADATA
# ==========================================================

class DatasetMetadata(BaseModel):
    """Metadata describing a historical dataset."""

    model_config = ConfigDict(frozen=True)

    source_name: str

    source_type: str

    downloaded_at: datetime

    dataset_version: str

    exchange: str

    segment: str

    start_date: date

    end_date: date

    resolution: str

    checksum: Optional[str] = None


# ==========================================================
# ROOT OBJECT
# ==========================================================

class MarketDataFile(BaseModel):
    """
    Complete market data file.

    One metadata object.

    Multiple market snapshots.
    """

    model_config = ConfigDict(extra="forbid")

    metadata: DatasetMetadata

    records: list[MarketSnapshot]