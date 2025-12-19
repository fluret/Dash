import dash
from dash import Dash, Input, Output, html, dcc, ctx, no_update
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.iris()
fig = px.scatter(df, x=df.columns[0], y=df.columns[1])

# App Layout
app.layout = dbc.Container(
    [dcc.Markdown(id="content"), dcc.Graph(id="graph-id", figure=fig)]
)


# Configure callbacks
@app.callback(
    Output("content", "children"),
    Input(component_id="graph-id", component_property="selectedData"),
    Input(component_id="graph-id", component_property="clickData"),
    prevent_initial_call=True,
)
def update_graph(selected, clicked):
    triggered_prop_id = ctx.triggered_prop_ids

    if "graph-id.selectedData" in triggered_prop_id:
        if selected:
            return "The x range of the selected data starts from {}".format(
                selected["range"]["x"][0]
            )
        else:
            return no_update

    elif "graph-id.clickData" in triggered_prop_id:
        print(clicked)
        return "The Sepal width of the clicked data is {}".format(
            clicked["points"][0]["y"]
        )


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
