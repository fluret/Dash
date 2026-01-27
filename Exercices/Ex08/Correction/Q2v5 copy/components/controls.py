"""Control components for the two tabs."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from config import (
    DEFAULT_START,
    DEFAULT_END,
    BADGE_COLOR,
    GRADIENT_BG,
    CARD_HEADER_CLASS,
    CONTROL_BODY_CLASS,
    CARD_CLASS,
)
from data import MIN_DATE, MAX_DATE, MIN_TS, MAX_TS


def create_date_range_card():
    from config import CONTROL_FLEX_ROW_STYLE
    BADGE_SHADOW_STYLE = {"boxShadow": "0 2px 8px rgba(0,0,0,0.15)"}
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div([html.I(className="bi bi-calendar me-2"), "Plage de dates"]),
                className=CARD_HEADER_CLASS,
                style={"background": GRADIENT_BG},
            ),
            dbc.CardBody(
                [
                    html.Div([
                        dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, style=BADGE_SHADOW_STYLE),
                        dcc.DatePickerRange(
                            id="date-range-solution2",
                            start_date_placeholder_text="start date",
                            end_date_placeholder_text="end date",
                            min_date_allowed=MIN_TS,
                            max_date_allowed=MAX_TS,
                            start_date=DEFAULT_START,
                            end_date=DEFAULT_END,
                            display_format="DD-MMM-YYYY",
                            first_day_of_week=1,
                        ),
                        dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, style=BADGE_SHADOW_STYLE),
                    ], style=CONTROL_FLEX_ROW_STYLE),
                ],
                className=CONTROL_BODY_CLASS,
            ),
        ],
        className=f"{CARD_CLASS} mb-3",
    )


def create_metric_select(options):
    return dbc.InputGroup(
        [
            dbc.InputGroupText("Metric"),
            dbc.Select(
                id="metric-dropdown-solution2",
                options=options,
                value="gdpPercap",
            ),
        ],
        className="mb-3",
    )
