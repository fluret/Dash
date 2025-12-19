# Import packages
from dash import Dash, dcc, Input, Output
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
radio = dcc.RadioItems(id="our-radio", options=["line", "scatter"], value="line")

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(radio, width=1)]),
        dbc.Row(dbc.Col(dcc.Graph(id="our-figure"))),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="our-figure", component_property="figure"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-radio", component_property="value"),
)
def update_graph(value_dropdown, value_radio):
    df_sub = df[df["country"].isin([value_dropdown])]

    if value_radio == "scatter":
        fig = px.scatter(
            df_sub,
            x="year",
            y="lifeExp",
            color="country",
            symbol="continent",
            title="PX {} plot".format(value_radio),
            template="plotly_white",
        )
    else:
        fig = px.line(
            df_sub,
            x="year",
            y="lifeExp",
            color="country",
            symbol="continent",
            title="PX {} plot".format(value_radio),
            template="plotly_white",
        )

    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
