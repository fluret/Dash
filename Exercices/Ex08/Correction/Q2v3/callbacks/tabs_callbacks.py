"""Tab rendering callbacks."""
from dash import Input, Output, callback
import dash_bootstrap_components as dbc
from components.controls import create_date_range_card, create_metric_select
from components.graph_card import create_graph_card, create_gapminder_card
from config import METRIC_OPTIONS


@callback(
    Output("tabs-content-solution2", "children"),
    Input("tabs-app-solution2", "active_tab"),
    prevent_initial_call=False,
)
def render_content(active_tab):
    if active_tab == "tab-app-1":
        card_left = create_graph_card("my-graph-left-solution2", "Before Range")
        card_center = create_graph_card("my-graph-center-solution2", "Selected Range")
        card_right = create_graph_card("my-graph-right-solution2", "After Range")

        return dbc.Container(
            [
                dbc.Row(dbc.Col(create_date_range_card(), width=12)),
                dbc.Row(
                    [
                        dbc.Col(card_left, md=4),
                        dbc.Col(card_center, md=4),
                        dbc.Col(card_right, md=4),
                    ],
                    className="g-3",
                ),
            ],
            fluid=True,
        )

    if active_tab == "tab-app-2":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(create_metric_select(METRIC_OPTIONS), md=3)),
                dbc.Row(dbc.Col(create_gapminder_card("figure1-solution2"), width=12)),
            ],
            fluid=True,
        )

    return dbc.Container(fluid=True)
