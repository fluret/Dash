"""Configuration constants for Q2v3 app."""
from datetime import date
import dash_bootstrap_components as dbc

THEME = dbc.themes.BOOTSTRAP
CHART_TEMPLATE = "plotly_dark"
TICKERS = ["GOOG", "AAPL"]
DEFAULT_START = date(2018, 5, 1)
DEFAULT_END = date(2019, 2, 1)
CHART_HEIGHT = "50vh"
GAPMINDER_CHART_HEIGHT = "70vh"
BADGE_COLOR = "secondary"

METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
