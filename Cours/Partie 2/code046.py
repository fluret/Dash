import plotly.express as px
import pandas as pd
import numpy as np

# data
df = px.data.gapminder()
df = df[
    df["country"].isin(["France", "Germany", "Sweden", "Finland", "United Kingdom"])
]
df = df.reset_index()

# instructions to drop random observations
np.random.seed(12)
remove_n = int(len(df) * 0.6)
drop_indices = np.random.choice(df.index, remove_n, replace=False)
df = df.drop(drop_indices)

# pivot to country in column names, integer as index, and years as values
dfp = df.pivot(index="index", columns="country", values="year")
dfp = dfp.agg(["min", "max"])
dfp = dfp.astype(int)
df = dfp.T
df = df.reset_index()
df = df.astype(str)

fig = px.timeline(df, x_start="min", x_end="max", y="country")
fig.update_yaxes(autorange="reversed")  # otherwise tasks are listed from the bottom up
fig.show()
