
# Import packages
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


print(dbc.__version__)
# Lien CDN Bootstrap Icons
bootstrap_icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css"

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, bootstrap_icons])

# Create app components
# Options communes
options = [
    {"label": "CA", "value": "CA"},
    {"label": "FL", "value": "FL"},
    {"label": "DC", "value": "DC"},
]

# Composant dbc.Select
dropdown1 = dbc.Select(
    options=options,
    value="DC"
)

# Composant dbc.DropdownMenu enrichi
dropdown2 = dbc.DropdownMenu(
    label="List of states",
    children=[
        dbc.DropdownMenuItem([
            html.I(className="bi bi-geo-alt me-2"), "CA"
        ]),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-sun me-2"), "FL"
        ]),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-building me-2"), "DC"
        ])
    ],
    color="primary"
)

# App Layout
app.layout = dbc.Container([
    html.H1("My new application", className="text-center my-4"),
    dbc.Row([
        dbc.Col(html.Label("Please select a state", className="form-label fw-bold"), width=2, align="center"),
        dbc.Col(dropdown1, width=2),
        dbc.Col([], width=8)
    ], className="mb-3 align-items-center"),
    html.Hr(className="my-4 border-3 border-primary rounded-pill", style={"opacity": 0.75}),
    dbc.Row([
        dbc.Col(html.Label("Please select a state", className="form-label fw-bold"), width=2, align="center"),
        dbc.Col(dropdown2, width=2),
        dbc.Col([], width=8)
    ], className="mb-3 align-items-center"),
], fluid=True, className="mt-4")

# Run the App
if __name__ == '__main__':
    app.run(debug=True)