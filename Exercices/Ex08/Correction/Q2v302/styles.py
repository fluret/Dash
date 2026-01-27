
import dash_bootstrap_components as dbc

# Thème et couleurs
THEME = dbc.themes.LITERA
COLOR_PRIMARY = "#667eea"
COLOR_ACCENT = "#764ba2"
GRADIENT = f"linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%)"

# Styles centralisés
STYLE = {
    "card": "shadow-sm border-0",
    "header": {
        "background": GRADIENT,
        "color": "white",
        "padding": "12px 20px",
        "borderRadius": "12px",
        "marginBottom": "28px",
        "textAlign": "center",
        "boxShadow": "0 4px 15px rgba(0,0,0,0.1)",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "justifyContent": "space-between",
    },
    "header_body": {
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "justifyContent": "space-between"
    },
    "container": {
        "backgroundColor": "#f8f9fa",
        "minHeight": "100vh",
        "padding": "20px",
    },
}

# Paramètres graphiques
CHART = {
    "template": "plotly_dark",
    "height": "50vh",
    "height_gap": "70vh",
    "tickers": ["GOOG", "AAPL"],
}

# Options de métriques
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]

# Libellés
LABEL_TITLE = "\U0001f4ca Exercice 8.2"
LABEL_SUBTITLE = "Deux onglets : séries financières et indicateurs globaux"
LABEL_TAB1 = "\U0001f4c8 Séries temporelles"
LABEL_TAB2 = "\U0001f30d Indicateurs mondiaux"
LABEL_DATE = "Plage de dates"
LABEL_METRIC = "Metric"
