import os
from pathlib import Path
from pprint import pprint

import dash
import psutil
from dash import Output, Input, State
from dotenv import load_dotenv

from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant
from src.rpg_music_player.app.app import app
from src.rpg_music_player.app.layout import create_card_layout
from src.rpg_music_player.tools.player import play_youtube_audio, kill_process_by_pid
from src.rpg_music_player.youtube.search import YoutubeSearchEngine
from src.rpg_music_player.database.database import Ambient

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

        if data['n_clicks'] == n_clicks:
            outputs_pid_store.append(data)
            continue

        data['n_clicks'] = n_clicks

        if data['url'].startswith('https://www.youtube.com/watch?v=') or data['url'].startswith('https://youtube.com/watch?v='):
            url = data['url']
            if n_clicks % 2:
                volume = 100 if 100 <= data['layout_id'] < 200 else 35
                pid = play_youtube_audio(url, volume_default=volume, loop_default=True)
                data['pid'] = pid
                outputs_pid_store.append(data)
            else:
                if data['pid']:
                    kill_process_by_pid(data['pid'])
                    data['pid'] = None
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

        # AI search assistant
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

        # AI search assistant
        assistant = YouTubeSearchAssistant()
        prompt_new = assistant.get_background_prompt(prompt)
        print('new background prompt:', prompt_new)

        # create cards layout
        cards: list = []
        path_ambient = Path(__file__).parent.parent.parent.parent / 'data' / 'bardify' / 'playlists' / 'ambience.yaml'
        ambient_db = Ambient(path_ambient)
        records = ambient_db.select_records(prompt_new)
        records = records.sample(2 if records.shape[0] >= 2 else records.shape[0])
        results_no: int = 4 - records.shape[0] if records.shape[0] < 4 else 2

        # search engine
        engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
        results = engine.search(prompt_new, max_results=results_no)

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

        ii = 0
        for _, rr in records.reset_index(drop=True).iterrows():
            local_id = ii+100+len(cards)
            ii += 1
            cards.append(
                create_card_layout(
                    layout_id=local_id,
                    title=rr['title'],
                    channel=rr['channel_name'],
                    url=rr['url'],
                    thumbnail=rr['thumbnail']
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

        # AI search assistant
        assistant = YouTubeSearchAssistant()
        prompt_new = assistant.get_combat_prompt(prompt)
        print('new combat prompt:', prompt_new)

        db = Ambient(Path(__file__).parent.parent.parent.parent / 'data' / 'bardify' / 'playlists' / 'roll_for_initiative!.yaml')
        results = db.df.sample(4)

        # create cards layout
        cards: list = []
        ii = 0
        for _, rr in results.iterrows():
            cards.append(
                create_card_layout(
                    layout_id=ii+200,
                    title=rr.title,
                    channel=rr.channel_name,
                    url=rr.url,
                    thumbnail=rr.thumbnail
                )
            )
            ii += 1

        return tuple(cards)

    return tuple([create_card_layout(ii) for ii in range(4)])


@app.callback(
    [Output(f"player-layout-{_id_}", "children", allow_duplicate=True) for _id_ in IDS],
    Input("kill-all-button", "n_clicks"),
    [State(f"pid-store-{_id_}", "data") for _id_ in IDS],
    prevent_initial_call=True
)
def kill_all_subprocesses(_, *data):
    # ToDo: change cards frame, n_click
    pprint(data)

    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Check if 'ffplay' is in the command line of the process
            if 'ffplay' in process.info['cmdline']:
                print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Command: {process.info['cmdline']}")
                process.terminate()
        except:
            pass  # Ignore processes that are no longer accessible

    cards = [
        create_card_layout(
            layout_id=dd['layout_id'],
            title=dd['title'],
            channel=dd['channel'],
            url=dd['url'],
            thumbnail=dd['thumbnail']
        ) for dd in data
    ]

    return tuple(cards)
