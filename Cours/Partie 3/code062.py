from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import base64
import io
from dash.dash import no_update


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

upload = dcc.Upload(
    id="upload-data",
    children=html.Div(["Drag & Drop or Click to Select CSV file"]),
    style={
        "width": "100%",
        "height": "10%",
        "lineHeight": "60px",
        "borderStyle": "dashed",
        "textAlign": "center",
    },
)
graph = dcc.Graph(id="graph1")


# App Layout
app.layout = dbc.Container([dbc.Row(dbc.Col(upload)), dbc.Row(dbc.Col(graph))])


@app.callback(Output("graph1", "figure"), Input("upload-data", "contents"))
def update_fig(contents):
    if contents is not None:
        content_type, content_data = contents.split(",")
        # Check if data is CSV
        if "csv" in content_type:
            decoded_data = base64.b64decode(content_data)
            df = pd.read_csv(io.StringIO(decoded_data.decode("utf-8")))
            fig = px.line(df, y="angle")
            return fig
    return no_update


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
