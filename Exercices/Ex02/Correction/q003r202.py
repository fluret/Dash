# Import packages
from dash import Dash
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('My new app', className='text-center fs-3 fw-bold')
        ])
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dbc.Label('Please select a state', html_for='state-select')
        ], width=4, className='d-flex align-items-center'),
        dbc.Col([
            dbc.Select(
                id='state-select',
                options=[
                    {'label': 'CA', 'value': 'CA'},
                    {'label': 'FL', 'value': 'FL'},
                    {'label': 'DC', 'value': 'DC'}
                ], 
                value='DC'
            )
        ], width=8)
    ])
], fluid=True, className='p-4')

# Run the App
if __name__ == '__main__':
    app.run(debug=True)