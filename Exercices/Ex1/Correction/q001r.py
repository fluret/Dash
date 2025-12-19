from dash import Dash, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Markdown(children='New title', style={'textAlign': 'left'})
])

if __name__ == '__main__':
    app.run(debug=True)