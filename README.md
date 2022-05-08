# DayZ Log Hook

This is a simply python script which essentially looks at the administrator logs (ADM) and is highly expandable. I was sick of all the solutions out on the internet (or maybe I wasn't looking properly) but have tried my best to make this very user friendly as long as you can follow these instructions. This python script should always be running so ensure you monitor the script and launch it again if it isn't found, later I will extend it into a windows service so you can make it auto-restart/start when something goes wrong locally on your server.

The only dependency you need is Python on your Windows server. Before you start, ensure you COPY the `settings.py.example` and rename it to `settings.py`.

### Flow

![flow](event_flow.png)

### Settings

Ensure you edit the settings.py and change the following for a great experience:

1) Change the Discord <change_me> webhook to your Discord webhook channel to enable messages
2) Change the `ADMIN_LOG_FILE` variable to reflect the location where your .ADM file is located. This will always be in the same directory that you specify --profile when running a server.


### Adding a new Event

If you want to record a new event, you will need to perform the following:

1) Create the event in a separate python file under `events`. This should look something like this if you are creating an event for the DayZ Expansion mod:

events\expansion.py
```
from modules.event import Event


class EventExpansionAirdrop(Event):
    def handle_discord(self):
        pass
```

2) Create the template under `templates` folder with the .ttp extension to filter the data within the log using TTP format (https://ttp.readthedocs.io/en/latest/Quick%20start.html) - An online tool can be used to test your log against a specific filter here (https://textfsm.nornir.tech/)

For example, if I want to match a Chat event which is a Vanillia log therefore the format can be found here https://community.bistudio.com/wiki/DayZ:Administration_Logs#Logged_events, my ttp template will be stored as `templates\expansion\airdrop.ttp` and contain the following:

```
{{ event_time }} | {{ _ }} [MissionAirdrop] An airdrop is heading towards "{{ location }}" (pos={{ pos_x }}, {{ pos_y }}, {{ pos_z }}> type={{ airdrop_type }}) with a {{ airdrop_container }}
```

3) You can now implement a function in the EventExpansionAirdrop that we created in step 1 to handle the discord webhook data. Example:

```
from modules.event import Event


class EventExpansionAirdrop(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] An airdrop is heading towards {self.data["location"]}!""",
        )
```

Notice I am accessing the filtered data via `self.data["location"]`. If the event is not processed (eg. data isn't matched) then this handle_discord method will not be called.

4) Finally, I need to attach this Event in my `run.py` like this:

```
# Custom Events
from events.expansion import EventExpansionAirdrop

settings = Settings()

EVENTS = [
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
```

### Adding new Webhook support

To add a new webhook you must create a file inside `webhooks` folder and create a class with the format of "Webhook<Name>", for example the Discord webhook is called WebhookDiscord. This class must always inherit `WebhookGeneric` by importing it and extending your class to use it, for example:

```
from webhooks.generic import WebhookGeneric

class WebhookDiscord(WebhookGeneric):
    def handle_webhook(self, event):
        pass
```

Notice, you must always create handle_webhook with (self, event) because the Event method `process` will attempt to call this method for every webhook supported by the Event, the `event` variable will give you access to your Event data. Your logic will then be implemented inside this method, for example the discord method will process the title and description of an Event as such:

```
class WebhookDiscord(WebhookGeneric):
    """Format: Title, Message"""
    def handle_webhook(self, event):
        check_attr = getattr(event, "handle_discord", None)
        if not callable(check_attr):
            logger.error(f"Unable to send Discord webhook message for {event.event_name} due to method 'handle_discord' being implemented incorrectly.")
            return

        title, message = event.handle_discord()

        webhook = DiscordWebhook(url=self.url)
        embed = DiscordEmbed(title=title, description=message)
        webhook.add_embed(embed)
        webhook.execute()
```

Any new webhook you implement must also have a function within the Event called `handle_<name of webhook>`. To support the discord webhook, your event must have a method called `handle_discord`. You must manually add support for your new webhook to all the events, all vanillia events will have support for Discord and planned support for databasehooks will include MongoDB (so your logs can go to a database which you can pull inside your website for things like kill stats and death stats)

If you have any questions or ideas for improvement then please feel free to join the discord at: https://dsc.gg/peytnuc_dayz and post in the support channel. Feel free to also take a look at our discord to examples of these events working in-game. Currently the support for per-webhook Event is a bit wack, if you want to specifically only send certain Events across different discord channels, then you must create a new `WebhookDiscord` in your settings.py and add that to your specific event. For example, if you have a generic discord channel and a killfeed channel you will need to do something like this:

```
WEBHOOKS = {
    "discord_admin": [
        WebhookDiscord(
            "<change-me>"
        )
    ],
    "discord_public": [
        WebhookDiscord(
            "<change-me>"
        )
    ],
    "discord_expansion_airdrops": [
        WebhookDiscord(
            "<change-me>"
        )
    ],
}
```

An example of these events being sent to a discord channel:

![discord_example](discord_example.png)