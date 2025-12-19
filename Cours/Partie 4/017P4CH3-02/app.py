import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_labs import print_registry

# Configure Themes
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# Create app FIRST
app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme2, dbc_css, dbc.icons.FONT_AWESOME], pages_folder='pages')

# Now create theme toggle AFTER app exists
theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

print_registry(exclude="layout")

header = dbc.NavbarSimple(
    [
        dbc.Nav([
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values() if page["module"] != "pages.not_found_404"
        ])
    ],
    brand="Multi page app | Advanced",
    brand_href='/',
    dark=True,
    color='dark'
)

app.layout = dbc.Container([header, theme_toggle, dash.page_container], className="dbc", fluid=True)

if __name__ == '__main__':
	app.run(debug=False)
