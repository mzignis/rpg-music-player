import dash
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define button and output ids
button_ids = ['button-0', 'button-1', 'button-2']
output_ids = ['output-0', 'output-1', 'output-2']

# Layout with buttons and outputs
app.layout = html.Div([
                          # Output containers
                          html.Div(id=f'output-{i}', children=f"Button {i} Clicks: 0") for i in range(3)
                      ] + [
                          # Button containers
                          html.Button(f'Button {i}', id=f'button-{i}') for i in range(3)
                      ])


# Define the callback to handle the button clicks and update the corresponding output
@app.callback(
    [Output(f'output-{i}', 'children') for i in range(3)],
    [Input(f'button-{i}', 'n_clicks') for i in range(3)]
)
def update_output(*args):
    # args will contain the number of clicks for each button
    ctx = dash.callback_context

    # Check if any button has been clicked, initialize counts as 0
    if not ctx.triggered:
        return [f"Button {i} Clicks: 0" for i in range(3)]

    # Create a list to hold the updated text for each output
    outputs = []

    # Iterate over each button's click count (args contain n_clicks values for each button)
    for i, n_clicks in enumerate(args):
        # If the button hasn't been clicked, set the default as 0
        click_count = n_clicks if n_clicks is not None else 0
        outputs.append(f"Button {i} Clicks: {click_count}")

    return outputs


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
