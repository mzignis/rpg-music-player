import os
import signal

from tools.ffplay import play_via_ffplay


def play_youtube_audio(
        yt_url_input: str, volume_default: int = 30, loop_default: bool = True, ask_about_settings: bool = False
) -> int:

    if ask_about_settings:
        # Loop input with default as True for values like 'Y', 'y', or 'yes'
        loop_input: str = input('Do you want to play music in loop? [Y/n] >> ')
        loop: bool = loop_input.lower() in ['y', 'yes', '']  # Default is True

        # Volume input with default value 30 and range validation
        volume_input: str = input('Please type the volume level (1-100) [30] >> ')
        try:
            volume = int(volume_input) if volume_input else volume_default
            if volume < 1 or volume > 100:
                print("Volume out of range. Setting volume to default (30).")
                volume = 30
        except ValueError:
            print("Invalid volume input. Setting volume to default (30).")
            volume = 30
    else:
        volume: int = volume_default
        loop: bool = loop_default

    # Call the play function (assuming `play_via_ffplay` is defined elsewhere)
    pid: int = play_via_ffplay(yt_url_input, volume, loop)
    print(f'Playing with pid: {pid}')
    print()

    return pid


def kill_process_by_pid(pid) -> None:
    try:
        os.kill(pid, signal.SIGTERM)  # Sends the termination signal
        print(f"Process {pid} has been terminated.")
    except ProcessLookupError:
        print(f"No process found with PID {pid}.")
    except PermissionError:
        print(f"Permission denied to kill process {pid}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    pass
