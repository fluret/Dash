import plotly.express as px
import pandas as pd

# sample dataset from plotly express
df = px.data.gapminder()

df = df[df["country"].isin(["Canada", "Norway", "Germany"])]

fig = px.scatter(
    df,
    x="year",
    y="lifeExp",
    color="country",
    title="PX scatter plot",
    template="plotly_white",
)
fig.show()
