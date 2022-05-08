from tail import Tail
from loguru import logger

class Listener:
    def __init__(self, file_path: str, interval: int, events: list) -> None:
        self.file_path = file_path
        self.interval = interval
        self.events = events
        self.tail = None

    def run(self):
        self.tail = Tail(self.file_path)
        for event in self.events:
            logger.info(f"Registered Event: {event.event_name}")

        self.register_webhooks()
        self.register_databasehooks()
        self.register_event_callbacks()

        self.tail.follow(self.interval)

    def register_event_callbacks(self):
        self.tail.register_callback(self.handle_events)

    def handle_events(self, event_message):
        for event in self.events:
           event.parse_event(event_message)
           if event.processed:
               event.process()
               event.processed = False
               break

    def register_webhooks(self):
        pass

    def register_databasehooks(self):
        pass