import json


"""
This modules has the single responsibility of provifing API functions to save and edit records.json.
records.json file is not used in any other module.
"""

def get_path():
    return "src/my_recordings/records.json"


def is_empty(records_list):
    """
    Checks wether the records_list is empty and returns a boolean
    """

    return len(records_list) == 0 or any(item.get("id") for item in records_list)


def get_records_file():
    """
    Opens and returns the saved timetables file. If no file is found, returns an empty list
    """

    try:
        with open(get_path(), "r", encoding="utf-8") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        with open(get_path(), "w", encoding="utf-8") as outfile:
            json.dump([], outfile, indent=4)

        # return new empty list for records_list. Needs to be a list!
        return []


def has_records():
    """
    Utility function for informing if saved timetables file is empty or not
    """

    records = get_records_file()
    return len(records) != 0


def schema_exists(schema_id, records_list):
    """
    Utility function for checking if a certain record with schema_id already exists
    """
    
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

    schema_id = data["gtfsId"]

    if schema_exists(schema_id, records_list):
        records_list = remove_schema(schema_id, records_list)

    new_schema = {
        "id": schema_id,
        "name": data["name"],
        "code": data["code"],
        "gtfsId": data["gtfsId"],
        "custom_name": data["custom_name"],

        # next feature
        # "timetable_cl_arg": data["timetable_cl_arg"]
    }

    records_list = add_schema(new_schema, records_list)

    with open(get_path(), mode="w", encoding="utf-8") as outfile:
        json.dump(records_list, outfile, indent=4)


def delete_timetable(data):
    records_list = get_records_file()

    schema_id = data["gtfsId"]

    if schema_exists(schema_id, records_list):
        records_list = remove_schema(schema_id, records_list)

        with open(get_path(), mode="w", encoding="utf-8") as outfile:
            json.dump(records_list, outfile, indent=4)

        return "success"
    else:
        return "failed"


    