from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


df = px.data.gapminder()

df_2007 = df[df.year == 2007]

fig1 = px.scatter(
    df_2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60
)
graph1 = dcc.Graph(id="figure1", figure=fig1)

fig2 = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    size_max=40,
    hover_name="country",
    log_x=True,
    animation_frame="year",
    animation_group="country",
    range_x=[100, 100000],
    range_y=[25, 90],
)
graph2 = dcc.Graph(id="figure2", figure=fig2)

fig3 = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=px.colors.sequential.Plasma,
    projection="natural earth",
)
graph3 = dcc.Graph(id="figure3", figure=fig3)

tab1_content = dbc.Card(
    dbc.CardBody([graph1]),
)

tab2_content = dbc.Card(
    dbc.CardBody([graph2]),
)

tab3_content = dbc.Card(
    dbc.CardBody([graph3]),
)

tabs = dbc.Tabs(
    [
        dbc.Tab(children=tab1_content, label="Tab 1"),
        dbc.Tab(children=tab2_content, label="Tab 2"),
        dbc.Tab(children=tab3_content, label="Tab 3"),
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([tabs])),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
