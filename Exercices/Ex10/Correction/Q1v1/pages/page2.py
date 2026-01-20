# Import packages
import dash
from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Initialise the App
dash.register_page(__name__)

# Import data
dfS = px.data.stocks()
dfS['date'] = pd.to_datetime(dfS['date'], format='%Y-%m-%d')

dfG = px.data.gapminder()
dfG = dfG.groupby(['year','continent']).agg({'pop':'sum', 'gdpPercap':'mean','lifeExp':'mean'}).reset_index()

# Create app components
tab_style = {
    'background-color' : '#800033',
    'fontWeight': 'bold',
    'color' : '#f2f2f2',
    'border': '1px solid #ffe6f0'
}

selected_tab_style = {
    'background-color' : '#800033',
    'fontWeight': 'bold',
    'text-decoration': 'underline',
    'color' : '#f2f2f2',
    'border': '1px solid #ffe6f0'
}

card_style = {
    'padding' : '0px',
    'border' : '0px'
}

title_ = dcc.Markdown(children='Exercise 11.2', style={'textAlign': 'center','fontSize': 20}, className='text-dark')
tabs_ = dcc.Tabs(
            id='tabs-app',
            children=[
                dcc.Tab(label='App One', value='tab-app-1', style=tab_style, selected_style=selected_tab_style),
                dcc.Tab(label='App Two', value='tab-app-2', style=tab_style, selected_style=selected_tab_style)],
            value='tab-app-1'
        )
tabs_content_ = dbc.Container(id='tabs-content', className='p-3')
# Specific for App 1
date_range_ = dcc.DatePickerRange(id='date-range',
    start_date_placeholder_text='start date',
    end_date_placeholder_text='end date',
    min_date_allowed=dfS.date.min(),
    max_date_allowed=dfS.date.max(),
    display_format='DD-MMM-YYYY',
    first_day_of_week = 1)
card_L = dbc.Card([
            dbc.CardBody([
                dcc.Graph(id='my-graph-left'),
        ],
        style = card_style),
    ],
    style = card_style)
card_C = dbc.Card([
            dbc.CardBody([
                dcc.Graph(id='my-graph-center'),
        ],
        style = card_style),
    ],
    style = card_style)
card_R = dbc.Card([
            dbc.CardBody([
                dcc.Graph(id='my-graph-right'),
        ],
        style = card_style),
    ],
    style = card_style)
# Specific for App 2
dropdown_ = dcc.Dropdown(
    id="metric-dropdown",
    placeholder="Select a metric",
    value="pop",
    options=[
        {"label": "Population", "value": "pop"},
        {"label": "GDP per capita", "value": "gdpPercap"},
        {"label": "Life Expectancy", "value": "lifeExp"},
    ],
    className="border border-primary border-2",
)
graph_ = dcc.Graph(id="figure1-2", style={"height": "600px"})

# App layout
layout = dbc.Container(
    [
        dbc.Row(dbc.Col([title_], width = 12)),
        dbc.Row(
            [
                dbc.Col([
                        tabs_,
                        tabs_content_
                ],
                width = 12)
            ]
        )
    ],
    className="bg-danger bg-opacity-75 m-0 p-3 bg-gradient",
    fluid=True,
    style={"height": "100vh"},
)

# Callbacks
@callback(
    Output('tabs-content', 'children'),
    Input('tabs-app', 'value'),
    suppress_callback_exceptions=True)
def render_content(tab):
    if tab == 'tab-app-1':
        app1_layout = dbc.Container(
            [
                dbc.Row(dbc.Col([date_range_], width = 12, style={'textAlign': 'center'})),
                dbc.Row([
                    dbc.Col([card_L], width = 4),
                    dbc.Col([card_C], width = 4),
                    dbc.Col([card_R], width = 4)
                ],
                className = 'p-4'),
            ]
        )
        return app1_layout

    elif tab == 'tab-app-2':
        # App 2 layout
        app2_layout = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col([dropdown_], width=2),
                        dbc.Col([graph_], width=10),
                    ],
                    style={"height": "600px"}
                )
            ]
        )
        return app2_layout

# Callback for App1
@callback(
    Output('my-graph-left','figure'),
    Output('my-graph-center','figure'),
    Output('my-graph-right','figure'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def plot_dt(start_date, end_date):
    figL = px.line(dfS, x='date', y=['GOOG','AAPL'], template = 'plotly_dark')
    figC = figL
    figR = figC
    if start_date is not None:
        figL = px.line(dfS.loc[dfS['date']<start_date, :], x='date', y=['GOOG','AAPL'], template = 'plotly_dark')
        if end_date is not None:
            figC = px.line(dfS.loc[(dfS['date']>=start_date) & (dfS['date']<=end_date), :], x='date', y=['GOOG','AAPL'], template = 'plotly_dark')
    if end_date is not None:
        figR = px.line(dfS.loc[dfS['date']>end_date, :], x='date', y=['GOOG','AAPL'], template = 'plotly_dark')

    return figL, figC, figR

# Callback for App2
@callback(
    Output('figure1-2','figure'),
    Input('metric-dropdown', 'value')
)
def update_markdown(metric_):
    fig = px.bar(dfG, x='year', y=metric_, color='continent', template='plotly_dark')
    return fig