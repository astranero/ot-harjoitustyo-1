import unittest
from unittest.mock import patch, MagicMock

from main import Main

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.main = Main()

    @patch("main.Ui.ask_action")
    def test_ask_action(self, mock):
        mock.return_value = "search_timetables"
        self.main.ask_action()
        self.assertEqual(self.main.action, "search_timetables")

    @patch("main.Ui.ask_action")
    def test_action_is_quit(self, mock):
        mock.return_value = "quit"
        self.main.ask_action()
        self.assertEqual(self.main.action, "quit")

    @patch("main.Ui.ask_next_action")
    def test_ask_next_action(self, mock):
        mock.return_value = "save_timetable"
        self.main.ask_next_action()
        self.assertEqual(self.main.action, "save_timetable")

    @patch("main.Ui.ask_next_action")
    def test_next_action_is_quit(self, mock):
        mock.return_value = "quit"
        self.main.ask_next_action()
        self.assertEqual(self.main.action, "quit")

    @patch("main.Ui.ask_search_word")
    def test_ask_search_word(self, mock):
        mock.return_value = "word"
        self.main.ask_search_word()
        self.assertEqual(self.main.search_word, "word")

    @patch("main.api.fetch_search_options")
    def test_ask_search_word(self, mock):
        mock.return_value = {"test": "option"}
        self.main.fetch_search_options()
        self.assertEqual(self.main.search_options, {"test": "option"})




if __name__ =="__main__":
    unittest.main()