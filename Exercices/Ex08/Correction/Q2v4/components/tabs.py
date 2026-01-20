"""Tabs component for switching apps."""
import dash_bootstrap_components as dbc
from dash import html


def create_tabs():
    return dbc.Tabs(
        id="tabs-app-solution2",
        children=[
            dbc.Tab(label="App One", tab_id="tab-app-1"),
            dbc.Tab(label="App Two", tab_id="tab-app-2"),
        ],
        active_tab="tab-app-1",
    )


def create_tabs_content():
    return html.Div(id="tabs-content-solution2", className="mt-3")
