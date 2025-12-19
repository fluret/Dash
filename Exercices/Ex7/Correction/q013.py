# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Setup data
df = px.data.tips()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(
    id="our-markdown", children="# Exercise 10.2", style={"textAlign": "center"}
)
data_table = dash_table.DataTable(
    id="input-data",
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
    editable=True,
    page_size=15,
    style_table={"overflowX": "auto"},
    column_selectable="single",
    selected_columns=["tip"],
)
graph = dcc.Graph(id="chart")

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row([dbc.Col(data_table, width=5), dbc.Col(graph, width=7)]),
        dbc.Row([dbc.Col([html.Div(id="content")])]),
    ]
)

def make_figure(df_src: pd.DataFrame, y_col: str = "total_bill"):
    dff = df_src.copy()
    # Convertir la cible en numérique si possible
    if y_col in dff.columns:
        y_vals = pd.to_numeric(dff[y_col], errors="coerce")
        # fallback si aucune valeur numérique valide
        if y_vals.notna().any():
            dff[y_col] = y_vals
        else:
            y_col = "total_bill"
    else:
        y_col = "total_bill"

    fig = px.bar(dff, x="time", y=y_col, color="day")
    fig.update_layout(height=450, margin=dict(t=40, l=40, r=20, b=40))
    return fig


# Configure callbacks
@app.callback(
    Output(component_id="chart", component_property="figure"),
    Output(component_id="content", component_property="children"),
    Input(component_id="input-data", component_property="active_cell"),
    Input(component_id="input-data", component_property="selected_columns"),
    Input(component_id="input-data", component_property="data"),
)
def plot_table(cell, col, table_data):
    triggered = next(iter(ctx.triggered_prop_ids), None)

    # Message utilisateur clair
    if triggered == "input-data.selected_columns":
        sel_txt = ", ".join(col) if col else "(none)"
        message = f"The column selected was: {sel_txt}"
    elif triggered == "input-data.active_cell":
        if cell:
            row = cell.get("row")
            col_id = cell.get("column_id")
            message = f"The active cell selected was row {row}, column '{col_id}'"
        else:
            message = "No active cell selected."
    else:
        message = "Nothing selected yet."

    # Construire la figure à partir des données du tableau et de la colonne choisie si possible
    dff = pd.DataFrame(table_data)
    y_col = col[0] if col else "total_bill"
    fig = make_figure(dff, y_col)
    return fig, message


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
