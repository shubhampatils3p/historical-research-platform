"""
option_schema.py

Version : 1.0.0

Canonical Option Contract Schema

Represents ONE option contract
for ONE timestamp.

Author:
Chief Architect
"""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# CONTRACT INFORMATION
# ==========================================================

class OptionContract(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    exchange: str

    segment: str

    underlying: str

    expiry: date

    strike: int

    option_type: str

    symbol: str

    token: Optional[str] = None

    lot_size: Optional[int] = None


# ==========================================================
# PRICE
# ==========================================================

class OptionPrice(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    open: float

    high: float

    low: float

    close: float

    ltp: float


# ==========================================================
# VOLUME
# ==========================================================

class VolumeSnapshot(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    volume: Optional[int] = None

    cumulative_volume: Optional[int] = None

    volume_delta: Optional[int] = None


# ==========================================================
# OPEN INTEREST
# ==========================================================

class OISnapshot(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    open_interest: Optional[int] = None

    oi_change: Optional[int] = None

    oi_change_percent: Optional[float] = None


# ==========================================================
# IMPLIED VOLATILITY
# ==========================================================

class IVSnapshot(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    implied_volatility: Optional[float] = None


# ==========================================================
# GREEKS
# ==========================================================

class GreeksSnapshot(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    delta: Optional[float] = None

    gamma: Optional[float] = None

    theta: Optional[float] = None

    vega: Optional[float] = None

    rho: Optional[float] = None


# ==========================================================
# OPTION SNAPSHOT
# ==========================================================

class OptionSnapshot(BaseModel):

    """
    Represents one option contract
    at one timestamp.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    version: str = Field(default="1.0")

    contract: OptionContract

    price: OptionPrice

    volume: VolumeSnapshot

    oi: OISnapshot

    iv: IVSnapshot

    greeks: GreeksSnapshot