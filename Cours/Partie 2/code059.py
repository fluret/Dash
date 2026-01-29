from dash import Dash, Input, Output, html, dcc, ctx
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = dbc.Container(
    [
        html.Button("Draw Graph", id="draw"),
        html.Button("Reset Graph", id="reset"),
        dcc.Graph(id="graph"),
    ]
)


# Configure callbacks
@app.callback(
    Output("graph", "figure"),
    Input(component_id="reset", component_property="n_clicks"),
    Input(component_id="draw", component_property="n_clicks"),
    prevent_initial_call=True,
)
def update_graph(b1, b2):
    triggered_id = ctx.triggered_id
    print(triggered_id)

    if triggered_id == "reset":
        return go.Figure()  # empty figure

    elif triggered_id == "draw":
        df = px.data.iris()
        return px.scatter(df, x=df.columns[0], y=df.columns[1])


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
