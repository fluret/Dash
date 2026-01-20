"""
Table component.
"""
from dash import dash_table
from config import TABLE_STYLES, TABLE_PAGE_SIZE


def create_table(df):
    """Create the styled data table component."""
    return dash_table.DataTable(
        id="input-data",
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
        editable=True,
        page_size=TABLE_PAGE_SIZE,
        column_selectable="single",
        selected_columns=["tip"],
        **TABLE_STYLES,
    )
