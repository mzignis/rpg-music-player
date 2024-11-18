import asyncio
import os
from pathlib import Path

import openai
from dotenv import load_dotenv

# -------- load dot-env & constants --------
load_dotenv(Path(__file__).parent.parent / '.env')
OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL: str = os.getenv('OPENAI_MODEL')
PROMPTS: dict = {
    'music': Path(__file__).parent.parent / 'prompts' / 'music.txt'
}

# -------- set openai key --------
openai.api_key = OPENAI_API_KEY


# ---------- functions ----------
def get_openai_response(prompt_user: str, prompt_type: str = 'music') -> list[str]:
    prompt_sys_filepath: Path = PROMPTS[prompt_type]
    with open(prompt_sys_filepath, 'r') as text_file:
        prompt_system: str = text_file.read()

    messages = [
        {'role': 'system', 'content': prompt_system},
        {'role': 'user', 'content': prompt_user}
    ]

    # Function to create response using OpenAI's GPT model
    async def create_response():
        return await openai.ChatCompletion.acreate(model=OPENAI_MODEL, messages=messages)

    # Get response from OpenAI
    gpt_response = asyncio.run(create_response())["choices"][0]["message"]["content"].strip()
    return [rr.strip() for rr in gpt_response.split('\n')]


if __name__ == '__main__':
    pass
