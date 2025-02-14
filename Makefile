run:
	python3 main.py

kill-all:
	python3 ./src/rpg_music_player/tools/kill_ffplay.py

kill-port:
	lsof -ti :8080 | xargs kill -9
