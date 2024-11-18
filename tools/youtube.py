import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# -------- load dot-env & constants --------
load_dotenv(Path(__file__).parent.parent / '.env')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


# -------- functions --------
def get_youtube_urls(search_text: str, max_results: int = 1) -> list:
    search_url = "https://www.googleapis.com/youtube/v3/search"

    # Parameters for the API request
    params = {
        'part': 'snippet',
        'q': search_text,
        'type': 'video',
        'maxResults': max_results,
        'key': YOUTUBE_API_KEY
    }

    # Make the request
    response = requests.get(search_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the response JSON to extract the video URLs
        results = response.json().get('items', [])
        video_urls = [f"https://www.youtube.com/watch?v={item['id']['videoId']}" for item in results]
        return video_urls

    else:
        print("Error:", response.status_code, response.text)
        return []


def search_youtube(yt_prompt_text: str, max_results: int = 1) -> list[str]:
    video_urls = get_youtube_urls(yt_prompt_text, max_results)
    return video_urls


def search_youtube_from_environment_ambient(
        environment_prompt: str, studio: str = 'Michael Ghelfi Studios', max_results: int = 1
) -> list[str]:
    # There are other studios I recommend to use:
    # Francis Bonin Music, Bardify, Lucas Quinn Creations, Michael Ghelfi Studios
    prompt: str = f"{studio} - {environment_prompt}"
    video_urls = get_youtube_urls(prompt, max_results)
    return video_urls


if __name__ == '__main__':
    pass
