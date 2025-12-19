from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("population by country", className="card-title"),
                dcc.Dropdown(
                    df.country.unique(),
                    multi=True,
                    value=[df.country[0], df.country[20]],
                    id="my-dropdown",
                ),
                dcc.Graph(id="my-graph"),
            ]
        ),
    ],
    style={"width": "50rem"},
)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([card])),
    ]
)


@app.callback(Output("my-graph", "figure"), Input("my-dropdown", "value"))
def update_graph_card(value):
    dff = df[df.country.isin(value)]
    fig = px.histogram(dff, "country", y="pop")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
