# Import packages
from dash import Dash, Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

TITLES = ['My First app', 'Welcome to the App', 'This is the title']
COLORS = ['red', 'orange', 'green']
BASE_FONT_SIZE = 12

TITLE_COL_CLASS = 'd-flex align-items-center justify-content-center'  # Bootstrap flexbox centering
MB_CLASS = 'mb-3'
FIRST_ROW_CLASS = f"{MB_CLASS} border-bottom"
TITLE_MIN_HEIGHT = '150px'

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout

# Déclaration des composants dans des variables
title_component = html.H1('My First app', id='target-text', className='fw-bold mb-0', style={"fontVariant": "small-caps"})

dropdown_component = dbc.Select(
    id='our-dropdown',
    options=[{'label': title, 'value': title} for title in TITLES],
    value='My First app',
    className=f"{MB_CLASS}"
)

slider_component = dcc.Slider(
    id='our-slider',
    min=16,
    max=52,
    step=1,
    value=0,
    marks={i: str(i) for i in range(0, 11)}
)

radioitems_component = dbc.RadioItems(
    id='color-radio',
    options=[{'label': color.capitalize(), 'value': color} for color in COLORS],
    value='red',
    inline=False,
    label_class_name='mb-2'
)

row1 = dbc.Row([
    dbc.Col(
        [title_component],
        width=12,
        className="d-flex align-items-center justify-content-center h-100",
        style={'minHeight': TITLE_MIN_HEIGHT}
    )
], className=FIRST_ROW_CLASS)

row2 = dbc.Row([
    dbc.Col([dropdown_component], width=3),
    dbc.Col([slider_component], width=9, className=f"{MB_CLASS}")
], className=f"{MB_CLASS}")

row3 = dbc.Row([
    dbc.Col([radioitems_component], width=8)
])

app.layout = dbc.Container([
    row1,
    row2,
    row3
], fluid=True, className='p-4')


# Callbacks
@app.callback(
    Output('target-text', 'children'),
    Output('target-text', 'style'),
    Input('our-dropdown', 'value'),
    Input('our-slider', 'value'),
    Input('color-radio', 'value'),
    State('target-text', 'style')
)
def update_label(dropdown_value, slider_value, radio_value, current_style):
    font_size = BASE_FONT_SIZE + slider_value
    style = dict(current_style) if current_style else {}
    style['color'] = radio_value
    style['fontSize'] = f"{font_size}px"
    return dropdown_value, style

# Run the App
if __name__ == '__main__':
    app.run(debug=True)