"""
inspection_rules.py

Version : 1.0.0

Reusable inspection functions.

Rules:
- Pure functions only
- No database
- No file reading
- No printing
- No side effects

Author:
Chief Architect
"""

from typing import Optional

from schemas.common.data_contract import (
    TimeFields,
    UnderlyingFields,
    OptionFields
)

import pandas as pd


# ==========================================================
# BASIC INFORMATION
# ==========================================================

def row_count(df: pd.DataFrame) -> int:
    return len(df)


def column_count(df: pd.DataFrame) -> int:
    return len(df.columns)


def column_names(df: pd.DataFrame) -> list[str]:
    return list(df.columns)


def data_types(df: pd.DataFrame) -> dict:
    return {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }


# ==========================================================
# DATA QUALITY
# ==========================================================

def missing_values(df: pd.DataFrame) -> int:
    return int(df.isnull().sum().sum())


def missing_values_by_column(df: pd.DataFrame) -> dict:

    return (
        df.isnull()
        .sum()
        .to_dict()
    )


def duplicate_rows(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())


def memory_usage_mb(df: pd.DataFrame) -> float:

    return round(

        df.memory_usage(deep=True).sum()

        / 1024

        / 1024,

        2

    )


# ==========================================================
# COLUMN DETECTION
# ==========================================================

def has_column(
    df: pd.DataFrame,
    column: str
) -> bool:

    return column in df.columns


def detect_timestamp_column(
    df: pd.DataFrame
) -> Optional[str]:

    candidates = [

        TimeFields.TIMESTAMP

    ]

    for column in candidates:

        if column in df.columns:
            return column

    return None


# ==========================================================
# TIME ANALYSIS
# ==========================================================

def first_timestamp(df: pd.DataFrame):

    column = detect_timestamp_column(df)

    if column is None:
        return None

    return df[column].min()


def last_timestamp(df: pd.DataFrame):

    column = detect_timestamp_column(df)

    if column is None:
        return None

    return df[column].max()


def unique_dates(df: pd.DataFrame):

    column = detect_timestamp_column(df)

    if column is None:
        return None

    return df[column].nunique()


# ==========================================================
# OPTION DATASET DETECTION
# ==========================================================

def strike_count(df: pd.DataFrame):

    if OptionFields.STRIKE not in df.columns:
        return None

    return df[OptionFields.STRIKE].nunique()


def expiry_count(df: pd.DataFrame):

    if OptionFields.EXPIRY not in df.columns:
        return None

    return df[OptionFields.EXPIRY].nunique()


def option_types(df: pd.DataFrame):

    if OptionFields.OPTION_TYPE not in df.columns:
        return None

    return sorted(
        df[OptionFields.OPTION_TYPE]
        .dropna()
        .unique()
        .tolist()
    )


def underlying(df: pd.DataFrame):

    if UnderlyingFields.UNDERLYING not in df.columns:
        return None

    values = (

        df[UnderlyingFields.UNDERLYING]

        .dropna()

        .unique()

    )

    if len(values) == 0:
        return None

    return values[0]


# ==========================================================
# PRICE INFORMATION
# ==========================================================

def price_columns(df: pd.DataFrame):

    keywords = [

        UnderlyingFields.OPEN,

        UnderlyingFields.HIGH,

        UnderlyingFields.LOW,

        UnderlyingFields.CLOSE,

        UnderlyingFields.LTP

    ]

    columns = []

    for column in df.columns:

        for keyword in keywords:

            if column == keyword:

                columns.append(column)

                break

    return columns


# ==========================================================
# SUMMARY
# ==========================================================

def dataset_summary(df: pd.DataFrame):

    """
    Complete inspection summary.

    Returns dictionary.
    """

    return {

        "rows": row_count(df),

        "columns": column_count(df),

        "column_names": column_names(df),

        "data_types": data_types(df),

        "missing_values": missing_values(df),

        "missing_by_column": missing_values_by_column(df),

        "duplicate_rows": duplicate_rows(df),

        "memory_mb": memory_usage_mb(df),

        "first_timestamp": first_timestamp(df),

        "last_timestamp": last_timestamp(df),

        "unique_dates": unique_dates(df),

        "strike_count": strike_count(df),

        "expiry_count": expiry_count(df),

        "option_types": option_types(df),

        "underlying": underlying(df),

        "price_columns": price_columns(df)

    }