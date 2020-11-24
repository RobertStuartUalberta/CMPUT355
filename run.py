from app.Exceptions.exceptions import *
from app.Views import Checkers
from app.Views import MenuScreen
from app.Models.Game import Game
import config

def main():
    try:
        if config.config():
            window_width = 400
            window_height = 400
            title = "Checkers"
            board_dimension = 8
            game = Game(title, window_width, window_height, board_dimension)
            MenuScreen.open_menu_screen(game)

            #Checkers.play_checkers(game)
        else:
            input("Above packages are missing. Press enter to close window.")

    except ConfigFileMissingError as e:
        print(e.args[0])
main()
