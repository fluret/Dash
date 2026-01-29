import plotly.express as px

df = px.data.gapminder()
df = df[df["continent"].isin(["Asia", "Europe"])]
fig = px.histogram(df, x="lifeExp", nbins=20, color="continent", barmode="overlay")
fig.show()
