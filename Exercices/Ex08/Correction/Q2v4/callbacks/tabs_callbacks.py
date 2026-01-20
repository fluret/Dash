"""Tab rendering callbacks."""
from dash import Input, Output, callback, html, get_app
import dash_bootstrap_components as dbc


@callback(
    Output("tabs-content-solution2", "children"),
    Input("tabs-app-solution2", "active_tab"),
    prevent_initial_call=False,
)
def render_content(active_tab):
    """Render tab content using pre-built components from app instance."""
    app = get_app()

    if active_tab == "tab-app-1":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(app.date_range_card, width=12)),
                dbc.Row(
                    [
                        dbc.Col(app.card_left, md=4),
                        dbc.Col(app.card_center, md=4),
                        dbc.Col(app.card_right, md=4),
                    ],
                    className="g-3",
                ),
            ],
            fluid=True,
        )

    if active_tab == "tab-app-2":
        return dbc.Container(
            [
                dbc.Row(dbc.Col(app.metric_select, md=3)),
                dbc.Row(dbc.Col(app.gapminder_card, width=12)),
            ],
            fluid=True,
        )

    return html.Div()
