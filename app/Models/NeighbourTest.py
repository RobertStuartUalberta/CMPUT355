from app.Models.Neighbour import Neighbour
from app.Models.Tile import Tile
from app.Models.Board import Board
from app.Views.Window import Window

test_pass = "Passed"

test_window = Window("Test", 50, 50)
test_board = Board(8, test_window)

tile1 = test_board.get_tile(1, 1)
tile2 = test_board.get_tile(6, 6)
tile3 = test_board.get_tile(3, 3)


test1 = Neighbour((0, 0), tile1, test_board)
test2 = Neighbour((7, 7), tile2, test_board)
test3 = Neighbour((4, 4), tile3, test_board)

if test1.is_captureable() != False: test_pass = "Failed"
if test2.is_captureable() != False: test_pass = "Failed"
if test3.is_captureable() != True: test_pass = "Failed"

print(test_pass)