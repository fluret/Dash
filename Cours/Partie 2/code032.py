from dash import Dash, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# data
df = px.data.gapminder()
df_filtered = df[df['country'].isin(['Canada', 'Brazil', 'Norway', 'Germany'])]

# figure
fig = px.line(df_filtered, x='year', y='lifeExp', color='country')

# Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='figure1', figure=fig)
        ], width = 8)
    ])
])

if __name__== '__main__':
    app.run(debug=True)