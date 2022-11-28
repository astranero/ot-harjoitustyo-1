import pandas as pd

from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.text import Text

# my modules
from myutils import *


class Display:
    def __init__(self) -> None:
        clear_cl()

    def render_timetable(self, timetable_data, timetable_custom_name=None):
        if timetable_data == None:
            return

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

            scheduled_departure_time, scheduled_departure_date = get_time_and_date(
                service_day + scheduled_departure)
            realtime_departure_time, realtime_departure_date = get_time_and_date(
                service_day + realtime_departure)
            delay_time, delay_date = get_time_and_date(departure_delay)
            bus_name = short_name
            last_stop = headsign

            hours, minutes = get_time_to_departure(
                service_day + realtime_departure)

            formatted_time = f"{minutes} min" if hours == 0 else f"{hours} h {minutes} min"

            data_list.append({
                # "Platform": platform_code,
                "Departure time": realtime_departure_time,
                # "Delay": delay_time,
                "Bus": bus_name,
                "Destination": last_stop,
            })

        # Creating the dataframe
        df = pd.DataFrame(data_list)

        # Printing the information

        # drop column ssn from df

        # # constructing the table title
        # table_title = timetable_custom_name or "Timetable name goes here"
        # table_title_style = Style(color="white", bgcolor="purple", bold=True)
        # title_text = Text(text=table_title, style=table_title_style)

        # # constructing any table labels
        # table_labels = "test1, test2"
        # table_labels_style = Style(color="white", bgcolor="yellow")
        # labels_text = Text(text=table_labels, style=table_labels_style)

        table = Table(padding=(0, 1))

        rows = df.values.tolist()
        rows = [[str(el) for el in row] for row in rows]
        columns = df.columns.tolist()

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row)

        console = Console()
        # console.print(title_text)
        # console.print(labels_text)
        console.print(table)
