"""Multipage Dash app for Q1v2, reusing Q1v1 approach."""

import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from pathlib import Path

# Create Dash app with built-in pages support
pages_folder = str(Path(__file__).parent / "pages")

app = Dash(
    __name__,
    use_pages=True,
    pages_folder=pages_folder,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MORPH],
)

# Layout with navigation links to registered pages
app.layout = dbc.Container([
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("Application multipage", className="text-uppercase"),
            dbc.Nav([
                dbc.NavItem(
                    dbc.NavLink(page['name'], href=page['path'], active="exact")
                ) for page in dash.page_registry.values()
            ], pills=True),
        ]),
        color="primary", dark=True, className="mb-4"
    ),
    dash.page_container,
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)
