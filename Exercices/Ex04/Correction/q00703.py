
from dash import Dash, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Constantes
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980
EMOJI_GLOBE = '🌍'
EMOJI_PIN = '📍'
EMOJI_SPARKLES = '✨'
ALERT_STYLE = {'minHeight': '100px', 'display': 'flex', 'alignItems': 'center'}
CONTAINER_STYLE = {'width': '80%', 'margin': '0 auto'}

# Données
df = pd.read_csv(DATA_URL, sep=';', decimal=',')
df = df[df['year'] >= MIN_YEAR]
df = df.groupby('continent', as_index=False)['lifeExp'].max()
CONTINENT_LIST = df['continent'].tolist()
DEFAULT_CONTINENT = CONTINENT_LIST[0] if CONTINENT_LIST else None
CONTINENT_OPTIONS = [{'label': f'{EMOJI_PIN} {cont}', 'value': cont} for cont in CONTINENT_LIST]

# App
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# Composants
header_card = dbc.Card([
    dbc.CardBody([
        html.H1(f'{EMOJI_GLOBE} Life Expectancy by Continent', className='text-center text-white mb-2'),
        html.P('Data since 1980', className='text-center text-white-50 mb-0')
    ])
], className='bg-primary mb-4 shadow')

radioitems_component = dbc.RadioItems(
    id='continent-radio',
    options=CONTINENT_OPTIONS,
    value=DEFAULT_CONTINENT,
    inline=False,
    label_class_name='mb-3'
)

radio_card = dbc.Card([
    dbc.CardHeader(html.H5('Select Continent', className='mb-0')),
    dbc.CardBody([radioitems_component])
], className='shadow-sm')

output_component = dbc.Alert(
    id='final-output',
    color='info',
    className='fs-5 shadow-sm',
    style=ALERT_STYLE
)

# Layout
app.layout = dbc.Container([
    header_card,
    dbc.Row([
        dbc.Col([radio_card], md=4),
        dbc.Col([output_component], md=8)
    ])
], fluid=True, className='p-4', style=CONTAINER_STYLE)

# Configure callbacks
@app.callback(
    Output('final-output', 'children'),
    Input('continent-radio', 'value')
)
def update_life_exp(continent):
    life_exp = df.loc[df['continent'] == continent, 'lifeExp'].iloc[0]
    return f'{EMOJI_SPARKLES} The life expectancy in {continent} is {life_exp:.1f} years.'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)