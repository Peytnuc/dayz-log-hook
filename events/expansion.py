from modules.event import Event


class EventExpansionAirdrop(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] An airdrop is heading towards {self.data["location"]}!""",
        )


class EventExpansionSpawnSelection(Event):
    def handle_discord(self):
        return (
            self.event_text,
            f"""[{self.data["event_time"]}] Player {self.data["player_name"]} spawned at: ({self.data["pos_x"]}, {self.data["pos_y"]}, {self.data["pos_z"]})""",
        )
