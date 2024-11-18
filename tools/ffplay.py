import subprocess

from yt_dlp import YoutubeDL


def stream_youtube_audio(youtube_url: str) -> str:
    ydl_opts = {'format': 'bestaudio', 'noplaylist': True, 'quiet': True}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        audio_url = info_dict['url']
    return audio_url


def play_via_ffplay(youtube_url: str, volume: int = None, loop: bool = False) -> int:
    cmd: list[str] = ['ffplay', '-nodisp', '-autoexit']

    if volume is not None:
        cmd += ['-volume', f'{volume}']
    if loop:
        cmd += ['-loop', '0']

    audio_url = stream_youtube_audio(youtube_url)
    cmd += ['-i', audio_url]

    pid = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return pid.pid


if __name__ == '__main__':
    pass
