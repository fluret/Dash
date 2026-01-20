"""Dash application factory for Q2v3."""
import dash_bootstrap_components as dbc
from dash import Dash, html
from config import THEME, METRIC_OPTIONS
from components.header import create_header
from components.tabs import create_tabs, create_tabs_content
from components.controls import create_date_range_card, create_metric_select
from components.graph_card import create_graph_card, create_gapminder_card


def create_app() -> Dash:
    app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)

    tabs_component = create_tabs()
    tabs_content = create_tabs_content()

    # Pre-built components reused in callbacks
    date_range_card = create_date_range_card()
    card_left = create_graph_card("my-graph-left-solution2", "Before Range")
    card_center = create_graph_card("my-graph-center-solution2", "Selected Range")
    card_right = create_graph_card("my-graph-right-solution2", "After Range")

    metric_select = create_metric_select(METRIC_OPTIONS)
    gapminder_card = create_gapminder_card("figure1-solution2")

    app.layout = dbc.Container(
        [
            dbc.Row(dbc.Col(create_header(), width=12)),
            dbc.Row(dbc.Col([tabs_component, tabs_content], width=12)),
        ],
        fluid=True,
    )

    # Store reusable components on app for callbacks to access
    app.date_range_card = date_range_card
    app.card_left = card_left
    app.card_center = card_center
    app.card_right = card_right
    app.metric_select = metric_select
    app.gapminder_card = gapminder_card

    return app
