from src.rpg_music_player.youtube.tools import get_channel_id, get_playlists_from_channel, get_videos_from_playlist, get_video_title
from pprint import pprint
from pathlib import Path
import yaml

channel_name: str = 'Bardify'
channel_id: str = get_channel_id(channel_name)
playlists: dict = get_playlists_from_channel(channel_id)
pprint(playlists)

path: Path = Path(__file__).parent.parent.parent.parent / 'data' / channel_name.lower() / 'playlists'
path.mkdir(parents=True, exist_ok=True)

for playlist_name, playlist_url in playlists.items():
    print(playlist_name, playlist_url)
    videos: list = get_videos_from_playlist(playlist_url)

    playlist_name = playlist_name.replace(' ', '_').lower()

    with open(path / f'{playlist_name}.yaml', 'w') as file:
        yaml.dump(videos, file)

    print('-' * 64)
    print()
