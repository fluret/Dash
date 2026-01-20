"""
Header component.
"""
from dash import html
import dash_bootstrap_components as dbc


def create_header():
    """Create the application header."""
    return dbc.Row(
        dbc.Col(
            html.H1("Exercise 7.1", className="text-center text-primary mt-4 mb-4"),
            width=12
        )
    )
