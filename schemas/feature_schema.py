"""
feature_schema.py

Version : 1.0.0

Canonical Feature Schema

Represents engineered features generated
from historical market data.

No feature calculation logic belongs here.

Author:
Chief Architect
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# FEATURE METADATA
# ==========================================================

class FeatureMetadata(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    feature_engine_version: str

    generated_at: datetime

    timeframe: str

    source_dataset: str


# ==========================================================
# TREND FEATURES
# ==========================================================

class TrendFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    ema9: Optional[float] = None

    ema20: Optional[float] = None

    ema50: Optional[float] = None

    ema100: Optional[float] = None

    ema200: Optional[float] = None

    supertrend: Optional[float] = None

    trend: Optional[str] = None


# ==========================================================
# MOMENTUM FEATURES
# ==========================================================

class MomentumFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    rsi: Optional[float] = None

    adx: Optional[float] = None

    momentum: Optional[float] = None

    atr: Optional[float] = None

    vwap: Optional[float] = None


# ==========================================================
# OPTION FEATURES
# ==========================================================

class OptionFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    pcr: Optional[float] = None

    iv_ce: Optional[float] = None

    iv_pe: Optional[float] = None

    ce_delta: Optional[float] = None

    pe_delta: Optional[float] = None

    ce_gamma: Optional[float] = None

    pe_gamma: Optional[float] = None

    ce_theta: Optional[float] = None

    pe_theta: Optional[float] = None

    ce_vega: Optional[float] = None

    pe_vega: Optional[float] = None


# ==========================================================
# VOLATILITY FEATURES
# ==========================================================

class VolatilityFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    india_vix: Optional[float] = None

    historical_volatility: Optional[float] = None

    realized_volatility: Optional[float] = None

    volatility_regime: Optional[str] = None


# ==========================================================
# MARKET REGIME
# ==========================================================

class MarketRegimeFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    regime: Optional[str] = None

    confidence: Optional[float] = None

    is_trending: Optional[bool] = None

    is_ranging: Optional[bool] = None

    is_breakout: Optional[bool] = None

    is_expiry_day: Optional[bool] = None


# ==========================================================
# AI FEATURES
# ==========================================================

class AIFeatures(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )

    signal_score: Optional[float] = None

    edge_score: Optional[float] = None

    market_score: Optional[float] = None

    confidence_score: Optional[float] = None


# ==========================================================
# FEATURE SNAPSHOT
# ==========================================================

class FeatureSnapshot(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    version: str = Field(default="1.0")

    metadata: FeatureMetadata

    trend: TrendFeatures

    momentum: MomentumFeatures

    options: OptionFeatures

    volatility: VolatilityFeatures

    regime: MarketRegimeFeatures

    ai: AIFeatures