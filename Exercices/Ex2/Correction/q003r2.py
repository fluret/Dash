# Import packages
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
title_ = dcc.Markdown(children='My new app', style={'textAlign': 'center'})
markdown_ = dcc.Markdown(children='Please select a state')
dropdown1 = dcc.Dropdown(options=['CA','FL','DC'], value='DC')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([title_], width=12)]),
        dbc.Row(
            [
                dbc.Col([markdown_], width = 4),
                dbc.Col([dropdown1], width = 8),
            ]
        )
    ]
)

# Run the App
if __name__ == '__main__':
    app.run()