"""Helper utilities for charts and formatting."""
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from config import TICKERS, CHART_TEMPLATE, BADGE_COLOR
from data import MIN_TS, MAX_TS


def make_stocks_fig(df_slice: pd.DataFrame):
    """Create a line chart for the selected tickers."""
    return px.line(df_slice, x="date", y=TICKERS, template=CHART_TEMPLATE)


def fmt_date(ts: pd.Timestamp) -> str:
    """Format timestamp as DD-MMM-YYYY."""
    return ts.date().strftime("%d-%b-%Y")


def make_badges(start_dt, end_dt):
    """Create start/end date badges."""
    BADGE_SHADOW_STYLE = {"boxShadow": "0 2px 8px rgba(0,0,0,0.15)"}
    return [
        dbc.Badge(f"Start: {fmt_date(start_dt)}", color=BADGE_COLOR, style=BADGE_SHADOW_STYLE),
        dbc.Badge(f"End: {fmt_date(end_dt)}", color=BADGE_COLOR, style=BADGE_SHADOW_STYLE),
    ]


def normalize_range(start_date, end_date):
    """
    Normalize date range, handling None values and swapping if reversed.
    
    Args:
        start_date: Start date string or None
        end_date: End date string or None
        
    Returns:
        Tuple of (start_dt, end_dt) as Pandas Timestamps
    """
    start_dt = pd.to_datetime(start_date) if start_date else MIN_TS
    end_dt = pd.to_datetime(end_date) if end_date else MAX_TS
    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt, end_dt
