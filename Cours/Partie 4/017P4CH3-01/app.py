import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR])

header = dbc.NavbarSimple(
    [
        dbc.Nav([
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ])
    ],
    brand="Multi page app | Advanced",
    brand_href='/'
)

app.layout = dbc.Container([header, dash.page_container], fluid=True)

if __name__ == '__main__':
	app.run(debug=False)