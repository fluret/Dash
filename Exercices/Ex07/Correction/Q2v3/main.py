"""
Main entry point for Q2v3 dashboard.
"""
from app import create_app
from data import load_data
from components.header import create_header
from components.table import create_table
from components.chart import create_chart
from components.buttons import create_plot_button
from utils.helpers import create_card
from callbacks import chart_callbacks  # noqa: F401
import dash_bootstrap_components as dbc
from dash import html
from config import CONTAINER_STYLE

# Initialize app
app = create_app()

# Load data
df = load_data()

# Components
header = create_header()
table = create_table(df)
chart = create_chart()
button = create_plot_button()

# Layout
app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                create_card("Input Data", html.I(className="bi bi-table"), table, 5),
                create_card("Chart", html.I(className="bi bi-graph-up"), chart, 7),
            ],
            className="g-4 mb-3",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Alert(html.Div(id="content"), color="info", className="text-center shadow-sm mb-4"),
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col(button, width=12, lg=6, className="mx-auto"),
            className="mb-4",
        ),
    ],
    fluid=True,
    style=CONTAINER_STYLE,
)


if __name__ == "__main__":
    app.run(debug=True)
