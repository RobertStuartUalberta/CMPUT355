from app.Exceptions.exceptions import *
from app.Views import Checkers
from app.Views import MenuScreen
from app.Models.Game import Game
import config

def main():
    try:
        if config.config():
            game = Game("Checkers", 600, 700, 8)
            MenuScreen.open_menu_screen(game)
        else:
            input("Above packages are missing. Press enter to close window.")

    except ConfigFileMissingError as e:
        print(e.args[0])
main()
