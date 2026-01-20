"""Control components for the two tabs."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from config import DEFAULT_START, DEFAULT_END, BADGE_COLOR
from data import MIN_DATE, MAX_DATE, load_stocks

stocks_df = load_stocks()


def create_date_range_card():
    return dbc.Card(
        [
            dbc.CardHeader("Select Date Range", className="fw-bold"),
            dbc.CardBody(
                [
                    dcc.DatePickerRange(
                        id="date-range-solution2",
                        start_date_placeholder_text="start date",
                        end_date_placeholder_text="end date",
                        min_date_allowed=stocks_df.date.min(),
                        max_date_allowed=stocks_df.date.max(),
                        start_date=DEFAULT_START,
                        end_date=DEFAULT_END,
                        display_format="DD-MMM-YYYY",
                        first_day_of_week=1,
                    ),
                    html.Div(
                        [
                            dbc.Badge(f"Min: {MIN_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="me-2 mt-3"),
                            dbc.Badge(f"Max: {MAX_DATE.strftime('%d-%b-%Y')}", color=BADGE_COLOR, className="mt-3"),
                        ],
                        className="d-flex gap-2 justify-content-center",
                    ),
                ],
                className="text-center",
            ),
        ],
        className="mb-3",
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
