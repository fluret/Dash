# Import packages
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
text_ = dcc.Markdown(id='our-markdown', children='Text', style={'textAlign': 'center'})
radioitems_ = dcc.RadioItems(id='our-radio', options=['red', 'orange', 'green'], value='red')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([text_], width=12)]),
        dbc.Row([dbc.Col([radioitems_], width=12)]),
    ]
)

# Callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-radio', component_property='value')
)
def update_markdown(value_radio):
    new_style = {'textAlign': 'center', 'color' : value_radio}
    return new_style

# Run the App
if __name__ == '__main__':
    app.run(debug=True)