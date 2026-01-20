"""Header component with gradient styling."""
from dash import html
from config import HEADER_STYLE


def create_header():
    return html.Div(
        [
            html.H2("📊 Exercice 8.2", className="mb-1 fw-bold"),
            html.P("Deux onglets : séries financières et indicateurs globaux", className="mb-0"),
        ],
        style=HEADER_STYLE,
    )
