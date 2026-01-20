"""
Main entry point for the Dashboard application.
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
                create_card("Input Data", table, 5),
                create_card("Chart", chart, 7)
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


if __name__ == "__main__":
    app.run(debug=True)
