import inquirer

# my modules
from myutils.myutils import clear_cl, error


class Ui:
    def __init__(self) -> None:
        # Schema
        self.answers = {
            "action": "",
            "next_action": "",
            "search_word": "",
            "bus_stop": {
                "name": "",
                "gtfsId": ""
            },
        }

    def ask_action(self) -> dict:
        inquiry_name = "action"
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
        print("")
        print("")
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

    def ask_timetable_custom_name(self):

        inquiry_name = "timetable_custom_name"
        question = [inquirer.Text(
            inquiry_name,
            message="Give your timetable a name (or skip)"
        )]

        self.answers[inquiry_name] = inquirer.prompt(question)[inquiry_name]
        clear_cl()

        return self.answers[inquiry_name]

    def get_answers(self):
        return self.answers
