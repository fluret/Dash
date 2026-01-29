
"""
Constantes de configuration et de style pour l'application Q2v5.
Centralise les couleurs, thèmes, options et styles réutilisables.
"""

from datetime import date
import dash_bootstrap_components as dbc

# Style flex pour la ligne de contrôle (badges + datepicker)
CONTROL_FLEX_ROW_STYLE = {
    "display": "flex",
    "flexDirection": "row",
    "alignItems": "center",
    "justifyContent": "space-between",
    "gap": "12px"
}

# Theme
THEME = dbc.themes.LITERA

# Chart constants
CHART_TEMPLATE = "plotly_dark"
CHART_HEIGHT = "50vh"
GAPMINDER_CHART_HEIGHT = "70vh"
TICKERS = ["GOOG", "AAPL"]

# Colors and styling
CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"
GRADIENT_BG = f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)"
BADGE_COLOR = "secondary"
CARD_CLASS = "shadow-sm border-0"
CARD_HEADER_CLASS = "fw-semibold text-white"
CONTROL_BODY_CLASS = "bg-light"

# Container styling
CONTAINER_STYLE = {
    "backgroundColor": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "20px",
}



# Style flex pour le CardBody du header (sans background)
HEADER_CARDBODY_STYLE = {
    "display": "flex",
    "flexDirection": "row",
    "alignItems": "center",
    "justifyContent": "space-between",
    "color": "white",
    "padding": "12px 20px",
    "borderRadius": "12px"
}

# Style pour le Card du header (background gradient)
HEADER_CARD_STYLE = {
    "background": GRADIENT_BG,
    "borderRadius": "12px",
    "marginBottom": "28px"
}

# Defaults
DEFAULT_START = date(2018, 5, 1)
DEFAULT_END = date(2019, 2, 1)

METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
