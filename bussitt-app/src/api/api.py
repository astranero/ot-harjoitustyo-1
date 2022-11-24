import requests
import json
import time

# my modules
from myutils import *

url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"

def fetch_timetable(bus_stop) -> dict:
    if not bus_stop: error()

    gtfsId = bus_stop["gtfsId"]
    query = f"""
        query {{
            stop(id: "{gtfsId}") {{
                name
                stoptimesWithoutPatterns(numberOfDepartures: 10, startTime: {int(time.time())}) {{
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
        response = requests.post(url, json={'query': query})
    except:
        error("Error", response.status_code)
    else:
        data = json.loads(response.text)

    return data

def fetch_search_options(search_word):
    if not search_word: error()

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
        response = requests.post(url, json={'query': query})
    except:
        error("Error", response.status_code)
    else:
        data = json.loads(response.text)
        if len(data["data"]["stops"]) == 0:
            return "no_matches"

    return data


