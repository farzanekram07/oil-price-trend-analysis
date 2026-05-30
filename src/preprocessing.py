import pandas as pd


def clean_wti_data(df):
    """
    Clean WTI crude oil dataset.
    """

    # Flatten MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Remove Adj Close if present
    if "Adj Close" in df.columns:
        df = df.drop(columns=["Adj Close"])

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Sort by date
    df = df.sort_index()

    return df
