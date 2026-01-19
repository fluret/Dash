from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div([
        dcc.Markdown(children='New title')
    ], className='text-center text-danger')
], fluid=True, className='bg-light p-4 border-bottom border-3 border-primary')

if __name__ == '__main__':
    app.run(debug=True)