# Callback decorator
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
# Callback function
def update_markdown(value_drop):
    title = value_drop
    return title