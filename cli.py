import os
import json


def find_json_file() -> str:
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        ext = filename.split('.')[-1]
        if ext.lower() == 'json':
            return os.path.realpath(filename)


def read_file(file_path) -> str:
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content


json_file_path = find_json_file()
pld_content = json.loads(read_file(json_file_path))
print(pld_content)
