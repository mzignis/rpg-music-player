import os
from pathlib import Path

import dash
from dash import Output, Input, State
from dotenv import load_dotenv

from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant
from src.rpg_music_player.app.app import app
from src.rpg_music_player.app.layout import create_card_layout
from src.rpg_music_player.tools import text as text_tools
from src.rpg_music_player.youtube.search import YoutubeSearchEngine
from tools.player import play_youtube_audio, kill_process_by_pid

# -------- load env variables --------
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# -------- define constants variables --------
IDS = [0, 1, 2, 3, 4, 5, 6, 7, 100, 101, 102, 103, 200, 201, 202, 203]


# -------- define callbacks --------
@app.callback(
    [
        Output(f"clickable-card-{_id_}", "style") for _id_ in IDS
    ] + [
        Output(f"pid-store-{_id_}", "data") for _id_ in IDS
    ],
    [Input(f"clickable-card-wrapper-{_id_}", "n_clicks") for _id_ in IDS],
    [State(f"pid-store-{_id_}", "data") for _id_ in IDS],
    prevent_initial_call=True
)
def change_card_color(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        return [], []

    outputs_clickable_card: list = []
    outputs_pid_store: list = []

    args_len = len(args)
    for i, (n_clicks, data) in enumerate(zip(args[:args_len//2], args[args_len//2:])):
        new_color = "white" if n_clicks % 2 else "black"
        outputs_clickable_card.append({"maxWidth": "400px", "cursor": "pointer", "border": f"2px solid {new_color}"})

        # ToDo: Add logic to run music player
        if data['url'].startswith('https://www.youtube.com/watch?v='):
            url = data['url']
            print(url)
            if n_clicks % 2:
                pid = play_youtube_audio(url)
                data['pid'] = pid
                outputs_pid_store.append(data)
            else:
                if data['pid']:
                    kill_process_by_pid(data['pid'])
                outputs_pid_store.append(data)
        else:
            outputs_pid_store.append(data)

    return outputs_clickable_card + outputs_pid_store


@app.callback(
    [
        Output(f"player-layout-{_id_}", "children") for _id_ in IDS[:8]
    ],
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
    prevent_initial_call=True
)
def update_output(n_clicks, prompt):
    if prompt and n_clicks:

        # ai search assistant
        assistant = YouTubeSearchAssistant()
        prompt_new = assistant.convert_search_prompt(prompt)
        print('new prompt:', prompt_new)

        # search engine
        engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
        results = engine.search(prompt_new, max_results=len(IDS[:8]))

        # create cards layout
        cards: list = []
        for ii, rr in enumerate(results):
            cards.append(
                create_card_layout(
                    layout_id=ii,
                    title=rr.title,
                    channel=rr.channel_name,
                    url=rr.url,
                    thumbnail=rr.thumbnail
                )
            )

        return tuple(cards)

    return tuple([create_card_layout(ii) for ii in range(len(IDS[:8]))])


@app.callback(
    [
        Output(f"player-layout-{_id_+100}", "children") for _id_ in range(4)
    ],
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
    prevent_initial_call=True
)
def update_output100(n_clicks, prompt):
    if prompt and n_clicks:

        # ai search assistant
        assistant = YouTubeSearchAssistant()
        prompt_new = assistant.get_background_prompt("dnd environment music")
        print('new background prompt:', prompt_new)

        # search engine
        engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
        results = engine.search(prompt_new, max_results=4)

        # create cards layout
        cards: list = []
        for ii, rr in enumerate(results):
            cards.append(
                create_card_layout(
                    layout_id=ii+100,
                    title=rr.title,
                    channel=rr.channel_name,
                    url=rr.url,
                    thumbnail=rr.thumbnail
                )
            )

        return tuple(cards)

    return tuple([create_card_layout(ii) for ii in range(4)])


@app.callback(
    [
        Output(f"player-layout-{_id_+200}", "children") for _id_ in range(4)
    ],
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
    prevent_initial_call=True
)
def update_output200(n_clicks, prompt):
    if prompt and n_clicks:

        # ai search assistant
        assistant = YouTubeSearchAssistant()
        prompt_new = assistant.get_combat_prompt("dnd combat music")
        print('new combat prompt:', prompt_new)

        # search engine
        engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
        results = engine.search(prompt_new, max_results=4)

        # create cards layout
        cards: list = []
        for ii, rr in enumerate(results):
            cards.append(
                create_card_layout(
                    layout_id=ii+200,
                    title=rr.title,
                    channel=rr.channel_name,
                    url=rr.url,
                    thumbnail=rr.thumbnail
                )
            )

        return tuple(cards)

    return tuple([create_card_layout(ii) for ii in range(4)])
