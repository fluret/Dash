from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc

COLORS = ["red", "orange", "green"]
LABEL_CLASS = "text-center fs-1 fw-bold d-block"
HEADER_ROW_CLASS = "mb-4 bg-light p-3 border border-3 border-primary rounded"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Label avec un style initial (fontSize + fontVariant)
label_component = dbc.Label('Text to modify', id='target-text', className=LABEL_CLASS, style={"fontSize": "2rem", "fontVariant": "small-caps"})
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

@app.callback(
    Output('target-text', 'style'),
    Input('color-radio', 'value'),
    State('target-text', 'style')
)
def update_markdown(color, current_style):
    style = dict(current_style) if current_style else {}
    style['color'] = color
    return style

if __name__ == '__main__':
    app.run(debug=True)
