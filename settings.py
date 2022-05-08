# Default Events
from events.vanilla import EventChat, EventDisconnect, EventSuicide, EventHit, EventDied

# Custom Events
from events.cot import EventCOTHealed

# Default Webhooks
from webhooks.discord import WebhookDiscord

# Admin Webhooks (eg. Private Admin Discord Channels)
ADMIN_WEBHOOKS = [
    WebhookDiscord("<insert-private-discord-webhook-here>")
]

# Public Webhooks (eg. Killfeeds or Live Feeds of your server)
WEBHOOKS = [
    WebhookDiscord("<insert-public-discord-webhook-here>")
]

EVENTS = [
    # Default Private Events
    EventChat("chat", "Chat Message", "chat.ttp", supported_webhooks=ADMIN_WEBHOOKS),
    EventDisconnect("disconnect", "Player Disconnected", "disconnected.ttp", supported_webhooks=ADMIN_WEBHOOKS),
    EventHit("hit", "Player Hit", "hit.ttp", supported_webhooks=ADMIN_WEBHOOKS),
    EventDied("died", "Player Died", "died.ttp", supported_webhooks=ADMIN_WEBHOOKS),

    # Default Public Events
    EventSuicide("suicide", "Player Died", "suicide.ttp", supported_webhooks=WEBHOOKS),

    # Custom Private Events
    EventCOTHealed("cot_healed", "[COT] Healed", "cot_healed.ttp", supported_webhooks=ADMIN_WEBHOOKS),

    # Custom Public Events
]

ADMIN_LOG_FILE = "<insert-full-path-to-DayZServer_x64.ADM-here>"

class Settings:
    def __init__(self, filepath: str = ADMIN_LOG_FILE, interval: int = 5) -> None:
        self.filepath = filepath
        self.interval = interval
        self.events = EVENTS