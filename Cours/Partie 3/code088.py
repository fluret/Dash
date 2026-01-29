from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-4 p-2",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 mt-1 p-3",
)
if __name__ == "__main__":
    app.run(debug=True)
