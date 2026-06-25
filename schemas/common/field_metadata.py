"""
Field Metadata v1.0

This file defines metadata for every canonical field in the project.

Purpose
-------
- Discovery Agent
- Downloader Agent
- Validator Agent
- Cleaner Agent
- Database Builder
- Feature Engineering
- AI Research Engine

Never hardcode field properties anywhere else.
"""

from schemas.common.data_contract import *


# ==========================================================
# PRIORITY LEVELS
# ==========================================================

P0 = "P0"  # Mandatory
P1 = "P1"  # Strongly Recommended
P2 = "P2"  # Optional
P3 = "P3"  # Future


# ==========================================================
# SOURCES
# ==========================================================

HISTORICAL = "historical"
DERIVED = "derived"
LIVE = "live"


# ==========================================================
# FIELD METADATA
# ==========================================================

FIELD_METADATA = {

    # ======================================================
    # TIME
    # ======================================================

    TimeFields.TIMESTAMP: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "datetime"
    },

    TimeFields.TRADING_DATE: {
        "priority": P0,
        "required": True,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "date"
    },

    TimeFields.TRADING_TIME: {
        "priority": P0,
        "required": True,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "time"
    },

    TimeFields.DAYS_TO_EXPIRY: {
        "priority": P0,
        "required": True,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "int"
    },

    # ======================================================
    # UNDERLYING
    # ======================================================

    UnderlyingFields.OPEN: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    UnderlyingFields.HIGH: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    UnderlyingFields.LOW: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    UnderlyingFields.CLOSE: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    UnderlyingFields.VOLUME: {
        "priority": P1,
        "required": False,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "int"
    },

    # ======================================================
    # OPTION
    # ======================================================

    OptionFields.STRIKE: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "int"
    },

    OptionFields.EXPIRY: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "date"
    },

    OptionFields.OPTION_TYPE: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "str"
    },

    # ======================================================
    # OPTION PRICE
    # ======================================================

    PriceFields.CE_OPEN: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.CE_HIGH: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.CE_LOW: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.CE_CLOSE: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.PE_OPEN: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.PE_HIGH: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.PE_LOW: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    PriceFields.PE_CLOSE: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    # ======================================================
    # OPEN INTEREST
    # ======================================================

    OIFields.CE_OI: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "int"
    },

    OIFields.PE_OI: {
        "priority": P0,
        "required": True,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "int"
    },

    OIFields.CE_OI_CHANGE: {
        "priority": P1,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "int"
    },

    OIFields.PE_OI_CHANGE: {
        "priority": P1,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "int"
    },

    # ======================================================
    # VOLATILITY
    # ======================================================

    VolatilityFields.IV_CE: {
        "priority": P1,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    VolatilityFields.IV_PE: {
        "priority": P1,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    VolatilityFields.VIX: {
        "priority": P1,
        "required": False,
        "recoverable": False,
        "source": HISTORICAL,
        "dtype": "float"
    },

    # ======================================================
    # GREEKS
    # ======================================================

    GreeksFields.CE_DELTA: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    GreeksFields.PE_DELTA: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    GreeksFields.CE_GAMMA: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    GreeksFields.PE_GAMMA: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    # ======================================================
    # OPTION CHAIN
    # ======================================================

    OptionChainFields.PCR: {
        "priority": P1,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    # ======================================================
    # DERIVED FEATURES
    # ======================================================

    DerivedFields.EMA20: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    DerivedFields.ATR: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    DerivedFields.RSI: {
        "priority": P2,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "float"
    },

    DerivedFields.MARKET_REGIME: {
        "priority": P3,
        "required": False,
        "recoverable": True,
        "source": DERIVED,
        "dtype": "str"
    },
}


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def get_metadata(field_name: str):
    return FIELD_METADATA.get(field_name)


def is_required(field_name: str):
    meta = get_metadata(field_name)
    return meta["required"] if meta else False


def is_recoverable(field_name: str):
    meta = get_metadata(field_name)
    return meta["recoverable"] if meta else False


def get_priority(field_name: str):
    meta = get_metadata(field_name)
    return meta["priority"] if meta else None


def get_source(field_name: str):
    meta = get_metadata(field_name)
    return meta["source"] if meta else None


def get_dtype(field_name: str):
    meta = get_metadata(field_name)
    return meta["dtype"] if meta else None