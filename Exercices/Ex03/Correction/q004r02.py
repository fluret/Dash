# Import packages
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc

COLORS = ["red", "orange", "green"]

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('Text', id='our-markdown', className='text-center fs-5 fw-bold d-block')
        ], width=12)
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dbc.RadioItems(
                id='our-radio',
                options=[{'label': color.capitalize(), 'value': color} for color in COLORS],
                value='red',
                inline=True,
                input_class_name='me-3'
            )
        ], width=12)
    ])
], fluid=True, className='p-4')

# Callbacks
@app.callback(
    Output('our-markdown', 'style'),
    Input('our-radio', 'value')
)
def update_markdown(color):
    return {'color': color}

# Run the App
if __name__ == '__main__':
    app.run(debug=True)