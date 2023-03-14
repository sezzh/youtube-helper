import os
import pathlib

def dealing_deltas(delta_folder, music_folder):
    list_of_delta_names = []
    list_of_music_folder = []
    current_path = pathlib.Path(os.getcwd())
    print(f"current path: {current_path}")
    iterator_of_files_delta = os.scandir(current_path.joinpath(delta_folder))
    for item in iterator_of_files_delta:
        if item.is_file():
            list_of_delta_names.append(item.name)
    iterator_of_files = os.scandir(current_path.joinpath(music_folder))
    for item in iterator_of_files:
        if item.is_file():
            list_of_music_folder.append(item.name)
    return process_deltas(list_of_delta_names, list_of_music_folder)

def process_deltas(delta_list, library_list):
    delta_founds = []
    for delta_item in delta_list:
        if delta_item in library_list:
            delta_founds.append(delta_item)
    return delta_founds

def clean_delta_extension(delta_founds):
    delta_founds_with_no_ext = []
    for delta in delta_founds:
        splitted_delta = delta.rsplit('.', 1)
        delta_founds_with_no_ext.append(splitted_delta[0])
    return delta_founds_with_no_ext

delta_list = dealing_deltas("delta_aac", "music_downloaded")
delta_clean_list = clean_delta_extension(delta_list)

print("delta list:")
print(delta_clean_list)