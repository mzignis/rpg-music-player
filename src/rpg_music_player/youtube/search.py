import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from src.rpg_music_player.youtube.result import YoutubeResult

# -------- load dot-env & constants --------
load_dotenv(Path(__file__).parent.parent.parent.parent / '.env')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


class YoutubeSearchEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key if api_key else YOUTUBE_API_KEY

    def __repr__(self):
        return f"YoutubeSearchEngine(api_key={self.api_key})"

    def __str__(self):
        return f"YoutubeSearchEngine(api_key={self.api_key})"

    def search(self, query, max_results: int = 10) -> list[YoutubeResult]:
        search_url = "https://www.googleapis.com/youtube/v3/search"

        # Parameters for the API request
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': max_results,
            'key': self.api_key
        }

        # Make the request
        response = requests.get(search_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON to extract the video URLs
            results = response.json().get('items', [])
            return [self._parse_result(item) for item in results]
        else:
            print("Error:", response.status_code, response.text)
            return []

    @staticmethod
    def _parse_result(item: dict) -> YoutubeResult:
        return YoutubeResult(
            title=item['snippet']['title'],
            url=f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            thumbnail=item['snippet']['thumbnails']['default']['url'],
            duration=0,
            channel_name=item['snippet']['channelTitle'],
            channel_url=f"https://www.youtube.com/channel/{item['snippet']['channelId']}",
            channel_thumbnail='',
            description=item['snippet']['description'],
            # tags=item['snippet']['tags'],
            # category=item['snippet']['categoryId']
        )


if __name__ == '__main__':
    from pprint import pp
    from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant

    prompt = 'ocean waves'
    assistant = YouTubeSearchAssistant()

    print(assistant.get_combat_prompt(prompt))



    # prompt_new = f'Bardify - {assistant.convert_search_prompt(prompt)}'
    # print(prompt_new)
    #
    # print('--------')
    #
    # prompt_new = f'{assistant.convert_search_prompt(prompt)}'
    # print(prompt_new)
    #
    # print('--------')

    # it better for the user to search for the original prompt

    # prompt_new = f'Michael Ghelfi Studios - {assistant.convert_search_prompt(prompt)}'
    # print(prompt_new)
    #
    # engine = YoutubeSearchEngine()
    # results = engine.search(prompt_new, 4)
    # pp(results)

