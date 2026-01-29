import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pathlib import Path

# Create Dash app with built-in pages support
pages_folder = str(Path(__file__).parent / "pages")

THEMES = [
    ("CYBORG", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/cyborg/bootstrap.min.css"),
    ("DARKLY", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/darkly/bootstrap.min.css"),
    ("FLATLY", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/flatly/bootstrap.min.css"),
    ("LUX", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/lux/bootstrap.min.css"),
    ("MORPH", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/morph/bootstrap.min.css"),
    ("MINTY", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/minty/bootstrap.min.css"),
    ("PULSE", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/pulse/bootstrap.min.css"),
    ("SANDSTONE", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/sandstone/bootstrap.min.css"),
    ("SKETCHY", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/sketchy/bootstrap.min.css"),
    ("SPACELAB", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/spacelab/bootstrap.min.css"),
    ("SUPERHERO", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/superhero/bootstrap.min.css"),
    ("UNITED", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/united/bootstrap.min.css"),
    ("YETI", "https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/yeti/bootstrap.min.css"),
]

app = Dash(
    __name__,
    use_pages=True,
    pages_folder=pages_folder,
    suppress_callback_exceptions=True,
    external_stylesheets=[],  # On gère le thème dynamiquement
)

nav_links = [
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
]


app.layout = html.Div([
    # Lien dynamique pour le thème Bootstrap
    html.Link(id="theme-link", rel="stylesheet", href=THEMES[0][1]),
    dbc.NavbarSimple(
        nav_links,
        brand="Application Dash MECEN",
        fluid=True,
    ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id="theme-dropdown",
                options=[{"label": name, "value": url} for name, url in THEMES],
                value=THEMES[0][1],
                clearable=False,
                style={"width": "300px"}
            ),
            width="auto",
            style={"display": "flex", "justifyContent": "center", "margin": "20px auto"}
        )
    ], justify="center"),
    dbc.Row(html.Hr(style={"borderWidth": "5px", "borderColor": "#007bff"})),
    dash.page_container,
])

# Callback pour changer dynamiquement le thème Bootstrap

@app.callback(
    Output("theme-link", "href"),
    Input("theme-dropdown", "value")
)
def update_theme(theme_url):
    return theme_url


if __name__ == "__main__":
    app.run(debug=True)
