from sys import platform
from datetime import datetime
import time
import os


def error(message=None):
    if not message:
        print("Error has occured")
    else:
        print(message)


def clear_cl():
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
    time_hm = datetime.fromtimestamp(unix).strftime('%H:%M')
    date = datetime.fromtimestamp(unix).strftime('%d-%m-%Y')
    return time_hm, date


def get_time_to_departure(timestamp):
    unix = int(timestamp)
    time_ts = datetime.fromtimestamp(unix)
    now = datetime.now()
    diff = abs(now - time_ts)
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 60) // 60

    return hours, minutes
