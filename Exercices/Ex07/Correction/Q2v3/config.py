"""
Configuration and styling constants for the Q2v3 dashboard.
"""
import dash_bootstrap_components as dbc

# Theme
DEFAULT_THEME = dbc.themes.LITERA

# Data / chart
TABLE_PAGE_SIZE = 15
DEFAULT_Y_COLUMN = "total_bill"
CHART_HEIGHT = 450
DEFAULT_MESSAGE = "Select a column or cell to update the chart"
COLOR_PALETTE = ["#667eea", "#764ba2", "#f093fb", "#4facfe"]

# Colors
CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"

# Card / container styling
CARD_CLASS = "mb-4 shadow-sm border-0"
CARD_BODY_STYLE = {
    "height": "55vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}
HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "32px 20px",
    "borderRadius": "12px",
    "marginBottom": "32px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)"
}
CONTAINER_STYLE = {
    "backgroundColor": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "24px"
}

# Table styling
TABLE_HEADER_STYLE = {
    "backgroundColor": CARD_HEADER_COLOR,
    "color": "white",
    "fontWeight": "bold",
    "padding": "12px"
}
TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left", "padding": "12px", "fontFamily": "Arial, sans-serif"},
    "style_header": TABLE_HEADER_STYLE,
    "style_data_conditional": [
        {"if": {"row_index": "odd"}, "backgroundColor": "rgba(102, 126, 234, 0.05)"},
        {"if": {"column_id": "total_bill"}, "color": CARD_HEADER_COLOR, "fontWeight": "bold"}
    ]
}
