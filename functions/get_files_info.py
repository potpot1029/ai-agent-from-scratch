import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        wd_abs_path = os.path.abspath(working_directory)
        target_full_path = os.path.normpath(os.path.join(wd_abs_path, directory))

        valid_target_dir = (
            os.path.commonpath([wd_abs_path, target_full_path]) == wd_abs_path
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        is_directory = os.path.isdir(target_full_path)
        if not is_directory:
            return f'Error: "{directory}" is not a directory'

        files_info = []
        for file in os.listdir(target_full_path):
            file_full_path = os.path.join(target_full_path, file)

            file_size = os.path.getsize(file_full_path)
            is_dir = os.path.isdir(file_full_path)

            files_info.append(f"  - {file}: file_size={file_size}, is_dir={is_dir}")

        return "\n".join(files_info)

    except Exception as e:
        return f"Error: {e}"
