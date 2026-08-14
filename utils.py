import os
import json
from datetime import datetime

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def format_timestamp(timestamp):
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def log_message(message, level='INFO'):
    formatted_time = format_timestamp(datetime.now())
    print(f'[{formatted_time}] {level}: {message}')  


def file_exists(file_path):
    return os.path.isfile(file_path)


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def read_lines(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()