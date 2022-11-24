import unittest
from unittest.mock import patch

# my modules
from ui import Ui

class TestUi(unittest.TestCase):
    def setUp(self) -> None:
        self.ui = Ui()


    def test_init(self):
        schema = {
            "action": "",
            "next_action": "",
            "search_word": "",
            "bus_stop": {
                "name": "",
                "gtfsId": ""
            }
        }
        self.assertEqual(self.ui.answers, schema)


    @patch("ui.inquirer")
    def test_ask_action(self, mock_inquirer):
        
        # mock search timetables option
        mock_inquirer.prompt.return_value = {"action": "search_timetables"}
        self.assertEqual(self.ui.ask_action(), "search_timetables")

        # mock add timetable option
        mock_inquirer.prompt.return_value = {"action": "add_timetable"}
        self.assertEqual(self.ui.ask_action(), "add_timetable")

        # mock manage timetable option
        mock_inquirer.prompt.return_value = {"action": "manage_timetables"}
        self.assertEqual(self.ui.ask_action(), "manage_timetables")

        # mock quit option
        mock_inquirer.prompt.return_value = {"action": "quit"}
        self.assertEqual(self.ui.ask_action(), "quit")


    @patch("ui.inquirer")
    def test_ask_next_action(self, mock_inquirer):
        
        # mock Home option
        mock_inquirer.prompt.return_value = {"next_action": None}
        self.assertEqual(self.ui.ask_next_action(), None)

        # mock save timetable option
        mock_inquirer.prompt.return_value = {"next_action": "save_timetable"}
        self.assertEqual(self.ui.ask_next_action(), "save_timetable")

        # mock quit option
        mock_inquirer.prompt.return_value = {"next_action": "quit"}
        self.assertEqual(self.ui.ask_next_action(), "quit")


    @patch("ui.inquirer")
    def test_ask_search_word(self, mock_inquirer):
        
        # mock sarch_word
        mock_inquirer.prompt.return_value = {"search_word": "kamppi"}
        self.assertEqual(self.ui.ask_search_word(), "kamppi")


    @patch("ui.inquirer")
    def test_ask_timetable_custom_name(self, mock_inquirer):
        
        # mock timetable custom name
        mock_inquirer.prompt.return_value = {"timetable_custom_name": "test"}
        self.assertEqual(self.ui.ask_timetable_custom_name(), "test")


    @patch("ui.inquirer")
    def test_choose_search_option(self, mock_inquirer):
        search_options = {
            "data": {
                "stops": [
                    {
                        "name": "kamppi",
                        "code": "1",
                        "gtfsId": "k1",
                    },
                ]
            }
        }
        # mock an option
        mock_inquirer.prompt.return_value = {"bus_stop": ("kamppi", "k1")}
        self.assertEqual(self.ui.choose_search_option(search_options), ("kamppi", "k1"))



if __name__ =="__main__":
    unittest.main()