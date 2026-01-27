from dash import Dash, dcc, Output, Input, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Constantes et styles
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
CARD_CLASS = "rounded-3"
CARD_SHADOW = "shadow-lg"

# Préparation des données
df = (
    px.data.gapminder()
    .groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# App Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# Header
header = dbc.Row(
    [
        dbc.Col(
            html.H1(
                "Gapminder Stacked Bar Charts",
                className="text-center text-white text-uppercase custom-title-font",
            ),
            width=12,
            className="bg-success bg-gradient mb-3 p-3 " + CARD_SHADOW,
        )
    ]
)

# Dropdown
dropdown = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Label(
                    [
                        html.I(className="bi bi-bar-chart-fill me-2 text-primary"),
                        "Sélectionnez une métrique :",
                    ],
                    className="fw-bold mb-3 d-inline-flex align-items-center",
                ),
                dbc.Select(
                    id="metric-dropdown",
                    value="pop",
                    options=METRIC_OPTIONS,
                    className="custom-dropdown",
                ),
            ]
        )
    ],
    className=f"{CARD_CLASS} {CARD_SHADOW} bg-light custom-dropdown-card my-2",
)

# Graph
graph = dbc.Card(
    [
        dbc.CardBody(
            [dcc.Graph(id="figure1", style={"height": "70vh", "borderRadius": "20px"})]
        )
    ],
    className=f"{CARD_CLASS} {CARD_SHADOW} border border-3 border-info",
)

# Layout principal
app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(dropdown, md=3),
                dbc.Col(graph, md=9),
            ]
        ),
    ],
    fluid=True,
)


# Callback
@app.callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_graph(metric):
    return px.bar(
        df,
        x="year",
        y=metric,
        color="continent",
        template="plotly_dark",
        barmode="stack",
    )


if __name__ == "__main__":
    app.run(debug=True)
