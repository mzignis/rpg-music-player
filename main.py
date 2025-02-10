from pathlib import Path

import yaml
from fastapi import FastAPI
from pydantic import BaseModel

from tools.player import play_youtube_audio, kill_process_by_pid
from tools.youtube import search_youtube_for_environment_ambient


# -------- custom request message --------
class CustomRequest(BaseModel):
    kind: str
    question: str


# -------- load settings --------
with open(Path(__file__).parent / 'config' / 'config.yaml', 'r') as yaml_file:
    settings = yaml.safe_load(yaml_file)

# -------- pids collector --------
pids: dict = {
    'music': None,
    'environment': None
}

# -------- FastAPI app --------
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/play")
async def play(request: CustomRequest) -> dict:
    kind: str = request.kind
    prompt: str = request.question

    # -------- play music --------
    if kind == 'music':
        youtube_url = search_youtube_for_environment_ambient(prompt, studio='bardify')[0]
        if pids['music'] is not None:
            kill_process_by_pid(pids['music'])
        pid = play_youtube_audio(
            youtube_url,
            volume_default=settings['music']['volume_default'],
            loop_default=settings['music']['loop_default'],
            ask_about_settings=settings['music']['ask_about_settings'],
        )
        pids['music'] = pid

    # -------- play environment music --------
    elif kind == 'environment':
        # play environment music here
        youtube_url = search_youtube_for_environment_ambient(prompt)[0]
        if pids['environment'] is not None:
            kill_process_by_pid(pids['environment'])
        pid = play_youtube_audio(
            youtube_url,
            volume_default=settings['environment']['volume_default'],
            loop_default=settings['environment']['loop_default'],
            ask_about_settings=settings['environment']['ask_about_settings'],
        )
        pids['environment'] = pid

    # -------- invalid kind --------
    else:
        return {"message": "Invalid kind", "pid": None}

    return {"message": f"Playing {request.kind} from question {request.question}.", "pid": pid}


@app.post("/stop")
async def stop(request: CustomRequest) -> dict:
    kind = request.kind

    # -------- stop music --------
    if kind == 'music':
        if pids['music'] is not None:
            kill_process_by_pid(pids['music'])
            pids['music'] = None
        else:
            return {"message": "No music is playing"}

    # -------- stop environment music --------
    elif kind == 'environment':
        if pids['environment'] is not None:
            kill_process_by_pid(pids['environment'])
            pids['environment'] = None
        else:
            return {"message": "No environment music is playing"}

    # -------- invalid kind --------
    else:
        return {"message": "Invalid kind"}

    return {"message": f"Stopping {request.kind} track."}
