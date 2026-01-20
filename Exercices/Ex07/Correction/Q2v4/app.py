"""
Dash application factory.
"""
from dash import Dash
from config import DEFAULT_THEME


def create_app():
    """Create and configure the Dash app."""
    return Dash(__name__, external_stylesheets=[DEFAULT_THEME])
