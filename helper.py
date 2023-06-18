import sys
import os
import pathlib

from delta import dealing_deltas, clean_delta_extension, delete_deltas 
from util import download_song, init_configuration, clean_workspace, execute_command



AAC = "aac"
MP3 = "mp3"

FOLDER_ACC = "music_downloaded"
FOLDER_MP3 = f"music_downloaded_{MP3}"
FOLDER_LATEST_DOWNLOAD_AAC=f"music_latest_downloaded_{AAC}"
DELTA_FOLDER_AAC = f"delta_{AAC}"
DELTA_FOLDER_MP3 = f"delta_{MP3}"

MUSIC_COMMAND_AAC = f'youtube-dl -f bestaudio --extract-audio --audio-quality 0 --audio-format aac --output "./{DELTA_FOLDER_AAC}/%(title)s.%(ext)s"'
MUSIC_COMMAND_MP3 = f'youtube-dl -f bestaudio --extract-audio --audio-quality 0 --audio-format mp3 --output "./{DELTA_FOLDER_MP3}/%(title)s.%(ext)s"'
COPY_DELTA_COMMAND_AAC = f"cp ./{DELTA_FOLDER_AAC}/* ./{FOLDER_ACC}"
COPY_DELTA_COMMAND_MP3 = f"cp ./{DELTA_FOLDER_MP3}/* ./{FOLDER_MP3}"

COPY_DELTA_TO_LATEST_COMMAND_AAC = f"cp ./{DELTA_FOLDER_AAC}/* ./{FOLDER_LATEST_DOWNLOAD_AAC}"

init_configuration(FOLDER_LATEST_DOWNLOAD_AAC)

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
# now we need to deal with deltas
list_of_repeated_deltas = dealing_deltas(DELTA_FOLDER_AAC, FOLDER_ACC)

list_of_cleaned_repeated_deltas = clean_delta_extension(list_of_repeated_deltas)

print("deltas to be deleted:")
for repeated_delta in list_of_cleaned_repeated_deltas:
    print(repeated_delta)

delete_deltas(list_of_cleaned_repeated_deltas, AAC)
delete_deltas(list_of_cleaned_repeated_deltas, MP3)

execute_command(COPY_DELTA_COMMAND_AAC)
execute_command(COPY_DELTA_COMMAND_MP3)
execute_command(COPY_DELTA_TO_LATEST_COMMAND_AAC)


file_error_instance.close()
file_music_list_instance.close()

clean_workspace()
