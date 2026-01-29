# Import packages
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc

# constants


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([


], fluid=True, className='p-4')

# Callbacks


# Run the App
if __name__ == '__main__':
    app.run(debug=True)