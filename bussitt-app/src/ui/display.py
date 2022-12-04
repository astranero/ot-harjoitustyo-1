import pandas as pd
from rich.console import Console
from rich.table import Table, box

# my modules
from myutils.myutils import clear_cl, get_time_and_date


class Display:
    def __init__(self) -> None:
        clear_cl()

    def construct_table(self, data, style="default"):
        data_frame = pd.DataFrame(data)

        if style == "simple":
            box_style = box.SIMPLE
        else:
            box_style = box.HEAVY_EDGE

        table = Table(padding=(0, 1), box=box_style)

        rows = data_frame.values.tolist()
        rows = [[str(el) for el in row] for row in rows]
        columns = data_frame.columns.tolist()

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row)

        return table

    def render_timetable(self, timetable_data):
        if timetable_data is None:
            return

        data_list = []

        for data in timetable_data["data"]["stop"]["stoptimesWithoutPatterns"]:
            realtime_departure = data["realtimeDeparture"]
            service_day = data["serviceDay"]
            short_name = data["trip"]["route"]["shortName"]
            headsign = data["headsign"]

            realtime_departure_time, realtime_departure_date = get_time_and_date(
                service_day + realtime_departure)
            bus_name = short_name
            last_stop = headsign

            data_list.append({
                "Departure time": realtime_departure_time,
                "Bus": bus_name,
                "Destination": last_stop,
            })

        table = self.construct_table(data_list)

        console = Console()
        console.print(table)
        print("")
        print("")

    def render_timetable_list(self, timetable_collection):
        data_list = []

        for timetable in timetable_collection:
            data_list.append({
                "Name": timetable["custom_name"],
                "Bus stop": timetable["name"] + " " + timetable["code"],
            })

        table = self.construct_table(data_list)

        console = Console()
        console.print(table)
        print("")
        print("")
