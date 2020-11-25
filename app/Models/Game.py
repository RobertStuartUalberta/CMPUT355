import pygame
from app.Views.Window import Window
from app.Models.Board import Board
from app.Models.Stone import Stone
from app.Models.Tile import Tile
from app.Exceptions.exceptions import *

class Game:
    def __init__(self, title, width, height, board_dimension):
        self.window = Window(title, width, height)
        self.board_dimension = board_dimension
    
    def get_window(self):
        return self.window

    def get_game_board_dimensions(self):
        return self.board_dimension

    def handle_click(self, game_board, position):
        window = self.get_window()
        turn = game_board.get_turn()
        if game_board.has_selected_tile():
            selected_tile = game_board.get_selected_tile()
            clicked = None
            neighbours = selected_tile.get_neighbours()
            clicked, capture = self.check_neighbours(game_board, position, neighbours) 
            if clicked != None:
                self.move_stone_and_update(clicked, capture, selected_tile, game_board)
            elif game_board.can_change_tile():
                self.stone_select(game_board, position, turn)
            elif selected_tile.get_rect().collidepoint(position):
                selected_tile.set_outlined(False)
                game_board.set_selected_tile(None)
                game_board.set_can_change_tile(True)
                game_board.update_turn_number()

        else:
            self.stone_select(game_board, position, turn)

    def move_stone_and_update(self, clicked, capture, selected_tile, game_board):
        if type(selected_tile.check_move(clicked)) == bool:
            if selected_tile.check_move(clicked):
                if capture != None or selected_tile.get_stone().can_capture_only() == False:
                    clicked.set_stone(selected_tile.get_stone())
                    clicked.get_stone().set_capture_only(False)
                    selected_tile.set_stone(None)
                    selected_tile.set_outlined(False)
                    game_board.set_selected_tile(None)
                    game_board.set_can_change_tile(True)
                    game_board.update_turn_number()
                if capture != None:
                    capture.set_stone(None)
                    if self.can_capture_again(clicked, game_board):
                        game_board.update_turn_number()
                        game_board.set_selected_tile(clicked)
                        clicked.get_stone().set_capture_only(True)
                        game_board.set_can_change_tile(False)
                        clicked.set_outlined(True)
                        return
                
        else:
            game_board.set_selected_tile(selected_tile.check_move(clicked))

    def can_capture_again(self, clicked, game_board):
        clicked_neighbours = clicked.get_neighbours()
        for neighbour in clicked_neighbours:
            if neighbour.is_captureable(game_board):
                if clicked.check_direction(neighbour.get_coords_for_capture(), False):
                    return True
        return False


    def check_neighbours(self, game_board, position, neighbours):
        for neighbour in neighbours:
            neighbour_coords = neighbour.get_coords()
            coords_for_capture = neighbour.get_coords_for_capture()
            if game_board.get_tile(neighbour_coords[0], neighbour_coords[1]).get_rect().collidepoint(position):
                return game_board.get_tile(neighbour_coords[0], neighbour_coords[1]), None
            elif neighbour.is_captureable(game_board):
                if game_board.get_tile(coords_for_capture[0], coords_for_capture[1]).get_rect().collidepoint(position):
                    return game_board.get_tile(coords_for_capture[0], coords_for_capture[1]), game_board.get_tile(neighbour_coords[0], neighbour_coords[1])
        return None, None

    def stone_select(self, game_board, position, turn):
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
        