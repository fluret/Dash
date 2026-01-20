"""
Chart callbacks and data visualization logic.
"""
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback
from config import COLOR_PALETTE, CHART_CONFIG


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
        table_data: Current table data from DataTable
        
    Returns:
        Updated Plotly figure
    """
    dff = pd.DataFrame(table_data)
    
    fig = px.bar(
        dff, 
        x="time", 
        y="total_bill", 
        color="day",
        title="Total Bill by Time and Day",
        labels={"total_bill": "Total Bill ($)", "time": "Time of Day"},
        color_discrete_sequence=COLOR_PALETTE
    )
    
    # Apply layout configuration
    fig.update_layout(**CHART_CONFIG)
    
    # Add grid styling
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="rgba(200,200,200,0.1)")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="rgba(200,200,200,0.1)")
    
    return fig
