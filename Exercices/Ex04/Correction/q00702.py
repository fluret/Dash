# Import packages
from dash import Dash, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Constants
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980
DEFAULT_CONTINENT = 'Africa'

# Import and process data
df = (pd.read_csv(DATA_URL, sep=';', decimal=',')
      .loc[lambda x: x['year'] >= MIN_YEAR]
      .groupby('continent')['lifeExp']
      .max()
      .reset_index())

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Life Expectation by continent since 1980', className='text-center fw-bold mb-4')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.RadioItems(
                id='continent-radio',
                options=[{'label': cont, 'value': cont} for cont in df.continent.unique()],
                value=DEFAULT_CONTINENT,
                inline=False,
                label_class_name='mb-2'
            )
        ], width=8)
    ], className='mb-3'),
    dbc.Row([
        dbc.Col([
            html.Div(id='final-output', className='fs-5')
        ], width=6)
    ])
], fluid=True, className='p-4')

# Configure callbacks
@app.callback(
    Output('final-output', 'children'),
    Input('continent-radio', 'value')
)
def update_life_exp(continent):
    life_exp = df.loc[df['continent'] == continent, 'lifeExp'].iloc[0]
    return f'The life expectation in {continent} is: {life_exp:.1f} years.'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)