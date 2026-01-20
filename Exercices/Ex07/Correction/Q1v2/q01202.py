# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Constants
DEFAULT_THEME = dbc.themes.BOOTSTRAP
CARD_CLASS = "mb-4"
TABLE_PAGE_SIZE = 15
CARD_BODY_STYLE = {
    "height": "50vh",
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto"
}

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[DEFAULT_THEME])

# Create app components
title = dbc.Row(
    dbc.Col(
        html.H1("Exercise 7.1", className="text-center text-primary mt-4 mb-4"),
        width=12
    )
)

graph = dcc.Graph(id="chart")

# Table styles
TABLE_STYLES = {
    "style_table": {"overflowX": "auto", "overflowY": "auto", "height": "100%"},
    "style_cell": {"textAlign": "left"},
    "style_header": {
        "backgroundColor": "rgb(230, 230, 230)",
        "fontWeight": "bold"
    }
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
    "Plot Graph",
    id="draw",
    color="primary",
    className="mt-3 w-100",
    n_clicks=0
)


def create_card(title_text, content, width_lg):
    """Create a card with standardized styling."""
    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                [html.H5(title_text, className="card-title pb-3"), content],
                style=CARD_BODY_STYLE
            ),
            className=CARD_CLASS
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
                create_card("Input Data", data_table, 5),
                create_card("Chart", graph, 7)
            ],
            className="g-3"
        ),
        dbc.Row(
            dbc.Col(button, width=12, lg=5, className="mx-auto"),
            className="d-flex justify-content-center mb-4"
        ),
    ],
    fluid=True
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
    return px.bar(dff, x="time", y="total_bill", color="day")


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
