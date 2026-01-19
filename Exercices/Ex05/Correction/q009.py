from dash import Dash, dcc, Output, Input
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
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
title_ = dcc.Markdown(
    children="Gapminder Stacked Bar Charts",
    style={"textAlign": "center", "fontSize": 20},
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
)
graph_ = dcc.Graph(id="figure1", style={'height': '70vh'})

# App Layout
app.layout = dbc.Container(
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
@app.callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
    prevent_initial_call=False,
)
def update_markdown(metric_):
    fig = px.bar(df, x="year", y=metric_, color="continent", template="plotly_dark")
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
