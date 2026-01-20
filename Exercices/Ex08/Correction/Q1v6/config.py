"""
Configuration and styling constants.
"""
import dash_bootstrap_components as dbc

# Theme
THEME = dbc.themes.LITERA

# Chart constants
CHART_TEMPLATE = "plotly_dark"
CHART_HEIGHT = "50vh"
TICKERS = ["GOOG", "AAPL"]

# Colors
CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"
BADGE_COLOR = "secondary"

# Styling classes
CARD_CLASS = "shadow-sm border-0"
CARD_HEADER_CLASS = "fw-semibold text-white"
CONTROL_BODY_CLASS = "bg-light"

# Container styling
CONTAINER_STYLE = {
    "backgroundColor": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "20px"
}

# Header styling
HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "32px 20px",
    "borderRadius": "12px",
    "marginBottom": "28px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)",
}
