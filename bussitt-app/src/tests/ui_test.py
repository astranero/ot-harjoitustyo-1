import unittest
from unittest.mock import patch

# my modules
from ui.ui import Ui


class TestUi(unittest.TestCase):
    def setUp(self) -> None:
        self.ui = Ui()

    def test_init(self):
        schema = {
            "action": "",
            "search_word": "",
            "bus_stop": {
                "name": "",
                "gtfsId": ""
            }
        }
        self.assertEqual(self.ui.answers, schema)

    @patch("ui.ui.inquirer")
    def test_ask_action(self, mock_inquirer):
        
        # mock view timetable option
        mock_inquirer.prompt.return_value = {"action": "view_timetable"}
        self.assertEqual(self.ui.ask_action(has_records=True), "view_timetable")

        # mock add timetable option
        mock_inquirer.prompt.return_value = {"action": "add_timetable"}
        self.assertEqual(self.ui.ask_action(has_records=True), "add_timetable")

        # mock manage timetable option
        mock_inquirer.prompt.return_value = {"action": "manage_timetables"}
        self.assertEqual(self.ui.ask_action(has_records=True), "manage_timetables")

        # mock quit option
        mock_inquirer.prompt.return_value = {"action": "quit"}
        self.assertEqual(self.ui.ask_action(has_records=True), "quit")

    @patch("ui.ui.inquirer")
    def test_ask_to_save_timetable(self, mock_inquirer):

        # mock Home option
        mock_inquirer.prompt.return_value = {"save_timetable": None}
        self.assertEqual(self.ui.ask_to_save_timetable(), None)

        # mock save timetable option
        mock_inquirer.prompt.return_value = {
            "save_timetable": "save_timetable"}
        self.assertEqual(self.ui.ask_to_save_timetable(), "save_timetable")

    @patch("ui.ui.inquirer")
    def test_ask_search_word(self, mock_inquirer):

        # mock sarch_word
        mock_inquirer.prompt.return_value = {"search_word": "kamppi"}
        self.assertEqual(self.ui.ask_search_word(), "kamppi")

    @patch("ui.ui.inquirer")
    def test_ask_timetable_custom_name(self, mock_inquirer):

        # mock timetable custom name
        mock_inquirer.prompt.return_value = {"custom_name": "test"}
        self.assertEqual(self.ui.ask_timetable_custom_name(), "test")

    @patch("ui.ui.inquirer")
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
        self.assertEqual(self.ui.choose_search_option(
            search_options), ("kamppi", "k1"))


if __name__ == "__main__":
    unittest.main()
