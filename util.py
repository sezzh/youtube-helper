import subprocess
import pathlib
import os
import shutil


def init_configuration(latest_downloaded_folder_acc_name):
    current_path = pathlib.Path(os.getcwd())
    latest_downloaded_path =  current_path.joinpath(latest_downloaded_folder_acc_name)
    if (os.path.exists(latest_downloaded_path)):
        shutil.rmtree(latest_downloaded_path, ignore_errors=True)
    os.mkdir(current_path.joinpath("delta_aac"))
    os.mkdir(current_path.joinpath("delta_mp3"))
    os.mkdir(current_path.joinpath(latest_downloaded_folder_acc_name))

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

def execute_command(copy_command):
    process = subprocess.Popen(copy_command, shell=True, stdout=subprocess.PIPE)
    process.wait()