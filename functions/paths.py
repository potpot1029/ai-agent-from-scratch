import os

def resolve_in_working_dir(working_directory: str, directory: str) -> str | None:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])  == working_dir_abs
        if not valid_target_dir:
            return None

        return target_dir