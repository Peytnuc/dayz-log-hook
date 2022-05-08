from modules.event import Event

class EventCOTHealed(Event):
    def handle_discord(self):
        return self.event_text, f"""Player {self.data["player_target"]} was healed by {self.data["player_source"]}"""