import pandas as pd
import yaml
from pathlib import Path
from src.rpg_music_player.ai.assistant import YouTubeSearchAssistant


class Ambient:
    def __init__(self, path):
        self.path = path
        self.data = self.load_data()
        self.df = pd.DataFrame(self.data)
        self.ai_assistant = YouTubeSearchAssistant()

    def load_data(self):
        with open(self.path, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def select_records(self, input_prompt):
        titles = self.df.title.tolist()
        titles_selected = self.ai_assistant.select_videos_by_title(input_prompt, titles)
        return self.df[self.df.title.isin(titles_selected)]


if __name__ == '__main__':
    path_ambient = Path(__file__).parent.parent.parent.parent / 'data' / 'bardify' / 'playlists' / 'ambience.yaml'
    ambient_db = Ambient(path_ambient)
    records = ambient_db.select_records('ship')
    print(records)
