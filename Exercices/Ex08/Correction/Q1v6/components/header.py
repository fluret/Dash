"""
Header component.
"""
from dash import html
import dash_bootstrap_components as dbc
from config import HEADER_STYLE


def create_header() -> dbc.Row:
    """Gradient header for the dashboard."""
    return dbc.Row(
        dbc.Col(
            html.Div(
                [
                    html.H2("📊 Exercice 8.1", className="mb-1 fw-bold"),
                    html.P("Analyse temporelle des cours (GOOG, AAPL)", className="mb-0"),
                ],
                style=HEADER_STYLE,
            ),
            width=12,
        )
    )
