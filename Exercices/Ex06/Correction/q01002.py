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

# Styles communs
HEADER_CLASS = 'text-center text-white text-uppercase bg-primary py-3 mb-4'
CARD_CLASS = 'shadow-sm border-2 rounded-3 mx-3'
TABLE_STYLE = {
    'cell': {'textAlign': 'center'},
    'header': {'backgroundColor': '#2c3e50', 'color': 'white', 'fontWeight': 'bold'},
    'data_conditional': [{'if': {'row_index': 'odd'}, 'backgroundColor': '#f8f9fa'}]
}

# Composants principaux
header = html.H1("Gapminder Table App", className=HEADER_CLASS)

datatable = dash_table.DataTable(
    id="dataTable1",
    data=df.to_dict("records"),
    columns=[{"name": col, "id": col, "selectable": True} for col in df.columns],
    page_size=25,
    column_selectable="single",
    filter_action="native",
    style_cell=TABLE_STYLE['cell'],
    style_header=TABLE_STYLE['header'],
    style_data_conditional=TABLE_STYLE['data_conditional']
)

table_card = dbc.Card(dbc.CardBody(datatable), className=CARD_CLASS)

app.layout = dbc.Container([
    header,
    table_card
], fluid=True, className='p-0')

# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
