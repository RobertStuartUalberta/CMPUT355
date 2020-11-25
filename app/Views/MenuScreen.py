import pygame
import app.Views.Checkers as Checkers

def open_menu_screen(game):
    window = game.get_window()
    window.get_window().fill((0, 0, 0))
    pygame.init()
    title_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 50)
    draw_text(title_font, "Checkers", window, ((window.get_dimensions()[0]//2) - (title_font.size("Checkers")[0]//2)), (window.get_dimensions()[1]//5))
    play_size = menu_font.size("Play Game")
    play_rect = draw_button(menu_font, "Play Game", window, ((window.get_dimensions()[0]//2) - (play_size[0]//2)), ((window.get_dimensions()[1]//2) - (play_size[1]//2)))
    rules_size = menu_font.size("Read Rules")
    rules_rect = draw_button(menu_font, "Read Rules", window, ((window.get_dimensions()[0]//2) - (rules_size[0]//2)), ((window.get_dimensions()[1]//2) - (rules_size[1]//2) + play_size[1] + 50))
    quit = False
    while quit is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if play_rect.collidepoint(position):
                    quit = Checkers.play_checkers(game)
                elif rules_rect.collidepoint(position):
                    quit = open_rules(window, window.get_dimensions()[0], window.get_dimensions()[1])
                    if quit == False:
                        quit = open_menu_screen(game)
            window.update()

def open_rules(window, width, height, remainder = None):
    window.get_window().fill((0, 0, 0))
    previous_line_y = 10
    width_offset = 0
    height_offset = height // 5
    rules_font = pygame.font.Font(None, 35)
    if remainder == None:
        rules = open("game_rules.txt", "r").readlines()
        all_words = []
        for line in rules:
            words = line.split(' ')
            for word in words:
                all_words.append(word.strip("\n"))
            all_words.append("\n")
    else:
        all_words = remainder
    current_line = ''
    next_page = False
    next_rect = None
    return_rect = None
    while len(all_words) != 0 and next_page == False:
        if rules_font.size(current_line + " " + all_words[0])[0] < (width - width_offset) and all_words[0] != "\n":
            current_line += (" " + all_words.pop(0))
        else:
            draw_text(rules_font, current_line, window, width_offset, (previous_line_y + 5))
            if all_words[0] != "\n":
                previous_line_y = previous_line_y + rules_font.size(current_line)[1] + 5
            else:
                previous_line_y = previous_line_y + (2*rules_font.size(current_line)[1]) + 5
                all_words.pop(0)
            if (height - previous_line_y) < height_offset:
                next_rect = draw_button(rules_font, "Next Page", window, (width - rules_font.size("Next Page")[0] - 5), (height - rules_font.size("Next Page")[1] - 5))
                next_page = True
            else:
                current_line = '' 

    if next_rect == None:
        if current_line != '':
            draw_text(rules_font, current_line, window, width_offset, (previous_line_y + 5))
            previous_line_y = previous_line_y + rules_font.size(current_line)[1] + 5
        return_rect = draw_button(rules_font, "Return to menu", window, ((width//2) - (rules_font.size("Return to menu")[0]//2)), (previous_line_y + 25))

    quit = False
    while quit is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if next_rect != None:
                    if next_rect.collidepoint(position):
                        return open_rules(window, width, height, all_words)
                if return_rect != None:
                    if return_rect.collidepoint(position):
                        return False
            window.update()

def draw_text(font, string, window, x, y):
    line_to_draw = font.render(string, True, (255, 255, 255))
    line_coords = (x, y)
    window.get_window().blit(line_to_draw, line_coords)

def draw_button(font, string, window, x, y):
    button = font.render(string, True, (255, 255, 255))
    button_size = font.size(string)
    button_coords = (x, y)
    button_rect = pygame.Rect((x - 5), (y - 5), (button_size[0] + 10), (button_size[1] + 10))
    pygame.draw.rect(window.get_surface(), (255, 255, 255), button_rect, 2, (button_size[1]//4))
    window.get_window().blit(button, button_coords)
    return button_rect

def show_end_screen(window, winner, game):
    window.get_window().fill((0, 0, 0))
    title_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 50)
    draw_text(title_font, winner + " Wins!", window, ((window.get_dimensions()[0]//2) - (title_font.size(winner + " Wins!")[0]//2)), (window.get_dimensions()[1]//5))
    play_size = menu_font.size("Play Again")
    play_rect = draw_button(menu_font, "Play Again", window, ((window.get_dimensions()[0]//2) - (play_size[0]//2)), ((window.get_dimensions()[1]//2) - (play_size[1]//2)))
    quit_size = menu_font.size("Quit")
    quit_rect = draw_button(menu_font, "Quit", window, ((window.get_dimensions()[0]//2) - (quit_size[0]//2)), ((window.get_dimensions()[1]//2) - (quit_size[1]//2) + play_size[1] + 50))
    quit = False
    while quit is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if play_rect.collidepoint(position):
                    quit = Checkers.play_checkers(game)
                elif quit_rect.collidepoint(position):
                    quit = True
            window.update()


        


        


    

    
