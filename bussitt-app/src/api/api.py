import json
import time

import requests

# my modules
from myutils.myutils import error


"""
This module has the single responsibilty of providing utility functions for sending API requests to the URL mentioned below.
"""

URL = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"


def fetch_timetable(bus_stop) -> dict:
    """
    Sends a API request for a particular timetable
    """

    if not bus_stop:
        error()

    gtfsId = bus_stop["gtfsId"]
    start_time = int(time.time())
    query = f"""
        query {{
            stop(id: "{gtfsId}") {{
                name
                stoptimesWithoutPatterns(numberOfDepartures: 10, startTime: {start_time}) {{
                    stop {{
                        platformCode
                    }}
                    scheduledDeparture
                    realtimeDeparture
                    departureDelay
                    realtime
                    realtimeState
                    serviceDay
                    trip {{
                        route {{
                        shortName
                        }}
                    }}
                    headsign
                }}
            }}
        }}"""

    response = None
    data = None

    try:
        response = requests.post(URL, json={'query': query}, timeout=4)
    except TimeoutError:
        error("Status code: "+ response.status_code)
    else:
        data = json.loads(response.text)

    return data


def fetch_search_options(search_word):
    """
    Sends an API request for different timetable options depending on the search_word
    """

    if not search_word:
        error()

    query = f"""
    query {{
        stops(name: "{search_word}") {{
            gtfsId
            name
            code
        }}
    }}"""

    response = None
    data = None

    try:
        response = requests.post(URL, json={'query': query}, timeout=4)
    except TimeoutError:
        error("Status code: " + response.status_code)
    else:
        data = json.loads(response.text)
        if len(data["data"]["stops"]) == 0:
            return "no_matches"

    return data
