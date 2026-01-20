# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, callback, ctx
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Constants & styling
DEFAULT_THEME = dbc.themes.LITERA
TABLE_PAGE_SIZE = 15
DEFAULT_Y_COLUMN = "total_bill"
CHART_HEIGHT = 450
DEFAULT_MESSAGE = "Select a column or cell to update the chart"

CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"
CARD_CLASS = "mb-4 shadow-sm border-0"

CARD_BODY_STYLE = {
    "height": "55vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "32px 20px",
    "borderRadius": "12px",
    "marginBottom": "32px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)"
}

TABLE_HEADER_STYLE = {
    "backgroundColor": CARD_HEADER_COLOR,
    "color": "white",
    "fontWeight": "bold",
    "padding": "12px"
}

TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left", "padding": "12px", "fontFamily": "Arial, sans-serif"},
    "style_header": TABLE_HEADER_STYLE,
    "style_data_conditional": [
        {"if": {"row_index": "odd"}, "backgroundColor": "rgba(102, 126, 234, 0.05)"},
        {"if": {"column_id": "total_bill"}, "color": CARD_HEADER_COLOR, "fontWeight": "bold"}
    ]
}

CONTAINER_STYLE = {"backgroundColor": "#f8f9fa", "minHeight": "100vh", "padding": "24px"}
COLOR_PALETTE = ["#667eea", "#764ba2", "#f093fb", "#4facfe"]

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[DEFAULT_THEME])

# Create app components
title = html.Div(
    [
        html.H1("📊 Sales Analytics", className="mb-1"),
        html.P("Interactive exploration of tips data", className="text-light mb-0")
    ],
    style=HEADER_STYLE
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

graph = dcc.Graph(id="chart", style={"height": "100%"})
message_display = html.Div(id="content")

# App Layout
app.layout = dbc.Container(
    [
        title,
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H5("📋 Data Table", className="mb-0 fw-semibold text-white"),
                                           style={"backgroundColor": CARD_HEADER_COLOR}),
                            dbc.CardBody([
                                data_table
                            ], style=CARD_BODY_STYLE)
                        ],
                        className=CARD_CLASS,
                        style={"borderRadius": "10px", "overflow": "hidden"}
                    ),
                    width=12,
                    lg=5
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H5("📈 Chart", className="mb-0 fw-semibold text-white"),
                                           style={"backgroundColor": CARD_HEADER_COLOR}),
                            dbc.CardBody([
                                graph
                            ], style={**CARD_BODY_STYLE, "padding": "16px"})
                        ],
                        className=CARD_CLASS,
                        style={"borderRadius": "10px", "overflow": "hidden"}
                    ),
                    width=12,
                    lg=7
                )
            ],
            className="g-4 mb-3"
        ),
        dbc.Row(
            dbc.Col(
                dbc.Alert(message_display, color="info", className="text-center shadow-sm mb-4"),
                width=12
            )
        ),
    ],
    fluid=True,
    style=CONTAINER_STYLE
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
    triggered_prop = (ctx.triggered[0]["prop_id"] if ctx.triggered else "").split(".")[1] if ctx.triggered else None

    # Defensive copy and default data fallback
    table_data = table_data or df.to_dict("records")
    dff = pd.DataFrame.from_records(table_data)

    # Generate user message
    selected_cols = col or []
    if triggered_prop == "selected_columns":
        sel_txt = ", ".join(selected_cols) if selected_cols else "(none)"
        message = html.Div([
            html.P(f"📊 Column selected: {sel_txt}", className="mb-0")
        ])
    elif triggered_prop == "active_cell":
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
