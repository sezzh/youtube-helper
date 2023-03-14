import subprocess
import pathlib
import os
import shutil


def init_configuration():
    current_path = pathlib.Path(os.getcwd())
    os.mkdir(current_path.joinpath("delta_aac"))
    os.mkdir(current_path.joinpath("delta_mp3"))

def download_song(command, song_url, file_error_instance):
    print(f"downloading: {song_url}")
    music_command_to_execute = f'{command} "{song_url}"'
    print("command to use:")
    print(music_command_to_execute)
    process = subprocess.Popen(music_command_to_execute, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 1:
        file_error_instance.write(f'{song_url}\n')

def clean_workspace():
    current_path = pathlib.Path(os.getcwd())
    shutil.rmtree(current_path.joinpath("delta_aac"), ignore_errors=True)
    shutil.rmtree(current_path.joinpath("delta_mp3"), ignore_errors=True)
