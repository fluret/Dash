"""
Chart callbacks.
"""
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback


@callback(
    Output("chart", "figure"),
    Input("draw", "n_clicks"),
    State("input-data", "data"),
)
def update_chart(n_clicks, table_data):
    """
    Update chart based on table data.
    
    Args:
        n_clicks: Number of button clicks
        table_data: Current table data
        
    Returns:
        Updated Plotly figure
    """
    dff = pd.DataFrame(table_data)
    return px.bar(dff, x="time", y="total_bill", color="day")
