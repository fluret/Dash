from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('My First App')
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
