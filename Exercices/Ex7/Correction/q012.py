# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(
    id="our-markdown", children="# Exercise 10.1", style={"textAlign": "center"}
)
button = html.Button(id="draw", children="Plot Graph", n_clicks=0)
data_table = dash_table.DataTable(
    id="input-data",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i} for i in df.columns],
    editable=True,
    page_size=15,
    style_table={"overflowX": "auto"},
)
graph = dcc.Graph(id="chart")

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row([dbc.Col(data_table, width=5), dbc.Col(graph, width=7)]),
        dbc.Row(
            [
                dbc.Col(button, width=5, style={"textAlign": "center"}),
            ]
        ),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="chart", component_property="figure"),
    Input(component_id="draw", component_property="n_clicks"),
    State(component_id="input-data", component_property="data"),
)
def plot_table(n_clicks, table_data):
    dff = pd.DataFrame(table_data)
    fig = px.bar(dff, x="time", y="total_bill", color="day")
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
