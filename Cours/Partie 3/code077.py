from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Markdown("# Dashboard title", className="bg-primary")],
                    width=10,
                )
            ]
        )
    ]
)
if __name__ == "__main__":
    app.run(debug=True)
