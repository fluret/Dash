from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Import data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df_ = pd.read_csv(url, sep=';')
df_ = df_.loc[df_['year'] >= 1980, :]
df_ = df_.groupby('continent')['lifeExp'].max().reset_index()
print(df_.head())

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dash_table.DataTable(df_.to_dict('records'))
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)