# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app', style={'fontSize': 12})
slider = dcc.Slider(id='our-slider', min=0, max=10, step=1, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([slider], width=9)]),
    ]
)


# Callback
@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-slider', component_property='value')
)
def update_markdown(value_slider):
    markdown_style = {'fontSize': 12+2*value_slider}
    return markdown_style


# Run the App
if __name__ == '__main__':
    app.run(debug=True)