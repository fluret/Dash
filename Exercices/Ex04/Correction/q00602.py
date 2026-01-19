from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# Constants
DATA_URL = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
MIN_YEAR = 1980
# Load and process data
df = (pd.read_csv(DATA_URL, sep=';')
      .loc[lambda x: x['year'] >= MIN_YEAR]
      .groupby('continent')['lifeExp']
      .max()
      .reset_index())

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Table.from_dataframe(  # type: ignore
        df,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className='mt-3'
    )
], fluid=True, className='p-4')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)