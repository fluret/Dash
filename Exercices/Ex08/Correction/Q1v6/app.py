"""
App initialization.
"""
from dash import Dash, html
import dash_bootstrap_components as dbc
from config import THEME, CONTAINER_STYLE
from components.header import create_header
from components.controls import create_controls
from components.graph_card import create_graph_card


def create_app() -> Dash:
    """Create and configure the Dash app."""
    app = Dash(__name__, external_stylesheets=[THEME])
    
    app.layout = dbc.Container(
        [
            create_header(),
            create_controls(),
            html.Div(
                dbc.Row(
                    [
                        dbc.Col(create_graph_card("Original Range", "my-graph-left", "badges-left"), md=4),
                        dbc.Col(create_graph_card("Selected Range", "my-graph-center", "badges-center"), md=4),
                        dbc.Col(create_graph_card("Inverted Range", "my-graph-right", "badges-right"), md=4),
                    ],
                    className="mb-4 g-3",
                )
            ),
        ],
        fluid=True,
        style=CONTAINER_STYLE,
    )
    
    return app
