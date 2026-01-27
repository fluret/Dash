import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/graph1", name="Graphique 1")

# Constants
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]

# Data
df = px.data.gapminder()
df = (
    df.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# Composants principaux

dropdown = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Label("Select a metric:", className="fw-bold mb-3"),
                dbc.Select(id="metric-dropdown", value="pop", options=METRIC_OPTIONS),
            ]
        )
    ],
)

graph = dbc.Card(
    [dbc.CardBody([dcc.Graph(id="figure1", style={"height": "70vh"})])],
)

main_row = dbc.Row(
    [
        dbc.Col([dropdown], md=3),
        dbc.Col([graph], md=9),
    ]
)

layout = dbc.Container([main_row], fluid=True)


# Callbacks
@callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_graph(metric):
    return px.bar(
        df,
        x="year",
        y=metric,
        color="continent",
        barmode="stack",
    )