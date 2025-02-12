import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


def create_layout():
    _layout_ = dbc.Container([
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
        html.Div(id="search-output", className="mt-2"),
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


def create_card_layout(
        layout_id: int,
        title: str = "Card title",
        channel: str = "Card channel",
        url: str = "Card URL",
        thumbnail: str = "https://picsum.photos/200"
) -> html.Div:
    card = html.Div(
        id=f'clickable-card-wrapper-{layout_id}',
        n_clicks=0,
        children=dbc.Card(
            [
                dcc.Store(
                    id=f"pid-store-{layout_id}",
                    data={"pid": None, "url": url}
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                id=f'player-thumbnail-{layout_id}',
                                src=thumbnail,
                                className="img-fluid rounded-start",
                                style={"maxWidth": "100%", "padding": "8px"}
                            ),
                            className="col-md-3",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        children=title,
                                        className="card-title",
                                        id=f'player-title-{layout_id}'
                                    ),
                                    html.P(
                                        children=channel,
                                        className="card-text",
                                        style={"fontSize": "0.9rem"},
                                        id=f'player-channel-{layout_id}',
                                    ),
                                    html.Small(
                                        children=url,
                                        className="card-text text-muted",
                                        id=f'player-url-{layout_id}',
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


def create_player_layout(layout_id: int) -> dbc.Row:
    player_id = layout_id * 100

    _layout_ = dbc.Row([
        dbc.Col(
            children=create_card_layout(player_id+0),
            width=4,
            id=f'player-layout-{player_id}'
        ),
        dbc.Col(
            children=create_card_layout(player_id+1),
            width=4,
            id=f'player-layout-{player_id+1}'),
        dbc.Col(
            children=create_card_layout(player_id+2),
            width=4,
            id=f'player-layout-{player_id+2}'
        ),
    ])

    return _layout_
