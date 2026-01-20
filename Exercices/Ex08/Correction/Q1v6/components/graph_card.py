"""
Graph card component.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc
from config import (
    CHART_HEIGHT,
    CARD_HEADER_CLASS,
    CARD_HEADER_COLOR,
    CARD_ACCENT_COLOR,
)


def create_graph_card(title: str, graph_id: str, badges_id: str) -> dbc.Card:
    """Reusable graph card with header, graph, and range badges."""
    return dbc.Card(
        [
            dbc.CardHeader(
                title,
                className=CARD_HEADER_CLASS,
                style={"background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)"},
            ),
            dbc.CardBody(
                [
                    dcc.Graph(
                        id=graph_id,
                        className="m-0",
                        style={"height": CHART_HEIGHT},
                        config={"responsive": True},
                    ),
                    html.Div(id=badges_id, className="d-flex gap-2 mt-2 flex-wrap"),
                ]
            ),
        ],
        className="shadow-sm h-100",
    )
