import sys

# my modules
from config import args_handler
from myutils import error, transient_print
from ui import Ui
from display import Display
from api import api
from recordings import record_api


class Main:
    def __init__(self) -> None:
        # check all init command-line arguments
        args_handler.check_arguments()

        # Class instantiations
        self.ui = Ui()
        self.display = Display()

        # App properties
        self.action = None
        self.bus_stop = None
        self.user_answers = None
        self.timetable_custom_name = None

        # Search properties
        self.search_word = None
        self.search_options = None

    def start(self) -> None:

        # Main loop
        while True:

            # If any recorded timetables, display them
            self.display.render_timetable_list(record_api.get_records_file())

            # Ask user for action
            self.ask_action()

            if self.action == "add_timetable":
                self.get_timetables()
                self.ask_to_save_timetable()
            elif self.action == "manage_timetables":
                transient_print("Feature not yet available")

    def ask_action(self) -> None:
        self.action = self.ui.ask_action()

        if self.action == "quit":
            if __name__ == "__main__":
                sys.exit()

    def ask_to_save_timetable(self) -> None:
        self.action = self.ui.ask_to_save_timetable()

        if self.action == "save_timetable":
            self.save_timetable()
        elif self.action == "quit":
            if __name__ == "__main__":
                sys.exit()

    def repeat_ask_search_word(self) -> None:
        while True:

            # Ask for a search word until there are search options
            self.ask_search_word()

            # Look for search options by search word
            self.fetch_search_options()

            # Ask until there == search options
            if self.search_options == "no_matches":
                transient_print(f"[?] 0 matches for: {self.search_word}")
            elif self.search_options is None:
                error()
                sys.exit()
            else:
                break

    def ask_search_word(self):
        self.search_word = self.ui.ask_search_word()

    def ask_timetable_custom_name(self):
        self.timetable_custom_name = self.ui.ask_timetable_custom_name()

    def fetch_search_options(self):
        self.search_options = api.fetch_search_options(self.search_word)

    def choose_searh_option(self) -> None:
        self.bus_stop = self.ui.choose_search_option(self.search_options)

    def display_timetable(self) -> None:
        data = api.fetch_timetable(self.bus_stop)
        self.display.render_timetable(data)

    def get_timetables(self) -> None:
        self.repeat_ask_search_word()

        # Ask user to choose specific bus stop
        self.choose_searh_option()

        # Display timetable
        self.display_timetable()

    def get_user_answers(self):
        self.user_answers = self.ui.get_answers()

    def save_timetable(self):
        self.get_user_answers()
        self.ask_timetable_custom_name()

        data = {
            "timetable_name": self.user_answers["bus_stop"]["name"],
            "timetable_code": self.user_answers["bus_stop"]["code"],
            "timetable_gtfsId": self.user_answers["bus_stop"]["gtfsId"],
            "timetable_custom_name": self.timetable_custom_name,
        }

        record_api.save_timetable(data)


if __name__ == "__main__":
    Main().start()
