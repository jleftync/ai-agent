import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory) 
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    try:
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Result for \"{directory}\" directory:\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif os.path.isdir(target_dir) == False:    
            return f'Error: "{target_dir}" is not a directory'
        
    except Exception as e:
        return f"Error: {e}"
    return_string = f"Result for \"{directory}\" directory:\n"
    directory_string_list = []
    for item in list(os.listdir(target_dir)):
        try:
            os.path.isdir(os.path.join(target_dir, item))
        except Exception as e:
            return f"Error: Checking whether {item} is a directory raised an exception."
        try:
            os.path.getsize(os.path.join(target_dir, item))
        except Exception as e:
            return f"Error: Checking {item}'s size raised an exception."
        size = os.path.getsize(os.path.join(target_dir, item))
        is_dir = os.path.isdir(os.path.join(target_dir, item))
        directory_string_list.append(f"  - {item}: file_size={size}, is_dir={is_dir}\n")
    final_string = "".join(directory_string_list)
    return_string += final_string
    return return_string

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
