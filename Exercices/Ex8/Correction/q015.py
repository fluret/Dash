# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Import data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

dfG = px.data.gapminder()
dfG = (
    dfG.groupby(["year", "continent"])
    .agg({"pop": "sum", "gdpPercap": "mean", "lifeExp": "mean"})
    .reset_index()
)

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Create app components
title_ = dcc.Markdown(
    children="Exercise 11.2", style={"textAlign": "center", "fontSize": 20}
)
tabs_ = dcc.Tabs(
    id="tabs-app-solution2",
    children=[
        dcc.Tab(label="App One", value="tab-app-1"),
        dcc.Tab(label="App Two", value="tab-app-2"),
    ],
    value="tab-app-1",
)
tabs_content_ = dbc.Container(id="tabs-content-solution2")

# Specific for App 1
date_range_ = dcc.DatePickerRange(
    id="date-range-solution2",
    start_date_placeholder_text="start date",
    end_date_placeholder_text="end date",
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    start_date=date(2018, 5, 1),
    end_date=date(2019, 2, 1),
    display_format="DD-MMM-YYYY",
    first_day_of_week=1,
)
card_L = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id="my-graph-left-solution2"),
        ]
    ),
)
card_C = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id="my-graph-center-solution2"),
        ]
    ),
)
card_R = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id="my-graph-right-solution2"),
        ]
    ),
)
# Specific for App 2
dropdown_ = dcc.Dropdown(
    id="metric-dropdown-solution2",
    placeholder="Select a metric",
    options=[
        {"label": "Population", "value": "pop"},
        {"label": "GDP per capita", "value": "gdpPercap"},
        {"label": "Life Expectancy", "value": "lifeExp"},
    ],
    value="gdpPercap",
    clearable=False,
)
graph_ = dcc.Graph(id="figure1-solution2", style={"height": "600px"})

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col([title_], width=12)),
        dbc.Row(dbc.Col([tabs_, tabs_content_], width=12)),
    ]
)


# Callbacks
@app.callback(
    Output("tabs-content-solution2", "children"), Input("tabs-app-solution2", "value")
)
def render_content(tab):
    if tab == "tab-app-1":
        app1_layout = dbc.Container(
            [
                dbc.Row(
                    dbc.Col([date_range_], width=12, style={"textAlign": "center"})
                ),
                dbc.Row(
                    [
                        dbc.Col([card_L], width=4),
                        dbc.Col([card_C], width=4),
                        dbc.Col([card_R], width=4),
                    ]
                ),
            ]
        )
        return app1_layout

    elif tab == "tab-app-2":
        # App 2 layout
        app2_layout = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col([dropdown_], width=2),
                        dbc.Col([graph_], width=10),
                    ]
                )
            ]
        )
        return app2_layout


# Callback for App1
@app.callback(
    Output("my-graph-left-solution2", "figure"),
    Output("my-graph-center-solution2", "figure"),
    Output("my-graph-right-solution2", "figure"),
    Input(component_id="date-range-solution2", component_property="start_date"),
    Input(component_id="date-range-solution2", component_property="end_date"),
)
def plot_dt(start_date, end_date):
    figL = px.line(
        df.loc[df["date"] < start_date, :],
        x="date",
        y=["GOOG", "AAPL"],
        template="plotly_dark",
    )
    figC = px.line(
        df.loc[(df["date"] >= start_date) & (df["date"] <= end_date), :],
        x="date",
        y=["GOOG", "AAPL"],
        template="plotly_dark",
    )
    figR = px.line(
        df.loc[df["date"] > end_date, :],
        x="date",
        y=["GOOG", "AAPL"],
        template="plotly_dark",
    )

    return figL, figC, figR


# Callback for App2
@app.callback(
    Output("figure1-solution2", "figure"),
    Input("metric-dropdown-solution2", "value"),
    prevent_initial_call=False,
)
def update_markdown(metric_):
    fig = px.bar(dfG, x="year", y=metric_, color="continent", template="plotly_dark")
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
