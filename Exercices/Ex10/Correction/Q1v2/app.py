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
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# Layout with navigation links to registered pages
app.layout = dbc.Container(
    [
        html.H2("My multipage app", className="mt-3 mb-2"),
        html.Div(
            [
                dcc.Link(f"{page['name']} - {page['path']}", href=page["path"], className="d-block mb-1")
                for page in dash.page_registry.values()
            ],
            className="mb-3",
        ),
        dash.page_container,
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)
