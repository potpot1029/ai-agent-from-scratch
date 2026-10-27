import os

from functions.paths import resolve_in_working_dir

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        target_file = resolve_in_working_dir(working_directory, file_path)
        if target_file is None:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
        is_directory = os.path.isdir(target_file)
        if is_directory:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)
    
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'