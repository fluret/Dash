import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/404", name="404")

layout = dbc.Container(
    dbc.Card(
        dbc.CardBody(
            [
                html.I(className="bi bi-emoji-frown display-1 text-danger mb-3"),
                html.H1("404 - Page introuvable", className="text-primary mb-3"),
                html.P(
                    "Désolé, la page que vous cherchez n'existe pas.",
                    className="lead text-secondary mb-4",
                ),
                dbc.Button(
                    "Retour à l'accueil",
                    href="/",
                    color="primary",
                    outline=True,
                ),
            ],
            className="text-center",
        ),
        className="shadow-lg bg-light",
        style={"maxWidth": "500px", "margin": "60px auto"},
    )
)
