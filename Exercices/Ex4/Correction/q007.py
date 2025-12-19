# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Import data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df_ = pd.read_csv(url, sep=';')
df_ = df_.loc[df_['year'] >= 1980, :]
df_ = df_.groupby('continent')['lifeExp'].max().reset_index()

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
_header=html.H1(children='Life Expectation by continent since 1980', style={'textAlign': 'center'})
continent_radio=dcc.RadioItems(id='continent-radio', options=df_.continent.unique(), value='Africa')
output_=dcc.Markdown(id='final-output')

# app Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([_header], width=8)]),
        dbc.Row([dbc.Col([continent_radio], width=8)]),
        dbc.Row([dbc.Col([output_], width=6)])
    ]
)

# Configure callbacks
@app.callback(
    Output(component_id='final-output', component_property='children'),
    Input(component_id='continent-radio', component_property='value')
)
def continent_lifeExp(continent_selection):
    lifeExp_value = df_.loc[df_['continent']==continent_selection, 'lifeExp'].values[0]
    output = ('The life expectation in '+continent_selection+' is: '+lifeExp_value+' years.')
    return output

# Run the app
if __name__ == '__main__':
    app.run(debug=True)