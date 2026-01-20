"""Data loading utilities."""
import pandas as pd
import plotly.express as px

# Stocks dataset
stocks_df = px.data.stocks()
stocks_df["date"] = pd.to_datetime(stocks_df["date"], format="%Y-%m-%d")
MIN_DATE = stocks_df["date"].min().date()
MAX_DATE = stocks_df["date"].max().date()
MIN_TS = stocks_df["date"].min()
MAX_TS = stocks_df["date"].max()

# Gapminder aggregated dataset
gapminder_df = px.data.gapminder()
gapminder_df = (
    gapminder_df.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)


def load_stocks():
    """Return the prepared stocks dataframe."""
    return stocks_df


def load_gapminder():
    """Return the aggregated gapminder dataframe."""
    return gapminder_df
