# Import libraries
from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Import data into Pandas dataframe
df = px.data.gapminder()

# Create a Dash DataTable
data_table = dash_table.DataTable(id="dataTable1", data=df.to_dict("records"))

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(dbc.Row([dbc.Col([data_table])]))

# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
