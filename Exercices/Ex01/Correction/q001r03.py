from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

markdown_content = """
# Exemple de titre

Voici une liste à puces :

- Élément 1
- Élément 2
- Élément 3

Ceci est un exemple de contenu markdown sur plusieurs lignes.
"""

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(
            html.H4("Markdown Example", className="text-center mb-0")
        ),
        dbc.CardBody([
            dcc.Markdown(children=markdown_content, className="text-justify")
        ])
    ], className="m-4 shadow-sm")
])

if __name__ == '__main__':
    app.run(debug=True)
