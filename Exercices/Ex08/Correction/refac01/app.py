
# Imports optimisés et regroupés
from dash import Dash, html, callback, Output, Input
import dash_bootstrap_components as dbc
from styles import THEME, STYLE, LABEL_TITLE
from utils import MIN_TS, MAX_TS, MIN_DATE, MAX_DATE
from CallBacks import register_callbacks, card_tab1, card_tab2



@callback(
    Output("tabs-content-solution2", "children"),
    Input("tabs-app-solution2", "active_tab"),
)
def render_tab(tab):
    if tab == "tab-app-1":
        return card_tab1(MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE)
    if tab == "tab-app-2":
        return card_tab2()
    return html.Div()



DEFAULT_START = MIN_DATE
DEFAULT_END = MAX_DATE

app = Dash(__name__, external_stylesheets=[THEME], suppress_callback_exceptions=True)

def create_layout():
    return dbc.Container([
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody(
                        [
                            html.H5(LABEL_TITLE, className="text-white fs-6 mb-2", style={"margin": 0}),
                            html.P("Analyse temporelle des cours (GOOG, AAPL)", className="text-white fs-6", style={"margin": 0}),
                        ],
                        style=STYLE["header_body"]
                    ),
                ], className=STYLE["card"], style=STYLE["header"]),
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col([
                dbc.Tabs(
                    id="tabs-app-solution2",
                    children=[
                        dbc.Tab(label="\U0001f4c8 Séries temporelles", tab_id="tab-app-1"),
                        dbc.Tab(label="\U0001f30d Indicateurs mondiaux", tab_id="tab-app-2"),
                    ],
                    active_tab="tab-app-1",
                    className="nav-pills mb-4",
                ),
                html.Div(id="tabs-content-solution2"),
            ], width=12)
        ),
    ], fluid=True, style=STYLE["container"])

app.layout = create_layout()


# ============================================================================
# APP
# ============================================================================


def create_app() -> Dash:
    """Create Dash app."""
    app = Dash(
        __name__, external_stylesheets=[THEME], suppress_callback_exceptions=True
    )
    app.layout = create_layout()

    # Suppression des attributs app.* inutiles, tout est généré dynamiquement dans les callbacks
    return app





# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    app = create_app()
    register_callbacks(app, MIN_TS, MAX_TS, DEFAULT_START, DEFAULT_END, MIN_DATE, MAX_DATE)
    app.run(debug=True, port=8051)
