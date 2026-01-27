from dash import Dash, dash_table, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Data
df = (
    px.data.gapminder()
    .query("continent == 'Americas'")
    .drop(columns=["continent", "iso_alpha", "iso_num"])
)

# App
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# Layout

# Styles communs
HEADER_CLASS = 'text-center text-white text-uppercase bg-primary py-3 mb-4'
CARD_CLASS = 'shadow-sm rounded-3 h-100'
TABLE_STYLE = {
    'table': {'maxHeight': '70vh', 'overflowY': 'auto'},
    'cell': {'textAlign': 'center'},
    'header': {'backgroundColor': '#2c3e50', 'color': 'white', 'fontWeight': 'bold'},
    'data_conditional': [{'if': {'row_index': 'odd'}, 'backgroundColor': '#f8f9fa'}]
}

# Composants principaux
header = html.H1("Gapminder Table App", className=HEADER_CLASS)

datatable = dash_table.DataTable(
    id="dataTable1",
    data=df.to_dict("records"),
    columns=[
        {"name": c, "id": c, "selectable": c not in ["country", "year"]}
        for c in df.columns
    ],
    page_size=25,
    column_selectable="single",
    filter_action="native",
    style_table=TABLE_STYLE['table'],
    style_cell=TABLE_STYLE['cell'],
    style_header=TABLE_STYLE['header'],
    style_data_conditional=TABLE_STYLE['data_conditional']
)

table_card = dbc.Card(dbc.CardBody(datatable), className=CARD_CLASS)

graph = dcc.Graph(id="line-chart-1", style={'height': '70vh'})
graph_card = dbc.Card(dbc.CardBody(graph), className=CARD_CLASS)

main_row = dbc.Row([
    dbc.Col([table_card], md=6),
    dbc.Col([graph_card], md=6),
])

app.layout = dbc.Container([
    header,
    main_row
], fluid=True, className='p-3')


# Callbacks
@app.callback(
    Output("line-chart-1", "figure"),
    Input("dataTable1", "data"),
    Input("dataTable1", "selected_columns"),
)
def display_output(rows, sel_col):
    table_df = pd.DataFrame(rows or df.to_dict("records"))

    y_col = sel_col[0] if sel_col else (table_df.columns[1] if len(table_df.columns) > 1 else table_df.columns[0])
    if y_col not in table_df.columns:
        y_col = table_df.columns[0]

    fig = px.line(table_df, x="year", y=y_col, color="country", markers=True, template="plotly_dark")
    return fig


# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
