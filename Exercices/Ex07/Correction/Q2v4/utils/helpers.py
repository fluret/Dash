"""
Helper utilities.
"""
from dash import html
import dash_bootstrap_components as dbc
from config import CARD_BODY_STYLE, CARD_CLASS, CARD_HEADER_COLOR


def create_card(title_text, icon, content, width_lg):
    """Create a standardized card with header and body."""
    return dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H5([icon, " ", title_text], className="mb-0 fw-semibold text-white"),
                    style={"backgroundColor": CARD_HEADER_COLOR},
                ),
                dbc.CardBody(content, style=CARD_BODY_STYLE),
            ],
            className=CARD_CLASS,
            style={"borderRadius": "10px", "overflow": "hidden"},
        ),
        width=12,
        lg=width_lg,
    )
