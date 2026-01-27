import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from pathlib import Path

# Create Dash app with built-in pages support
pages_folder = str(Path(__file__).parent / "pages")

app = Dash(
    __name__,
    use_pages=True,
    pages_folder=pages_folder,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# Layout with navigation links to registered pages
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H2("My multipage app", className="mt-3 mb-4 text-center"),
                    width=12,
                )
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [],
                    width=1,
                ),
                dbc.Col(
                    [
                        html.H6("Menu construit avec dcc.Link", className="mb-2"),
                        *[
                            dcc.Link(
                                f"{page['name']} - {page['path']}",
                                href=page["path"],
                                className="d-block mb-1",
                            )
                            for page in dash.page_registry.values()
                        ],
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H6(
                            "Menu construit avec dbc.ButtonGroup", className="mb-2"
                        ),
                        dbc.ButtonGroup(
                            [
                                *(
                                    dcc.Link(
                                        page["name"],
                                        href=page["path"],
                                        className="btn btn-outline-primary",
                                    )
                                    for page in list(dash.page_registry.values())
                                    if not page["name"].lower().startswith("graph")
                                ),
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(
                                            page["name"], href=page["path"]
                                        )
                                        for page in list(dash.page_registry.values())
                                        if page["name"].lower().startswith("graph")
                                    ],
                                    label="Graph Pages",
                                    color="primary",
                                    className="w-100",
                                    direction="down",
                                    group=True,
                                ),
                            ],
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H6(
                            "Menu construit avec dbc.ButtonGroup vertical",
                            className="mb-2",
                        ),
                        dbc.ButtonGroup(
                            [
                                *(
                                    dcc.Link(
                                        page["name"],
                                        href=page["path"],
                                        className="btn btn-outline-primary",
                                    )
                                    for page in list(dash.page_registry.values())
                                    if not page["name"].lower().startswith("graph")
                                ),
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem(
                                            page["name"], href=page["path"]
                                        )
                                        for page in list(dash.page_registry.values())
                                        if page["name"].lower().startswith("graph")
                                    ],
                                    label="Graph Pages",
                                    color="primary",
                                    className="w-100",
                                    direction="down",
                                    group=True,
                                ),
                            ],
                            vertical=True,
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H6(
                            "Menu construit avec dbc.DropdownMenu", className="mb-2"
                        ),
                        dbc.DropdownMenu(
                            [
                                # Deux premières pages séparées
                                *(
                                    [
                                        dbc.DropdownMenuItem(
                                            page["name"], href=page["path"]
                                        )
                                        for page in list(dash.page_registry.values())
                                        if not page["name"].lower().startswith("graph")
                                    ]
                                ),
                                # Divider et header si pages 'graph' présentes
                                *(
                                    [
                                        dbc.DropdownMenuItem(divider=True),
                                        dbc.DropdownMenuItem("Graphiques", header=True),
                                    ]
                                    if any(
                                        page["name"].lower().startswith("graph")
                                        for page in list(dash.page_registry.values())
                                    )
                                    else []
                                ),
                                # Pages commençant par 'graph'
                                *(
                                    [
                                        dbc.DropdownMenuItem(
                                            page["name"], href=page["path"]
                                        )
                                        for page in list(dash.page_registry.values())
                                        if page["name"].lower().startswith("graph")
                                    ]
                                ),
                            ],
                            label="Toutes les pages",
                            color="primary",
                            className="w-100",
                            direction="down",
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H6("Menu construit avec dbc.ListGroup", className="mb-2"),
                        dbc.ListGroup(
                            [
                                dbc.ListGroupItem(
                                    dcc.Link(
                                        page["name"],
                                        href=page["path"],
                                        className="text-decoration-none",
                                    )
                                )
                                for page in dash.page_registry.values()
                            ]
                        ),
                    ],
                    width=2,
                ),
                dbc.Col([], width=1),
            ],
            className="mb-3",
        ),
        dash.page_container,
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)
