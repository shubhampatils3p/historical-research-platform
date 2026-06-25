"""
Master Data Contract v1.1

Single Source of Truth (SSOT) for all field names used across the
Historical Research Platform.

RULES
-----
1. Never hardcode column names anywhere else.
2. Every agent must import fields from this file.
3. Raw field names must never change without version increment.
"""

# ==========================================================
# TIME
# ==========================================================

class TimeFields:
    TIMESTAMP = "timestamp"
    TRADING_DATE = "trading_date"
    TRADING_TIME = "trading_time"

    YEAR = "year"
    MONTH = "month"
    WEEK = "week"
    WEEKDAY = "weekday"

    SESSION = "session"

    DAYS_TO_EXPIRY = "days_to_expiry"

    IS_EXPIRY = "is_expiry"
    IS_WEEKLY_EXPIRY = "is_weekly_expiry"
    IS_MONTHLY_EXPIRY = "is_monthly_expiry"


# ==========================================================
# UNDERLYING
# ==========================================================

class UnderlyingFields:

    EXCHANGE = "exchange"

    SEGMENT = "segment"

    UNDERLYING = "underlying"

    INDEX_NAME = "index_name"

    OPEN = "index_open"
    HIGH = "index_high"
    LOW = "index_low"
    CLOSE = "index_close"

    LTP = "index_ltp"

    PREVIOUS_CLOSE = "previous_close"

    VOLUME = "index_volume"

    GAP = "gap"
    GAP_PERCENT = "gap_percent"


# ==========================================================
# OPTION CONTRACT
# ==========================================================

class OptionFields:

    STRIKE = "strike"

    EXPIRY = "expiry"

    OPTION_TYPE = "option_type"

    CE_SYMBOL = "ce_symbol"
    PE_SYMBOL = "pe_symbol"

    ATM_DISTANCE = "atm_distance"


# ==========================================================
# OPTION PRICE
# ==========================================================

class PriceFields:

    CE_OPEN = "ce_open"
    CE_HIGH = "ce_high"
    CE_LOW = "ce_low"
    CE_CLOSE = "ce_close"

    PE_OPEN = "pe_open"
    PE_HIGH = "pe_high"
    PE_LOW = "pe_low"
    PE_CLOSE = "pe_close"


# ==========================================================
# VOLUME
# ==========================================================

class VolumeFields:

    CE_VOLUME = "ce_volume"
    PE_VOLUME = "pe_volume"

    CE_CUMULATIVE_VOLUME = "ce_cumulative_volume"
    PE_CUMULATIVE_VOLUME = "pe_cumulative_volume"

    CE_VOLUME_DELTA = "ce_volume_delta"
    PE_VOLUME_DELTA = "pe_volume_delta"


# ==========================================================
# OPEN INTEREST
# ==========================================================

class OIFields:

    CE_OI = "ce_open_interest"
    PE_OI = "pe_open_interest"

    CE_OI_CHANGE = "ce_oi_change"
    PE_OI_CHANGE = "pe_oi_change"

    TOTAL_CE_OI = "total_ce_oi"
    TOTAL_PE_OI = "total_pe_oi"


# ==========================================================
# VOLATILITY
# ==========================================================

class VolatilityFields:

    IV_CE = "iv_ce"
    IV_PE = "iv_pe"

    VIX = "vix"

    HISTORICAL_VOLATILITY = "historical_volatility"
    REALIZED_VOLATILITY = "realized_volatility"


# ==========================================================
# GREEKS
# ==========================================================

class GreeksFields:

    CE_DELTA = "ce_delta"
    PE_DELTA = "pe_delta"

    CE_GAMMA = "ce_gamma"
    PE_GAMMA = "pe_gamma"

    CE_THETA = "ce_theta"
    PE_THETA = "pe_theta"

    CE_VEGA = "ce_vega"
    PE_VEGA = "pe_vega"

    CE_RHO = "ce_rho"
    PE_RHO = "pe_rho"


# ==========================================================
# OPTION CHAIN
# ==========================================================

class OptionChainFields:

    PCR = "pcr"

    TOTAL_CALL_OI = "total_call_oi"
    TOTAL_PUT_OI = "total_put_oi"

    CALL_WRITING = "call_writing"
    PUT_WRITING = "put_writing"

    LONG_BUILDUP = "long_buildup"
    SHORT_BUILDUP = "short_buildup"

    LONG_UNWINDING = "long_unwinding"
    SHORT_COVERING = "short_covering"


# ==========================================================
# DERIVED FEATURES
# ==========================================================

class DerivedFields:

    EMA9 = "ema9"
    EMA20 = "ema20"
    EMA50 = "ema50"
    EMA100 = "ema100"
    EMA200 = "ema200"

    VWAP = "vwap"

    ATR = "atr"

    ADX = "adx"

    RSI = "rsi"

    SUPERTREND = "supertrend"

    TREND = "trend"

    MOMENTUM = "momentum"

    VOLATILITY_REGIME = "volatility_regime"

    MARKET_REGIME = "market_regime"


# ==========================================================
# TRADE LABELS
# ==========================================================

class TradeFields:

    SIGNAL = "signal"

    ENTRY = "entry"

    EXIT = "exit"

    STOP_LOSS = "stop_loss"

    TARGET = "target"

    PNL = "pnl"

    HOLDING_TIME = "holding_time"

    STRATEGY = "strategy"

    CONFIDENCE = "confidence"


# ==========================================================
# VALIDATION RULES
# ==========================================================

class ValidationRules:

    TIMESTAMP_CONTINUITY = "timestamp_continuity"

    OHLC_VALID = "ohlc_valid"

    OI_VALID = "oi_valid"

    VOLUME_VALID = "volume_valid"

    EXPIRY_VALID = "expiry_valid"

    STRIKE_VALID = "strike_valid"

    DUPLICATE_CHECK = "duplicate_check"

    NULL_CHECK = "null_check"

    PRICE_CHECK = "price_check"

    PRIMARY_KEY_CHECK = "primary_key_check"

    DATA_TYPE_CHECK = "data_type_check"


# ==========================================================
# MASTER REGISTRY
# ==========================================================

ALL_FIELDS = {
    "time": TimeFields,
    "underlying": UnderlyingFields,
    "option": OptionFields,
    "price": PriceFields,
    "volume": VolumeFields,
    "oi": OIFields,
    "volatility": VolatilityFields,
    "greeks": GreeksFields,
    "option_chain": OptionChainFields,
    "derived": DerivedFields,
    "trade": TradeFields,
    "validation": ValidationRules,
}