from webhooks.generic import WebhookGeneric
from discord_webhook import DiscordWebhook, DiscordEmbed
from loguru import logger


class WebhookDiscord(WebhookGeneric):
    """Format: Title, Message"""

    def handle_webhook(self, event):
        check_attr = getattr(event, "handle_discord", None)
        if not callable(check_attr):
            logger.error(
                f"Unable to send Discord webhook message for {event.event_name} due to method 'handle_discord' being implemented incorrectly."
            )

        title, message = event.handle_discord()

        webhook = DiscordWebhook(url=self.url)
        embed = DiscordEmbed(title=title, description=message)
        webhook.add_embed(embed)
        webhook.execute()
