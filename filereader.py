import json
import os
from pathlib import Path


def find_all_files(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def read_test_data():
    test_data_filepath = Path.cwd().joinpath('data.json')
    with test_data_filepath.open(mode='r') as file:
        test_data = json.load(file)
    return test_data


def search_replace():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_data = read_test_data()
    for data in test_data:
        result = find_all_files(data['fileName'], dir_path)
        for x in result:
            path = Path(x)
            with open(x, 'r') as fileRead:
                fileData = fileRead.read()
                if data['previousString'] in fileData:
                    # Replace the target string
                    fileData = fileData.replace(data['previousString'], data['newString'])
                    # Write the file out again
                    with open(path, 'w') as fileWrite:
                        fileWrite.write(fileData)
                    print("data replaced in: ", data['fileName'], "with previous string as", data['previousString'],
                          "to new string as", data['newString'])
