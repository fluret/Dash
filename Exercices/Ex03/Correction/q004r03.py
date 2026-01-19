# Import packages
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc

COLORS = ["red", "orange", "green"]
LABEL_CLASS = "text-center fs-1 fw-bold d-block"
HEADER_ROW_CLASS = "mb-4 bg-light p-3 border border-3 border-primary rounded"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([dbc.Label('Text', id='our-markdown', className=LABEL_CLASS)])
    ], className=HEADER_ROW_CLASS),
    dbc.Row([
        dbc.Col([
            dbc.RadioItems(
                id='our-radio',
                options=[{'label': color.capitalize(), 'value': color} for color in COLORS],
                value='red',
                inline=False,
                input_class_name='me-2',
                label_class_name='mb-2'
            )
        ])
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