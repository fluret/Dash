import plotly.express as px

df = px.data.gapminder()

# data subset
df = df[df["continent"].isin(["Europe", "Americas", "Asia"])]
df = df[df["year"] > 1962]

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    facet_col="year",
    facet_col_wrap=3,
)
fig.show()
