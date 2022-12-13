import inquirer

# my modules
from myutils.myutils import clear_cl, error


class Ui:
    """
    This Class has the single responsibility of communicating with user.
    """

    def __init__(self) -> None:
        # Schema
        self.answers = {
            "action": "",
            "search_word": "",
            "bus_stop": {
                "name": "",
                "gtfsId": ""
            },
        }

    def ask_action(self, has_records) -> dict:
        inquiry_name = "action"
        question = []

        if has_records:
            question = [
                inquirer.List(
                    inquiry_name,
                    message="Your action",
                    choices=[
                            ('View a timetable', 'view_timetable'),
                            ('Add new timetable', 'add_timetable'),
                            ('Manage saved timetables', "manage_timetables"),
                            ('Quit', 'quit')
                    ],
                )
            ]
        else:
            question = [
                inquirer.List(
                    inquiry_name,
                    message="Your action",
                    choices=[
                            ('Add new timetable', 'add_timetable'),
                            ('Manage saved timetables', "manage_timetables"),
                            ('Quit', 'quit')
                    ],
                )
            ]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def ask_to_save_timetable(self) -> dict:
        inquiry_name = "save_timetable"
        question = [inquirer.List(
            inquiry_name,
            message="Would you like to save timetable?",
            choices=[
                    ("Yes", "save_timetable"),
                    ("No", None)
            ]
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def ask_search_word(self) -> dict:

        inquiry_name = "search_word"
        question = [inquirer.Text(
            inquiry_name,
            message="Search timetable by stop name"
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def choose_timetable_options(self, records):
        if not records:
            error()

        inquiry_name = "recorded_timetables"
        choices = []

        for record in records:
            choice = (
                f"{record['custom_name']}",
                {
                    "name": record['name'],
                    "code": record['code'],
                    "gtfsId": record["gtfsId"]}
            )
            choices.append(choice)

        question = [inquirer.List(
            inquiry_name,
            # message="Choose timetable",
            choices=choices
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def choose_search_option(self, search_options) -> dict:
        if not search_options:
            error()

        inquiry_name = "bus_stop"
        choices = []

        for item in search_options["data"]["stops"]:
            choice = (
                f"{item['name']} {item['code']}",
                {
                    "name": item['name'],
                    "code": item['code'],
                    "gtfsId": item["gtfsId"]}
            )
            choices.append(choice)

        question = [inquirer.List(
            inquiry_name,
            message="Specify bus stop",
            choices=choices
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def choose_management_operation(self):
        inquiry_name = "management_operation"

        question = [inquirer.List(
            inquiry_name,
            message="What would you like to do?",
            choices=[
                ("Delete a timetable", "delete_timetable"),
                ("Rename a timetable", "rename_timetable")
            ]
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def ask_timetable_custom_name(self):

        inquiry_name = "custom_name"
        question = [inquirer.Text(
            inquiry_name,
            message="Name your timetable"
        )]

        name = inquirer.prompt(question)[inquiry_name]
        self.answers[inquiry_name] = name if name or name != "" else "No name"
        clear_cl()

        return self.answers[inquiry_name]

    def ask_home_or_quit(self):
        inquiry_name = "action"

        question = [inquirer.List(
            inquiry_name,
            message="What next?",
            choices=[
                ("Home", None),
                ("Quit", "quit")
            ]
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]


    def get_answers(self):
        return self.answers