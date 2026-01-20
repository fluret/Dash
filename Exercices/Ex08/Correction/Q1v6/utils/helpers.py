"""
Utility helper functions.
"""
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from data import MIN_TS, MAX_TS
from config import TICKERS, CHART_TEMPLATE, BADGE_COLOR


def normalize_range(start_date, end_date):
    """Return (start, end) timestamps with bounds fallback and swap if inverted."""
    start_dt = pd.to_datetime(start_date) if start_date else MIN_TS
    end_dt = pd.to_datetime(end_date) if end_date else MAX_TS
    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt, end_dt


def fmt_date(ts: pd.Timestamp) -> str:
    """Format timestamp as DD-MMM-YYYY."""
    return ts.date().strftime("%d-%b-%Y")


def make_fig(df_slice: pd.DataFrame):
    """Helper to create a line chart for the selected tickers."""
    fig = px.line(df_slice, x="date", y=TICKERS, template=CHART_TEMPLATE)
    return fig


def make_badges(start_dt, end_dt):
    """Return two badges with formatted start/end dates."""
    return [
        dbc.Badge(f"Start: {fmt_date(start_dt)}", color=BADGE_COLOR),
        dbc.Badge(f"End: {fmt_date(end_dt)}", color=BADGE_COLOR),
    ]
