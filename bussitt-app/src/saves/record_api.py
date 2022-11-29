import json



def get_path():
    return "src/recordings/records.json"


def is_empty(records_list):
    return len(records_list) == 0 or any(item.get("id") for item in records_list)


def get_records_file():
    try:
        with open(get_path(), "r", encoding="utf-8") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        with open(get_path(), "w", encoding="utf-8") as outfile:
            json.dump([], outfile, indent=4)

        # return new empty list for records_list. Needs to be a list!
        return []


def schema_exists(schema_id, records_list):
    try:
        return any(item.get("id") == schema_id for item in records_list)
    except LookupError:
        return False


def remove_schema(schema_id, records_list):
    for item in records_list.copy():
        if item.get("id") == schema_id:
            records_list.remove(item)
    return records_list


def add_schema(new_schema, records_list):
    records_list.append(new_schema)
    return records_list


def save_timetable(data):
    records_list = get_records_file()

    schema_id = data["timetable_gtfsId"]

    if schema_exists(schema_id, records_list):
        records_list = remove_schema(schema_id, records_list)

    new_schema = {
        "id": schema_id,
        "timetable_name": data["timetable_name"],
        "timetable_code": data["timetable_code"],
        "timetable_gtfsId": data["timetable_gtfsId"],
        "timetable_custom_name": data["timetable_custom_name"],

        # next feature
        # "timetable_cl_arg": data["timetable_cl_arg"]
    }

    records_list = add_schema(new_schema, records_list)

    with open(get_path(), mode="w", encoding="utf-8") as outfile:
        json.dump(records_list, outfile, indent=4)
