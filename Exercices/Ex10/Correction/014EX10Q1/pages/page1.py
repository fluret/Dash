import dash
from dash import Dash, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Dash App
dash.register_page(__name__, path="/")

# data
df = px.data.gapminder()
df = df.groupby(['year','continent']).agg({'pop':'sum', 'gdpPercap':'mean','lifeExp':'mean'}).reset_index()



# Create app components
title_ = dcc.Markdown(
    children="Gapminder Stacked Bar Charts",
    style={"textAlign": "center", "fontSize": 25},
    className="text-warning",
)
dropdown_ = dcc.Dropdown(
    id="metric-dropdown",
    placeholder="Select a metric",
    value="pop",
    options=[
        {"label": "Population", "value": "pop"},
        {"label": "GDP per capita", "value": "gdpPercap"},
        {"label": "Life Expectancy", "value": "lifeExp"},
    ],
    className="border border-primary border-2",
)
graph_ = dcc.Graph(id="figure1-1", style={"height": "600px"})

# App Layout
layout = dbc.Container(
    [
        dbc.Row([dbc.Col([title_], width=12)], className="border-bottom border-dark border-3"),
        dbc.Row(
            [
                dbc.Col([dropdown_], className="p-3", width=2),
                dbc.Col([graph_], className="p-3", width=10),
            ],
            className="m-1",
            justify="evenly",
        ),
    ],
    className="bg-light m-0 p-3",
    fluid=True,
    style={"height": "100vh"},
)

# Callbacks
@callback(
    Output('figure1-1','figure'),
    Input('metric-dropdown', 'value'),
    prevent_initial_call=False
)
def update_markdown(metric_):
    fig = px.bar(df, x='year', y=metric_, color='continent', template='plotly_dark')
    return fig