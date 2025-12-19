layout = html.Div(
    children=[
        html.H1(children="This is our Graphs page"),
        dcc.Dropdown(["one", "two", "three"]),
        html.Div(
            children="""
        This is our Graphs page content.
    """
        ),
    ]
)
