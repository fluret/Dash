# Import packages
from dash import Dash, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Setup data
df = px.data.gapminder()
dropdown_list = df["country"].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
dropdown = dcc.Dropdown(
    id="our-dropdown", options=dropdown_list, value=dropdown_list[0]
)
data_table = dash_table.DataTable(id="our-data-table", page_size=10)
graph = dcc.Graph(id="our-figure")

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(dropdown, width=6)),
        dbc.Row(dbc.Col(graph)),
        dbc.Row(dbc.Col(data_table)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="our-figure", component_property="figure"),
    Output(component_id="our-data-table", component_property="data"),
    Input(component_id="our-dropdown", component_property="value"),
)
def update_graph(value_dropdown):
    df_sub = df[df["country"].isin([value_dropdown])]

    fig = px.line(
        df_sub,
        x="year",
        y="lifeExp",
        color="country",
        symbol="continent",
        title="PX line plot",
        template="plotly_white",
    )

    data = df_sub.to_dict("records")
    return fig, data


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
