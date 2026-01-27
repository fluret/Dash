# Codes unicode utilisés dans les titres et boutons
ICON_SALES = "\U0001F4CA"  # 📊
ICON_TABLE = "\U0001F4CB"  # 📋
ICON_CHART = "\U0001F4C8"  # 📈
# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Constants
DEFAULT_THEME = dbc.themes.LITERA
CARD_CLASS = "mb-4 shadow-sm border-0"
TABLE_PAGE_SIZE = 15
CARD_HEADER_COLOR = "#667eea"
CARD_ACCENT_COLOR = "#764ba2"

CARD_BODY_STYLE = {
    "height": "50vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

HEADER_STYLE = {
    "background": f"linear-gradient(135deg, {CARD_HEADER_COLOR} 0%, {CARD_ACCENT_COLOR} 100%)",
    "color": "white",
    "padding": "40px 20px",
    "borderRadius": "10px",
    "marginBottom": "30px",
    "textAlign": "center",
    "boxShadow": "0 4px 15px rgba(0,0,0,0.1)"
}

TABLE_HEADER_STYLE = {
    "backgroundColor": CARD_HEADER_COLOR,
    "color": "white",
    "fontWeight": "bold",
    "padding": "12px",
    "borderRadius": "4px"
}

COLOR_PALETTE = ["#667eea", "#764ba2", "#f093fb", "#4facfe"]

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[DEFAULT_THEME])

# Create app components
title = html.Div(
    [
        html.H1(f"{ICON_SALES} Sales Analytics Dashboard", className="mb-0"),
        html.P("Interactive data visualization and analysis", className="text-light mt-2 mb-0")
    ],
    style=HEADER_STYLE
)

graph = dcc.Graph(id="chart")

# Table styles
TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left", "padding": "12px", "fontFamily": "Arial, sans-serif"},
    "style_header": TABLE_HEADER_STYLE,
    "style_data_conditional": [
        {
            "if": {"row_index": "odd"},
            "backgroundColor": f"rgba(102, 126, 234, 0.05)"
        },
        {
            "if": {"column_id": "total_bill"},
            "color": CARD_HEADER_COLOR,
            "fontWeight": "bold"
        }
    ]
}

data_table = dash_table.DataTable(
    id="input-data",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i} for i in df.columns],
    editable=True,
    page_size=TABLE_PAGE_SIZE,
    **TABLE_STYLES
)

button = dbc.Button(
    [html.I(className="bi bi-graph-up me-2"), "Generate Chart"],
    id="draw",
    color="info",
    className="mt-3 w-100 btn-lg",
    n_clicks=0,
    style={"fontWeight": "600", "padding": "12px"}
)


def create_card(title_text, icon, content, width_lg):
    """Create a card with standardized styling and unicode icons."""
    return dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H5(f"{icon} {title_text}", className="mb-0"),
                    style={"backgroundColor": CARD_HEADER_COLOR, "color": "white", "fontWeight": "600"}
                ),
                dbc.CardBody(
                    content,
                    style={**CARD_BODY_STYLE, "padding": "20px"}
                )
            ],
            className="border-0 shadow-sm",
            style={"borderRadius": "8px", "overflow": "hidden"}
        ),
        width=12,
        lg=width_lg
    )


# App Layout
app.layout = dbc.Container(
    [
        title,
        dbc.Row(
            [
                create_card("Input Data", ICON_TABLE, data_table, 5),
                create_card("Chart Visualization", ICON_CHART, graph, 7)
            ],
            className="g-4 mb-4"
        ),
        dbc.Row(
            dbc.Col(button, width=12, lg=6, className="mx-auto"),
            className="mb-5"
        ),
    ],
    fluid=True,
    style={"backgroundColor": "#f8f9fa", "minHeight": "100vh", "padding": "20px"}
)


# Configure callbacks
@app.callback(
    Output("chart", "figure"),
    Input("draw", "n_clicks"),
    State("input-data", "data"),
)
def plot_table(n_clicks, table_data):
    """Update chart based on table data."""
    dff = pd.DataFrame(table_data)
    
    fig = px.scatter(
        dff,
        x="total_bill",
        y="tip",
        color="day",
        size="size",
        hover_data=["sex", "smoker", "time"]
    )
    
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        font={"family": "Arial, sans-serif", "size": 12},
    )
    
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
