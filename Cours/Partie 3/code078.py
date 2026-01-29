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
                            "# Dashboard title", className="text-info bg-primary m-2"
                        )
                    ]
                )
            ],
            className="bg-secondary",
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
