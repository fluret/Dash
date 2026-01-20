"""
Utility helper functions.
"""
import dash_bootstrap_components as dbc
from dash import html
from config import CARD_BODY_STYLE, CARD_CLASS


def create_card(title_text, content, width_lg):
    """
    Create a card with standardized styling.
    
    Args:
        title_text: Title of the card
        content: Content component
        width_lg: Bootstrap width for large screens
        
    Returns:
        dbc.Col with styled card
    """
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [html.H5(title_text, className="card-title pb-3"), content],
                style=CARD_BODY_STYLE
            ),
            className=CARD_CLASS
        ),
        width=12,
        lg=width_lg
    )
