# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Constants
THEME = dbc.themes.BOOTSTRAP
CHART_TEMPLATE = "plotly_dark"
TICKERS = ["GOOG", "AAPL"]
DEFAULT_START = date(2018, 5, 1)
DEFAULT_END = date(2019, 2, 1)

METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]

# Import data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

dfG = px.data.gapminder()
dfG = (
    dfG.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# Helper functions
def make_stocks_fig(df_slice):
    """Create line chart for stocks data."""
    return px.line(df_slice, x="date", y=TICKERS, template=CHART_TEMPLATE)


def make_graph_card(graph_id):
    """Create reusable graph card."""
    return dbc.Card(dbc.CardBody([dcc.Graph(id=graph_id)]))


# Initialise the App
app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)

# Create app components
title_ = dcc.Markdown(
    children="Exercise 8.2", style={"textAlign": "center", "fontSize": 20}
)
tabs_ = dcc.Tabs(
    id="tabs-app-solution2",
    children=[
        dcc.Tab(label="App One", value="tab-app-1"),
        dcc.Tab(label="App Two", value="tab-app-2"),
    ],
    value="tab-app-1",
)
tabs_content_ = dbc.Container(id="tabs-content-solution2")

# Specific for App 1
date_range_ = dcc.DatePickerRange(
    id="date-range-solution2",
    start_date_placeholder_text="start date",
    end_date_placeholder_text="end date",
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    start_date=DEFAULT_START,
    end_date=DEFAULT_END,
    display_format="DD-MMM-YYYY",
    first_day_of_week=1,
)
card_L = make_graph_card("my-graph-left-solution2")
card_C = make_graph_card("my-graph-center-solution2")
card_R = make_graph_card("my-graph-right-solution2")
# Specific for App 2
dropdown_ = dcc.Dropdown(
    id="metric-dropdown-solution2",
    placeholder="Select a metric",
    options=METRIC_OPTIONS,
    value="gdpPercap",
    clearable=False,
)
graph_ = dcc.Graph(id="figure1-solution2", style={"height": "600px"})

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([title_], width=12)),
        dbc.Row(dbc.Col([tabs_, tabs_content_], width=12)),
    ]
)


# Callbacks
@app.callback(
    Output("tabs-content-solution2", "children"), Input("tabs-app-solution2", "value")
)
def render_content(tab):
    if tab == "tab-app-1":
        app1_layout = dbc.Container(
            [
                dbc.Row(
                    dbc.Col([date_range_], width=12, style={"textAlign": "center"})
                ),
                dbc.Row(
                    [
                        dbc.Col([card_L], width=4),
                        dbc.Col([card_C], width=4),
                        dbc.Col([card_R], width=4),
                    ]
                ),
            ]
        )
        return app1_layout

    elif tab == "tab-app-2":
        # App 2 layout
        app2_layout = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col([dropdown_], width=2),
                        dbc.Col([graph_], width=10),
                    ]
                )
            ]
        )
        return app2_layout


# Callback for App1
@app.callback(
    Output("my-graph-left-solution2", "figure"),
    Output("my-graph-center-solution2", "figure"),
    Output("my-graph-right-solution2", "figure"),
    Input("date-range-solution2", "start_date"),
    Input("date-range-solution2", "end_date"),
)
def plot_dt(start_date, end_date):
    start_dt = pd.to_datetime(start_date) if start_date else df["date"].min()
    end_dt = pd.to_datetime(end_date) if end_date else df["date"].max()
    
    df_left = df[df["date"] < start_dt]
    df_center = df[(df["date"] >= start_dt) & (df["date"] <= end_dt)]
    df_right = df[df["date"] > end_dt]

    return make_stocks_fig(df_left), make_stocks_fig(df_center), make_stocks_fig(df_right)


# Callback for App2
@app.callback(
    Output("figure1-solution2", "figure"),
    Input("metric-dropdown-solution2", "value"),
)
def update_gapminder_chart(metric):
    return px.bar(dfG, x="year", y=metric, color="continent", template=CHART_TEMPLATE)


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
