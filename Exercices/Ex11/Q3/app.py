import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from pathlib import Path

# Create Dash app with built-in pages support
pages_folder = str(Path(__file__).parent / "pages")

url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

app = Dash(
    __name__,
    use_pages=True,
    pages_folder=pages_folder,
    suppress_callback_exceptions=True,
    external_stylesheets=[url_theme2],
)

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "bi bi-sun", "right": "bi bi-moon"},  # Bootstrap Icons
)

nav_items = [
    dbc.NavItem(
        dbc.NavLink(
            page["name"],
            href=page["path"],
            active="exact",
        )
    )
    for page in dash.page_registry.values()
    if not page["name"].lower().startswith("graph") and page["module"] != "pages.not_found_404"
]

dropdown_menu = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem(page["name"], href=page["path"])
        for page in dash.page_registry.values()
        if page["name"].lower().startswith("graph")
    ],
    label="Graphiques",
    nav=True,
    in_navbar=True,
)

# Placer le menu déroulant en avant-dernière position
if len(nav_items) > 1:
    nav_links = nav_items[:-1] + [dropdown_menu] + [nav_items[-1]]
else:
    nav_links = nav_items + [dropdown_menu]

# Layout with navigation links to registered pages
app.layout = (
    dbc.NavbarSimple(
        nav_links,
        brand="Application Dash MECEN",
        fluid=True,
    ),
    html.Div(theme_toggle, style={"display": "flex", "justifyContent": "flex-end", "padding": "0.5rem 1rem"}),
    dbc.Row(html.Hr(style={"borderWidth": "5px", "borderColor": "#007bff"})),
    dash.page_container,
)


if __name__ == "__main__":
    app.run(debug=True)
