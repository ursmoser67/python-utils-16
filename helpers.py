def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


def append_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)


def list_files(directory):
    import os
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def clear_directory(directory):
    import os
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def copy_file(source, destination):
    import shutil
    shutil.copy2(source, destination)