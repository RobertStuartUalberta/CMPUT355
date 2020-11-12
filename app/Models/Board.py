import pygame
from app.Models.Tile import Tile
from app.Models.Stone import Stone
from app.Models.Player import Player
from pygame.locals import*

class Board:
    # Creates new game board
    def __init__(self, size, window):
        self.size = size
        self.board = list()
        self.window = window
        self.selected_tile = None
        self.can_change_selected_tile = True
        self.turns = ("Black", "Red")
        self.players = {"Black" : Player("Black"), "Red" : Player("Red")}
        self.turn_number = 0
        self.generate_board()
        self.fill_board()
        self.draw_board()
    
    def generate_board(self):
        for row in range(self.get_size()):
            self.board.append(list())
            for col in range(self.get_size()):
                self.board[row].append(None)

    # Populates blank checkers board with white and red player stones
    # and initializes the tiles with appropriate colours
    def fill_board(self):
        window = self.get_window()
        square_size = window.get_dimensions()[0] / self.get_size()
        for row in range(self.get_size()):
            top = (row * square_size)
            for col in range(self.get_size()):
                left = (col * square_size)
                new_tile = Tile(row, col, square_size)

                # Sets tile colour and creates rect object for tile
                if ((row + col) %2) == 1:
                    new_tile.set_colour(pygame.Color(100, 40, 0))
                else:
                    new_tile.set_colour(pygame.Color(255,255,255))
                new_tile.set_rect(Rect(left, top, square_size, square_size))

                # Checks if a stone should be on this tile and what color it should be
                if row <= 2 or row >= (self.get_size() - 3):
                    colour = "Red"
                    if row <= 2:
                        colour = "Black"
                    if row % 2 == 1:
                        if col % 2 == 0:
                            new_stone = Stone(colour, row, col)
                            self.get_players()[colour].add_stone(new_stone)
                            new_tile.set_stone(new_stone)
                    elif row % 2 == 0:
                        if col % 2 == 1:
                            new_stone = Stone(colour, row, col)
                            self.get_players()[colour].add_stone(new_stone)
                            new_tile.set_stone(new_stone)
                self.set_tile(row, col, new_tile)

    def set_tile(self, row, col, tile):
        self.board[row][col] = tile
    
    def get_players(self):
        return self.players

    def get_tile(self, row, col):
        return self.board[row][col]

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board
    
    def get_window(self):
        return self.window
    
    def has_selected_tile(self):
        return self.selected_tile != None
    
    def get_selected_tile(self):
        return self.selected_tile
    
    def set_selected_tile(self, tile):
        self.selected_tile = tile

    def get_turn(self):
        return self.turns[self.get_turn_number()%2]
    
    def get_turn_number(self):
        return self.turn_number
    
    def update_turn_number(self):
        self.turn_number += 1

    def draw_board(self):
        board = self.get_board()
        window = self.get_window()
        for row in board:
            for tile in row:
                tile.draw_tile(window)
                if tile.get_stone() != None:
                    tile.draw_stone(window)
                    
    def can_change_tile(self):
        return self.can_change_selected_tile

    def set_can_change_tile(self, state):
        self.can_change_selected_tile = state

    


                


