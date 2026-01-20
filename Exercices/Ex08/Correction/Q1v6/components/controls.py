"""
Date picker control component.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc
from datetime import date
from data import df, MIN_DATE, MAX_DATE
from config import (
    CARD_CLASS,
    CARD_HEADER_CLASS,
    CARD_HEADER_COLOR,
    CARD_ACCENT_COLOR,
    CONTROL_BODY_CLASS,
    BADGE_COLOR,
)


def create_controls() -> dbc.Card:
    """Card containing the date picker range."""
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div([html.I(className="bi bi-calendar me-2"), "Plage de dates"]),
                className=CARD_HEADER_CLASS,
                style={"background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)"},
            ),
            dbc.CardBody(
                [
                    dcc.DatePickerRange(
                        id="my-date-picker-range",
                        start_date_placeholder_text="start date",
                        end_date_placeholder_text="end date",
                        min_date_allowed=df.date.min(),
                        max_date_allowed=df.date.max(),
                        start_date=date(2018, 5, 1),
                        end_date=date(2019, 2, 1),
                        display_format="DD-MMM-YYYY",
                        first_day_of_week=1,
                    ),
                    html.Div(
                        [
                            dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="me-2 mt-3"),
                            dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="mt-3"),
                        ],
                        className="d-flex gap-2",
                    ),
                ],
                className=CONTROL_BODY_CLASS,
            ),
        ],
        className=f"{CARD_CLASS} mb-3",
    )
