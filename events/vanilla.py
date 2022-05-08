from modules.event import Event

class EventChat(Event):
    def handle_discord(self):
        return self.event_text, f"""Player {self.data["player_name"]} ({self.data["player_guid"]})\n\n{self.data["text"]}"""

class EventDisconnect(Event):
    def handle_discord(self):
        return self.event_text, f"""Player {self.data["player_name"]} disconnected from the server"""

class EventHit(Event):
    def handle_discord(self):
        if not self.data.get("hit_location"):
            return self.event_text, f"""Player {self.data["player_name"]}[HP: {self.data["player_hp"]}] was hit by {self.data["hit_by"]}"""
        return self.event_text, f"""Player {self.data["player_name"]}[HP: {self.data["player_hp"]}] was hit by {self.data["hit_by"]} in {self.data["hit_location"]} for damage: {self.data["hit_damage"]} ({self.data["hit_source"]})"""

class EventSuicide(Event):
    def handle_discord(self):
        return self.event_text, f"""Player {self.data["player_name"]} committed suicide..."""

class EventDied(Event):
    def handle_discord(self):
        return self.event_text, f"""Player {self.data["player_name"]} died..."""