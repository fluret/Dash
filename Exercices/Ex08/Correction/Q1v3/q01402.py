# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Import data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
MIN_DATE = df["date"].min().date()
MAX_DATE = df["date"].max().date()
MIN_TS = df["date"].min()
MAX_TS = df["date"].max()

# Styling / chart constants
THEME = dbc.themes.BOOTSTRAP
CHART_TEMPLATE = "plotly_dark"
TICKERS = ["GOOG", "AAPL"]

# Initialise the App
app = Dash(__name__, external_stylesheets=[THEME])


def build_header() -> dbc.Row:
    """Lightweight header row for the page title."""
    return dbc.Row(
        dbc.Col(
            html.H4("Exercice 8.1", className="fw-semibold text-primary text-center my-3"),
            width=12,
        )
    )


def build_controls() -> dbc.Card:
    """Card containing the date picker range."""
    return dbc.Card(
        [
            dbc.CardHeader(html.Div([html.I(className="bi bi-calendar me-2"), "Plage de dates"])),
            dbc.CardBody(
                [
                    dcc.DatePickerRange(
                        id="date-range",
                        start_date_placeholder_text="start date",
                        end_date_placeholder_text="end date",
                        min_date_allowed=df.date.min(),
                        max_date_allowed=df.date.max(),
                        start_date=date(2018, 5, 1),
                        end_date=date(2019, 2, 1),
                        display_format="DD-MMM-YYYY",
                        first_day_of_week=1,
                    ),
                    html.Div(
                        [
                            dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color="secondary", className="me-2 mt-3"),
                            dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color="secondary", className="mt-3"),
                        ],
                        className="d-flex gap-2",
                    ),
                ]
            ),
        ],
        className="shadow-sm mb-3",
    )


def build_graph_card(title: str, graph_id: str) -> dbc.Card:
    """Reusable graph card with header and body."""
    return dbc.Card(
        [
            dbc.CardHeader(title, className="fw-semibold"),
            dbc.CardBody([dcc.Graph(id=graph_id, className="m-0")]),
        ],
        className="shadow-sm h-100",
    )


def make_fig(df_slice: pd.DataFrame):
    """Helper to create a line chart for the selected tickers."""
    return px.line(df_slice, x="date", y=TICKERS, template=CHART_TEMPLATE)


def normalize_range(start_date, end_date):
    """Return (start, end) timestamps with bounds fallback and swap if inverted."""
    start_dt = pd.to_datetime(start_date) if start_date else MIN_TS
    end_dt = pd.to_datetime(end_date) if end_date else MAX_TS
    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt, end_dt


# App layout
app.layout = dbc.Container(
    [
        build_header(),
        build_controls(),
        dbc.Row(
            [
                dbc.Col(build_graph_card("Avant la date de début", "my-graph-left"), md=4, xs=12, className="mb-3"),
                dbc.Col(build_graph_card("Dans la plage", "my-graph-center"), md=4, xs=12, className="mb-3"),
                dbc.Col(build_graph_card("Après la date de fin", "my-graph-right"), md=4, xs=12, className="mb-3"),
            ],
            className="g-3",
        ),
    ],
    fluid=True,
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
    start_dt, end_dt = normalize_range(start_date, end_date)

    df_left = df.loc[df["date"] < start_dt, :]
    df_center = df.loc[(df["date"] >= start_dt) & (df["date"] <= end_dt), :]
    df_right = df.loc[df["date"] > end_dt, :]

    figL = make_fig(df_left)
    figC = make_fig(df_center)
    figR = make_fig(df_right)

    return figL, figC, figR


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
