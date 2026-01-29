# Import packages
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

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
    value="DC",
    className="mb-3"
)


# Composant dbc.DropdownMenu enrichi
dropdown2 = dbc.DropdownMenu(
    label="Select state",
    children=[
        dbc.DropdownMenuItem("Select an option", header=True),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-geo-alt me-2"), "CA"
        ]),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-sun me-2"), "FL"
        ]),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-building me-2"), "DC"
        ], active=True),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Section 2", header=True),
        dbc.DropdownMenuItem("Option désactivée", disabled=True),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem([
            html.I(className="bi bi-link-45deg me-2"), "Lien Google"
        ], href="https://google.com", target="_blank"),
    ],
    color="primary",
    className="mb-3"
)

# App Layout
app.layout = dbc.Container([
    dropdown1,
    dropdown2
], fluid=True, className="mt-4")

# Run the App
if __name__ == '__main__':
    app.run(debug=True)