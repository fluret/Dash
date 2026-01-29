import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

import dash_bootstrap_components as dbc

layout = dbc.Container(
    dbc.Card(
        dbc.CardBody([
            html.I(className="bi bi-house-door-fill display-3 text-primary mb-3"),
            html.H1("Bienvenue sur l'application MECEN", className="mb-4 fw-bold"),
            html.P(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque euismod, nisi eu consectetur consectetur, nisl nisi consectetur nisi, euismod euismod nisi nisi euismod.",
                className="lead mb-4"
            ),
            dbc.Row([
                dbc.Col([
                    html.H5("Pourquoi utiliser cette application ?", className="mb-3 mt-2"),
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            html.I(className="bi bi-lightning-charge-fill text-warning me-2"),
                            "Rapide et intuitive"
                        ], className="d-flex align-items-center border-0 bg-transparent"),
                        dbc.ListGroupItem([
                            html.I(className="bi bi-bar-chart-fill text-success me-2"),
                            "Visualisation claire des données"
                        ], className="d-flex align-items-center border-0 bg-transparent"),
                        dbc.ListGroupItem([
                            html.I(className="bi bi-shield-lock-fill text-info me-2"),
                            "Sécurité et confidentialité"
                        ], className="d-flex align-items-center border-0 bg-transparent"),
                    ], flush=True),
                ], width=12)
            ]),
            html.P(
                "Suspendisse potenti. Etiam ac mauris lectus. Etiam nec lectus urna. Sed sodales ultrices dapibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.",
                className="text-secondary mt-4"
            ),
            dbc.Button("Découvrir les fonctionnalités", href="/about", color="primary", className="mt-4 px-4"),
        ], className="text-center"),
        className="my-5 p-5 bg-light border-0 shadow-lg",
        style={"borderRadius": "2rem"}
    ),
    style={"maxWidth": "700px", "minWidth": "33vw", "margin": "0 auto"}
)