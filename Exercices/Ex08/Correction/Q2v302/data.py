
# Imports regroupés
import pandas as pd
import plotly.express as px

def load_data():
    """Charge et retourne les datasets nécessaires à l'application."""
    stocks = px.data.stocks()
    stocks["date"] = pd.to_datetime(stocks["date"], format="%Y-%m-%d")

    gap = px.data.gapminder()
    gap = (
        gap.groupby(["year", "continent"])
        .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
        .reset_index()
    )

    return stocks, gap, stocks["date"].min(), stocks["date"].max()
