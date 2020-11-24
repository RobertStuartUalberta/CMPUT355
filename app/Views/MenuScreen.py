import pygame
from app.Views.Checkers import play_checkers

def open_menu_screen(game):
    window = game.get_window()
    window.get_window().fill((0, 0, 0))
    pygame.init()
    title_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 70)

    title = title_font.render("Checkers", True, (255,255,255))
    title_size = title_font.size("Checkers")

    play = menu_font.render("Play Game", True, (255, 255, 255))
    play_size = menu_font.size("Play Game")
    

    rules = menu_font.render("Read Rules", True, (255, 255, 255))
    rules_size = menu_font.size("Read Rules")

    title_coords = (((window.get_dimensions()[0]//2) - (title_size[0]//2)), (window.get_dimensions()[1]//5))
    window.get_window().blit(title, (title_coords))

    play_coords = (((window.get_dimensions()[0]//2) - (play_size[0]//2)), ((window.get_dimensions()[1]//2) - (play_size[1]//2)))
    window.get_window().blit(play, (play_coords))
    play_rect = pygame.Rect(play_coords[0], play_coords[1], play_size[0], play_size[1])

    rules_coords = (((window.get_dimensions()[0]//2) - (rules_size[0]//2)), ((window.get_dimensions()[1]//2) - (rules_size[1]//2) + play_size[1] + 50))
    window.get_window().blit(rules, (rules_coords))
    rules_rect = pygame.Rect(rules_coords[0], rules_coords[1], rules_size[0], rules_size[1])

    quit = False
    while quit is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if play_rect.collidepoint(position):
                    quit = play_checkers(game)
                elif rules_rect.collidepoint(position):
                    quit = open_rules(window, window.get_dimensions()[0], window.get_dimensions()[1])
                    if quit == False:
                        quit = open_menu_screen(game)
            window.update()


            

def open_rules(window, width, height, remainder = None):
    window.get_window().fill((0, 0, 0))
    previous_line_y = 10
    width_offset = width// 20
    height_offset = height // 10
    rules_font = pygame.font.Font(None, 35)
    if remainder == None:
        rules = open("game_rules.txt", "r").readlines()
        all_words = []
        for line in rules:
            words = line.split(' ')
            for word in words:
                all_words.append(word.strip("\n"))
    else:
        all_words = remainder
    current_line = ''
    next_page = False
    next_rect = None
    return_rect = None
    while len(all_words) != 0 and next_page == False:
        if rules_font.size(current_line + " " + all_words[0])[0] < (width - width_offset):
            current_line += (" " + all_words.pop(0))
        else:
            line_to_draw = rules_font.render(current_line, True, (255, 255, 255))
            line_coords = (width_offset, (previous_line_y + 5))
            window.get_window().blit(line_to_draw, line_coords)
            previous_line_y = line_coords[1] + rules_font.size(current_line)[1]
            if (height - previous_line_y) < height_offset:
                next_button = rules_font.render("Next Page", True, (255, 255, 255))
                next_size = rules_font.size("Next Page")
                next_coords = ((width - next_size[0] - 5), (height - next_size[1] - 5))
                window.get_window().blit(next_button, next_coords)
                next_rect = pygame.Rect(next_coords[0], next_coords[1], next_size[0], next_size[1])
                next_page = True
            else:
                current_line = '' 

    if next_rect == None:
        if current_line != '':
            line_to_draw = rules_font.render(current_line, True, (255, 255, 255))
            line_coords = (width_offset, (previous_line_y + 5))
            window.get_window().blit(line_to_draw, line_coords)
            previous_line_y = line_coords[1] + rules_font.size(current_line)[1]
        return_button = rules_font.render("Return to menu", True, (255, 255, 255))
        return_size = rules_font.size("Return to menu")
        return_coords = (width_offset + 50, (previous_line_y + 5))
        window.get_window().blit(return_button, return_coords)
        return_rect = pygame.Rect(return_coords[0], return_coords[1], return_size[0], return_size[1])

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



        


        


    

    
