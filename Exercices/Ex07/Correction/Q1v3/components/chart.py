"""
Chart component.
"""
from dash import dcc


def create_chart():
    """Create the chart component."""
    return dcc.Graph(id="chart")
