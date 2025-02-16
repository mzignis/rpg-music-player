import os
from pathlib import Path
import yt_dlp

from dotenv import load_dotenv
from googleapiclient.discovery import build
from pytube import Playlist

load_dotenv(Path(__file__).parent.parent.parent.parent / '.env')
YOUTUBE_API_KEY: str = os.getenv('YOUTUBE_API_KEY')


def get_channel_id(channel_name: str) -> str:
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    response = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1
    ).execute()

    if response["items"]:
        channel_id = response["items"][0]["id"]["channelId"]
        return channel_id


def get_playlists_from_channel(channel_id: str, max_results: int = 64) -> dict:
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    playlists = youtube.playlists().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results
    ).execute()

    results: dict = {}

    for playlist in playlists["items"]:
        playlist_id = playlist["id"]
        playlist_title = playlist["snippet"]["title"]
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        results[playlist_title] = playlist_url

    return results


def get_videos_from_playlist(playlist_url: str) -> list[dict]:
    playlist = Playlist(playlist_url)
    videos: list = [
        {
            "title": get_video_title(vv.watch_url),
            "url": vv.watch_url
        }
        for vv in playlist.videos
    ]
    return videos


def get_video_title(video_url: str) -> str:
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        title: str = info['title']
        return title.split('|')[0].strip().lower() if '|' in title else title
