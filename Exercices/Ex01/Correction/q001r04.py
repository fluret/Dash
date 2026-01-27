from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

with open("mdexample.md", encoding="utf-8") as f:
    markdown_content = f.read()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Markdown(children=markdown_content)
], fluid=True, className='bg-light p-4 border-bottom border-3 border-primary')

if __name__ == '__main__':
    app.run(debug=True)
