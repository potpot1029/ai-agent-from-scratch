import os

from config import MAX_CHARS
from functions.paths import resolve_in_working_dir

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Read the content of a file with a specified file path relative to the working directory. Content exceeding {MAX_CHARS} characters will be truncated.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read the content from, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        target_file = resolve_in_working_dir(working_directory, file_path)
        if target_file is None:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return content
    except Exception as e:
        return f"Error: {e}"

