from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

# Import data
df = px.data.gapminder()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
_header = html.H1(children="Alerts by GDP Per Capita", style={"textAlign": "center"})
_text1 = html.P(
    children="The below alert will adapt depending on GDP for the selected country and year, compared to the world's average GDP",
    style={"textAlign": "center"},
)
year_sel = dcc.Dropdown(
    id="year-dropdown", placeholder="Select a year", options=df.year.unique()
)
country_sel = dcc.Dropdown(
    id="country-dropdown", placeholder="Select a country", options=df.country.unique()
)
alert_msg = dbc.Alert(
    id="alert-gdp", children="Select a year and country to trigger alert", color="info"
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([_header], width=8)]),
        dbc.Row([dbc.Col([_text1], width=8)]),
        dbc.Row([dbc.Col([year_sel], width=4), dbc.Col([country_sel], width=4)]),
        dbc.Row([dbc.Col([alert_msg], width=8)]),
    ]
)


@app.callback(
    Output("alert-gdp", "color"),
    Output("alert-gdp", "children"),
    Input("year-dropdown", "value"),
    Input("country-dropdown", "value"),
    prevent_initial_call=True,
)
def update_alert(y, c):
    gdp_sel = df.loc[
        (df["country"] == c) & (df["year"] == y), "gdpPercap"
    ]  # Filter for selection
    gdp_global_avg = df.loc[
        (df["year"] == y), "gdpPercap"
    ]  # Calculate world avg for the same year

    if (gdp_sel.values.size > 0) & (gdp_global_avg.values.size > 0):
        gdp_sel_v = round(gdp_sel.values[0], 2)
        gdp_avg_v = round(np.mean(gdp_global_avg.values), 2)

        new_children = [
            "The GDP per Capita in "
            + c
            + " in "
            + str(y)
            + " was: "
            + gdp_sel_v.astype(str)
            + "; The world average was: "
            + gdp_avg_v.astype(str)
        ]

        if gdp_sel_v < gdp_avg_v:
            new_color = "danger"
        else:
            new_color = "success"
    else:
        new_color = "dark"
        new_children = "Insufficient Data. Try another selection"

    return new_color, new_children


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
