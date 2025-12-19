# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id="our-markdown")
button = html.Button(id="our-button", children="Update title", n_clicks=0)

# App Layout
app.layout = dbc.Container([dbc.Row(dbc.Col(markdown)), dbc.Row(dbc.Col(button))])


# Configure callbacks
@app.callback(
    Output(component_id="our-markdown", component_property="children"),
    Input(component_id="our-button", component_property="n_clicks"),
)
def update_title(n_clicks):
    if n_clicks == 0:
        title = "My first app. The button has not been clicked yet."
    else:
        title = "My first app with a button that I have clicked {} times.".format(
            n_clicks
        )
    return title


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
