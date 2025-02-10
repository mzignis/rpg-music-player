import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


def create_layout():
    _layout_ = dbc.Container([
        dcc.Store(id="card-click-state", data={"clicked": False}),
        html.H1("RPG Music Player"),
        html.Hr(),
        create_search_layout(),
        html.Hr(),
        html.H1("Ambient music"),
        create_player_layout(0),
        html.Br(),
        html.Hr(),
        html.H1("Background music"),
        create_player_layout(1),
        html.Br(),
        html.Hr(),
        html.H1("Combat music"),
        create_player_layout(2),
        html.Br(),
        html.Hr(),
    ])

    return _layout_


def create_search_layout():
    _layout_ = dbc.Row(
        children=[
            dbc.Row(
                dbc.Input(id="search-input", type="text", placeholder="Enter search term..."),
            ),
            dbc.Row(
                dbc.Button("Search", id="search-button", color="primary", className="mt-2"),
                style={"maxWidth": "200px"}
            ),
        ]
    )

    return _layout_


def create_card_layout(layout_id):
    card = html.Div(
        id=f'clickable-card-wrapper-{layout_id}',
        n_clicks=0,
        children=dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                id=f'player-image-{layout_id}',
                                src="https://picsum.photos/200",
                                className="img-fluid rounded-start",
                                style={"maxWidth": "100%"}  # Reduce image size
                            ),
                            className="col-md-3",  # Reduce column width proportionally
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H5("Card title", className="card-title"),  # Slightly smaller heading
                                    html.P(
                                        "This is a slightly smaller card ...",
                                        className="card-text",
                                        style={"fontSize": "0.9rem"}  # Reduce font size slightly
                                    ),
                                    html.Small(
                                        "Last updated 3 mins ago",
                                        className="card-text text-muted",
                                    ),
                                ]
                            ),
                            className="col-md-9",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="mb-3",
            style={"maxWidth": "400px", "cursor": "pointer", "border": "2px solid black"},
            id=f'clickable-card-{layout_id}'
        )
    )

    return card


def create_player_layout(layout_id: int):
    player_id = layout_id * 100

    _layout_ = dbc.Row([
        dbc.Col(children=create_card_layout(player_id+0), width=4),
        dbc.Col(children=create_card_layout(player_id+1), width=4),
        dbc.Col(children=create_card_layout(player_id+2), width=4),
    ], id=f'player-layout-{player_id}')
    # _layout_ = dbc.Row(
    #     children=[
    #         dbc.Col(
    #             children=[
    #                 dbc.Button(
    #                     children="▶ Play",
    #                     id=f"play-stop-button-{layout_id}",
    #                     color="primary",
    #                     className="me-2"
    #                 ),
    #                 html.Div(id=f"status-text-{layout_id}"),
    #             ],
    #             width=2
    #         ),
    #         dbc.Col(
    #             children=[
    #                 html.Plaintext(id=f"player-image-{layout_id}", children=""),
    #             ],
    #             width=2
    #         ),
    #         dbc.Col(
    #             children=[
    #                 html.Plaintext(id=f"plain-text-{layout_id}", children=""),
    #             ],
    #             width=2
    #         ),
    #     ],
    #     className="p-3")

    return _layout_
