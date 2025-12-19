# Import libraries
import dash
from dash import Dash, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Filter columns we want to use
df.drop(['continent', 'iso_alpha', 'iso_num'], axis=1, inplace=True)

# Helper to build the figure with consistent layout and bounded y-axis
def make_figure(dataframe: pd.DataFrame, y_col: str):
    if dataframe.empty or y_col not in dataframe.columns:
        return dash.no_update

    # Coerce numeric columns to avoid type errors after edits
    year = pd.to_numeric(dataframe['year'], errors='coerce')
    y_vals = pd.to_numeric(dataframe[y_col], errors='coerce')
    mask = year.notna() & y_vals.notna()
    df_plot = dataframe.loc[mask].copy()
    df_plot['year'] = year[mask]
    df_plot[y_col] = y_vals[mask]

    if df_plot.empty:
        return dash.no_update

    fig = px.line(df_plot, x='year', y=y_col, color='country', markers=True)
    y_min, y_max = df_plot[y_col].min(), df_plot[y_col].max()

    # Avoid zero-height range when values are constant
    if y_min == y_max:
        y_min -= 1
        y_max += 1

    fig.update_yaxes(autorange=False, range=[y_min, y_max])
    fig.update_layout(yaxis_autorange=False, height=450, margin=dict(t=40, l=40, r=20, b=40))
    return fig


# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i,'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        selected_columns=['lifeExp'],
        editable=True
)

# Create a line graph of life expectancy over time
graph1 = dcc.Graph(id='figure1', figure=make_figure(df, 'lifeExp'), style={'height': '450px'})

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            graph1,
            data_table,
        ])
    ])
)


# Link DataTable edits to the plot with a callback function
@app.callback(
    Output('figure1', 'figure'),
    Input('dataTable1', 'data'),
    Input('dataTable1', 'columns'),
    Input('dataTable1', 'selected_columns')
)
def display_output(rows, columns, sel_col):
    if not sel_col:
        return dash.no_update

    # Create data frame from data table 
    df_cb = pd.DataFrame(rows, columns=[c['name'] for c in columns])

    return make_figure(df_cb, sel_col[0])

# Launch the app server
if __name__ == '__main__':
    app.run(debug=True)