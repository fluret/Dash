import plotly.express as px

df = px.data.gapminder()
df = df[df["country"].isin(["Spain", "United Kingdom"])]

fig = px.bar(
    df,
    x="year",
    y="lifeExp",
    color="country",
    barmode="group",
    title="Grouped Bar Chart",
    template="plotly_white",
)
fig.update_yaxes(range=[60, 80])
fig.show()
