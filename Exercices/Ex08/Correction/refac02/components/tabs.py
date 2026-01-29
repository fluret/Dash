
"""
Composant d'onglets avec style moderne (pills) pour Q2v5.
"""

import dash_bootstrap_components as dbc
from dash import html


def create_tabs():
    """Create pills-style tabs."""
    return dbc.Tabs(
        id="tabs-app-solution2",
        children=[
            dbc.Tab(
                label="📈 Séries temporelles",
                tab_id="tab-app-1",
            ),
            dbc.Tab(
                label="🌍 Indicateurs mondiaux",
                tab_id="tab-app-2",
            ),
        ],
        active_tab="tab-app-1",
        className="nav-pills mb-4",
    )


def create_tabs_content():
    return html.Div(id="tabs-content-solution2")
