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
date_range = dcc.DatePickerRange(
    id="date-range",
    start_date_placeholder_text="start date",
    end_date_placeholder_text="end date",
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    display_format="DD-MMM-YYYY",
    first_day_of_week=1,
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([date_range], width=8)]),
        dbc.Row(dbc.Col([dcc.Graph(id="stock-line")], width=8)),
    ]
)


# Configure callback
@app.callback(
    Output(component_id="stock-line", component_property="figure"),
    Input(component_id="date-range", component_property="start_date"),
    Input(component_id="date-range", component_property="end_date"),
)
def plot_dt(start_date, end_date):
    df_plot = df
    if start_date is not None:
        df_plot = df_plot.loc[(df_plot["date"] >= start_date), :]
    if end_date is not None:
        df_plot = df_plot.loc[(df_plot["date"] <= end_date), :]
    fig = px.line(
        df_plot,
        x="date",
        y=["GOOG", "AAPL", "AMZN", "FB", "NFLX", "MSFT"],
        template="plotly_white",
    )

    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
