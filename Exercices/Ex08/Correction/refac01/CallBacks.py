import plotly.express as px
import plotly.graph_objs as go
from dash import Output, Input, html
import dash_bootstrap_components as dbc
from styles import CHART
from utils import stocks_df, gapminder_df, normalize_range, make_badges, make_stocks_fig
from components import card, date_card, metric_select, gapminder_card

# Callbacks Dash

def register_callbacks(app, MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE):
    @app.callback(
        Output("my-graph-left-solution2", "figure"),
        Output("my-graph-center-solution2", "figure"),
        Output("my-graph-right-solution2", "figure"),
        Output("my-graph-left-solution2-badges", "children"),
        Output("my-graph-center-solution2-badges", "children"),
        Output("my-graph-right-solution2-badges", "children"),
        Input("date-range-solution2", "start_date"),
        Input("date-range-solution2", "end_date"),
    )
    def update_stocks(start, end):
        try:
            s, e = normalize_range(start, end)
            dfs = [
                stocks_df[stocks_df["date"] < s],
                stocks_df[(stocks_df["date"] >= s) & (stocks_df["date"] <= e)],
                stocks_df[stocks_df["date"] > e],
            ]
            figs = [make_stocks_fig(df, CHART) for df in dfs]
            badges = [make_badges(b, c) for b, c in [(MIN_TS, s), (s, e), (e, MAX_TS)]]
            return (*figs, *badges)
        except Exception as ex:
            import plotly.graph_objs as go
            empty_fig = go.Figure()
            error_badge = [html.Div(f"Erreur: {ex}", style={"color": "red"})]
            return empty_fig, empty_fig, empty_fig, error_badge, error_badge, error_badge

    @app.callback(
        Output("figure1-solution2", "figure"),
        Input("metric-dropdown-solution2", "value"),
    )
    def update_gap(metric):
        return px.bar(
            gapminder_df, x="year", y=metric, color="continent", template=CHART["template"]
        )

    @app.callback(
        Output("tabs-content-solution2", "children"),
        Input("tabs-app-solution2", "active_tab"),
    )
    def render_tab(tab):
        if tab == "tab-app-1":
            return card_tab1(MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE)
        if tab == "tab-app-2":
            return card_tab2()
        return html.Div()


def card_tab1(MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE):
    return dbc.Container([
        dbc.Row(dbc.Col(date_card(MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE), width=12)),
        dbc.Row([
            dbc.Col(card("my-graph-left-solution2", "Before Range"), md=4),
            dbc.Col(card("my-graph-center-solution2", "Selected Range"), md=4),
            dbc.Col(card("my-graph-right-solution2", "After Range"), md=4),
        ], className="g-3"),
    ], fluid=True)

def card_tab2():
    return dbc.Container([
        dbc.Row(dbc.Col(metric_select(), md=3)),
        dbc.Row(dbc.Col(gapminder_card(CHART), width=12)),
    ], fluid=True)
