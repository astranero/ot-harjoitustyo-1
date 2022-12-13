import sys

# my modules
from myutils.myutils import error, transient_print, boilerplate
from ui.ui import Ui
from ui.display import Display
from api import api
from my_recordings import record_api


class Main:
    """
    Main class works as the antry point for the applications logic. 
    It is the most important class all the other classes adhere to.
    """

    def __init__(self) -> None:
        # Class instantiations
        self.ui = Ui()
        self.display = Display()

        # App properties
        self.action = None
        self.timetable = None
        self.user_answers = None

        # Search properties
        self.search_word = None
        self.search_options = None

    def start(self) -> None:
        """
        Start function works as the main loop of the application and starting point of the Main class.
        """

        # Main loop
        while True:
            # adds a boilerplate text everytime homeview is rendered
            boilerplate()

            # check if any records exist
            timetable_list = record_api.get_records_file()

            # If any recorded timetables, display them
            self.display.render_timetable_list(timetable_list)

            # Ask user for action
            self.ask_action()

            if self.action == "view_timetable":
                self.view_timetable()
                self.ask_home_or_quit()
            elif self.action == "add_timetable":
                self.get_timetables()
                self.ask_to_save_timetable()
            elif self.action == "manage_timetables":
                if not record_api.has_records():
                    transient_print("No timetables to operate on")
                    continue

                self.choose_management_operation()
                self.choose_timetable_options()

                if self.action == "delete_timetable":
                    self.delete_timetable()
                elif self.action == "rename_timetable":
                    self.rename_timetable()

    def ask_action(self) -> None:
        """
        Gets the user input for the available actions in app
        """

        has_records = record_api.has_records()
        self.action = self.ui.ask_action(has_records)

        if self.action == "quit":
            if __name__ == "__main__":
                sys.exit()

    def ask_home_or_quit(self) -> None:
        """
        Asks the user to exit the app or to return to the start of the main loop
        """

        answer = self.ui.ask_home_or_quit()

        if answer == "quit":
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
        """
        Repeats the user input call untill a valid search word has been given
        """

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

    def ask_timetable_custom_name(self) -> str:
        """
        Asks user for a custom name for a timetable and returns a string to be used. 
        """

        custom_name = self.ui.ask_timetable_custom_name()
        return custom_name

    def fetch_search_options(self):
        self.search_options = api.fetch_search_options(self.search_word)

    def choose_searh_option(self) -> None:
        self.timetable = self.ui.choose_search_option(self.search_options)

    def choose_timetable_options(self) -> None:
        """
        Retrieves the saved timetabled and prompts the user to choose between saved timetables
        """

        records = record_api.get_records_file()
        self.timetable = self.ui.choose_timetable_options(records)

    def display_timetable(self, timetable) -> None:
        data = api.fetch_timetable(timetable)
        self.display.render_timetable(data)

    def view_timetable(self) -> None:
        """
        Display the timetable chosen by the user when given the options
        """

        self.choose_timetable_options()
        self.display_timetable(self.timetable)

    def get_timetables(self) -> None:
        self.repeat_ask_search_word()

        # Ask user to choose specific bus stop
        self.choose_searh_option()

        # Display timetable
        self.display_timetable(self.timetable)

    def get_timetable_info(self):
        self.user_answers = self.ui.get_answers()

    def save_timetable(self):
        self.get_timetable_info()
        custom_name = self.ask_timetable_custom_name()

        data = {
            "name": self.user_answers["bus_stop"]["name"],
            "code": self.user_answers["bus_stop"]["code"],
            "gtfsId": self.user_answers["bus_stop"]["gtfsId"],
            "custom_name": custom_name,
        }

        record_api.save_timetable(data)

    def choose_management_operation(self) -> None:
        """
        Asks the user wether to rename or delete a timetable
        """

        self.action = self.ui.choose_management_operation()

    def delete_timetable(self) -> None:
        status = record_api.delete_timetable(self.timetable)
        if status == "success":
            transient_print("Timetable deleted successfully")
        elif status == "fail":
            transient_print("Failed to delete timetable")

    def rename_timetable(self) -> None:
        custom_name = self.ask_timetable_custom_name()

        data = {
            "name": self.timetable["name"],
            "code": self.timetable["code"],
            "gtfsId": self.timetable["gtfsId"],
            "custom_name": custom_name,
        }

        record_api.save_timetable(data)


if __name__ == "__main__":
    Main().start()
