import psutil
import json

def run(args: dict) -> str:
    info = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }
    return json.dumps(info)

def register():
    return "system_info", run
