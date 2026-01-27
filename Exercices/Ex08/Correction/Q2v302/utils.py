
# Imports regroupés
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from data import load_data

# Chargement des données et bornes
stocks_df, gapminder_df, MIN_TS, MAX_TS = load_data()
MIN_DATE, MAX_DATE = MIN_TS.date(), MAX_TS.date()

def get_header_style(COLOR_PRIMARY, COLOR_ACCENT):
    return {
        "padding": "18px 20px",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "justifyContent": "space-between",
        "background": f"linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%)",
        "borderRadius": "12px"
    }

def fmt_date(ts: pd.Timestamp) -> str:
    return ts.date().strftime("%d-%b-%Y")

def make_badges(start, end) -> list:
    return [
        dbc.Badge(f"Start: {fmt_date(start)}", color="secondary"),
        dbc.Badge(f"End: {fmt_date(end)}", color="secondary"),
    ]

def normalize_range(start, end) -> tuple:
    s = pd.to_datetime(start) if start else MIN_TS
    e = pd.to_datetime(end) if end else MAX_TS
    return (s, e) if s <= e else (e, s)

def make_stocks_fig(df: pd.DataFrame, CHART):
    if df.empty:
        df = pd.DataFrame({"date": [], **{t: [] for t in CHART["tickers"]}})
    return px.line(df, x="date", y=CHART["tickers"], template=CHART["template"])
