# Import packages
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components


# App Layout
app.layout = dbc.Container([

])

# Run the App
if __name__ == '__main__':
    app.run()