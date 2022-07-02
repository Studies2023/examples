from datetime import datetime

import pandas as pd

from src.schema import DataSchema


def get_year_options(transactions: pd.DataFrame) -> list[dict[str, str]]:
    available_years: set[str] = set(transactions.loc[:, DataSchema.YEAR.value])
    return [{"label": i, "value": i} for i in available_years]


def get_month_options(transactions: pd.DataFrame) -> list[dict[str, str]]:
    available_months: set[str] = set(transactions.loc[:, DataSchema.MONTH.value])
    return [{"label": i, "value": i} for i in available_months]


def get_category_options(transactions: pd.DataFrame) -> list[dict[str, str]]:
    categories = get_category_values(transactions)
    base_options = [{"label": i, "value": i} for i in categories]
    filtered_options = filter(lambda option: not pd.isna(option["label"]), base_options)
    final_options = sorted(filtered_options, key=lambda x: x["label"])
    return final_options


def get_category_values(transactions: pd.DataFrame) -> list[str]:
    categories = transactions.loc[:, DataSchema.CATEGORY.value].unique()
    return sorted(filter(lambda category: not pd.isna(category), categories))


def get_year_values() -> list[str]:
    return [str(datetime.now().year)]


def get_month_values() -> list[str]:
    return [datetime.now().strftime("%m-%b")]
