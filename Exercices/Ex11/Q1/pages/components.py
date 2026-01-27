import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container([
    html.H1("Aperçu des composants Dash Bootstrap Components", className="mb-4 mt-4 text-primary"),
    dbc.Row([
        dbc.Col([
            html.H5("Boutons"),
            dbc.Button("Primary", color="primary", className="me-2 mb-2"),
            dbc.Button("Secondary", color="secondary", className="me-2 mb-2"),
            dbc.Button("Success", color="success", className="me-2 mb-2"),
            dbc.Button("Warning", color="warning", className="me-2 mb-2"),
            dbc.Button("Danger", color="danger", className="me-2 mb-2"),
            dbc.Button("Info", color="info", className="me-2 mb-2"),
            dbc.Button("Light", color="light", className="me-2 mb-2"),
            dbc.Button("Dark", color="dark", className="me-2 mb-2"),
        ], width=12),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            html.H5("Alertes"),
            dbc.Alert("Ceci est une alerte primaire!", color="primary"),
            dbc.Alert("Ceci est une alerte secondaire!", color="secondary"),
            dbc.Alert("Ceci est une alerte succès!", color="success"),
            dbc.Alert("Ceci est une alerte warning!", color="warning"),
            dbc.Alert("Ceci est une alerte danger!", color="danger"),
            dbc.Alert("Ceci est une alerte info!", color="info"),
            dbc.Alert("Ceci est une alerte light!", color="light"),
            dbc.Alert("Ceci est une alerte dark!", color="dark"),
        ], width=12),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            html.H5("Badges"),
            dbc.Badge("Primary", color="primary", className="me-2"),
            dbc.Badge("Secondary", color="secondary", className="me-2"),
            dbc.Badge("Success", color="success", className="me-2"),
            dbc.Badge("Warning", color="warning", className="me-2"),
            dbc.Badge("Danger", color="danger", className="me-2"),
            dbc.Badge("Info", color="info", className="me-2"),
            dbc.Badge("Light", color="light", className="me-2 text-dark"),
            dbc.Badge("Dark", color="dark", className="me-2"),
        ], width=12),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            html.H5("Cartes"),
            dbc.Card([
                dbc.CardHeader("En-tête de carte"),
                dbc.CardBody([
                    html.H5("Titre de la carte", className="card-title"),
                    html.P("Ceci est un exemple de carte Bootstrap avec Dash.", className="card-text"),
                    dbc.Button("Action", color="primary"),
                ]),
            ], className="mb-3", style={"width": "18rem"}),
        ], width=12),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            html.H5("Progress Bar"),
            dbc.Progress(value=60, color="success", className="mb-2"),
            dbc.Progress(value=40, color="warning", className="mb-2"),
            dbc.Progress(value=80, color="danger", className="mb-2"),
        ], width=12),
    ], className="mb-4"),
    dbc.Row([
            dbc.Col([
                html.H5("Spinner"),
                dbc.Spinner(size="md", color="primary", spinnerClassName="me-2"),
                dbc.Spinner(size="md", color="secondary", spinnerClassName="me-2"),
                dbc.Spinner(size="md", color="success", spinnerClassName="me-2"),
            ], width=12),
    ], className="mb-4"),
], fluid=True)