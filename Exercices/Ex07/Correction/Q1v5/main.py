"""
Main entry point for the Sales Analytics Dashboard application.
"""
from app import create_app
from data import load_data
from components.header import create_header
from components.table import create_table
from components.chart import create_chart
from components.buttons import create_plot_button
from utils.helpers import create_card
from callbacks import chart_callbacks
import dash_bootstrap_components as dbc
from dash import html
from config import CONTAINER_STYLE


# Initialize app
app = create_app()

# Load data
df = load_data()

# Create components
header = create_header()
table = create_table(df)
chart = create_chart()
button = create_plot_button()

# Create layout
app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                create_card("📋 Input Data", html.I(className="bi bi-table"), table, 5),
                create_card("📈 Chart Visualization", html.I(className="bi bi-graph-up"), chart, 7)
            ],
            className="g-4 mb-4"
        ),
        dbc.Row(
            dbc.Col(button, width=12, lg=6, className="mx-auto"),
            className="mb-5"
        ),
    ],
    fluid=True,
    style=CONTAINER_STYLE
)


if __name__ == "__main__":
    app.run(debug=True)
