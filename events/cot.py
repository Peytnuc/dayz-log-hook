from modules.event import Event


class EventCOTHealed(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] Player {self.data["player_target"]} was healed by {self.data["player_source"]}""",
        )


class EventCOTTeleported(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] Player {self.data["player_guid"]} just teleported to: ({self.data["pos_x"]}, {self.data["pos_y"]}, {self.data["pos_z"]})""",
        )


class EventCOTSetCheat(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] Player {self.data["player_guid"]} set {self.data["cheat"]} to {self.data["cheat_state"]} for player {self.data["target_guid"]}""",
        )
