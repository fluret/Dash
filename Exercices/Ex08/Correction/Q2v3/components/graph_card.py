"""Graph card components."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from config import CHART_HEIGHT, GAPMINDER_CHART_HEIGHT


def create_graph_card(graph_id: str, title: str = "") -> dbc.Card:
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


def create_gapminder_card(graph_id: str) -> dbc.Card:
    return dbc.Card(
        dbc.CardBody(
            dcc.Graph(id=graph_id, style={"height": GAPMINDER_CHART_HEIGHT})
        ),
        className="shadow-sm",
    )
