
# --- Imports & Constantes ---
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from datetime import date

THEME = dbc.themes.BOOTSTRAP
CHART_TEMPLATE = "plotly_dark"
TICKERS = ["GOOG", "AAPL"]
CHART_HEIGHT = "50vh"
BADGE_COLOR = "secondary"
DEFAULT_START = date(2018, 5, 1)
DEFAULT_END = date(2019, 2, 1)
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]

# --- Données ---
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"])
dfG = px.data.gapminder().groupby(["year", "continent"]).agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"}).reset_index()
MIN_DATE, MAX_DATE = df["date"].min().date(), df["date"].max().date()

# --- Fonctions utilitaires ---
def make_stocks_fig(df_slice):
    return px.line(df_slice, x="date", y=TICKERS, template=CHART_TEMPLATE)

def fmt_date(ts):
    return pd.to_datetime(ts).date().strftime("%d-%b-%Y")

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



def make_graph_card(graph_id, title=None):
    content = [
        dbc.CardBody([
            dcc.Graph(id=graph_id, style={"height": CHART_HEIGHT}),
            html.Div(id=f"{graph_id}-badges", className="d-flex gap-2 mt-2 flex-wrap"),
        ])
    ]
    if title:
        content.insert(0, dbc.CardHeader(title, className="fw-bold"))
    return dbc.Card(content, className="shadow-sm h-100")



# --- Layout principal ---
app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H2("Exercise 8.2", className="text-center my-3"), width=12)),
    dbc.Row(dbc.Col([
        dbc.Tabs(
            id="tabs-app-solution2",
            children=[
                dbc.Tab(label="App One", tab_id="tab-app-1"),
                dbc.Tab(label="App Two", tab_id="tab-app-2"),
            ],
            active_tab="tab-app-1",
        ),
        html.Div(id="tabs-content-solution2", className="mt-3"),
    ], width=12)),
], fluid=True)


# Callbacks
@app.callback(
    Output("tabs-content-solution2", "children"),
    Input("tabs-app-solution2", "active_tab")
)
def render_content(tab):
    if tab == "tab-app-1":
        return dbc.Container([
            dbc.Row(dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Select Date Range", className="fw-bold"),
                    dbc.CardBody([
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
                        html.Div([
                            dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="me-2 mt-3"),
                            dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="mt-3"),
                        ], className="d-flex gap-2 justify-content-center"),
                    ], className="text-center"),
                ], className="mb-3"), width=12)),
            dbc.Row([
                dbc.Col(make_graph_card("my-graph-left-solution2", "Before Range"), md=4),
                dbc.Col(make_graph_card("my-graph-center-solution2", "Selected Range"), md=4),
                dbc.Col(make_graph_card("my-graph-right-solution2", "After Range"), md=4),
            ], className="g-3"),
        ], fluid=True)
    elif tab == "tab-app-2":
        return dbc.Container([
            dbc.Row(dbc.Col(
                dbc.InputGroup([
                    dbc.InputGroupText("Metric"),
                    dbc.Select(
                        id="metric-dropdown-solution2",
                        options=METRIC_OPTIONS,
                        value="gdpPercap",
                    ),
                ], className="mb-3"), md=3)),
            dbc.Row(dbc.Col(
                dbc.Card(dbc.CardBody(dcc.Graph(id="figure1-solution2", style={"height": "70vh"})), className="shadow-sm"), width=12)),
        ], fluid=True)



# --- Callbacks ---
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
    return (
        make_stocks_fig(df_left),
        make_stocks_fig(df_center),
        make_stocks_fig(df_right),
        make_badges(df["date"].min(), start_dt),
        make_badges(start_dt, end_dt),
        make_badges(end_dt, df["date"].max()),
    )

@app.callback(
    Output("figure1-solution2", "figure"),
    Input("metric-dropdown-solution2", "value"),
)
def update_gapminder_chart(metric):
    return px.bar(dfG, x="year", y=metric, color="continent", template=CHART_TEMPLATE)


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
