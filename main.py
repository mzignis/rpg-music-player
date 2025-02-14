from src.rpg_music_player.app.app import app
from src.rpg_music_player.app.layout import create_layout
import src.rpg_music_player.app.callbacks       # Import to register callbacks


app.layout = create_layout()


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)