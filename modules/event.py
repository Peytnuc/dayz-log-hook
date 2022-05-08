from ttp import ttp
from pathlib import Path
from loguru import logger

class Event:
    def __init__(self, event_name: str, event_text: str, event_ttp: str, supported_webhooks: list = []) -> None:
        self.event_name = event_name
        self.event_text = event_text
        self.event_ttp = Path(__file__).parents[1].joinpath("templates", event_ttp).open().read()
        self.webhooks = supported_webhooks
        self.processed = False
        self.data = None

    def parse_event(self, event_message):
        logger.debug(f"Attempting to process event using: {self.event_name} ({event_message})")
        parser = ttp(event_message, self.event_ttp)
        parser.parse()
        results = parser.result()[0][0]
        if not results:
            return
        
        self.data = results
        self.processed = True
        logger.info(f"Event parsed ({self.event_name})")

    def process(self):
        for webhook in self.webhooks:
            check_attr = getattr(webhook, "handle_webhook", None)
            if not check_attr:
                logger.error("Unable to process a Webhook due to handle_webhook method missing...")
                return
            webhook.handle_webhook(self)    