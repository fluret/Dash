import plotly.express as px

df = px.data.gapminder()

fig = px.bar(
    df,
    x="year",
    y="pop",
    color="country",
    title="PX scatter plot",
    template="plotly_white",
)
fig.show()
