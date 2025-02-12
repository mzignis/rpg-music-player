import os
from pathlib import Path
from pprint import pp

import dash
from dash import Output, Input, State
from dotenv import load_dotenv

from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant
from src.rpg_music_player.app.app import app
from src.rpg_music_player.app.layout import create_card_layout
from src.rpg_music_player.youtube.search import YoutubeSearchEngine
from tools.player import play_youtube_audio, kill_process_by_pid

from src.rpg_music_player.tools import text as text_tools

# -------- load env variables --------
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# -------- define constants variables --------
IDS = [0, 1, 2]


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
            if n_clicks % 2:
                pid = play_youtube_audio(url)
                data['pid'] = pid
                outputs_pid_store.append(data)
            else:
                if data['pid']:
                    kill_process_by_pid(data['pid'])
                outputs_pid_store.append(data)

    return outputs_clickable_card + outputs_pid_store


@app.callback(
    [
        Output(f"player-layout-{_id_}", "children") for _id_ in IDS
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

        # search engine
        engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
        results = engine.search(prompt_new, max_results=3)

        # create cards layout
        cards: list = []
        for ii, rr in enumerate(results):
            cards.append(
                create_card_layout(
                    layout_id=ii,
                    title=text_tools.shorten_text(rr.title, 16),
                    channel=text_tools.shorten_text(rr.channel_name),
                    url=text_tools.shorten_text(rr.url),
                    thumbnail=rr.thumbnail
                )
            )

        return cards[0], cards[1], cards[2]

    return create_card_layout(0), create_card_layout(1), create_card_layout(2)
