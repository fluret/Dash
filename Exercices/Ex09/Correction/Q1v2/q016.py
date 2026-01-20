from dash import Dash, dcc, Output, Input, html, callback
import plotly.express as px
import dash_bootstrap_components as dbc

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
CHART_HEIGHT = "600px"

# Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("Gapminder Stacked Bar Charts", className="text-warning text-center pb-3"),
            ),
            className="border-bottom border-dark border-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Select(
                        id="metric-dropdown",
                        placeholder="Select a metric",
                        value="pop",
                        options=METRIC_OPTIONS,
                        className="border-primary border-2",
                    ),
                    width=12,
                    xl=2,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(dcc.Graph(id="figure1", style={"height": CHART_HEIGHT})),
                        className="shadow-sm",
                    ),
                    width=12,
                    xl=10,
                ),
            ],
            className="p-3",
        ),
    ],
    className="bg-light p-3",
    fluid=True,
    style={"minHeight": "100vh"},
)


@callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_chart(metric):
    """Update bar chart based on selected metric."""
    return px.bar(df, x="year", y=metric, color="continent", template=CHART_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True)
