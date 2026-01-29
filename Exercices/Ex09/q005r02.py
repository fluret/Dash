from dash import Dash, dcc, Output, Input, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Constants
METRIC_OPTIONS = [
    {"label": "Population", "value": "pop"},
    {"label": "GDP per capita", "value": "gdpPercap"},
    {"label": "Life Expectancy", "value": "lifeExp"},
]
CARD_CLASS = 'shadow-sm rounded-3'

# Data
df = px.data.gapminder()
df = (df.groupby(["year", "continent"])
      .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
      .reset_index())

# Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# App Layout

# Composants principaux
header = dbc.Row([
    dbc.Col([
        html.H1("Gapminder Stacked Bar Charts", className='text-center text-white text-uppercase')
    ], width=12, className='bg-primary mb-3 p-3')
])

dropdown = dbc.Card([
    dbc.CardBody([
        dbc.Label("Select a metric:", className='fw-bold mb-3'),
        dbc.Select(id="metric-dropdown", value="pop", options=METRIC_OPTIONS)
    ])
], className=CARD_CLASS)

graph = dbc.Card([
    dbc.CardBody([
        dcc.Graph(id="figure1", style={'height': '70vh'})
    ])
], className=CARD_CLASS)

main_row = dbc.Row([
    dbc.Col([dropdown], md=3),
    dbc.Col([graph], md=9),
])

app.layout = dbc.Container([
    header,
    main_row
], fluid=True)


# Callbacks
@app.callback(
    Output("figure1", "figure"),
    Input("metric-dropdown", "value"),
)
def update_graph(metric):
    return px.bar(df, x="year", y=metric, color="continent", 
                  template="plotly_dark", barmode="stack")


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
