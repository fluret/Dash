"""
Chart callbacks and message handling.
"""
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, html, ctx
from config import DEFAULT_Y_COLUMN, DEFAULT_MESSAGE, COLOR_PALETTE, CHART_HEIGHT
from data import load_data

INITIAL_DATA = load_data().to_dict("records")


def make_figure(df_src: pd.DataFrame, y_col: str = DEFAULT_Y_COLUMN) -> px.bar:
    """Create a bar chart from the dataframe."""
    dff = df_src.copy()

    # Validate and convert column to numeric
    if y_col in dff.columns:
        y_vals = pd.to_numeric(dff[y_col], errors="coerce")
        if y_vals.notna().any():
            dff[y_col] = y_vals
        else:
            y_col = DEFAULT_Y_COLUMN
    else:
        y_col = DEFAULT_Y_COLUMN

    fig = px.bar(
        dff,
        x="time",
        y=y_col,
        color="day",
        title=f"{y_col.replace('_', ' ').title()} by Time and Day",
        color_discrete_sequence=COLOR_PALETTE,
    )
    fig.update_layout(
        height=CHART_HEIGHT,
        margin=dict(t=60, l=40, r=20, b=40),
        template="plotly_white",
        hovermode="x unified",
    )
    return fig


@callback(
    Output("content", "children"),
    Input("input-data", "data"),
    Input("input-data", "active_cell"),
    Input("input-data", "selected_columns"),
    prevent_initial_call=False,
)
def update_message(table_data, cell, col):
    """Update message whenever the table, cell selection, or column selection changes."""
    table_data = table_data or INITIAL_DATA
    dff = pd.DataFrame.from_records(table_data)
    selected_cols = col or []

    # Generate user message (based on last known selection / cell)
    if cell is not None and not dff.empty:
        row = cell.get("row")
        col_id = cell.get("column_id")
        cell_value = dff.at[row, col_id] if (row in dff.index and col_id in dff.columns) else "N/A"
        message = html.Div([
            html.P(f"📍 Active cell: Row {row}, Column '{col_id}'", className="mb-1"),
            html.P(f"💡 Value: {cell_value}", className="mb-0 fw-bold text-primary"),
        ])
    elif selected_cols:
        sel_txt = ", ".join(selected_cols)
        message = html.Div([
            html.P(f"📊 Column selected: {sel_txt}", className="mb-0")
        ])
    else:
        message = html.P(DEFAULT_MESSAGE, className="mb-0")

    return message


@callback(
    Output("chart", "figure"),
    Input("draw", "n_clicks"),
    State("input-data", "selected_columns"),
    State("input-data", "data"),
    prevent_initial_call=False,
)
def update_chart(n_clicks, col, table_data):
    """Update chart only when the button is clicked."""
    # Use INITIAL_DATA if table_data is empty
    table_data = table_data or INITIAL_DATA
    dff = pd.DataFrame.from_records(table_data)

    selected_cols = col or []

    # Build chart only on button click (or initial render)
    y_col = selected_cols[0] if selected_cols else DEFAULT_Y_COLUMN
    fig = make_figure(dff, y_col)

    return fig
