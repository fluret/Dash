"""
Main Dash application initialization.
"""
from dash import Dash
import dash_bootstrap_components as dbc
from config import DEFAULT_THEME


def create_app():
    """
    Create and configure the Dash application.
    
    Returns:
        Configured Dash app instance
    """
    return Dash(__name__, external_stylesheets=[DEFAULT_THEME])
