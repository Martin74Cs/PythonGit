import os

def changeExtension(file_path, new_extension):
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + new_extension
    return new_file_path