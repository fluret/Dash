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
        html.H5("Menu construit avec dbc.Nav", className="my-3"),
        dbc.Nav(
            [
                dbc.NavLink(page["name"], href=page["path"], active="exact")
                for page in dash.page_registry.values()
                if page["name"].lower() in ["home", "about"]
            ]
            + [
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if page["name"].lower().startswith("graph")
                    ],
                    label="Graphiques",
                    nav=True,
                    in_navbar=True,
                )
            ],
            pills=True,
        ),
        html.H5(
            "Menu construit avec dbc.NavBarSimple",
            className="my-3",
        ),
        dbc.NavbarSimple(
            children=[
                *[
                    dbc.NavItem(
                        dbc.NavLink(
                            page["name"],
                            href=page["path"],
                            active="exact",
                        )
                    )
                    for page in dash.page_registry.values()
                    if not page["name"].lower().startswith("graph")
                ],
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if page["name"].lower().startswith("graph")
                    ],
                    label="Graphiques",
                    nav=True,
                    in_navbar=True,
                ),
            ],
            brand="Navigation Bar Simple",
            fluid=True,
            color="primary",
            dark=True,
            className="my-3",
        ),
        dbc.Row(
            html.Hr(
                style={"borderWidth": "5px", "borderColor": "#007bff"}
            )  # bleu Bootstrap
        ),
        dash.page_container,
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)
