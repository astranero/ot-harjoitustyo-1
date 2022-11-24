from sys import platform
from datetime import datetime
import time
import os
import json

def error(message=None):
    if not message:
        print("Error has occured")
    else:
        print(message)

def clear_cl():
# check which clear command to use depending on os
    clear_cmd = "cls" if platform == "win32" else "clear"
    os.system(clear_cmd)

def boilerplate():
    print('+++++++++++ This is Bussitt +++++++++++')
    print("")

def transient_print(message):
    boilerplate()
    print(message)
    time.sleep(2)
    clear_cl()

def get_time_and_date(timestamp):
    unix = int(timestamp)
    t = datetime.fromtimestamp(unix).strftime('%H:%M')
    d = datetime.fromtimestamp(unix).strftime('%d-%m-%Y')
    return t, d

def get_time_to_departure(timestamp):
    unix = int(timestamp)
    t = datetime.fromtimestamp(unix)
    now = datetime.now()
    diff = abs(now - t)
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 60) // 60

    return hours, minutes


def save_timetable(bus_stop_name=None, bus_stop_gtfsId=None, custom_name=None):
    schema = {
        "bus_stop_name": bus_stop_name,
        "bus_stop_gtfsId": bus_stop_gtfsId,
        "custom_name": custom_name
    }

    json_obj = json.dumps(schema)

    with open("/recordings/record.json", "w") as outfile:
        outfile.write(json_obj)