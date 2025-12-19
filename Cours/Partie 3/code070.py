# Import packages
from dash import Dash, dcc, Input, Output, html, dash_table
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# App Layout
app.layout = html.Div(
    [
        html.H1("Store App with Data", style={"textAlign": "center"}),
        dcc.Store(id="memo", data={}, storage_type="session"),
        dcc.Tabs(
            id="store-example-data",
            value="tab-1-data-input",
            children=[
                dcc.Tab(label="Tab One", value="tab-1-data-input"),
                dcc.Tab(label="Tab Two", value="tab-2-data-store"),
            ],
        ),
        html.Div(id="tabs-content"),
    ]
)


# Display tab content, based on the tab selected
@app.callback(Output("tabs-content", "children"), Input("store-example-data", "value"))
def render_content(tab):
    if tab == "tab-1-data-input":
        df = px.data.gapminder()  # Data imported in tab 1
        return html.Div(
            [
                html.H3("Select gapminder data to store in memory"),
                dcc.Dropdown(
                    id="country-dropdown",
                    placeholder="Select a country",
                    options=[c for c in df.country.unique()],
                ),
            ]
        )
    elif tab == "tab-2-data-store":
        return html.Div(
            [html.H3("Selected data from previous Tab"), html.Div(id="data-table")]
        )


# save the filtered dataframe in dcc.Store once user selects dropdown option
@app.callback(
    Output("memo", "data"),
    Input("country-dropdown", "value"),
    prevent_initial_call=True
)
def sel_records(c):  # Write in memory
    if c is None:
        raise PreventUpdate
    else:
        df = px.data.gapminder()  # Data imported in tab 1
        recs = df.loc[(df["country"] == c), :]
    return recs.to_dict("records")


# retrieve the stored data to populate the DataTable shown in tab 2
@app.callback(
    Output("data-table", "children"),
    Input("memo", "data")
)
def show_records(data_):  # Read from memory
    if not data_ or len(data_) == 0:
        return html.P("Select a country in Tab One to see the data")
    
    data_df = pd.DataFrame(data_)
    my_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in data_df.columns],
        data=data_df.to_dict("records"),
    )
    return my_table


if __name__ == "__main__":
    app.run(debug=True)
