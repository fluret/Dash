# Import packages
from dash import Dash, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Constants
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980
DEFAULT_CONTINENT = 'Africa'

# UI Constants
EMOJI_GLOBE = '🌍'  # U+1F30D
EMOJI_PIN = '📍'  # U+1F4CD
EMOJI_SPARKLES = '✨'  # U+2728
ALERT_STYLE = {'minHeight': '100px', 'display': 'flex', 'alignItems': 'center'}
CONTAINER_STYLE = {'maxWidth': '1200px'}

# Import and process data
df = (pd.read_csv(DATA_URL, sep=';', decimal=',')
      .loc[lambda x: x['year'] >= MIN_YEAR]
      .groupby('continent')['lifeExp']
      .max()
      .reset_index())

# Precompute continent options
CONTINENT_OPTIONS = [{'label': f'{EMOJI_PIN} {cont}', 'value': cont} for cont in sorted(df.continent.unique())]  # type: ignore[arg-type]

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# app Layout
app.layout = dbc.Container([
    # Header Card
    dbc.Card([
        dbc.CardBody([
            html.H1(f'{EMOJI_GLOBE} Life Expectancy by Continent', className='text-center text-white mb-2'),
            html.P('Data since 1980', className='text-center text-white-50 mb-0')
        ])
    ], className='bg-primary mb-4 shadow'),
    
    # Content
    dbc.Row([
        # Radio selection
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Select Continent', className='mb-0')),
                dbc.CardBody([
                    dbc.RadioItems(
                        id='continent-radio',
                        options=CONTINENT_OPTIONS,
                        value=DEFAULT_CONTINENT,
                        inline=False,
                        label_class_name='mb-3'
                    )
                ])
            ], className='shadow-sm')
        ], md=4),
        
        # Output
        dbc.Col([
            dbc.Alert(
                id='final-output',
                color='info',
                className='fs-5 shadow-sm',
                style=ALERT_STYLE
            )
        ], md=8)
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