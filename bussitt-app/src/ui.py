import inquirer

# my modules
from myutils import *


class Ui:
    def __init__(self) -> None:
        self.answers: dict = {}

    def ask_action(self) -> dict:
        boilerplate()
        inquiry_name = "action"
        question = [
            inquirer.List(
                    inquiry_name,
                    message="Your action",
                    choices=[
                        ('Search for timetables', "search_timetables"), 
                        ('Add new timetable', 'add_timetable'),
                        ('Manage saved timetables', "manage_timetables"),
                        ('Quit', 'quit')
                    ],
                )
            ]

        self.answers = inquirer.prompt(question)
        clear_cl()

        return self.answers[inquiry_name]

    def ask_next_action(self) -> dict:
        print("")
        print("")
        inquiry_name = "next_action"
        question = [inquirer.List(
            inquiry_name,
            message = "Select new action",
            choices = [
                    ("Home", None),
                    ("Save timetable", "save_timetable"),
                    ("Quit", "quit")
                ]
        )]

        self.answers = inquirer.prompt(question)
        clear_cl()

        return self.answers[inquiry_name]

    def ask_search_word(self) -> dict:
        boilerplate()

        inquiry_name = "search_word"
        question = [inquirer.Text(
            inquiry_name,
            message="Search timetable by stop name"
        )]

        self.answers = inquirer.prompt(question)
        clear_cl()

        return self.answers[inquiry_name]
        
    def choose_search_option(self, search_options) -> dict:
        boilerplate()
        if not search_options: error()

        inquiry_name = "bus_stop"
        choices = []

        for item in search_options["data"]["stops"]:
            tuple = (
                f"{item['name']} {item['code']}",
                (item['name'], item["gtfsId"])
            )
            choices.append(tuple)
        
        question = [inquirer.List(
            inquiry_name,
            message="Specify bus stop",
            choices=choices
        )]

        self.answers = inquirer.prompt(question)
        clear_cl()

        return self.answers[inquiry_name]







