def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)


def clear_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')


def file_exists(file_path):
    import os
    return os.path.isfile(file_path)


def get_file_size(file_path):
    import os
    return os.path.getsize(file_path) if file_exists(file_path) else 0


def list_files(directory):
    import os
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]