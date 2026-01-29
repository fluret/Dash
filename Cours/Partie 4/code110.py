# version de app.py avec navbar
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
            ],
            nav=True,
            label="Pages",
            align_end=True,
        ),
    ],
    brand="Dash App",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run(debug=True)
