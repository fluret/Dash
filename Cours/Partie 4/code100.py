# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import datashader as ds
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px

# Setup data
df = px.data.gapminder()[["continent", "year", "lifeExp"]]
dropdown_list = df["continent"].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id="our-markdown")
dropdown = dcc.Dropdown(
    id="our-dropdown", options=dropdown_list, value=dropdown_list[0]
)
markdown_scatter = dcc.Markdown(id="markdown-scatter")
slider = dcc.Slider(id="our-slider", min=1, max=50000, marks=None, value=1)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id="our-figure"))]),
        dbc.Row([dbc.Col(markdown_scatter)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="our-markdown", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df["continent"].isin([value_dropdown])]
    title = "Data points aggregated: {:,}".format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id="our-figure", component_property="figure"),
    Output(component_id="markdown-scatter", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df["continent"].isin([value_dropdown])]
    df_new = pd.DataFrame(
        np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns
    )
    df_new["year"] = pd.to_numeric(df_new["year"])
    df_new["lifeExp"] = pd.to_numeric(df_new["lifeExp"])
    start_time = datetime.now()
    cvs = ds.Canvas(plot_width=100, plot_height=100)
    agg = cvs.points(df_new, "year", "lifeExp")
    zero_mask = agg.values == 0
    agg.values = np.log10(agg.values, where=np.logical_not(zero_mask))
    agg.values[zero_mask] = np.nan
    fig = px.imshow(agg, origin="lower", labels={"color": "Log10(count)"})
    end_time = datetime.now()
    subtitle = "Duration for datashader loading: {} s".format(
        round((end_time - start_time).total_seconds(), 2)
    )
    return fig, subtitle


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
