# Import libraries
from dash import Dash, dash_table, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ["Canada", "Brazil", "Norway", "Germany"]
df = df[df["country"].isin(country_list)]

# Filter columns we want to use
df.drop(["continent", "iso_alpha", "iso_num"], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
    id="dataTable1",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
    page_size=10,
    column_selectable="single",
    sort_action="native",
    filter_action="native",
)

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        data_table,
                    ]
                ),
            ]
        ),
    ]
)


# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
