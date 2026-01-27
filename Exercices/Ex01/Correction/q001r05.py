from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('New title', className='text-center text-warning')
], fluid=True, className='bg-secondary p-4 border-bottom border-3 border-primary')

if __name__ == '__main__':
    app.run(debug=True)
