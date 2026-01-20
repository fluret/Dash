"""
Configuration and constants for the Dashboard application.
"""
import dash_bootstrap_components as dbc

# Theme and styling
DEFAULT_THEME = dbc.themes.LITERA

# Colors
CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"
COLOR_PALETTE = ["#667eea", "#764ba2", "#f093fb", "#4facfe"]

# Card styling
CARD_CLASS = "mb-4 shadow-sm border-0"
CARD_BODY_STYLE = {
    "height": "50vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

# Header styling
HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "40px 20px",
    "borderRadius": "10px",
    "marginBottom": "30px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)"
}

# Table header styling
TABLE_HEADER_STYLE = {
    "backgroundColor": CARD_HEADER_COLOR,
    "color": "white",
    "fontWeight": "bold",
    "padding": "12px",
    "borderRadius": "4px"
}

# Container styling
CONTAINER_STYLE = {
    "backgroundColor": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "20px"
}

# Data configuration
TABLE_PAGE_SIZE = 15

# Table styles
TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left", "padding": "12px", "fontFamily": "Arial, sans-serif"},
    "style_header": TABLE_HEADER_STYLE,
    "style_data_conditional": [
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "rgba(102, 126, 234, 0.05)"
        },
        {
            "if": {"column_id": "total_bill"},
            "color": CARD_HEADER_COLOR,
            "fontWeight": "bold"
        }
    ]
}

# Chart configuration
CHART_CONFIG = {
    "template": "plotly_white",
    "hovermode": "x unified",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "font": {"family": "Arial, sans-serif", "size": 12},
    "title_font_size": 16,
    "margin": {"l": 50, "r": 50, "t": 50, "b": 50},
    "height": 500
}
