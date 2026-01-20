from dash import dcc, Output, Input, html, callback
import dash
import plotly.express as px
import dash_bootstrap_components as dbc

# Register page for multipage app
dash.register_page(__name__, path="/")

# Data preparation
_gapminder_df = px.data.gapminder()
df = (
    _gapminder_df.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# Constants
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
CHART_TEMPLATE = "plotly_dark"
CHART_HEIGHT = "60vh"


# App Layout
layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H3("Gapminder Stacked Bar Charts", className="text-warning text-center"),
            ),
            className="m-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Select(
                        id="metric-dropdown",
                        placeholder="Select a metric",
                        options=METRIC_OPTIONS,
                        value="gdpPercap",
                    ),
                    className="p-3",
                    width=12,
                    xl=2,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(dcc.Graph(id="figure1", style={"height": CHART_HEIGHT})),
                        className="border-warning border-1 rounded-3",
                    ),
                    width=12,
                    xl=10,
                ),
            ],
            className="flex-fill",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Slider(min=0, max=10), width=4),
                dbc.Col(dcc.Slider(min=0, max=10), width=6),
            ],
            justify="center",
            className="p-5",
        ),
    ],
    className="min-vh-100 border border-warning border-4 rounded-4 mx-auto p-4 d-flex flex-column",
    style={"maxHeight": "100vh", "overflow": "auto"},
)


@callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_chart(metric):
    """Update bar chart based on selected metric."""
    return px.bar(df, x="year", y=metric, color="continent", template=CHART_TEMPLATE)
