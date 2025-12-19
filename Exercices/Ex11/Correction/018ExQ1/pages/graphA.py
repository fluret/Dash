from dash import Dash, dcc, Output, Input, callback
import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# data
df = px.data.gapminder()
df = (
    df.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# Dash App
dash.register_page(__name__)

# Create app components
title_ = dcc.Markdown(
    children="Gapminder Stacked Bar Charts",
    style={"textAlign": "center", "fontSize": 20},
)
dropdown_ = dcc.Dropdown(
    id="metric-dropdown",
    placeholder="Select a metric",
    options=[
        {"label": "Population", "value": "pop"},
        {"label": "GDP per capita", "value": "gdpPercap"},
        {"label": "Life Expectancy", "value": "lifeExp"},
    ],
    value="pop",
)
graph_ = dcc.Graph(id="figure1", style={"height": "600px"})

# App Layout
layout = dbc.Container(
    [
        dbc.Row([dbc.Col([title_], width=12)]),
        dbc.Row(
            [
                dbc.Col([dropdown_], width=2),
                dbc.Col([graph_], width=10),
            ]
        ),
    ]
)


# Callbacks
@callback(Output("figure1", "figure"), Input("metric-dropdown", "value"))
def update_markdown(metric_):
    fig = px.bar(df, x="year", y=metric_, color="continent", template="plotly_dark")
    return fig
