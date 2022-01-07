import json
import os
import sys
from pathlib import Path


def find_all_files(plugin_name):
    filenames = []
    path = Path.cwd().joinpath('Data').joinpath(plugin_name)
    for dir_path, _, file_names in os.walk(path):
        for f in file_names:
            filenames.append(os.path.abspath(os.path.join(dir_path, f)))
    return filenames


def read_test_data():
    test_data_filepath = Path.cwd().joinpath('data.json')
    with test_data_filepath.open(mode='r') as file:
        test_data = json.load(file)
    return test_data


def search_replace(plugin_name):
    no_of_replaced_files = 0
    test_data = read_test_data()
    for data in test_data:
        file_names = find_all_files(plugin_name)
        for file in file_names:
            path = Path(file)
            with open(path, 'r', errors="ignore") as read_file:
                file_data = read_file.read()
                if data['previousString'] in file_data:
                    # Replace the target string
                    file_data = file_data.replace(data['previousString'], data['newString'])
                    # Write the file out again
                    with open(path, 'w') as write_file:
                        write_file.write(file_data)
                    print("data replaced in the path:", path, "with previous string as", data['previousString'],
                          "to new string as", data['newString'])
                    no_of_replaced_files = no_of_replaced_files + 1
    if no_of_replaced_files > 0:
        print("Replaced in", no_of_replaced_files, "files")
    else:
        print("No files modified")


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
