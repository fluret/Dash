"""
Header component.
"""
from dash import html
from config import HEADER_STYLE


def create_header():
    """Create the application header with gradient background."""
    return html.Div(
        [
            html.H1("📊 Sales Analytics Dashboard", className="mb-0"),
            html.P("Interactive data visualization and analysis", className="text-light mt-2 mb-0")
        ],
        style=HEADER_STYLE
    )
