import os

def run(args: dict) -> str:
    path = args.get("path")
    if not path:
        return "Error: missing 'path' argument"

    if not os.path.exists(path):
        return f"Error: file not found: {path}"

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def register():
    return "read_file", run
