from dash import Dash, dcc, Output, Input, html, callback
import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from datetime import date
import plotly.express as px

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MORPH])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(page["name"], href=page["path"], active="exact"))
        for page in dash.page_registry.values()
    ],
    brand="My Multipage App",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-3",
)

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container,
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run()
