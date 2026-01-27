# Codes unicode utilisés dans les messages
ICON_SALES = "\U0001F4CA"  # 📊
ICON_TABLE = "\U0001F4CB"  # 📋
ICON_CHART = "\U0001F4C8"  # 📈
ICON_POINTER = "\U0001F4CD"  # 📍
ICON_BULB = "\U0001F4A1"  # 💡
# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, callback, ctx
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Constants & styling

# === THEME & STYLE ===
DEFAULT_THEME = dbc.themes.LITERA
TABLE_PAGE_SIZE = 15
DEFAULT_Y_COLUMN = "total_bill"
CHART_HEIGHT = 450
DEFAULT_MESSAGE = "Select a column or cell to update the chart"

# Palette et couleurs principales
PRIMARY_COLOR = "#667eea"
ACCENT_COLOR = "#764ba2"
COLOR_PALETTE = [PRIMARY_COLOR, ACCENT_COLOR, "#f093fb", "#4facfe"]

# Styles fusionnés et simplifiés
CARD_CLASS = "mb-4 shadow-sm border-0"
CARD_BODY_STYLE = {
    "height": "55vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto",
}
HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {PRIMARY_COLOR} 0%, {ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "32px 20px",
    "borderRadius": "12px",
    "marginBottom": "32px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)",
}
TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {
        "textAlign": "left",
        "padding": "12px",
        "fontFamily": "Arial, sans-serif",
    },
    "style_header": {
        "backgroundColor": PRIMARY_COLOR,
        "color": "white",
        "fontWeight": "bold",
        "padding": "12px",
    },
    "style_data_conditional": [
        {"if": {"row_index": "odd"}, "backgroundColor": "rgba(102, 126, 234, 0.05)"},
        {
            "if": {"column_id": "total_bill"},
            "color": PRIMARY_COLOR,
            "fontWeight": "bold",
        },
    ],
}
CONTAINER_STYLE = {
    "backgroundColor": "#f8f9fa",
    "minHeight": "100vh",
    "padding": "24px",
}

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[DEFAULT_THEME])

# Create app components
title = html.Div(
    [
        html.H1(f"{ICON_SALES} Sales Analytics", className="mb-1"),
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
    **TABLE_STYLES,
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
                            dbc.CardHeader(
                                html.H5(
                                    f"{ICON_TABLE} Data Table",
                                    className="mb-0 fw-semibold text-white",
                                ),
                                style={"backgroundColor": PRIMARY_COLOR},
                            ),
                            dbc.CardBody([data_table], style=CARD_BODY_STYLE),
                        ],
                        className=CARD_CLASS,
                        style={"borderRadius": "10px", "overflow": "hidden"},
                    ),
                    width=12,
                    lg=5,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                html.H5(
                                    f"{ICON_CHART} Chart", className="mb-0 fw-semibold text-white"
                                ),
                                style={"backgroundColor": PRIMARY_COLOR},
                            ),
                            dbc.CardBody(
                                [graph], style={**CARD_BODY_STYLE, "padding": "16px"}
                            ),
                        ],
                        className=CARD_CLASS,
                        style={"borderRadius": "10px", "overflow": "hidden"},
                    ),
                    width=12,
                    lg=7,
                ),
            ],
            className="g-4 mb-3",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Alert(
                    message_display,
                    color="info",
                    className="text-center shadow-sm mb-4",
                ),
                width=12,
            )
        ),
    ],
    fluid=True,
    style=CONTAINER_STYLE,
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
    # Vérification explicite de la colonne y
    y_col_final = y_col if y_col in dff.columns else DEFAULT_Y_COLUMN
    y_vals = pd.to_numeric(dff.get(y_col_final, pd.Series()), errors="coerce")
    if y_vals.notna().any():
        dff[y_col_final] = y_vals
    else:
        y_col_final = DEFAULT_Y_COLUMN

    fig = px.scatter(
        dff,
        x="total_bill",
        y=y_col_final,
        color="day",
        size="size",
        hover_data=["sex", "smoker", "time"],
    )
    fig.update_layout(
        height=CHART_HEIGHT,
        margin=dict(t=60, l=40, r=20, b=40),
        template="plotly_white",
        hovermode="x unified",
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
    triggered_prop = (
        ctx.triggered[0]["prop_id"].split(".")[1] if ctx.triggered else None
    )
    table_data = table_data if table_data is not None else df.to_dict("records")
    dff = pd.DataFrame.from_records(table_data)
    selected_cols = col or []

    # Gestion simplifiée des messages
    if triggered_prop == "active_cell" and cell and dff.shape[0] > 0:
        row = cell.get("row", 0)
        col_id = cell.get("column_id", DEFAULT_Y_COLUMN)
        cell_value = (
            dff.at[row, col_id]
            if (row in dff.index and col_id in dff.columns)
            else "N/A"
        )
        message = html.Div(
            [
                html.P(
                    f"{ICON_POINTER} Active cell: Row {row}, Column '{col_id}'", className="mb-1"
                ),
                html.P(
                    f"{ICON_BULB} Value: {cell_value}", className="mb-0 fw-bold text-primary"
                ),
            ]
        )
    elif triggered_prop == "selected_columns":
        sel_txt = ", ".join(selected_cols) if selected_cols else "(none)"
        message = html.P(f"{ICON_SALES} Column selected: {sel_txt}", className="mb-0")
    else:
        message = html.P(DEFAULT_MESSAGE, className="mb-0")

    # Choix de la colonne y simplifié
    y_col = next((c for c in selected_cols if c in dff.columns), DEFAULT_Y_COLUMN)
    fig = make_figure(dff, y_col)
    return fig, message


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
