from modules.listener import Listener
from settings import Settings

if __name__ == "__main__":
    settings = Settings()

    listener = Listener(settings.filepath, settings.interval, settings.events)
    listener.run()