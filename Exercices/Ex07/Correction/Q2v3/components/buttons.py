"""
Button components.
"""
from dash import html
import dash_bootstrap_components as dbc


def create_plot_button():
    """Create the plot trigger button with icon."""
    return dbc.Button(
        [html.I(className="bi bi-graph-up me-2"), "Generate Chart"],
        id="draw",
        color="info",
        className="mt-3 w-100 btn-lg",
        n_clicks=0,
        style={"fontWeight": "600", "padding": "12px"},
    )
