import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    try:
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_dir) == False:
            return f'Error: File not found or is not a regular file "{file_path}"'
    except Exception as e:
        return f"Error: {e}"
    with open(target_dir, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(1):
            file_content_string += f'[...File "{target_dir}" truncated at {MAX_CHARS} characters]'
        return file_content_string

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Retrieves a string containing the first 10,000 characters of an input file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the exact file from which the content is extracted",
                },
            },
        },
    },
}
