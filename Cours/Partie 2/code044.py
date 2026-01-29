import plotly.express as px
import numpy as np

df = px.data.gapminder().query("year == 2007")
fig = px.treemap(
    df,
    path=[px.Constant("world"), "continent", "country"],
    values="pop",
    color="lifeExp",
    hover_data=["iso_alpha"],
)
fig.show()
