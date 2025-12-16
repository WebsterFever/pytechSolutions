"""
Tests for Executive Analytics - data_loader.py

Purpose:
- Ensure executive data is loaded correctly
- Validate structure and basic integrity
"""

import pandas as pd

# Import the function under test
from acompany.aExecutive.analytics.data_loader import load_executive_data



# -----------------------------
# Mock Company for Testing
# -----------------------------

class MockCompany:
    def __init__(self):
        self.finance_history = [
            {"date": "2024-01-01", "revenue": 10000, "cost": 7000},
            {"date": "2024-02-01", "revenue": 12000, "cost": 8000},
        ]

        self.sales_history = [
            {"date": "2024-01-01", "leads": 50, "deals": 10},
            {"date": "2024-02-01", "leads": 65, "deals": 14},
        ]

        self.hr_history = [
            {"date": "2024-01-01", "employees": 10},
            {"date": "2024-02-01", "employees": 12},
        ]

        self.delivery_history = [
            {"date": "2024-01-01", "features": 3, "bugs": 5},
            {"date": "2024-02-01", "features": 5, "bugs": 4},
        ]

        self.support_history = [
            {"date": "2024-01-01", "tickets": 20},
            {"date": "2024-02-01", "tickets": 18},
        ]


# -----------------------------
# Tests
# -----------------------------

def test_load_executive_data_structure():
    company = MockCompany()
    data = load_executive_data(company)

    # Check keys
    expected_keys = {"finance", "sales", "hr", "delivery", "support"}
    assert set(data.keys()) == expected_keys


def test_all_outputs_are_dataframes():
    company = MockCompany()
    data = load_executive_data(company)

    for df in data.values():
        assert isinstance(df, pd.DataFrame)


def test_date_column_is_datetime():
    company = MockCompany()
    data = load_executive_data(company)

    for df in data.values():
        assert pd.api.types.is_datetime64_any_dtype(df["date"])


def test_data_is_sorted_by_date():
    company = MockCompany()
    data = load_executive_data(company)

    for df in data.values():
        assert df["date"].is_monotonic_increasing


# -----------------------------
# Manual run (optional)
# -----------------------------

if __name__ == "__main__":
    test_load_executive_data_structure()
    test_all_outputs_are_dataframes()
    test_date_column_is_datetime()
    test_data_is_sorted_by_date()

    print("✅ All data_loader tests passed")
