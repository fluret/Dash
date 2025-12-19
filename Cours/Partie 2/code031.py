import plotly.express as px
import pandas as pd

df = px.data.gapminder()
df_filtered = df[df['country'].isin(['Canada', 'Brazil', 'Norway', 'Germany'])]

# figure
fig = px.line(df_filtered, x='year', y='lifeExp', color='country')
fig.show()
