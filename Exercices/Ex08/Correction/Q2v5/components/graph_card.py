
"""
Composants de cartes graphiques avec en-têtes stylisés pour Q2v5.
"""

from dash import dcc, html
import dash_bootstrap_components as dbc
from config import (
    CHART_HEIGHT,
    GAPMINDER_CHART_HEIGHT,
    GRADIENT_BG,
    CARD_HEADER_CLASS,
    CARD_CLASS,
)


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
        card_content.insert(
            0,
            dbc.CardHeader(
                title,
                className=CARD_HEADER_CLASS,
                style={"background": GRADIENT_BG},
            ),
        )
    return dbc.Card(card_content, className=f"{CARD_CLASS} h-100")


def create_gapminder_card(graph_id: str) -> dbc.Card:
    return dbc.Card(
        dbc.CardBody(
            dcc.Graph(id=graph_id, style={"height": GAPMINDER_CHART_HEIGHT})
        ),
        className=CARD_CLASS,
    )
