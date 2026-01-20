"""
Header component.
"""
from dash import html
from config import HEADER_STYLE


def create_header():
    """Return the gradient header block."""
    return html.Div(
        [
            html.H1("📊 Sales Analytics", className="mb-1"),
            html.P("Interactive exploration of tips data", className="text-light mb-0"),
        ],
        style=HEADER_STYLE,
    )
