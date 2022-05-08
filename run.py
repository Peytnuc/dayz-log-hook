from modules.listener import Listener
from settings import Settings
from pathlib import Path

if __name__ == "__main__":
    settings = Settings()

    check_admin_log = Path(settings.filepath)
    if not check_admin_log.is_file():
        exit("Please ensure you update ADMIN_LOG_FILE variable inside settings.py to reflect the path where your .ADM file is (typically in the same directory as --profile used when running the server...")

    listener = Listener(settings.filepath, settings.interval, settings.events)
    listener.run()