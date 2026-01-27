
from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# --- Constantes ---
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980

# --- Chargement et traitement des données ---
df_lifeexp_max = (
    pd.read_csv(DATA_URL, sep=';')
      .loc[lambda x: x['year'] >= MIN_YEAR]
      .groupby('continent')['lifeExp']
      .max()
      .reset_index()
)

# --- Initialisation de l'application ---
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --- Création du composant Table ---
table_lifeexp = dbc.Table.from_dataframe(
    df_lifeexp_max,
    striped=True,
    bordered=True,
    hover=True,
    responsive=True,
    className='mt-3'
)

# --- Layout principal ---
app.layout = dbc.Container([
    table_lifeexp
], fluid=True, className='p-4')

# --- Exécution de l'application ---
if __name__ == '__main__':
    app.run(debug=True)