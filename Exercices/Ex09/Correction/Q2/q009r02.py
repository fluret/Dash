from dash import Dash, dcc, Output, Input, html
import plotly.express as px
import dash_bootstrap_components as dbc
import pathlib
from dash.dependencies import Input, Output, State

# Présentation du jeu de données Gapminder


with open(
    pathlib.Path(__file__).parent / "gapminder_description.md", encoding="utf-8"
) as f:
    GAPMINDER_DESCRIPTION_MD = f.read()

# Constante pour la bordure des cards
BORDER_CARD_CLASS = "border border-primary border-3 rounded-3"

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

# Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

####### App Layout

# Titre
header = dbc.Row(
    [
        dbc.Col(
            [
                html.H1(
                    "Gapminder Stacked Bar Charts",
                    className="text-center text-uppercase m-3",
                )
            ],
            width=12,
        )
    ],
)
# Dropdown Card et bouton d'info
dropdown = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Label("Select a metric:", className="fw-bold mb-3"),
                dbc.Select(id="metric-dropdown", value="pop", options=METRIC_OPTIONS),
                dbc.Button(
                    [
                        html.Span(className="bi bi-info-circle-fill me-2"),
                        "Informations",
                    ],
                    id="info-btn",
                    color="primary",
                    className="mt-3 w-100",
                ),
            ]
        )
    ],
    className=BORDER_CARD_CLASS,
)
# Graph Card
graph = dbc.Card(
    [dbc.CardBody([dcc.Graph(id="figure1", style={"height": "70vh"})])],
    className=BORDER_CARD_CLASS,
)

main_row = dbc.Row(
    [
        dbc.Col(dropdown, xs=12, md=3, className="mb-3 mb-md-0"),
        dbc.Col(graph, xs=12, md=9),
    ]
)
# Offcanvas pour la description du jeu de données
offcanvas = dbc.Offcanvas(
    [
        dcc.Markdown(
            GAPMINDER_DESCRIPTION_MD,
            className="mb-3",
        ),
    ],
    id="offcanvas-gapminder",
    title="À propos du jeu de données",
    is_open=False,
    placement="end",
    close_button=True,
    style={"color": "white"},
)

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(
                    [
                        dropdown,
                        html.Div(id="toast-container"),
                    ],
                    xs=12,
                    md=3,
                    className="mb-3 mb-md-0",
                ),
                dbc.Col(graph, xs=12, md=9),
            ]
        ),
        offcanvas,
    ],
    fluid=True,
)


# Callbacks
@app.callback(
    [Output("figure1", "figure"), Output("toast-container", "children")],
    Input("metric-dropdown", "value"),
)
def update_graph(metric):
    fig = px.bar(
        df,
        x="year",
        y=metric,
        color="continent",
        barmode="stack",
    )
    metric_details = {
        "pop": "Population totale (somme des habitants par continent et année)",
        "gdpPercap": "PIB moyen par habitant (moyenne du PIB par habitant par continent et année)",
        "lifeExp": "Espérance de vie moyenne (moyenne par continent et année)",
    }
    label = next(
        (opt["label"] for opt in METRIC_OPTIONS if opt["value"] == metric), metric
    )
    detail = metric_details.get(metric, "")
    toast = dbc.Toast(
        [html.Strong(f"Métrique affichée : {label}"), html.Br(), html.Span(detail)],
        id="metric-toast",
        header=html.Span(
            [
                html.Span(className="bi bi-info-circle-fill me-2"),
                "Changement de métrique",
            ]
        ),
        # icon="success",
        duration=8000,
        is_open=True,
        dismissable=True,
        style={"width": "100%", "marginTop": "1rem"},
    )
    return fig, toast


# Callback simple pour ouvrir/fermer l'OffCanvas (bouton ou croix)
@app.callback(
    Output("offcanvas-gapminder", "is_open"),
    [Input("info-btn", "n_clicks")],
    [State("offcanvas-gapminder", "is_open")],
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
