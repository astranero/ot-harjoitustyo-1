from sys import platform
from datetime import datetime
import time
import os


"""
This module contains all utility functions used throuhout the application.
"""

def error(message=None):
    """
    Error utility function to print a default message or given str
    """

    if not message:
        print("Error has occured")
    else:
        print(message)


def clear_cl():
    """
    Utility function to clear the commandline
    """

    clear_cmd = "cls" if platform == "win32" else "clear"
    os.system(clear_cmd)


def boilerplate():
    """
    Prints a default display text in every home view
    """

    print('+++++++++++ This is Bussitt +++++++++++')
    print("")


def transient_print(message):
    """
    Utility function to print a message that disappears after 2 seconds
    """

    boilerplate()
    print(message)
    time.sleep(2)
    clear_cl()


def get_time_and_date(timestamp):
    """
    Utility function to convert timestamp to time and date
    """

    unix = int(timestamp)
    time_hm = datetime.fromtimestamp(unix).strftime('%H:%M')
    date = datetime.fromtimestamp(unix).strftime('%d-%m-%Y')
    return time_hm, date


def get_time_to_departure(timestamp):
    """
    Utility function that converts difference from given timestamp to current timestamp to minutes
    """

    unix = int(timestamp)
    time_ts = datetime.fromtimestamp(unix)
    now = datetime.now()
    diff = abs(now - time_ts)
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 60) // 60

    return hours, minutes
