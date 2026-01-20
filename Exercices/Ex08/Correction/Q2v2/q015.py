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
CHART_HEIGHT = "50vh"
BADGE_COLOR = "secondary"

METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]

# Import data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
MIN_DATE = df["date"].min().date()
MAX_DATE = df["date"].max().date()

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


def fmt_date(ts: pd.Timestamp) -> str:
    return ts.date().strftime("%d-%b-%Y")


def make_badges(start_dt, end_dt):
    return [
        dbc.Badge(f"Start: {fmt_date(start_dt)}", color=BADGE_COLOR),
        dbc.Badge(f"End: {fmt_date(end_dt)}", color=BADGE_COLOR),
    ]


def normalize_range(start_date, end_date):
    start_dt = pd.to_datetime(start_date) if start_date else df["date"].min()
    end_dt = pd.to_datetime(end_date) if end_date else df["date"].max()
    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt, end_dt


def make_graph_card(graph_id, title=""):
    """Create reusable graph card with optional header and badges placeholder."""
    card_content = [
        dbc.CardBody(
            [
                dcc.Graph(id=graph_id, style={"height": CHART_HEIGHT}),
                html.Div(id=f"{graph_id}-badges", className="d-flex gap-2 mt-2 flex-wrap"),
            ]
        )
    ]
    if title:
        card_content.insert(0, dbc.CardHeader(title, className="fw-bold"))
    return dbc.Card(card_content, className="shadow-sm h-100")


# Initialise the App
app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)

# Create app components
title_ = html.H2("Exercise 8.2", className="text-center my-3")

tabs_ = dbc.Tabs(
    id="tabs-app-solution2",
    children=[
        dbc.Tab(label="App One", tab_id="tab-app-1"),
        dbc.Tab(label="App Two", tab_id="tab-app-2"),
    ],
    active_tab="tab-app-1",
)
tabs_content_ = html.Div(id="tabs-content-solution2", className="mt-3")

# Specific for App 1
date_range_card_ = dbc.Card(
    [
        dbc.CardHeader("Select Date Range", className="fw-bold"),
        dbc.CardBody(
            [
                dcc.DatePickerRange(
                    id="date-range-solution2",
                    start_date_placeholder_text="start date",
                    end_date_placeholder_text="end date",
                    min_date_allowed=df.date.min(),
                    max_date_allowed=df.date.max(),
                    start_date=DEFAULT_START,
                    end_date=DEFAULT_END,
                    display_format="DD-MMM-YYYY",
                    first_day_of_week=1,
                ),
                html.Div(
                    [
                        dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="me-2 mt-3"),
                        dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="mt-3"),
                    ],
                    className="d-flex gap-2 justify-content-center",
                ),
            ],
            className="text-center",
        ),
    ],
    className="mb-3",
)

card_L = make_graph_card("my-graph-left-solution2", "Before Range")
card_C = make_graph_card("my-graph-center-solution2", "Selected Range")
card_R = make_graph_card("my-graph-right-solution2", "After Range")

# Specific for App 2
metric_select_ = dbc.InputGroup(
    [
        dbc.InputGroupText("Metric"),
        dbc.Select(
            id="metric-dropdown-solution2",
            options=METRIC_OPTIONS,
            value="gdpPercap",
        ),
    ],
    className="mb-3",
)

graph_card_ = dbc.Card(
    dbc.CardBody(dcc.Graph(id="figure1-solution2", style={"height": "70vh"})),
    className="shadow-sm",
)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([title_], width=12)),
        dbc.Row(dbc.Col([tabs_, tabs_content_], width=12)),
    ],
    fluid=True,
)


# Callbacks
@app.callback(
    Output("tabs-content-solution2", "children"), Input("tabs-app-solution2", "active_tab")
)
def render_content(tab):
    if tab == "tab-app-1":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(date_range_card_, width=12)),
                dbc.Row(
                    [
                        dbc.Col(card_L, md=4),
                        dbc.Col(card_C, md=4),
                        dbc.Col(card_R, md=4),
                    ],
                    className="g-3",
                ),
            ],
            fluid=True,
        )

    elif tab == "tab-app-2":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(metric_select_, md=3)),
                dbc.Row(dbc.Col(graph_card_, width=12)),
            ],
            fluid=True,
        )


# Callback for App1
@app.callback(
    Output("my-graph-left-solution2", "figure"),
    Output("my-graph-center-solution2", "figure"),
    Output("my-graph-right-solution2", "figure"),
    Output("my-graph-left-solution2-badges", "children"),
    Output("my-graph-center-solution2-badges", "children"),
    Output("my-graph-right-solution2-badges", "children"),
    Input("date-range-solution2", "start_date"),
    Input("date-range-solution2", "end_date"),
)
def plot_dt(start_date, end_date):
    start_dt, end_dt = normalize_range(start_date, end_date)

    df_left = df[df["date"] < start_dt]
    df_center = df[(df["date"] >= start_dt) & (df["date"] <= end_dt)]
    df_right = df[df["date"] > end_dt]

    badges_left = make_badges(df["date"].min(), start_dt)
    badges_center = make_badges(start_dt, end_dt)
    badges_right = make_badges(end_dt, df["date"].max())

    return (
        make_stocks_fig(df_left),
        make_stocks_fig(df_center),
        make_stocks_fig(df_right),
        badges_left,
        badges_center,
        badges_right,
    )


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
