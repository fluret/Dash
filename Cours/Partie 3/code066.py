# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Select the number of computers to purchase:"),
                        dcc.Dropdown([10, 44, 103], value=10, id="my-dropdown"),
                    ],
                    width=4,
                ),
                dbc.Col([html.Div(id="content")], width=6),
            ]
        )
    ]
)


@app.callback(
    Output("content", "children"),
    Input("my-dropdown", "value"),
)
def toggle_offcanvas(value):
    if value:
        if value < 100:
            return f"You have selected to purchase {value} computers."
        if value > 100:
            return dbc.Alert(
                children="We don't have so many computers in stock. Please select fewer computers",
                color="danger",
            )
    else:
        no_update


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
