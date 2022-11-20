import unittest
from unittest.mock import patch

from main import Main
import ui

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.main = Main()

    @patch("main.Ui.ask_action")
    def test_ask_action(self, mock_ui_ask_action):
        mock_ui_ask_action.return_value = "search_timetables"
        self.main.ask_action()
        self.assertEqual(self.main.action, "search_timetables")

    @patch("main.Ui.ask_next_action")
    def test_ask_next_action(self, mock_ui_ask_next_action):
        mock_ui_ask_next_action.return_value = "search_timetables"
        self.main.ask_next_action()
        self.assertEqual(self.main.action, "search_timetables")

if __name__ =="__main__":
    unittest.main()