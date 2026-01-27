# Import packages
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc

COLORS = ["red", "orange", "green"]
LABEL_CLASS = "text-center fs-1 fw-bold d-block"
HEADER_ROW_CLASS = "mb-4 bg-light p-3 border border-3 border-primary rounded"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Création directe des composants via variables
label_component = dbc.Label('Text to modify', id='target-text', className=LABEL_CLASS)

radioitems_component = dbc.RadioItems(
    id='color-radio',
    options=[{'label': color.capitalize(), 'value': color} for color in COLORS],
    value='red',
    inline=False,
    input_class_name='me-2',
    label_class_name='mb-2'
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([label_component])
    ], className=HEADER_ROW_CLASS),
    dbc.Row([
        dbc.Col([radioitems_component])
    ])
], fluid=True, className='p-4')

# Callbacks
@app.callback(
    Output('target-text', 'style'),
    Input('color-radio', 'value')
)
def update_target_text(color):
    return {'color': color}

# Run the App
if __name__ == '__main__':
    app.run(debug=True)