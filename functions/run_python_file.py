import os, subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    try:
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_dir) != True:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif file_path.endswith("py") == False:
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_dir]
        if args:
            command.extend(args)
        subprocess_result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)                                                        
        output_str = ""
        if subprocess_result.returncode != 0:
            output_str += "Process exited with code X\n"
        if not subprocess_result.stdout and not subprocess_result.stderr:
            output_str += "No output produced\n"
        else:
            if subprocess_result.stdout:
                output_str += f'STDOUT: {subprocess_result.stdout}\n'
            if subprocess_result.stderr:
                output_str += f'STDERR: {subprocess_result.stderr}\n'
        return output_str


    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Retrieves a string containing the first 10,000 characters of an input file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the exact file from which the content is extracted",
                },
                "args": {
                    "type": "list",
                    "description": "List of arguments required to call the necessary python function",
                },
            },
        },
    },
}

