from models.toggl import Toggl
import json     # Temp, will be fully implemented with a token manager later

class LogController():
    def __init__(self, view):
        self.view = view

    def get_time_entries(self, date):
        # get token
        with open("token.json") as f:
            data = json.load(f)
            token = data["token"]
        toggl = Toggl(token)
        times = toggl.build_time_string(date)
        return times