from modules.listener import Listener
from settings import Settings
from pathlib import Path

# Default Events
from events.vanilla import (
    EventChat,
    EventDisconnect,
    EventConnected,
    EventSuicide,
    EventHit,
    EventDied,
    EventKilledByPlayer,
)

# Custom Events
from events.cot import EventCOTHealed, EventCOTTeleported, EventCOTSetCheat
from events.expansion import EventExpansionAirdrop, EventExpansionSpawnSelection

settings = Settings()

EVENTS = [
    # Default Private Events
    EventChat(
        "chat",
        "Chat Message",
        "vanilla\chat.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventConnected(
        "connect",
        "Player Connected",
        "vanilla\connected.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventDisconnect(
        "disconnect",
        "Player Disconnected",
        "vanilla\disconnected.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventHit(
        "hit",
        "Player Hit",
        "vanilla\hit.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventDied(
        "died",
        "Player Died",
        "vanilla\died.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    # Default Public Events
    EventSuicide(
        "suicide",
        "Player Died",
        "vanilla\suicide.ttp",
        supported_webhooks=settings.webhooks["discord_public"],
    ),
    EventKilledByPlayer(
        "killed_by_player",
        "Player Killed",
        "vanilla\killed_by_player.ttp",
        supported_webhooks=settings.webhooks["discord_public"],
    ),
    # Custom Private Events
    # COT
    EventCOTHealed(
        "cot_healed",
        "[COT] Healed",
        "cot\healed.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventCOTTeleported(
        "cot_teleported",
        "[COT] Teleported",
        "cot\\teleport.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    EventCOTSetCheat(
        "cot_setcheat",
        "[COT] Player Management",
        "cot\setcheat.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    # Expansion
    EventExpansionSpawnSelection(
        "expansion_spawnselection",
        "[Expansion] SpawnSelection",
        "expansion\spawn.ttp",
        supported_webhooks=settings.webhooks["discord_admin"],
    ),
    # Custom Public Events
    # Expansion
    # You can also be more specific if you only want a certain event to go to a separate dedicated Discord channel for example
    EventExpansionAirdrop(
        "expansion_airdrop",
        "[Expansion] Airdrop",
        "expansion\\airdrop.ttp",
        supported_webhooks=settings.webhooks["discord_expansion_airdrops"],
    ),
]

if __name__ == "__main__":
    check_admin_log = Path(settings.filepath)
    if not check_admin_log.is_file():
        exit(
            "Please ensure you update ADMIN_LOG_FILE variable inside settings.py to reflect the path where your .ADM file is (typically in the same directory as --profile used when running the server..."
        )

    listener = Listener(settings.filepath, settings.interval, EVENTS)
    listener.run()
