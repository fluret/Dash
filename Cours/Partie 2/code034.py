import plotly.express as px
import pandas as pd

# sample data
df = px.data.gapminder()

df = df[df["country"].isin(["Canada"])]

# Line chart
fig = px.line(df, x="year", y="lifeExp", title="PX Line plot", template="plotly_white")
fig.show()