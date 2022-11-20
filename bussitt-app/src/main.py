#my modules
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
        self.search_options = None

    def start(self) -> None:
        # Main loop
        while True:
            # Ask user for action
            self.ask_action()

            if self.action == "search_timetables":
                self.get_timetables()
                self.ask_next_action()
            elif self.action == "add_timetable":
                transient_print("Feature not yet available")
            elif self.action == "manage_timetables":
                transient_print("Feature not yet available")
                
    def ask_action(self) -> None:
        self.action = self.ui.ask_action()
        if self.action == "quit": exit()

    def ask_next_action(self) -> None:
        self.action = self.ui.ask_next_action()
        if self.action == "save_timetable":
            transient_print("Feature not yet available")
        elif self.action == "quit": exit()

    def ask_search_word(self) -> None:
        while True:
            # Ask for a search word until there are search options
            search_word = self.ui.ask_search_word()

            # Look for search options by search word
            self.search_options = api.fetch_search_options(search_word)
            
            # Ask until there is search options
            if self.search_options == None:
                transient_print(f"[?] 0 matches for: {search_word}")
            else:
                break

    def ask_searh_option(self) -> None:
        self.bus_stop = self.ui.choose_search_option(self.search_options)

    def display_timetable(self) -> None:
        data = api.fetch_timetable(self.bus_stop)
        self.display.render_timetable(data)

    def get_timetables(self) -> None:
        self.ask_search_word()

        # Ask for specific bus stop
        self.ask_searh_option()

        # Display timetable
        self.display_timetable()
    
if __name__ == "__main__":
    Main().start()



