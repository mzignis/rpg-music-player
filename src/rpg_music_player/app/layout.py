import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

from src.rpg_music_player.tools import text as text_tools


def create_layout():
    _layout_ = dbc.Container([
        html.H1("RPG Music Player"),
        html.Hr(),
        create_search_layout(),
        html.Hr(),
        create_player_layout(0),
        create_player_layout(0, layout_offset=4),
        html.Hr(),
        create_player_layout(1),
        html.Hr(),
        create_player_layout(2),
    ])

    return _layout_


def create_search_layout():
    _layout_ = dbc.Container(
        children=[
            dbc.Row(
                dbc.Input(id="search-input", type="text", placeholder="Enter search term..."),
            ),
            dbc.Stack([
                dbc.Button("Search", id="search-button", color="primary", className="mt-2"),
                html.Div("", className="mx-auto"),
                dbc.Button("KILL ALL", id="kill-all-button", color="danger", className="mt-2"),
                ], direction="horizontal", gap=1,
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
                    data={
                        "pid": None, "url": url, "title": title, "channel": channel, "thumbnail": thumbnail,
                        "layout_id": layout_id, "n_clicks": 0,
                    }
                ),
                dbc.CardBody(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                id=f'player-thumbnail-{layout_id}',
                                src=thumbnail,
                                className="img-fluid rounded-start",
                                style={"maxWidth": "100%", "padding": "8px"}
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            [
                                html.H5(
                                    children=text_tools.shorten_text(title, 16),
                                    className="card-title",
                                    id=f'player-title-{layout_id}'
                                ),
                                html.H6(
                                    children=text_tools.shorten_text(channel, 16),
                                    className="card-text",
                                    style={"fontSize": "0.9rem"},
                                    id=f'player-channel-{layout_id}',
                                ),
                                html.Small(
                                    children=text_tools.shorten_text(url, 16),
                                    className="card-text text-muted",
                                    id=f'player-url-{layout_id}',
                                ),
                            ],
                            width=8,
                        ),
                    ],
                    className="g-12 d-flex align-items-center",
                    style={"padding": "8px"}
                )
            ],
            className="mb-1",
            style={"maxWidth": "400px", "cursor": "pointer", "border": "2px solid black"},
            id=f'clickable-card-{layout_id}'
        ),
    )

    return card


def create_player_layout(layout_id: int, layout_offset: int = 0) -> dbc.Row:
    player_id = layout_id * 100

    _layout_ = dbc.Row([
        dbc.Col(
            children=create_card_layout(player_id + ii + layout_offset),
            width=3,
            id=f'player-layout-{player_id + ii + layout_offset}',
            className="mb-1"
        ) for ii in range(4)
    ], className="mb-1"
    )

    return _layout_
