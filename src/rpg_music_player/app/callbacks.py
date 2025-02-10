import os
from pprint import pp

import dash

from dash import Output, Input, State
from pathlib import Path
from dotenv import load_dotenv

from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant
from src.rpg_music_player.app.app import app
from src.rpg_music_player.youtube.search import YoutubeSearchEngine
from tools.player import play_youtube_audio, kill_process_by_pid

load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

pid0 = None
pid1 = None
pid2 = None
results = ["", "", ""]

ids = [0, 1, 2, 100, 101, 102, 200, 201, 202]


@app.callback(
    [Output(f"clickable-card-{_id_}", "style") for _id_ in ids],
    [Input(f"clickable-card-wrapper-{_id_}", "n_clicks") for _id_ in ids],
    prevent_initial_call=True
)
def change_card_color(*args):
    ctx = dash.callback_context

    # Check if any button has been clicked, initialize counts as 0
    if not ctx.triggered:
        return [f"Button {i} Clicks: 0" for i in range(3)]

    # Create a list to hold the updated text for each output
    outputs = []

    # Iterate over each button's click count (args contain n_clicks values for each button)
    for i, n_clicks in enumerate(args):
        # If the button hasn't been clicked, set the default as 0
        new_color = "blue" if n_clicks % 2 else "black"
        outputs.append({"maxWidth": "400px", "cursor": "pointer", "border": f"2px solid {new_color}"})

        # ToDo: Add logic to run music player


    return outputs

# # ------------------------------------------------------------
# @app.callback(
#     Output("play-stop-button-0", "children"),
#     Output("status-text-0", "children"),
#     Input("play-stop-button-0", "n_clicks"),
#     State("play-stop-button-0", "children"),
#     prevent_initial_call=True
# )
# def toggle_button(n_clicks, current_text):
#     global pid0
#     global results
#
#     print("button 0")
#     if current_text == "▶ Play":
#         print('playing')
#         pid0 = play_youtube_audio(results[0].url)
#         return "⏹ Stop", "Playing..."
#     else:
#         print('stopping')
#         kill_process_by_pid(pid0)
#
#         return "▶ Play", "Stopped."
#
#
# @app.callback(
#     Output("play-stop-button-1", "children"),
#     Output("status-text-1", "children"),
#     Input("play-stop-button-1", "n_clicks"),
#     State("play-stop-button-1", "children"),
#     prevent_initial_call=True
# )
# def toggle_button(n_clicks, current_text):
#     global pid1
#     global results
#
#     print("button 1")
#     if current_text == "▶ Play":
#         print('playing')
#         play_youtube_audio(results[1].url)
#         return "⏹ Stop", "Playing..."
#     else:
#         print('stopping')
#         kill_process_by_pid(pid1)
#         return "▶ Play", "Stopped."
#
#
# @app.callback(
#     Output("play-stop-button-2", "children"),
#     Output("status-text-2", "children"),
#     Input("play-stop-button-2", "n_clicks"),
#     State("play-stop-button-2", "children"),
#     prevent_initial_call=True
# )
# def toggle_button(n_clicks, current_text):
#     global pid2
#     global results
#
#     print("button 2")
#     if current_text == "▶ Play":
#         print('playing')
#         pid2 = play_youtube_audio(results[2].url)
#         return "⏹ Stop", "Playing..."
#     else:
#         print('stopping')
#         kill_process_by_pid(pid2)
#         return "▶ Play", "Stopped."
#
#
# @app.callback(
#     Output("search-output", "children"),
#     Output("plain-text-0", "children"),
#     # Output("plain-text-1", "children"),
#     # Output("plain-text-2", "children"),
#     Input("search-button", "n_clicks"),
#     Input("search-input", "value")
# )
# def update_output(n_clicks, value):
#     if value and n_clicks:
#         prompt = value
#         assistant = YouTubeSearchAssistant()
#
#         prompt_new = assistant.convert_search_prompt(prompt)
#         print(prompt_new)
#
#         engine = YoutubeSearchEngine(YOUTUBE_API_KEY)
#         rr = engine.search(prompt_new, max_results=1)
#
#         pp(rr)
#
#         global results
#         results = rr
#
#         return "Searching for:" + " ".join([str(r) for r in rr]), rr[0].title
#
#     return "", ""
