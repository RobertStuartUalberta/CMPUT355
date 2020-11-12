from app.Models.Board import Board
from app.Models.Stone import Stone
from app.Models.Tile import Tile
from app.Exceptions.exceptions import *


def handle_click(game_board, position):
        window = game_board.get_window()
        turn = game_board.get_turn()
        if game_board.has_selected_tile():
            selected_tile = game_board.get_selected_tile()
            clicked = None
            neighbours = selected_tile.get_neighbours()
            clicked, capture = check_neighbours(game_board, position, neighbours) 
            if clicked != None:
                move_stone_and_update(clicked, capture, selected_tile, game_board)
            elif game_board.can_change_tile():
                stone_select(game_board, position, turn)
        else:
            stone_select(game_board, position, turn)

def move_stone_and_update(clicked, capture, selected_tile, game_board):
    if type(selected_tile.check_move(clicked)) == bool:
        if selected_tile.check_move(clicked):
            clicked.set_stone(selected_tile.get_stone())
            selected_tile.set_stone(None)
            selected_tile.set_outlined(False)
            game_board.set_selected_tile(None)
            game_board.set_can_change_tile(True)
            if capture != None:
                capture.set_stone(None)
                if can_capture_again(clicked, game_board):
                    game_board.set_selected_tile(clicked)
                    game_board.set_can_change_tile(False)
                    clicked.set_outlined(True)
                    return
            game_board.update_turn_number()
    else:
        game_board.set_selected_tile(selected_tile.check_move(clicked))

def can_capture_again(clicked, game_board):
    clicked_neighbours = clicked.get_neighbours()
    for neighbour in clicked_neighbours:
        if neighbour.is_captureable(game_board):
            if clicked.check_direction(neighbour.get_coords_for_capture()):
                return True
    return False


def check_neighbours(game_board, position, neighbours):
    for neighbour in neighbours:
        neighbour_coords = neighbour.get_coords()
        coords_for_capture = neighbour.get_coords_for_capture()
        if game_board.get_tile(neighbour_coords[0], neighbour_coords[1]).get_rect().collidepoint(position):
            return game_board.get_tile(neighbour_coords[0], neighbour_coords[1]), None
        elif neighbour.is_captureable(game_board):
            if game_board.get_tile(coords_for_capture[0], coords_for_capture[1]).get_rect().collidepoint(position):
                return game_board.get_tile(coords_for_capture[0], coords_for_capture[1]), game_board.get_tile(neighbour_coords[0], neighbour_coords[1])
    return None, None

def stone_select(game_board, position, turn):
    board = game_board.get_board()
    for row in board:
        for tile in row:
            if tile.has_stone():
                if tile.get_rect().collidepoint(position):
                    if game_board.get_players()[turn].stone_owned(tile.get_stone()):
                        tile.set_outlined(True)
                        if game_board.has_selected_tile():
                            game_board.get_selected_tile().set_outlined(False)
                        game_board.set_selected_tile(tile)