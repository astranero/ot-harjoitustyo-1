import sys
from tabulate import tabulate

# my modules
from config import config


def check_arguments():
    if "-h" in sys.argv or "help" in sys.argv:
        print(tabulate(config.configs_list, headers="keys", showindex=False))
        exit()

    if "-dc" in sys.argv or "disable-clear" in sys.argv:
        config.disable_clear_cl = True

