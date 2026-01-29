import dash
from dash import html, dcc


layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),
])