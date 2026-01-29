# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Import data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_table(url, sep=';')

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
continent_dropdown = dcc.Dropdown(id='continent-dropdown', options=df3.continent.unique())
continent_output = html.Div(id='continent-output')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([continent_dropdown], width=8)]),
        dbc.Row([dbc.Col([continent_output], width=8)])
    ]
)

# Configure callback
@app.callback(
    Output(component_id='continent-output', component_property='children'),
    Input(component_id='continent-dropdown', component_property='value')
)
def dropdown_sel(value_dropdown):
    if value_dropdown:
        selection = ("You've selected: "+value_dropdown)
        return selection
    else: ""

# Run the App
if __name__ == '__main__':
    app.run(debug=True)