import plotly.express as px
import pandas as pd

# sample dataset from plotly express
df = px.data.gapminder()

df = df[df["country"].isin(["Canada", "Norway", "Germany"])]

fig = px.line(
    df,
    x="year",
    y="lifeExp",
    color="country",
    symbol="continent",
    title="Multidimensional data",
    template="plotly_white",
)
fig.show()
