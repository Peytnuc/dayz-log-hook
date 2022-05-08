class WebhookGeneric:
    def __init__(self, url: str, token: str = None) -> None:
        self.url = url
        self.token = token

    def handle_webhook(self, event):
        """This function must be implemented in all custom webhook implementations. The logic must simply handle the Event, typically by correctly
        formatting the JSON data sent to the Webhook URL

        Args:
            event:  Event that inherits the modules.event.Event class
        """
        pass
