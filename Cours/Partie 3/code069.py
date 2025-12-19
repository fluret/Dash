# Import packages
from dash import Dash, dcc, Input, Output, html
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Import data
df = px.data.gapminder()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
_header = html.H1(children="Store App", style={"textAlign": "center"})
_text1 = html.P(
    children="The selected countries below will be stored in memory",
    style={"textAlign": "center"},
)
country_sel = dcc.Dropdown(
    id="country-dropdown",
    placeholder="Select countries",
    options=[c for c in df.country.unique()],
    multi=True,
)
mstorage = dcc.Store(id="memory", data=[], storage_type="memory")
sstorage = dcc.Store(id="session", data=[], storage_type="session")
lstorage = dcc.Store(id="local", data=[], storage_type="local")
_subheader41 = html.H4(
    children="Memory Store based chart", style={"textAlign": "center"}
)
_subheader42 = html.H4(
    children="Session Store based chart", style={"textAlign": "center"}
)
_subheader43 = html.H4(
    children="Local Store based chart", style={"textAlign": "center"}
)
_subheader51 = html.H5(children="Memory Store content:", style={"textAlign": "center"})
_subheader52 = html.H5(children="Session Store content:", style={"textAlign": "center"})
_subheader53 = html.H5(children="Local Store content:", style={"textAlign": "center"})

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([_header], width=12)]),
        dbc.Row([dbc.Col([_text1], width=12)]),
        dbc.Row([dbc.Col([country_sel], width=12)]),
        dbc.Row(
            [
                dbc.Col([_subheader41], width=4),
                dbc.Col([_subheader42], width=4),
                dbc.Col([_subheader43], width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([dcc.Graph(id="memory-life-exp-line")], width=4),
                dbc.Col([dcc.Graph(id="session-life-exp-line")], width=4),
                dbc.Col([dcc.Graph(id="local-life-exp-line")], width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([_subheader51], width=2),
                dbc.Col(
                    [
                        html.P(
                            id="memory-output",
                        )
                    ],
                    width=2,
                ),
                dbc.Col([_subheader52], width=2),
                dbc.Col(
                    [
                        html.P(
                            id="session-output",
                        )
                    ],
                    width=2,
                ),
                dbc.Col([_subheader53], width=2),
                dbc.Col(
                    [
                        html.P(
                            id="local-output",
                        )
                    ],
                    width=2,
                ),
            ]
        ),
        mstorage,
        lstorage,
        sstorage,
    ]
)

# Configure callbacks

## Generate callbacks, one per memory type
for store_type in ["memory", "session", "local"]:

    chart_type = store_type + "-life-exp-line"
    output_type = store_type + "-output"

    # Write in memory
    @app.callback(
        Output(store_type, "data"),
        Input("country-dropdown", "value"),
        Input(store_type, "data"),
        prevent_initial_call=True
    )
    def write_memo(new_sel, memo):
        if new_sel is None:
            raise PreventUpdate  # We avoid update the store if there is no selection or if a different memory was selected
        else:
            for c in new_sel:
                if c not in memo:
                    memo.append(c)
        return memo

    ## Update graphs
    @app.callback(Output(chart_type, "figure"), Input(store_type, "data"))
    def plot_gen(memory_sel):
        fig = px.line()
        # Vérifier que memory_sel existe et n'est pas vide
        if memory_sel and len(memory_sel) > 0:
            df_plot = df.loc[df["country"].isin(memory_sel), :]
            fig = px.line(
                df_plot, x="year", y="lifeExp", color="country", template="plotly_white"
            )
        return fig

    ## Output memory content
    @app.callback(Output(output_type, "children"), Input(store_type, "data"))
    def print_memo(current_memory):
        if current_memory is None:
            output = ""
        else:
            output = ", ".join(current_memory)
        return output


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
