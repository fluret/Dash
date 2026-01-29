# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import numpy as np
from plotly_resampler import register_plotly_resampler

# Call the register function once and all Figures/FigureWidgets will be wrapped
# according to the register_plotly_resampler its `mode` argument
register_plotly_resampler(mode="auto")

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
slider = dcc.Slider(id="our-slider", min=10000, max=200000, marks=None, value=10000)


# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([dropdown], width=4, className="mt-2"),
                dbc.Col([slider], width=8, className="mt-4"),
            ]
        ),
        dbc.Row([dbc.Col([markdown])]),
        dbc.Row([dbc.Col(dcc.Graph(id="our-resample-figure"))]),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id="our-resample-figure", component_property="figure"),
    Output(component_id="our-markdown", component_property="children"),
    Input(component_id="our-dropdown", component_property="value"),
    Input(component_id="our-slider", component_property="value"),
)
def update_graph(value_dropdown, slider_value):
    df_sub = df[df["country"].isin([value_dropdown])]
    df_new = pd.DataFrame(
        np.repeat(df_sub.to_numpy(), slider_value, axis=0), columns=df_sub.columns
    )
    print(len(df_new))

    fig = px.scatter(df_new, x="year", y=pd.to_numeric(df_new["lifeExp"]))
    fig.update_layout(
        title="Plotly Resampler scatter plot",
        xaxis_title="year",
        yaxis_title="lifeExp",
    )
    fig.update_traces(marker=dict(size=5 + (slider_value / 30000) * 25))

    title = "Data points displayed: {:,}".format(len(df_sub.index) * slider_value)

    return fig, title


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
