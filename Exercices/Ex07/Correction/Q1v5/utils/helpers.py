"""
Utility helper functions.
"""
from dash import html
import dash_bootstrap_components as dbc
from config import CARD_BODY_STYLE, CARD_CLASS, CARD_HEADER_COLOR


def create_card(title_text, icon, content, width_lg):
    """
    Create a card with standardized styling and icons.
    
    Args:
        title_text: Title of the card
        icon: Icon component (e.g., html.I)
        content: Content component
        width_lg: Bootstrap width for large screens
        
    Returns:
        dbc.Col with styled card
    """
    return dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H5([icon, " ", title_text], className="mb-0"),
                    style={"backgroundColor": CARD_HEADER_COLOR, "color": "white", "fontWeight": "600"}
                ),
                dbc.CardBody(
                    content,
                    style={**CARD_BODY_STYLE, "padding": "20px"}
                )
            ],
            className="border-0 shadow-sm",
            style={"borderRadius": "8px", "overflow": "hidden"}
        ),
        width=12,
        lg=width_lg
    )
