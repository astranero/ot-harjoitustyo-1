import unittest
from unittest.mock import patch, MagicMock

from index import Main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.main = Main()

    # def ask_action

    @patch("main.Ui.ask_action")
    def test_ask_action(self, mock):
        mock.return_value = "add_timetables"
        self.main.ask_action()
        self.assertEqual(self.main.action, "add_timetables")

    @patch("main.Ui.ask_action")
    def test_action_is_quit(self, mock):
        mock.return_value = "quit"
        self.main.ask_action()
        self.assertEqual(self.main.action, "quit")

    # def get_user_answers

    @patch("main.Ui.get_answers")
    def test_get_user_answers(self, mock):
        schema = {
            "test": "test"
        }

        mock.return_value = schema
        self.main.get_user_answers()
        self.assertEqual(self.main.user_answers, schema)

    # def ask_to_save_timetable
    @unittest.skip(reason="Have to figure out how to mock sub function returns")
    @patch("main.Ui.ask_to_save_timetable")
    def test_ask_to_save_timetable(self, mock):
        mock.return_value = "save_timetable"
        self.main.ask_to_save_timetable()
        self.assertEqual(self.main.action, "save_timetable")

    @patch("main.Ui.ask_to_save_timetable")
    def test_next_action_is_quit(self, mock):
        mock.return_value = "quit"
        self.main.ask_to_save_timetable()
        self.assertEqual(self.main.action, "quit")

    @patch("main.Ui.ask_to_save_timetable")
    def test_next_action_is_home(self, mock):
        mock.return_value = None
        self.main.ask_to_save_timetable()
        self.assertEqual(self.main.action, None)

    # def ask_timetable_custom_name

    @patch("main.Ui.ask_timetable_custom_name")
    def test_ask_timetable_custom_name(self, mock):
        mock.return_value = "test name"
        self.main.ask_timetable_custom_name()
        self.assertEqual(self.main.timetable_custom_name, "test name")

    # def ask_search_word

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


if __name__ == "__main__":
    unittest.main()
