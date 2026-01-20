"""
Chart component.
"""
from dash import dcc


def create_chart():
    """Create the chart container."""
    return dcc.Graph(id="chart", style={"height": "100%"})
