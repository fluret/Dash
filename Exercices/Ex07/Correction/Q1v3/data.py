"""
Data management and loading.
"""
import plotly.express as px

def load_data():
    """Load the tips dataset."""
    return px.data.tips()
