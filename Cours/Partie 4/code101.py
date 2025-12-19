# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from functools import lru_cache
import plotly.express as px
import time

# Setup data
df = px.data.gapminder()[["country", "year", "lifeExp"]]
dropdown_list = df["country"].unique()


# Define own functionality and initialise cache
@lru_cache(maxsize=len(dropdown_list))
def calculation_function(string):
    time.sleep(3)
    return string


# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
dropdown = dcc.Dropdown(
    id="our-dropdown", options=dropdown_list, value=dropdown_list[0]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown)]),
        dbc.Row([dbc.Col(dbc.Spinner(children=dcc.Graph(id="our-figure")))]),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="our-figure", component_property="figure"),
    Input(component_id="our-dropdown", component_property="value"),
)
def update_graph(value_dropdown):
    calculation_function(value_dropdown)
    df_sub = df[df["country"].isin([value_dropdown])]
    fig = px.scatter(
        df_sub,
        x="year",
        y="lifeExp",
        title="PX scatter plot",
        template="plotly_white",
    )
    fig.update_traces(marker=dict(size=20))
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
