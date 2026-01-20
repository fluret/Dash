"""
Button components.
"""
import dash_bootstrap_components as dbc


def create_plot_button():
    """Create the plot button."""
    return dbc.Button(
        "Plot Graph",
        id="draw",
        color="primary",
        className="mt-3 w-100",
        n_clicks=0
    )
