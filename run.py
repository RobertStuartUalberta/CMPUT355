from app.Exceptions.exceptions import *
from app.Views import Checkers
import config

def main():
    try:
        if config.config():
            Checkers.play_checkers()
        else:
            input("Above packages are missing. Press enter to close window.")

    except ConfigFileMissingError as e:
        print(e.args[0])
main()
