import os

from functions.paths import resolve_in_working_dir


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        target_dir = resolve_in_working_dir(working_directory, directory)
        if target_dir is None:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        is_directory = os.path.isdir(target_dir)
        if not is_directory:
            return f'Error: "{directory}" is not a directory'

        files_info = []
        for file in os.listdir(target_dir):
            file_full_path = os.path.join(target_dir, file)

            file_size = os.path.getsize(file_full_path)
            is_dir = os.path.isdir(file_full_path)

            files_info.append(f"  - {file}: file_size={file_size}, is_dir={is_dir}")

        return "\n".join(files_info)

    except Exception as e:
        return f"Error: {e}"
