"""Header component with gradient styling."""


import dash_bootstrap_components as dbc
from dash import html
from config import HEADER_CARDBODY_STYLE, HEADER_CARD_STYLE


def create_header():
    return dbc.Card([
        dbc.CardBody([
            html.H5("📊 Exercice 8.2", className="mb-0 fw-bold", style={"margin": 0}),
            html.P("Deux onglets : séries financières et indicateurs globaux", className="mb-0", style={"margin": 0}),
        ], style=HEADER_CARDBODY_STYLE)
    ], style=HEADER_CARD_STYLE)
