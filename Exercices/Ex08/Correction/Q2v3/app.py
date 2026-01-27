# Utilitaire pour CardHeader avec gradient
def gradient_card_header(content, className="fw-semibold text-white"):
    return dbc.CardHeader(
        content,
        className=className,
        style={"background": GRADIENT},
    )

"""Consolidated Dash app - Q2v3: Optimized single file version."""

from datetime import date
from functools import lru_cache
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html, get_app
import dash_bootstrap_components as dbc


# =====================
# CONSTANTES CENTRALES
# =====================
THEME = dbc.themes.LITERA
# Couleurs et dégradés
COLOR_PRIMARY = "#667eea"
COLOR_ACCENT = "#764ba2"
GRADIENT = f"linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%)"
# Icônes
ICON_CHART = "\U0001f4ca"  # 📊
ICON_LINE = "\U0001f4c8"  # 📈
ICON_WORLD = "\U0001f30d"  # 🌍
# Styles
STYLE = {
    "card": "shadow-sm border-0",
    "header": {
        "background": GRADIENT,
        "color": "white",
        "padding": "32px 20px",
        "borderRadius": "12px",
        "marginBottom": "28px",
        "textAlign": "center",
        "boxShadow": "0 4px 15px rgba(0,0,0,0.1)",
    },
    "container": {
        "backgroundColor": "#f8f9fa",
        "minHeight": "100vh",
        "padding": "20px",
    },
}
# Chart
CHART = {
    "template": "plotly_dark",
    "height": "50vh",
    "height_gap": "70vh",
    "tickers": ["GOOG", "AAPL"],
}
# Options métriques
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
# Labels et textes
LABEL_TITLE = f"{ICON_CHART} Exercice 8.2"
LABEL_SUBTITLE = "Deux onglets : séries financières et indicateurs globaux"
LABEL_TAB1 = f"{ICON_LINE} Séries temporelles"
LABEL_TAB2 = f"{ICON_WORLD} Indicateurs mondiaux"
LABEL_DATE = "Plage de dates"
LABEL_METRIC = "Metric"
# Dates par défaut
DEFAULT_START = date(2018, 5, 1)
DEFAULT_END = date(2019, 2, 1)


# ============================================================================
# DATA LOADING
# ============================================================================


@lru_cache(maxsize=1)
def load_data():
    """Load and cache datasets."""
    stocks = px.data.stocks()
    stocks["date"] = pd.to_datetime(stocks["date"], format="%Y-%m-%d")

    gap = px.data.gapminder()
    gap = (
        gap.groupby(["year", "continent"])
        .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
        .reset_index()
    )

    return stocks, gap, stocks["date"].min(), stocks["date"].max()


stocks_df, gapminder_df, MIN_TS, MAX_TS = load_data()
MIN_DATE, MAX_DATE = MIN_TS.date(), MAX_TS.date()


# ============================================================================
# UTILITIES
# ============================================================================

def get_header_style():
    return {
        "padding": "18px 20px",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "justifyContent": "space-between",
        "background": f"linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%)",
        "borderRadius": "12px"
    }

def fmt_date(ts: pd.Timestamp) -> str:
    """Format timestamp."""
    return ts.date().strftime("%d-%b-%Y")


def make_badges(start, end) -> list:
    """Create date badges."""
    return [
        dbc.Badge(f"Start: {fmt_date(start)}", color="secondary"),
        dbc.Badge(f"End: {fmt_date(end)}", color="secondary"),
    ]


def normalize_range(start, end) -> tuple:
    """Normalize date range."""
    s = pd.to_datetime(start) if start else MIN_TS
    e = pd.to_datetime(end) if end else MAX_TS
    return (s, e) if s <= e else (e, s)


def make_stocks_fig(df: pd.DataFrame):
    """Create stock chart."""
    if df.empty:
        df = pd.DataFrame({"date": [], **{t: [] for t in CHART["tickers"]}})
    return px.line(df, x="date", y=CHART["tickers"], template=CHART["template"])


# ============================================================================
# COMPONENTS
# ============================================================================


def card(gid: str, title: str = "", height: str = "") -> dbc.Card:
    """Generic card builder for stock charts."""
    h = height or CHART["height"]
    card_content = [
        dbc.CardBody(
            [
                dcc.Graph(id=gid, style={"height": h}),
                html.Div(id=f"{gid}-badges", className="d-flex gap-2 mt-2"),
            ]
        )
    ]
    if title:
        card_content.insert(0, gradient_card_header(title))
    return dbc.Card(card_content, className=f"{STYLE['card']} h-100")

# Card générique pour tout contenu (ex: gapminder)
def custom_card(content, title=None, body_style=None, card_class=None):
    card_items = []
    if title:
        card_items.append(gradient_card_header(title))
    card_items.append(
        dbc.CardBody(content, style=body_style or {})
    )
    return dbc.Card(card_items, className=card_class or STYLE["card"])


def date_card():
    """Card for date range selection."""
    return custom_card(
        [
            dcc.DatePickerRange(
                id="date-range-solution2",
                min_date_allowed=MIN_TS,
                max_date_allowed=MAX_TS,
                start_date=DEFAULT_START,
                end_date=DEFAULT_END,
                display_format="DD-MMM-YYYY",
                first_day_of_week=1,
            ),
            html.Div(
                [
                    dbc.Badge(
                        f"Min: {MIN_DATE.strftime('%d-%b-%Y')}",
                        color="secondary",
                        className="me-2 mt-3",
                    ),
                    dbc.Badge(
                        f"Max: {MAX_DATE.strftime('%d-%b-%Y')}",
                        color="secondary",
                        className="mt-3",
                    ),
                ],
                className="d-flex gap-2 justify-content-center",
            ),
        ],
        title=html.Div([html.I(className="bi bi-calendar me-2"), LABEL_DATE]),
        body_style={"background": "#f8f9fa"},
        card_class=f"{STYLE['card']} mb-3"
    )


def metric_select():
    """InputGroup for metric selection."""
    return dbc.InputGroup(
        [
            dbc.InputGroupText(
                LABEL_METRIC,
                style={
                    "background": GRADIENT,
                    "color": "white",
                    "border": "none",
                    "fontWeight": "bold",
                    "borderRadius": "8px 0 0 8px"
                }
            ),
            dbc.Select(
                id="metric-dropdown-solution2",
                options=METRIC_OPTIONS,
                value="gdpPercap",
            ),
        ],
        className="mb-3",
    )


def gapminder_card():
    """Card for gapminder graph."""
    return custom_card(
        dcc.Graph(id="figure1-solution2", style={"height": CHART["height_gap"]}),
        body_style={
            "background": GRADIENT,
            "borderRadius": "12px",
            "padding": "16px"
        }
    )


def create_layout() -> dbc.Container:
    """Build layout."""
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(
                                        f"{ICON_CHART} Exercice 8.1",
                                        className="text-white fs-6",
                                    ),
                                    html.P(
                                        "Analyse temporelle des cours (GOOG, AAPL)",
                                        className="text-white fs-6",
                                    ),
                                ],
                                style=get_header_style(),
                            ),
                        ],
                        className=STYLE["card"],
                        style={
                            "marginBottom": "8px",
                            "borderRadius": "12px",
                            "boxShadow": "0 4px 15px rgba(0,0,0,0.1)",
                        },
                    ),
                    width=12,
                )
            ),
            dbc.Row(
                dbc.Col(
                    [
                        dbc.Tabs(
                            id="tabs-app-solution2",
                            children=[
                                dbc.Tab(
                                    label="📈 Séries temporelles", tab_id="tab-app-1"
                                ),
                                dbc.Tab(
                                    label="🌍 Indicateurs mondiaux", tab_id="tab-app-2"
                                ),
                            ],
                            active_tab="tab-app-1",
                            className="nav-pills mb-4",
                        ),
                        html.Div(id="tabs-content-solution2"),
                    ],
                    width=12,
                )
            ),
        ],
        fluid=True,
        style=STYLE["container"],
    )


# ============================================================================
# APP
# ============================================================================


def create_app() -> Dash:
    """Create Dash app."""
    app = Dash(
        __name__, external_stylesheets=[THEME], suppress_callback_exceptions=True
    )
    app.layout = create_layout()

    # Suppression des attributs app.* inutiles, tout est généré dynamiquement dans les callbacks
    return app


# ============================================================================
# CALLBACKS
# ============================================================================


@callback(
    Output("my-graph-left-solution2", "figure"),
    Output("my-graph-center-solution2", "figure"),
    Output("my-graph-right-solution2", "figure"),
    Output("my-graph-left-solution2-badges", "children"),
    Output("my-graph-center-solution2-badges", "children"),
    Output("my-graph-right-solution2-badges", "children"),
    Input("date-range-solution2", "start_date"),
    Input("date-range-solution2", "end_date"),
)
def update_stocks(start, end):
    """Update stock charts."""
    s, e = normalize_range(start, end)
    dfs = [
        stocks_df[stocks_df["date"] < s],
        stocks_df[(stocks_df["date"] >= s) & (stocks_df["date"] <= e)],
        stocks_df[stocks_df["date"] > e],
    ]
    return (
        *[make_stocks_fig(df) for df in dfs],
        *[make_badges(b, c) for b, c in [(MIN_TS, s), (s, e), (e, MAX_TS)]],
    )


@callback(
    Output("figure1-solution2", "figure"),
    Input("metric-dropdown-solution2", "value"),
)
def update_gap(metric):
    """Update gapminder chart."""
    return px.bar(
        gapminder_df, x="year", y=metric, color="continent", template=CHART["template"]
    )


@callback(
    Output("tabs-content-solution2", "children"),
    Input("tabs-app-solution2", "active_tab"),
)
def render_tab(tab):
    """Render tab content."""
    if tab == "tab-app-1":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(date_card(), width=12)),
                dbc.Row(
                    [
                        dbc.Col(card("my-graph-left-solution2", "Before Range"), md=4),
                        dbc.Col(
                            card("my-graph-center-solution2", "Selected Range"), md=4
                        ),
                        dbc.Col(card("my-graph-right-solution2", "After Range"), md=4),
                    ],
                    className="g-3",
                ),
            ],
            fluid=True,
        )
    if tab == "tab-app-2":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(metric_select(), md=3)),
                dbc.Row(dbc.Col(gapminder_card(), width=12)),
            ],
            fluid=True,
        )
    return html.Div()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8051)
