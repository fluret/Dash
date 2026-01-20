"""Dash application factory for Q2v4."""
import dash_bootstrap_components as dbc
from dash import Dash
from config import THEME, METRIC_OPTIONS, CONTAINER_STYLE
from components.header import create_header
from components.tabs import create_tabs, create_tabs_content
from components.controls import create_date_range_card, create_metric_select
from components.graph_card import create_graph_card, create_gapminder_card


def create_app() -> Dash:
    """Create and configure the Dash application."""
    app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)

    # Store reusable components on app for callbacks
    app.date_range_card = create_date_range_card()
    app.card_left = create_graph_card("my-graph-left-solution2", "Before Range")
    app.card_center = create_graph_card("my-graph-center-solution2", "Selected Range")
    app.card_right = create_graph_card("my-graph-right-solution2", "After Range")
    app.metric_select = create_metric_select(METRIC_OPTIONS)
    app.gapminder_card = create_gapminder_card("figure1-solution2")

    # Build layout
    app.layout = dbc.Container(
        [
            dbc.Row(dbc.Col(create_header(), width=12)),
            dbc.Row(dbc.Col([create_tabs(), create_tabs_content()], width=12)),
        ],
        fluid=True,
        style=CONTAINER_STYLE,
    )

    return app
