"""
Data loading utilities.
"""
import plotly.express as px

def load_data():
    """Load the tips dataset from Plotly Express."""
    return px.data.tips()
