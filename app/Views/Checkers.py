import pygame
from app.Models import Stone, Tile, Player
from app.Views.Window import Window
from app.Models.Board import Board
from app.Models.Game import Game
from pygame.locals import*
from app.Helpers.HandleClick import handle_click


def play_checkers(game):
    quit = False
    window = game.get_window()
    game_board = Board(game.get_game_board_dimensions(), window)
    #game_board.draw_board(window)
    while quit is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                window.update()
                handle_event(event, game_board)

def handle_event(event, game_board):
    if event.type == pygame.MOUSEBUTTONUP:
        position = pygame.mouse.get_pos()
        handle_click(game_board, position)
        game_board.draw_board()

