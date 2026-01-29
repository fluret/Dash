
"""
Utilitaires de chargement et de préparation des données pour Q2v5.
Inclut le chargement des jeux de données stocks et gapminder, avec cache.
"""

import pandas as pd
import plotly.express as px

# Stocks dataset (singleton)
_stocks_df = None
_gapminder_df = None

# Date constants
MIN_DATE = None
MAX_DATE = None
MIN_TS = None
MAX_TS = None


def load_stocks():
    """Return the prepared stocks dataframe (cached)."""
    global _stocks_df, MIN_DATE, MAX_DATE, MIN_TS, MAX_TS
    
    if _stocks_df is None:
        _stocks_df = px.data.stocks()
        _stocks_df["date"] = pd.to_datetime(_stocks_df["date"], format="%Y-%m-%d")
        MIN_DATE = _stocks_df["date"].min().date()
        MAX_DATE = _stocks_df["date"].max().date()
        MIN_TS = _stocks_df["date"].min()
        MAX_TS = _stocks_df["date"].max()
    
    return _stocks_df


def load_gapminder():
    """Return the aggregated gapminder dataframe (cached)."""
    global _gapminder_df
    
    if _gapminder_df is None:
        _gapminder_df = px.data.gapminder()
        _gapminder_df = (
            _gapminder_df.groupby(["year", "continent"])
            .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
            .reset_index()
        )
    
    return _gapminder_df


# Initialize data on module load
stocks_df = load_stocks()
gapminder_df = load_gapminder()
