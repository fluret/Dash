from dash import Dash, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Import data & perform data-preprocessing
df = px.data.gapminder()
df = df.loc[df["continent"] == "Americas", :]
df.drop(["continent", "iso_alpha", "iso_num"], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
    id="dataTable1",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
    page_size=15,
    column_selectable="single",
    filter_action="native",
)

# Create the Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
title_ = dcc.Markdown(
    children="Gapminder Table App", style={"textAlign": "center", "fontSize": 20}
)

app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([title_], width=12)]),
        dbc.Row([dbc.Col([data_table], width=6)]),
    ]
)

# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
