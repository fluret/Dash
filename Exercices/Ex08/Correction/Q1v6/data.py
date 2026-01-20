"""
Data loading utilities.
"""
import pandas as pd
import plotly.express as px

# Load and prepare data
df = px.data.stocks()
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Date bounds
MIN_DATE = df["date"].min().date()
MAX_DATE = df["date"].max().date()
MIN_TS = df["date"].min()
MAX_TS = df["date"].max()


def load_data() -> pd.DataFrame:
    """Load the stocks dataset."""
    return df
