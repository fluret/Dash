# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly_resampler import FigureResampler

# Setup data
df = px.data.gapminder()[["country", "year", "lifeExp"]]
dropdown_list = df["country"].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id="our-markdown")
dropdown = dcc.Dropdown(
    id="our-dropdown", options=dropdown_list, value=dropdown_list[0]
)
markdown_scatter = dcc.Markdown(id="markdown-scatter")
markdown_gl = dcc.Markdown(id="markdown-gl")
markdown_resampler = dcc.Markdown(id="markdown-resample")
slider = dcc.Slider(id="our-slider", min=0, max=50000, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="our-figure")),
                dbc.Col(dcc.Graph(id="our-gl-figure")),
                dbc.Col(dcc.Graph(id="our-resample-figure")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(markdown_scatter),
                dbc.Col(markdown_gl),
                dbc.Col(markdown_resampler),
            ]
        ),
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
    df_sub = df[df["country"].isin([value_dropdown])]
    title = "Data points displayed: {:,}".format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id="our-figure", component_property="figure"),
    Output(component_id="markdown-scatter", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df["country"].isin([value_dropdown])]
    df_new = pd.DataFrame(
        np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns
    )
    start_time = datetime.now()
    fig = px.scatter(
        df_new,
        x="year",
        y="lifeExp",
        title="PX scatter plot",
        template="plotly_white",
    )
    fig.update_traces(marker=dict(size=5 + (value_slider / 30000) * 25))
    end_time = datetime.now()
    subtitle = "Duration for scatter plot loading: {} s".format(
        round((end_time - start_time).total_seconds(), 2)
    )
    return fig, subtitle


@app.callback(
    Output(component_id="our-gl-figure", component_property="figure"),
    Output(component_id="markdown-gl", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df["country"].isin([value_dropdown])]
    df_new = pd.DataFrame(
        np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns
    )
    start_time = datetime.now()
    fig = go.Figure()
    fig.add_trace(
        go.Scattergl(
            x=df_new["year"],
            y=pd.to_numeric(df_new["lifeExp"]),
            mode="markers",
            marker=dict(colorscale="Viridis", size=5 + (value_slider / 30000) * 25),
        )
    )
    fig.update_layout(
        title="GO gl-scatter plot",
        xaxis_title="year",
        yaxis_title="lifeExp",
    )
    end_time = datetime.now()
    subtitle = "Duration for gl-scatter plot loading: {} s".format(
        round((end_time - start_time).total_seconds(), 2)
    )
    return fig, subtitle


@app.callback(
    Output(component_id="our-resample-figure", component_property="figure"),
    Output(component_id="markdown-resample", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df["country"].isin([value_dropdown])]
    df_new = pd.DataFrame(
        np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns
    )
    start_time = datetime.now()
    fig = FigureResampler(go.Figure())
    fig.add_trace(
        go.Scattergl(
            x=df_new["year"],
            y=pd.to_numeric(df_new["lifeExp"]),
            mode="markers",
            marker=dict(colorscale="Viridis", size=5 + (value_slider / 30000) * 25),
        )
    )
    fig.update_layout(
        title="Plotly Resampler scatter plot",
        xaxis_title="year",
        yaxis_title="lifeExp",
    )
    end_time = datetime.now()
    subtitle = "Duration for Plotly Resampler scatter plot loading: {} s".format(
        round((end_time - start_time).total_seconds(), 2)
    )
    return fig, subtitle


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
