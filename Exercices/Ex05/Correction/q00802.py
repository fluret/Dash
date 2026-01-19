from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Data
df = px.data.gapminder()
df = df.groupby(["year", "continent"]).agg({"pop": "sum"}).reset_index()

# Figure
fig = px.bar(df, x="year", y="pop", color="continent", template="plotly_dark")

# App
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

app.layout = dbc.Container([
    dbc.Card([
        dbc.CardBody([
            html.H1("Population by Continent Over Time", className='text-center mb-4'),
            dcc.Graph(figure=fig, style={'height': '70vh'})
        ])
    ], className='shadow mt-4 border-2 rounded-3')
], fluid=True, className='p-4')

if __name__ == '__main__':
    app.run(debug=True)
