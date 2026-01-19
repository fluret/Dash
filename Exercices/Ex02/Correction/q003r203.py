# Import packages
from dash import Dash, Input, Output, ctx, no_update, ALL
import dash_bootstrap_components as dbc

STATES = ("CA", "FL", "DC")
DEFAULT_STATE = "DC"

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('My new app', className='text-center fs-3 fw-bold')
        ])
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dbc.Label('Please select a state')
        ], width=4, className='d-flex align-items-center'),
        dbc.Col([
            dbc.DropdownMenu(
                id="state-menu",
                label=DEFAULT_STATE,
                children=[
                    dbc.DropdownMenuItem(
                        state,
                        id={"type": "state", "value": state},
                        active=state == DEFAULT_STATE,
                    )
                    for state in STATES
                ],
                color="primary",
                className="w-100"
            )
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Badge(DEFAULT_STATE, id="state-selected", color="secondary", className="mt-3")
        ])
    ])
], fluid=True, className='p-4')


@app.callback(
    Output("state-menu", "label"),
    Output("state-selected", "children"),
    Input({"type": "state", "value": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def update_state_label(_clicks):
    """Met à jour le label du menu et l'affichage sélectionné."""
    trigger = ctx.triggered_id

    if not trigger or "value" not in trigger:
        return no_update, no_update

    selected = trigger["value"]
    return selected, selected

# Run the App
if __name__ == '__main__':
    app.run(debug=True)