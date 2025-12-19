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
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

# Create app components
title_ = dcc.Markdown(
    children="Gapminder Stacked Bar Charts",
    style={"textAlign": "center", "fontSize": 20},
    className="text-warning"
)
dropdown_ = dcc.Dropdown(
    id="metric-dropdown",
    placeholder="Select a metric",
    options=[
        {"label": "Population", "value": "pop"},
        {"label": "GDP per capita", "value": "gdpPercap"},
        {"label": "Life Expectancy", "value": "lifeExp"},
    ],
    value="gdpPercap",
    clearable=False,
)
graph_ = dcc.Graph(id="figure1", style={"height": "100%"})

slider_1 = dcc.Slider(min=0, max=10)
slider_2 = dcc.Slider(min=0, max=10)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [dbc.Col([title_])],
            className="m-3",
        ),
        dbc.Row(
            [
                dbc.Col([dropdown_], className="col-2 p-3"),
                dbc.Col([graph_], className="col-10 h-75 border border-warning border-1 rounded-3"),
            ],
            className="flex-fill",
        ),
        dbc.Row(
            [
                dbc.Col([slider_1], className="col-4"),
                dbc.Col([slider_2], className="col-6"),
            ],
            justify="center",
            className="p-5",
        ),
    ],
    className="min-vh-100 border border-warning border-4 rounded-4 mx-auto p-4 d-flex flex-column",
    style={"height": "100vh", "overflow": "auto"}
)


# Callbacks
@app.callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_graph(metric_):
    fig = px.bar(df, x="year", y=metric_, color="continent", template="plotly_dark")
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
