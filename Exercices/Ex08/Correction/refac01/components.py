
# Imports regroupés
import dash_bootstrap_components as dbc
from dash import dcc, html
from styles import GRADIENT, STYLE, CHART, LABEL_DATE, LABEL_METRIC, METRIC_OPTIONS

def gradient_card_header(content, className="fw-semibold text-white"):
    return dbc.CardHeader(
        content,
        className=className,
        style={"background": GRADIENT},
    )

def card(gid: str, title: str = "", height: str = ""):
    h = height or CHART["height"]
    card_content = [
        dbc.CardBody([
            dcc.Graph(id=gid, style={"height": h}),
            html.Div(id=f"{gid}-badges", className="d-flex gap-2 mt-2"),
        ])
    ]
    if title:
        card_content.insert(0, gradient_card_header(title))
    return dbc.Card(card_content, className=f"{STYLE['card']} h-100")

def custom_card(content, title=None, body_style=None, card_class=None):
    card_items = []
    if title:
        card_items.append(gradient_card_header(title))
    card_items.append(
        dbc.CardBody(content, style=body_style or {})
    )
    return dbc.Card(card_items, className=card_class or STYLE["card"])

def date_card(MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE):
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
            html.Div([
                dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color="secondary", className="me-2 mt-3"),
                dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color="secondary", className="mt-3"),
            ], className="d-flex gap-2 justify-content-center"),
        ],
        title=html.Div([html.I(className="bi bi-calendar me-2"), LABEL_DATE]),
        body_style={"background": "#f8f9fa"},
        card_class=f"{STYLE['card']} mb-3"
    )

def metric_select():
    return dbc.InputGroup([
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
    ], className="mb-3")

def gapminder_card(CHART):
    return custom_card(
        dcc.Graph(id="figure1-solution2", style={"height": CHART["height_gap"]}),
        body_style={
            "background": GRADIENT,
            "borderRadius": "12px",
            "padding": "16px"
        }
    )
