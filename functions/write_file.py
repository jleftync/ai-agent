import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    try:
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot write to  "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_dir) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    except Exception as e:
        return f"Error: {e}"
    directory_path = os.path.dirname(file_path)
    if directory_path:
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    with open(target_dir, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Retrieves a string containing the first 10,000 characters of an input file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the exact file from which the content is extracted",
                },
                "content": {
                    "type": "string",
                    "description": "Content to be written into the file by the AI agent",
                },
            },
        },
    },
}

