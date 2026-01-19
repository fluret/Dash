# Import packages
from dash import Dash
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components (Bootstrap only)
dropdown1 = dbc.DropdownMenu(
    label="Select state",
    children=[
        dbc.DropdownMenuItem("CA"),
        dbc.DropdownMenuItem("FL"),
        dbc.DropdownMenuItem("DC", active=True),
    ],
    color="primary",
    className="mb-3",
)

# App Layout
app.layout = dbc.Container([
    dropdown1
], fluid=True, className="mt-4")

# Run the App
if __name__ == '__main__':
    app.run(debug=True)