# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Import data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
title_ = dcc.Markdown(children="Exercice 8.1", style={"textAlign": "center", "fontSize": 20})
date_range_ = dcc.DatePickerRange(
    id="date-range",
    start_date_placeholder_text="start date",
    end_date_placeholder_text="end date",
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    start_date=date(2018, 5, 1),
    end_date=date(2019, 2, 1),
    display_format="DD-MMM-YYYY",
    first_day_of_week=1,
)
card_L = dbc.Card(dbc.CardBody([dcc.Graph(id="my-graph-left")]),)
card_C = dbc.Card(dbc.CardBody([dcc.Graph(id="my-graph-center")]),)
card_R = dbc.Card(dbc.CardBody([dcc.Graph(id="my-graph-right")]),)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([title_], width=12)),
        dbc.Row(dbc.Col([date_range_], width=12, style={"textAlign": "center"})),
        dbc.Row(
            [
                dbc.Col([card_L], width=4),
                dbc.Col([card_C], width=4),
                dbc.Col([card_R], width=4),
            ]
        ),
    ]
)

# Callbacks
@app.callback(
    Output("my-graph-left", "figure"),
    Output("my-graph-center", "figure"),
    Output("my-graph-right", "figure"),
    Input(component_id="date-range", component_property="start_date"),
    Input(component_id="date-range", component_property="end_date"),
)
def plot_dt(start_date, end_date):
    """Filter by date: left < start, center in range, right > end."""
    # Normalize inputs to timestamps; fallback to dataset bounds if missing
    start_dt = pd.to_datetime(start_date) if start_date else df["date"].min()
    end_dt = pd.to_datetime(end_date) if end_date else df["date"].max()

    figL = px.line(df.loc[df["date"] < start_dt, :], x="date", y=["GOOG", "AAPL"], template="plotly_dark")
    figC = px.line(
        df.loc[(df["date"] >= start_dt) & (df["date"] <= end_dt), :],
        x="date",
        y=["GOOG", "AAPL"],
        template="plotly_dark",
    )
    figR = px.line(df.loc[df["date"] > end_dt, :], x="date", y=["GOOG", "AAPL"], template="plotly_dark")

    return figL, figC, figR


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
