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
app.layout = dbc.Container([
    html.H1(
        "Gapminder Table App",
        className='text-center text-white text-uppercase bg-primary py-3 mb-4'
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dash_table.DataTable(
                        id="dataTable1",
                        data=df.to_dict("records"),
                        columns=[{"name": c, "id": c, "selectable": True} for c in df.columns],
                        page_size=25,
                        column_selectable="single",
                        filter_action="native",
                        style_table={'maxHeight': '70vh', 'overflowY': 'auto'},
                        style_cell={'textAlign': 'center'},
                        style_header={
                            'backgroundColor': '#2c3e50',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_data_conditional=[
                            {'if': {'row_index': 'odd'}, 'backgroundColor': '#f8f9fa'}
                        ]
                    )
                ])
            ], className='shadow-sm rounded-3 h-100')
        ], md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="line-chart-1", style={'height': '70vh'})
                ])
            ], className='shadow-sm rounded-3 h-100')
        ], md=6),
    ])
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
