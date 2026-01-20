"""
Chart callbacks for updating the graphs and badges based on date selection.
"""
from dash import Input, Output, callback
from data import df
from utils.helpers import normalize_range, make_fig, make_badges


@callback(
    [
        Output("my-graph-left", "figure"),
        Output("my-graph-center", "figure"),
        Output("my-graph-right", "figure"),
        Output("badges-left", "children"),
        Output("badges-center", "children"),
        Output("badges-right", "children"),
    ],
    [
        Input("my-date-picker-range", "start_date"),
        Input("my-date-picker-range", "end_date"),
    ],
)
def plot_dt(start_date, end_date):
    """
    Update all three graphs and their badges when date range changes.
    
    - Left graph: full original date range (MIN_TS to MAX_TS)
    - Center graph: selected date range (start_date to end_date)
    - Right graph: inverted date range (end_date to start_date, normalized)
    """
    start_dt, end_dt = normalize_range(start_date, end_date)
    df_left = df.copy()
    df_center = df[(df["date"] >= start_dt) & (df["date"] <= end_dt)]
    df_right = df[(df["date"] >= end_dt) & (df["date"] <= start_dt)]
    
    fig_left = make_fig(df_left)
    fig_center = make_fig(df_center)
    fig_right = make_fig(df_right)
    
    badges_left = make_badges(df["date"].min(), df["date"].max())
    badges_center = make_badges(start_dt, end_dt)
    badges_right = make_badges(end_dt, start_dt)
    
    return (
        fig_left,
        fig_center,
        fig_right,
        badges_left,
        badges_center,
        badges_right,
    )
