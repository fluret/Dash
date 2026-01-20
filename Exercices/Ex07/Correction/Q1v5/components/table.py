"""
Table component.
"""
from dash import dash_table
from config import TABLE_STYLES, TABLE_PAGE_SIZE


def create_table(data):
    """
    Create the data table component with styling.
    
    Args:
        data: DataFrame to display
        
    Returns:
        DataTable component
    """
    return dash_table.DataTable(
        id="input-data",
        data=data.to_dict("records"),
        columns=[{"name": i, "id": i} for i in data.columns],
        editable=True,
        page_size=TABLE_PAGE_SIZE,
        **TABLE_STYLES
    )
