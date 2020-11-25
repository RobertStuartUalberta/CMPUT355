import pygame
from app.Models import Stone, Tile, Player
from app.Views.Window import Window
from app.Models.Board import Board
from app.Models.Game import Game
from pygame.locals import*
from app.Helpers.HandleClick import handle_click
import app.Views.MenuScreen as MenuScreen


def play_checkers(game):
    quit = False
    window = game.get_window()
    game_board = Board(game.get_game_board_dimensions(), window, game)
    concede_button = get_concede_button(window)
    while quit is False and game_board.game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                handle_event(event, game_board, game, concede_button, window)
                draw_turn_indicator(window, game_board)
                window.update()

def handle_event(event, game_board, game, concede_button, window):
    if event.type == pygame.MOUSEBUTTONUP:
        position = pygame.mouse.get_pos()
        game.handle_click(game_board, position)
        game_board.draw_board()
        if concede_button.collidepoint(position):
            game_board.set_game_over(True)
            if game_board.get_turn() == "Red":
                winner = "Black"
            else:
                winner = "Red"
            MenuScreen.show_end_screen(window, winner, game)

def draw_turn_indicator(window, game_board):
    turn_font = pygame.font.Font(None, 60)
    turn = "Turn: " + game_board.get_turn()
    text_size = turn_font.size(turn)
    width = window.get_dimensions()[0]
    height = window.get_dimensions()[1]
    clear_rect = pygame.Rect(0, width, width//2, height - width)
    pygame.draw.rect(window.get_window(), (0, 0, 0), clear_rect)
    x = (width//4) - (text_size[0]//2)
    y = width + ((height - width)//2) - (text_size[1]//2)
    MenuScreen.draw_text(turn_font, turn, window, x, y)

def get_concede_button(window):
    button_font = pygame.font.Font(None, 60)
    width = window.get_dimensions()[0]
    height = window.get_dimensions()[1]
    text_size = button_font.size("Concede")
    x = (width//2) + (width//4) - (text_size[0]//2)
    y = width + ((height - width)//2) - (text_size[1]//2)
    return MenuScreen.draw_button(button_font, "Concede", window, x, y)
