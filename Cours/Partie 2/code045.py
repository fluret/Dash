import plotly.express as px

df = px.data.gapminder()
df = df[df["gdpPercap"] < 60000]
fig = px.density_heatmap(
    df,
    x="gdpPercap",
    y="lifeExp",
    nbinsx=20,
    nbinsy=20,
    color_continuous_scale="Viridis",
)
fig.show()
