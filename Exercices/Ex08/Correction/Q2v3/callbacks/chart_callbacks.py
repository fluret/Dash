"""Chart callbacks for both tabs."""
from dash import Input, Output, callback
import plotly.express as px
from data import load_stocks, load_gapminder, MIN_TS, MAX_TS
from utils.helpers import normalize_range, make_stocks_fig, make_badges
from config import CHART_TEMPLATE

stocks_df = load_stocks()
gapminder_df = load_gapminder()


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
def plot_dt(start_date, end_date):
    start_dt, end_dt = normalize_range(start_date, end_date)

    df_left = stocks_df[stocks_df["date"] < start_dt]
    df_center = stocks_df[(stocks_df["date"] >= start_dt) & (stocks_df["date"] <= end_dt)]
    df_right = stocks_df[stocks_df["date"] > end_dt]

    badges_left = make_badges(MIN_TS, start_dt)
    badges_center = make_badges(start_dt, end_dt)
    badges_right = make_badges(end_dt, MAX_TS)

    return (
        make_stocks_fig(df_left),
        make_stocks_fig(df_center),
        make_stocks_fig(df_right),
        badges_left,
        badges_center,
        badges_right,
    )


@callback(
    Output("figure1-solution2", "figure"),
    Input("metric-dropdown-solution2", "value"),
)
def update_gapminder_chart(metric):
    return px.bar(gapminder_df, x="year", y=metric, color="continent", template=CHART_TEMPLATE)
