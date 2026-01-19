from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
import plotly.express as px

# Data
df = (px.data.gapminder()
      .query("continent == 'Americas'")
      .drop(columns=["continent", "iso_alpha", "iso_num"]))

# App
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# Layout
app.layout = dbc.Container([
    html.H1("Gapminder Table App", className='text-center text-white text-uppercase bg-primary py-3 mb-4'),
    dbc.Card([
        dbc.CardBody([
            dash_table.DataTable(
                id="dataTable1",
                data=df.to_dict("records"),
                columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
                page_size=25,
                column_selectable="single",
                filter_action="native",
                style_cell={'textAlign': 'center'},
                style_header={'backgroundColor': '#2c3e50', 'color': 'white', 'fontWeight': 'bold'},
                style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#f8f9fa'}]
            )
        ])
    ], className='shadow-sm border-2 rounded-3 mx-3')
], fluid=True, className='p-0')

# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
