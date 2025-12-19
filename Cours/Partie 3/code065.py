from dash import Dash, Input, Output, State, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

open_button = dbc.Button("Open", id="open_modal")
close_button = dbc.Button("Close", id="close_modal")


modal = dbc.Modal(
    [
        dbc.ModalHeader(html.H1("Title")),
        dbc.ModalBody("This is the content of the modal"),
        dbc.ModalFooter(close_button),
    ],
    id="modal",
    is_open=False,
)

# App Layout
app.layout = dbc.Container([dbc.Row(dbc.Col([open_button])), dbc.Row(dbc.Col([modal]))])


@app.callback(
    Output("modal", "is_open"),
    Input("open_modal", "n_clicks"),
    Input("close_modal", "n_clicks"),
    State("modal", "is_open"),
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
