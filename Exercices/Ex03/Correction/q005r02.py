# Import packages
from dash import Dash, Input, Output, dcc, html
import dash_bootstrap_components as dbc

TITLES = ['My First app', 'Welcome to the App', 'This is the title']
COLORS = ['red', 'orange', 'green']
BASE_FONT_SIZE = 12

TITLE_COL_CLASS = 'd-flex align-items-center justify-content-center'  # Bootstrap flexbox centering
MB_CLASS = 'mb-3'
FIRST_ROW_CLASS = f"{MB_CLASS} border-bottom"
TITLE_MIN_HEIGHT = '100px'

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('My First app', id='our-markdown', className='fw-bold mb-0')
        ], width=8, className=f"{TITLE_COL_CLASS}", style={'minHeight': TITLE_MIN_HEIGHT})
    ], className=FIRST_ROW_CLASS),
    dbc.Row([
        dbc.Col([
            dbc.Select(
                id='our-dropdown',
                options=[{'label': title, 'value': title} for title in TITLES],
                value='My First app',
                className=f"{MB_CLASS}"
            )
        ], width=3),
        dbc.Col([
            dcc.Slider(
                id='our-slider',
                min=0,
                max=10,
                step=1,
                value=0,
                marks={i: str(i) for i in range(0, 11)}
            )
        ], width=9, className=f"{MB_CLASS}")
    ], className=f"{MB_CLASS}"),
    dbc.Row([
        dbc.Col([
            dbc.RadioItems(
                id='our-radio',
                options=[{'label': color.capitalize(), 'value': color} for color in COLORS],
                value='red',
                inline=False,
                label_class_name='mb-2'
            )
        ], width=8)
    ])
], fluid=True, className='p-4')


# Callbacks
@app.callback(
    Output('our-markdown', 'children'),
    Output('our-markdown', 'style'),
    Input('our-dropdown', 'value'),
    Input('our-slider', 'value'),
    Input('our-radio', 'value')
)
def update_label(dropdown_value, slider_value, radio_value):
    font_size = BASE_FONT_SIZE + 2 * slider_value
    return dropdown_value, {'fontSize': font_size, 'color': radio_value}

# Run the App
if __name__ == '__main__':
    app.run(debug=True)