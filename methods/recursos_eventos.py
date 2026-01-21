from datetime import date, time

class Event:
    def __init__(self, date:list[date], time: tuple, type: str, resources: dict[int], place: str):
        self.date = date
        self.time = time
        self.type = type
        self.resources = resources
        self.place = place
    def to_dict(self):
        dict = {
            "date": date_dict(self.date),
            "time": (self.time[0].hour,self.time[0].minute,self.time[1].hour,self.time[1].minute),
            "type": self.type,
            "resources": self.resources,
            "place": self.place
        }
        return dict

def dict_event(list: list[dict[int]]):
    for i in range(len(list)):
        list[i] = Event(dict_date(list[i]["date"]),dict_time(list[i]["time"]),list[i]["type"],list[i]["resources"],list[i]["place"])
    return list



def dict_time(quatruple):
    return (time(quatruple[0], quatruple[1]),time(quatruple[2],quatruple[3]))
def date_event_dict(date_event):
    temporal = (date_event[0].year,date_event[0].month,date_event[0].day,date_event[1])
    return temporal
def dict_date_event(quatruple):
    return (date(quatruple[0], quatruple[1], quatruple[2]),quatruple[3])
def dict_date(list: list[list[int]]):
    temporal = []
    for i in range(len(list)):
        temporal.append(date(list[i][0],list[i][1],list[i][2]))
    return temporal
def date_dict(dates_list):
    dict_dates = []
    for i in range(len(dates_list)):
        dict_dates.append((dates_list[i].year,dates_list[i].month,dates_list[i].day))
    return dict_dates