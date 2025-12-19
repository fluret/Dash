# Import libraries
import dash
from dash import Dash, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ["Canada", "Brazil", "Norway", "Germany"]
df = df[df["country"].isin(country_list)]

# Filter columns we want to use
df.drop(["continent", "iso_alpha", "iso_num"], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
    id="dataTable1",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
    page_size=10,
    column_selectable="single",
    selected_columns=["lifeExp"],
)

# Base figure factory so we keep one place to tweak styling
def make_figure(y_col: str) -> px.line:
    fig = px.line(df, x="year", y=y_col, color="country", markers=True)
    y_min, y_max = df[y_col].min(), df[y_col].max()
    fig.update_yaxes(autorange=False, range=[y_min, y_max])
    fig.update_layout(yaxis_autorange=False, height=450, margin=dict(t=40, l=40, r=20, b=40))
    return fig


# Create a line graph of life expectancy over time
graph1 = dcc.Graph(id="figure1", figure=make_figure("lifeExp"), style={"height": "450px"})

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    graph1,
                    data_table,
                ]
            )
        ]
    )
)


# Link DataTable edits to the plot with a callback function
@app.callback(Output("figure1", "figure"), Input("dataTable1", "selected_columns"))
def display_output(sel_col):
    if not sel_col:
        return dash.no_update

    return make_figure(sel_col[0])


# Launch the app server
if __name__ == "__main__":
    app.run(debug=True)
