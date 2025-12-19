# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")

# App Layout 
app.layout = dbc.Container([
    markdown,
    button,
])

# Run the App 
if __name__ == '__main__':
    app.run(debug=True)