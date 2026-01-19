import plotly.express as px
import pandas as pd

df = px.data.gapminder()
df = df.groupby(["year", "continent"]).agg({"pop": "sum"}).reset_index()

fig = px.bar(df, x="year", y="pop", color="continent", template="plotly_dark")
fig.show()
