"""
Executive Analytics - Data Loader

Purpose:
- Collect
- Clean
- Normalize

company-wide data so it can be safely used by:
- trend_analysis
- correlation
- dashboards

This module MUST NOT:
- make decisions
- create charts
- forecast the future
"""

from typing import Dict
import pandas as pd


# -----------------------------
# Helper normalization functions
# -----------------------------

def _normalize_time_series(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure the dataframe has a proper datetime index
    and is sorted by time.
    """
    if "date" not in df.columns:
        raise ValueError("DataFrame must contain a 'date' column")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    return df


# -----------------------------
# Sector-specific loaders
# -----------------------------

def _load_finance_data(company) -> pd.DataFrame:
    """
    Load finance-related historical data.
    """
    df = pd.DataFrame(company.finance_history)
    return _normalize_time_series(df)


def _load_sales_data(company) -> pd.DataFrame:
    """
    Load sales-related historical data.
    """
    df = pd.DataFrame(company.sales_history)
    return _normalize_time_series(df)


def _load_hr_data(company) -> pd.DataFrame:
    """
    Load HR-related historical data.
    """
    df = pd.DataFrame(company.hr_history)
    return _normalize_time_series(df)


def _load_delivery_data(company) -> pd.DataFrame:
    """
    Load software delivery / engineering data.
    """
    df = pd.DataFrame(company.delivery_history)
    return _normalize_time_series(df)


def _load_support_data(company) -> pd.DataFrame:
    """
    Load customer support data.
    """
    df = pd.DataFrame(company.support_history)
    return _normalize_time_series(df)


# -----------------------------
# Public API (THIS is what others call)
# -----------------------------

def load_executive_data(company) -> Dict[str, pd.DataFrame]:
    """
    Central entry point for executive analytics data.

    Returns:
        dict[str, pd.DataFrame]
        {
            "finance": DataFrame,
            "sales": DataFrame,
            "hr": DataFrame,
            "delivery": DataFrame,
            "support": DataFrame
        }
    """
    return {
        "finance": _load_finance_data(company),
        "sales": _load_sales_data(company),
        "hr": _load_hr_data(company),
        "delivery": _load_delivery_data(company),
        "support": _load_support_data(company),
    }
