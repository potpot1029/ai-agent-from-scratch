from ast import arg
import os
import subprocess
from sys import stderr, stdout
from functions.paths import resolve_in_working_dir


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        target_file = resolve_in_working_dir(working_directory, file_path)
        if target_file is None:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        is_exist_file = os.path.isfile(target_file)
        if not is_exist_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        is_py_file = target_file.endswith(".py")
        if not is_py_file:
            return f'Error: "{file_path}" is not a Python file'
    
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
            
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        out = ""
        if result.returncode != 0:
            out += f"Process exited with code {result.returncode}\n"
        if result.stdout:
            out += f"STDOUT: {result.stdout}\n"
        elif result.stderr:
            out += f"STDERR: {result.stderr}\n"
        else:
            out += "No output produced\n"
            
        return out 
    except Exception as e:
        return f"Error: executing Python file: {e}"