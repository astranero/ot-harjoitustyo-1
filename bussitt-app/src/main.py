import pprint

# my modules
from myutils import *
from ui import Ui
from display import Display
from api import api

class Main:
    def __init__(self) -> None:
        self.ui = Ui()
        self.display = Display()

        # App properties
        self.action = None
        self.bus_stop = None

        # Search properties
        self.search_word = None
        self.search_options = None


    def start(self) -> None:
        # self.display.render_all_timetables()

        # Main loop
        while True:

            # Ask user for action
            self.ask_action()
            print(self.action)

            if self.action == "search_timetables":
                self.get_timetables()
                self.ask_next_action()
            elif self.action == "add_timetable":
                transient_print("Feature not yet available")
            elif self.action == "manage_timetables":
                transient_print("Feature not yet available")

                
    def ask_action(self) -> None:
        self.action = self.ui.ask_action()
        if self.action == "quit": 
            if __name__ == "__main__": exit()
            
    def ask_next_action(self) -> None:
        self.action = self.ui.ask_next_action()
        if self.action == "save_timetable":
            self.save_timetable()
        elif self.action == "quit": 
            if __name__ == "__main__": exit()


    def repeat_ask_search_word(self) -> None:
        while True:
            # Ask for a search word until there are search options
            self.ask_search_word()

            # Look for search options by search word
            self.fetch_search_options()
            
            # Ask until there is search options
            if self.search_options == "no_matches":
                transient_print(f"[?] 0 matches for: {self.search_word}")
            elif self.search_options == None:
                error()
                exit()
            else:
                break

    def ask_search_word(self):
        self.search_word = self.ui.ask_search_word()

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
    
    def save_timetable(self):
        timetable_name = None
        timetable_gtfsId = None
        timetable_custom_name = None

        answers = self.ui.get_answers()
        timetable_custom_name = self.ui.ask_timetable_custom_name()

        timetable_name = answers["bus_stop"]["name"]
        timetable_gtfsId = answers["bus_stop"]["gtfsId"]

        save_timetable(timetable_name, timetable_gtfsId, timetable_custom_name)


if __name__ == "__main__":
    Main().start()



