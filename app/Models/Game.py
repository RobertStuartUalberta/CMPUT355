import pygame
from app.Views.Window import Window
from app.Models.Board import Board

class Game:
    def __init__(self, title, width, height, board_dimension):
        self.window = Window(title, width, height)
        self.board_dimension = board_dimension
    
    def get_window(self):
        return self.window

    def get_game_board_dimensions(self):
        return self.board_dimension
    