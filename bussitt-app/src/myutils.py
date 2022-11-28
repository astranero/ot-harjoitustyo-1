from sys import platform
from datetime import datetime
import time
import os
from random import randint

# my modules
from config import config


def error(message=None):
    if not message:
        print("Error has occured")
    else:
        print(message)


def random_hint():
    preprefix = "* For new user:"
    prefix = "* Random hint:"
    term = randint(0, 5)

    no_timetables = True

    if no_timetables:
        print(preprefix, "Add a new timetable, so you can view them here")
    else:
        match term:
            case 1:
                print(
                    prefix, "You can edit your timetable when viewing a saved timetable.")
            case 2:
                print(
                    prefix, "You can give a custom argument for opening specific timetables when starting bussitt.")
            case 3:
                print(
                    prefix, "Start bussitt with argument -h or help, to get a list of available arguments.")
            case 4:
                print(prefix, "Start bussitt with...")
            case _:
                print(prefix, "You can delete a saved timetable you are viewing.")


def clear_cl():
    # check which clear command to use depending on os
    if config.disable_clear_cl:
        return

    clear_cmd = "cls" if platform == "win32" else "clear"
    os.system(clear_cmd)


def boilerplate():
    print('+++++++++++ This is Bussitt +++++++++++')
    print("")
    random_hint()
    print("")
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
