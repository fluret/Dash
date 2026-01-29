# Import packages
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import base64

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

image_file = "https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part3/ch11_files/img/plotly.png"
img = html.Img(src=image_file, width=300)
offcanvas_doc = dcc.Link(
    "Off-Canvas documentation",
    id="oc_doc",
    target="_blank",
    href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/offcanvas/",
)
link_doc = dcc.Link(
    "Link documentation",
    id="link_doc",
    target="_blank",
    href="https://dash.plotly.com/dash-core-components/link",
)

offcanvas_layout = dbc.Container(
    [
        dbc.Row([dbc.Col(img)]),
        dbc.Row([dbc.Col(offcanvas_doc)]),
        dbc.Row([dbc.Col(link_doc)]),
    ]
)
offcanvas = html.Div(
    [
        dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            [offcanvas_layout],
            id="offcanvas",
            title="Off-Canvas",
            is_open=False,
        ),
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([offcanvas], width=3),
                dbc.Col(
                    [
                        html.H1(
                            "Content of app here below", style={"textAlign": "center"}
                        ),
                        dcc.Dropdown(["A", "B", "C"], id="main-dropdown"),
                        html.H4("Empty Graph", style={"textAlign": "center"}),
                        dcc.Graph(id="main-graph", style={"height": "500px"}),
                    ],
                    width=9,
                ),
            ]
        )
    ]
)


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    State("offcanvas", "is_open"),
    prevent_initial_call=True
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
