import datetime
import time
import requests
import json
from base64 import b64encode

class Toggl:
    def __init__(self, token):
        self.token = token
        self.api_token_str = self.token + ":api_token"
        # Set your Toggl API token
        self.api_token = b64encode(bytes(self.api_token_str, "ascii")).decode("ascii")

    def verify_set_date(self, date):
        # check date
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            date_iso = date_obj.date().isoformat()
        except ValueError:
            print("DUMBASS")
            exit()

        day_obj = datetime.date.fromisoformat(date_iso)
        next_day_obj = day_obj + datetime.timedelta(days=1)
        next_day_iso = next_day_obj.isoformat()

        return [date_iso, next_day_iso]
    
    # Connects to the API and returns a JSON that represents the content of the GET request
    def get_time_entries(self, date):
        dates = self.verify_set_date(date)
        params = {
            "start_date":dates[0]+"T08:00:00.000-07:00",
            "end_date":dates[1]+"T07:59:59.999-07:00",
            "tag_ids": "Freeflow Immersion,Intensive Immersion",
        }

        # Set the URL for the Toggl API endpoint
        url = "https://api.track.toggl.com/api/v9/me/time_entries"

        # Set headers for API request
        headers = {"Authorization": "Basic " + self.api_token}

        # Send a GET request to the API endpoint
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Convert response content to JSON obj and return
            return(json.loads(response.content))
        print("Request failed, error code:", response.status_code)
        return False    # Request failed
    
    # Returns a list of the total time spent on Freeflow Immersion and Intensive Immersion and their descriptions
    def get_time_totals(self, date):
        time_entries = self.get_time_entries(date)
        if time_entries:
            # Print the time entries to the console
            freeflow_sec = 0
            freeflow_descs = []
            intensive_sec = 0
            intensive_descs = []
            for entry in time_entries:
                if "Freeflow Immersion" in entry["tags"]:
                    freeflow_sec += entry["duration"]
                    if entry["description"] not in freeflow_descs:
                        freeflow_descs.append(entry["description"])
                elif "Intensive Immersion" in entry["tags"]:
                    intensive_sec += entry["duration"]
                    if entry["description"] not in intensive_descs:
                        intensive_descs.append(entry["description"])
            if len(freeflow_descs) == 0:
                freeflow_descs.append("nothing!")
            if len(intensive_descs) == 0:
                intensive_descs.append("nothing!")

            # Print the totals and descriptions to the console
            ffiTime = time.strftime('%H:%M:%S', time.gmtime(freeflow_sec))
            iiTime = time.strftime('%H:%M:%S', time.gmtime(intensive_sec))
            return [freeflow_sec, intensive_sec, freeflow_descs, intensive_descs]
        print("Invalid time entries, perhaps no time entries for that date?")
        return False    # Request failed
    
    # Builds string from times, descriptions, to be displayed in the GUI
    def build_time_string(self, date):
        # Get the list of time totals and descriptions
        time_totals = self.get_time_totals(date)
        # Format the time totals into readable strings
        ffiTime = time.strftime('%H:%M:%S', time.gmtime(time_totals[0]))
        iiTime = time.strftime('%H:%M:%S', time.gmtime(time_totals[1]))
        # Format date into format "Month Day, Year"
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        date_obj = date_obj.strftime('%B %d, %Y')

        date_string = f"""Date: {date_obj}
Anki: <:angryanki:823714398317051914>
Freeflow Immersion: {ffiTime} ({', '.join(time_totals[2])})
Intensive Immersion: {iiTime} ({', '.join(time_totals[3])})
Total time: {time.strftime('%H:%M:%S', time.gmtime(time_totals[0] + time_totals[1]))}"""

        return date_string
