# Import packages
from dash import Dash, dcc, Input, Output, html, no_update
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from datetime import datetime
import pytz

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

_header1 = html.H1(children="Current Time", style={"textAlign": "center"})
_header4 = html.H4(
    children="The New York time below is refreshed whenever the interval component triggers the callback.",
    style={"textAlign": "center"},
)
_p = html.P(
    children="",
    id="livet",
    style={"textAlign": "center", "font-family": "Courier New", "font-size": "250%"},
)
_interval = dcc.Interval(id="int1", disabled=False, interval=2000)

# App Layout
app.layout = dbc.Container(
    [
        _interval,
        dbc.Row([dbc.Col([_header1], width=12)]),
        dbc.Row([dbc.Col([_header4], width=12)]),
        dbc.Row([dbc.Col([_p], width=12)]),
    ]
)


# Configure callback
@app.callback(
    Output("livet", "children"),
    Output("int1", "disabled"),
    Input("int1", "n_intervals"),
    prevent_initial_call=True,
)
def refresh_time(i):
    if i == 0:
        raise PreventUpdate  # Prevent the callback from updating when the app first loads (n_intervals==0)
    elif i < 8:
        tz = pytz.timezone("America/New_York")
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return now, False
    else:
        return no_update, True


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
