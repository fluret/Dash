
# --- Imports ---
from dash import Dash, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# --- Constantes ---
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980

# --- Chargement et traitement des données ---
df = pd.read_csv(DATA_URL, sep=';', decimal=',')
df = df[df['year'] >= MIN_YEAR]
df = df.groupby('continent', as_index=False)['lifeExp'].max()
CONTINENT_LIST = df['continent'].tolist()
DEFAULT_CONTINENT = CONTINENT_LIST[0] if CONTINENT_LIST else None

# --- Initialisation de l'application ---
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --- Déclaration des composants ---
title_component = html.H1('Life Expectation by continent since 1980', className='text-center fw-bold mb-4')
radioitems_component = dbc.RadioItems(
    id='continent-radio',
    options=[{'label': cont, 'value': cont} for cont in CONTINENT_LIST],
    value=DEFAULT_CONTINENT,
    inline=False,
    label_class_name='mb-2'
)
output_component = dbc.Row([
    dbc.Col(html.Span('The life expectation in', className='fw-bold'), width=5, style={"textAlign": "right"}),
    dbc.Col(dbc.Badge(id='final-output', color='primary', className='fs-5'), width=7, style={"textAlign": "left"})
], className='align-items-center')

# --- Layout principal ---
app.layout = dbc.Container([
    dbc.Row([dbc.Col([title_component])]),
    dbc.Row([dbc.Col([radioitems_component], width=8)], className='mb-3'),
    dbc.Row([dbc.Col([output_component], width=6)])
], fluid=True, className='p-4')

# --- Callback ---
@app.callback(
    Output('final-output', 'children'),
    Input('continent-radio', 'value')
)
def update_life_exp(continent):
    life_exp = df.loc[df['continent'] == continent, 'lifeExp'].iloc[0]
    return f'{continent} : {life_exp:.1f} years.'

# --- Exécution de l'application ---
if __name__ == '__main__':
    app.run(debug=True)