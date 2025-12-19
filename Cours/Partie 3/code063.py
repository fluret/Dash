from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and make up the bulk of the card's content.",
                    className="card-text",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([card])),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
