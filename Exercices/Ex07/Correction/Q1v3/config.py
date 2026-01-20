"""
Configuration and constants for the Dashboard application.
"""
import dash_bootstrap_components as dbc

# Theme and styling
DEFAULT_THEME = dbc.themes.BOOTSTRAP
CARD_CLASS = "mb-4"

# Component styling
CARD_BODY_STYLE = {
    "height": "50vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left"},
    "style_header": {
        "backgroundColor": "rgb(230, 230, 230)",
        "fontWeight": "bold"
    }
}

# Data configuration
TABLE_PAGE_SIZE = 15
