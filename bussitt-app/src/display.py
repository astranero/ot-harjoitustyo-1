import pandas as pd
from tabulate import tabulate

# my modules
from myutils import *

class Display:
    def __init__(self) -> None:
        clear_cl()

    def render_timetable(self, timetable_data):
        boilerplate()

        data_list = []

        for data in timetable_data["data"]["stop"]["stoptimesWithoutPatterns"]:
            platform_code = data["stop"]["platformCode"]
            scheduled_departure = data["scheduledDeparture"]
            realtime_departure = data["realtimeDeparture"]
            departure_delay = data["departureDelay"]
            service_day = data["serviceDay"]
            short_name = data["trip"]["route"]["shortName"]
            headsign = data["headsign"]

            scheduled_departure_time, scheduled_departure_date = get_time_and_date(service_day + scheduled_departure)
            realtime_departure_time, realtime_departure_date = get_time_and_date(service_day + realtime_departure)
            delay_time, delay_date = get_time_and_date(departure_delay)
            bus_name = short_name
            last_stop = headsign

            hours, minutes = get_time_to_departure(service_day + realtime_departure)

            formatted_time = f"{minutes} min" if hours == 0 else f"{hours} h {minutes} min"

            data_list.append({
                    "": "",
                    # "Platform": platform_code,
                    "Departs in": formatted_time,
                    "Departure time": realtime_departure_time,
                    # "Delay": delay_time,
                    "Bus": bus_name,
                    "Destination": last_stop,
                })

        df = pd.DataFrame(data_list)
        print(tabulate(df, headers="keys", showindex=False))
            
