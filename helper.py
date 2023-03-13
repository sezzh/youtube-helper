import subprocess
import sys
import os
import pathlib

MUSIC_COMMAND_AAC = f'youtube-dl -f bestaudio --extract-audio --audio-quality 0 --audio-format aac --output "./music_downloaded/%(title)s.%(ext)s"'
MUSIC_COMMAND_MP3 = f'youtube-dl -f bestaudio --extract-audio --audio-quality 0 --audio-format mp3 --output "./music_downloaded_mp3/%(title)s.%(ext)s"'

def download_song(command, song_url, file_error_instance):
    print(f"downloading: {song_url}")
    music_command_to_execute = f'{command} "{song_url}"'
    print("command to use:")
    print(music_command_to_execute)
    process = subprocess.Popen(music_command_to_execute, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 1:
        file_error_instance.write(f'{song_url}\n')


current_path = pathlib.Path(os.getcwd())
music_file_name = sys.argv[1]
list_of_songs_to_download = []
# check if music_not_downloaded.txt is present

file_error_path = current_path.joinpath("music_not_downloaded.txt")

print(file_error_path)

if file_error_path.is_file:
    pathlib.Path.unlink(file_error_path)


file_error_instance = open(file_error_path, "x")
file_music_list_instance = open(current_path.joinpath(music_file_name), "r")
readlines_of_music_file = file_music_list_instance.readlines()

for line_url_song in readlines_of_music_file:
    line_url_song.strip()
    list_of_songs_to_download.append(line_url_song)

index = 1
for song_url in list_of_songs_to_download:
    print(f"downloading song: {index}/{len(list_of_songs_to_download)}")
    download_song(MUSIC_COMMAND_AAC, song_url, file_error_instance)
    download_song(MUSIC_COMMAND_MP3, song_url, file_error_instance)
    index = index + 1


file_error_instance.close()
file_music_list_instance.close()
