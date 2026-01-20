# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, callback, ctx
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Constants
DEFAULT_THEME = dbc.themes.BOOTSTRAP
TABLE_PAGE_SIZE = 15
DEFAULT_Y_COLUMN = "total_bill"
CHART_HEIGHT = 450
DEFAULT_MESSAGE = "Select a column or cell to update the chart"

# Styling constants
CARD_BODY_STYLE = {
    "height": "50vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left", "padding": "10px"},
    "style_header": {
        "backgroundColor": "rgb(230, 230, 230)",
        "fontWeight": "bold"
    }
}

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[DEFAULT_THEME])

# Create app components
title = dbc.Row(
    dbc.Col(
        html.H1("Exercise 10.2", className="text-center text-primary mt-4 mb-4"),
        width=12
    )
)

data_table = dash_table.DataTable(
    id="input-data",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
    editable=True,
    page_size=TABLE_PAGE_SIZE,
    column_selectable="single",
    selected_columns=["tip"],
    **TABLE_STYLES
)

graph = dcc.Graph(id="chart")
message_display = html.Div(id="content", className="mt-3 p-3 bg-light rounded")

# App Layout
app.layout = dbc.Container(
    [
        title,
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5("Data Table", className="card-title mb-3"),
                            data_table
                        ],
                        style=CARD_BODY_STYLE
                        ),
                        className="mb-4 shadow-sm"
                    ),
                    width=12,
                    lg=5
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5("Chart", className="card-title mb-3"),
                            graph
                        ],
                        style=CARD_BODY_STYLE
                        ),
                        className="mb-4 shadow-sm"
                    ),
                    width=12,
                    lg=7
                )
            ],
            className="g-3"
        ),
        dbc.Row(
            dbc.Col(
                dbc.Alert(message_display, color="info", className="text-center"),
                width=12
            )
        ),
    ],
    fluid=True
)

def make_figure(df_src: pd.DataFrame, y_col: str = DEFAULT_Y_COLUMN) -> px.bar:
    """
    Create a bar chart from the dataframe.
    
    Args:
        df_src: Source dataframe
        y_col: Column name for y-axis
        
    Returns:
        Plotly bar chart figure
    """
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

    fig = px.bar(dff, x="time", y=y_col, color="day", title=f"{y_col.replace('_', ' ').title()} by Time and Day")
    fig.update_layout(
        height=CHART_HEIGHT,
        margin=dict(t=60, l=40, r=20, b=40),
        template="plotly_white",
        hovermode="x unified"
    )
    return fig


# Configure callbacks
@callback(
    Output("chart", "figure"),
    Output("content", "children"),
    Input("input-data", "active_cell"),
    Input("input-data", "selected_columns"),
    Input("input-data", "data"),
)
def update_chart_and_message(cell, col, table_data):
    """
    Update chart and display message based on user interaction.
    
    Args:
        cell: Active cell information
        col: Selected columns list
        table_data: Current table data
        
    Returns:
        Tuple of (figure, message)
    """
    triggered = ctx.triggered_id

    # Defensive copy and default data fallback
    table_data = table_data or df.to_dict("records")
    dff = pd.DataFrame.from_records(table_data)

    # Generate user message
    selected_cols = col or []
    if triggered == "input-data.selected_columns":
        sel_txt = ", ".join(selected_cols) if selected_cols else "(none)"
        message = html.Div([
            html.P(f"📊 Column selected: {sel_txt}", className="mb-0")
        ])
    elif triggered == "input-data.active_cell":
        if cell and dff.shape[0] > 0:
            row = cell.get("row")
            col_id = cell.get("column_id")
            # Get cell value safely
            cell_value = dff.at[row, col_id] if (row is not None and col_id in dff.columns and row in dff.index) else "N/A"
            message = html.Div([
                html.P(f"📍 Active cell: Row {row}, Column '{col_id}'", className="mb-1"),
                html.P(f"💡 Value: {cell_value}", className="mb-0 fw-bold text-primary")
            ])
        else:
            message = html.P("No active cell selected", className="mb-0")
    else:
        message = html.P(DEFAULT_MESSAGE, className="mb-0")

    # Build chart from table data and selected column
    y_col = selected_cols[0] if selected_cols else DEFAULT_Y_COLUMN
    fig = make_figure(dff, y_col)

    return fig, message


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
