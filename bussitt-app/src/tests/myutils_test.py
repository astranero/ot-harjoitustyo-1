import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

from myutils.myutils import *


def test_error_without_message(capsys):
    error()
    out, err = capsys.readouterr()
    assert out == "Error has occured\n"


def test_error_with_message(capsys):
    error("a message")
    out, err = capsys.readouterr()
    assert out == "a message\n"


@unittest.skip(reason="Not sure yet what to display in boilerplate")
def test_boilerplate(capsys):
    boilerplate()
    out, err = capsys.readouterr()
    assert out == "+++++++++++ This is Bussitt +++++++++++\n\n"


@unittest.skip(reason="Not sure yet what to display yet")
def test_transient_print_with_message(capsys):
    transient_print("a message")
    out, err = capsys.readouterr()
    assert out == "+++++++++++ This is Bussitt +++++++++++\n\na message\n"


def test_get_time_and_date():
    t, d = get_time_and_date(0)
    assert t == "02:00"
    assert d == '01-01-1970'


if __name__ == "__main__":
    unittest.main()
