import plotly.express as px

df = px.data.gapminder()

fig = px.box(
    df,
    x="continent",
    y="lifeExp",
    category_orders={
        "continent": ["Oceania", "Europe", "Americas", "Asia", "Asia", "Africa"]
    },
)
fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
fig.show()
