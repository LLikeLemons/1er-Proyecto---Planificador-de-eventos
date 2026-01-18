from datetime import datetime
class Event:
    def __init__(self, date:list[datetime], time: tuple, type: str, resources: dict[int], place: str):
        self.date = date
        self.time = time
        self.type = type
        self.resources = resources
        self.place = place
    def to_dict(self):
        dict = {
            "date": self.date,
            "time": self.time,
            "type": self.type,
            "resources": self.resources,
            "place": self.place
        }
        return dict

