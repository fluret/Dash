import dash
from dash import html, dcc

dash.register_page(__name__)

import dash_bootstrap_components as dbc

layout = dbc.Container(
    dbc.Card(
        dbc.CardBody([
            html.H1('À propos', className='mb-4'),
            html.P(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna eu tincidunt consectetur, nisi nisl aliquam enim, eget facilisis massa nunc nec erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
                className="lead mb-4"
            ),
            html.H4("Quelques points clés :", className="mt-4"),
            dbc.ListGroup([
                dbc.ListGroupItem([
                    html.I(className="bi bi-check-circle-fill text-success me-2"),
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                ], className="d-flex align-items-center"),
                dbc.ListGroupItem([
                    html.I(className="bi bi-check-circle-fill text-success me-2"),
                    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                ], className="d-flex align-items-center"),
                dbc.ListGroupItem([
                    html.I(className="bi bi-check-circle-fill text-success me-2"),
                    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris."
                ], className="d-flex align-items-center"),
                dbc.ListGroupItem([
                    html.I(className="bi bi-check-circle-fill text-success me-2"),
                    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore."
                ], className="d-flex align-items-center"),
            ], className="mb-4"),
            html.P(
                "Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Nulla porttitor accumsan tincidunt. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui.",
                className="text-secondary"
            ),
        ], className="text-center"),
        className="my-5 p-5 bg-light border-0 shadow-lg",
        style={"borderRadius": "2rem"}
    ),
    style={"maxWidth": "700px", "minWidth": "33vw", "margin": "0 auto"}
)